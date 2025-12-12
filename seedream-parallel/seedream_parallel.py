#!/usr/bin/env python3
"""
Seedream 4.5 Parallel Image Processing Tool
여러 이미지에 동일한 프롬프트를 병렬로 적용하는 도구
"""

import asyncio
import aiohttp
import base64
import json
import os
import sys
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Dict, Any
from dataclasses import dataclass, field
from enum import Enum


class TaskType(Enum):
    TEXT_TO_IMAGE = "text_to_image"
    IMAGE_TO_IMAGE = "image_to_image"


@dataclass
class ReferenceImageGroup:
    """참조 이미지 그룹 (1~5번 슬롯)"""
    slot: int  # 1-5
    images: List[str] = field(default_factory=list)  # 파일 경로 리스트

    def add_image(self, path: str):
        self.images.append(path)


@dataclass
class ProcessingTask:
    """처리 작업 정의"""
    task_id: str
    task_type: TaskType
    prompt: str
    reference_groups: List[ReferenceImageGroup] = field(default_factory=list)
    output_dir: str = "./output"
    image_size: str = "2K"  # "1K", "2K", "4K"
    seed: Optional[int] = None


class SeedreamAPI:
    """Seedream 4.5 API 클라이언트"""

    # 여러 API 제공자 지원
    API_PROVIDERS = {
        "aimlapi": {
            "url": "https://api.aimlapi.com/v1/images/generations",
            "model": "bytedance/seedream-4-5"
        },
        "byteplus": {
            "url": "https://api.byteplus.com/v1/images/generations",
            "model": "doubao-seedream-4-5-251128"
        }
    }

    def __init__(self, api_key: str, provider: str = "aimlapi"):
        self.api_key = api_key
        self.provider = provider
        self.config = self.API_PROVIDERS.get(provider, self.API_PROVIDERS["aimlapi"])

    def _encode_image_to_base64(self, image_path: str) -> str:
        """이미지 파일을 Base64로 인코딩"""
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")

    def _get_image_data_url(self, image_path: str) -> str:
        """이미지를 data URL 형식으로 변환"""
        ext = Path(image_path).suffix.lower()
        mime_types = {
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".png": "image/png",
            ".gif": "image/gif",
            ".webp": "image/webp"
        }
        mime_type = mime_types.get(ext, "image/png")
        b64_data = self._encode_image_to_base64(image_path)
        return f"data:{mime_type};base64,{b64_data}"

    async def generate_image(
        self,
        session: aiohttp.ClientSession,
        prompt: str,
        reference_images: Optional[List[str]] = None,
        image_size: str = "2K",
        seed: Optional[int] = None,
        response_format: str = "url"
    ) -> Dict[str, Any]:
        """이미지 생성/편집 API 호출"""

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.config["model"],
            "prompt": prompt,
            "image_size": image_size,
            "response_format": response_format
        }

        # 참조 이미지가 있으면 추가 (이미지 편집 모드)
        if reference_images:
            image_urls = []
            for img_path in reference_images:
                if os.path.exists(img_path):
                    image_urls.append(self._get_image_data_url(img_path))
                elif img_path.startswith(("http://", "https://", "data:")):
                    image_urls.append(img_path)
            if image_urls:
                payload["image_urls"] = image_urls

        if seed is not None:
            payload["seed"] = seed

        try:
            async with session.post(
                self.config["url"],
                headers=headers,
                json=payload,
                timeout=aiohttp.ClientTimeout(total=300)
            ) as response:
                result = await response.json()

                if response.status != 200:
                    return {
                        "success": False,
                        "error": result.get("error", {}).get("message", str(result)),
                        "status_code": response.status
                    }

                return {
                    "success": True,
                    "data": result.get("data", []),
                    "meta": result.get("meta", {})
                }

        except asyncio.TimeoutError:
            return {"success": False, "error": "Request timeout"}
        except Exception as e:
            return {"success": False, "error": str(e)}


class ParallelImageProcessor:
    """병렬 이미지 처리기"""

    def __init__(self, api_key: str, provider: str = "aimlapi", max_concurrent: int = 5):
        self.api = SeedreamAPI(api_key, provider)
        self.max_concurrent = max_concurrent
        self.semaphore = asyncio.Semaphore(max_concurrent)

    async def _process_single_group(
        self,
        session: aiohttp.ClientSession,
        group: ReferenceImageGroup,
        prompt: str,
        output_dir: str,
        image_size: str,
        seed: Optional[int],
        task_id: str
    ) -> Dict[str, Any]:
        """단일 참조 이미지 그룹 처리"""

        async with self.semaphore:
            print(f"  [슬롯 {group.slot}] 처리 시작... ({len(group.images)}개 참조 이미지)")

            result = await self.api.generate_image(
                session=session,
                prompt=prompt,
                reference_images=group.images if group.images else None,
                image_size=image_size,
                seed=seed
            )

            if result["success"]:
                # 결과 이미지 저장
                output_path = Path(output_dir)
                output_path.mkdir(parents=True, exist_ok=True)

                saved_files = []
                for idx, img_data in enumerate(result.get("data", [])):
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"{task_id}_slot{group.slot}_{timestamp}_{idx}.png"
                    filepath = output_path / filename

                    # URL이면 다운로드, base64면 디코딩
                    if "url" in img_data:
                        async with session.get(img_data["url"]) as img_response:
                            if img_response.status == 200:
                                with open(filepath, "wb") as f:
                                    f.write(await img_response.read())
                                saved_files.append(str(filepath))
                    elif "b64_json" in img_data:
                        img_bytes = base64.b64decode(img_data["b64_json"])
                        with open(filepath, "wb") as f:
                            f.write(img_bytes)
                        saved_files.append(str(filepath))

                print(f"  [슬롯 {group.slot}] 완료! 저장: {saved_files}")
                return {
                    "slot": group.slot,
                    "success": True,
                    "saved_files": saved_files
                }
            else:
                print(f"  [슬롯 {group.slot}] 실패: {result.get('error')}")
                return {
                    "slot": group.slot,
                    "success": False,
                    "error": result.get("error")
                }

    async def process_task(self, task: ProcessingTask) -> Dict[str, Any]:
        """작업 처리 (병렬)"""

        print(f"\n{'='*60}")
        print(f"작업 ID: {task.task_id}")
        print(f"타입: {task.task_type.value}")
        print(f"프롬프트: {task.prompt[:100]}...")
        print(f"참조 그룹 수: {len(task.reference_groups)}")
        print(f"{'='*60}\n")

        async with aiohttp.ClientSession() as session:
            # 텍스트 → 이미지 (참조 이미지 없음)
            if task.task_type == TaskType.TEXT_TO_IMAGE or not task.reference_groups:
                print("  [텍스트→이미지] 생성 중...")
                result = await self.api.generate_image(
                    session=session,
                    prompt=task.prompt,
                    image_size=task.image_size,
                    seed=task.seed
                )

                if result["success"]:
                    output_path = Path(task.output_dir)
                    output_path.mkdir(parents=True, exist_ok=True)

                    saved_files = []
                    for idx, img_data in enumerate(result.get("data", [])):
                        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                        filename = f"{task.task_id}_generated_{timestamp}_{idx}.png"
                        filepath = output_path / filename

                        if "url" in img_data:
                            async with session.get(img_data["url"]) as img_response:
                                if img_response.status == 200:
                                    with open(filepath, "wb") as f:
                                        f.write(await img_response.read())
                                    saved_files.append(str(filepath))

                    return {"success": True, "saved_files": saved_files}
                else:
                    return {"success": False, "error": result.get("error")}

            # 이미지 → 이미지 (참조 이미지 있음, 병렬 처리)
            else:
                tasks = [
                    self._process_single_group(
                        session=session,
                        group=group,
                        prompt=task.prompt,
                        output_dir=task.output_dir,
                        image_size=task.image_size,
                        seed=task.seed,
                        task_id=task.task_id
                    )
                    for group in task.reference_groups
                ]

                results = await asyncio.gather(*tasks, return_exceptions=True)

                successful = [r for r in results if isinstance(r, dict) and r.get("success")]
                failed = [r for r in results if isinstance(r, dict) and not r.get("success")]
                errors = [r for r in results if isinstance(r, Exception)]

                return {
                    "success": len(failed) == 0 and len(errors) == 0,
                    "total": len(results),
                    "successful": len(successful),
                    "failed": len(failed),
                    "errors": len(errors),
                    "details": results
                }


def create_reference_groups_from_folders(base_path: str) -> List[ReferenceImageGroup]:
    """
    폴더 구조에서 참조 이미지 그룹 생성
    예: base_path/slot1/, base_path/slot2/, ...
    """
    groups = []
    base = Path(base_path)

    for slot_num in range(1, 6):  # slot1 ~ slot5
        slot_dir = base / f"slot{slot_num}"
        if slot_dir.exists() and slot_dir.is_dir():
            group = ReferenceImageGroup(slot=slot_num)
            for img_file in slot_dir.glob("*"):
                if img_file.suffix.lower() in [".jpg", ".jpeg", ".png", ".gif", ".webp"]:
                    group.add_image(str(img_file))
            if group.images:
                groups.append(group)

    return groups


def create_reference_groups_from_files(file_paths: List[str], images_per_slot: int = 1) -> List[ReferenceImageGroup]:
    """
    파일 리스트에서 참조 이미지 그룹 생성
    images_per_slot: 각 슬롯당 이미지 수
    """
    groups = []
    slot_num = 1
    current_group = ReferenceImageGroup(slot=slot_num)

    for path in file_paths:
        if len(current_group.images) >= images_per_slot:
            groups.append(current_group)
            slot_num += 1
            if slot_num > 5:
                break
            current_group = ReferenceImageGroup(slot=slot_num)
        current_group.add_image(path)

    if current_group.images:
        groups.append(current_group)

    return groups


# ============================================================
# CLI 인터페이스
# ============================================================

def print_banner():
    print("""
╔═══════════════════════════════════════════════════════════╗
║       Seedream 4.5 Parallel Image Processing Tool         ║
║                    병렬 이미지 처리 도구                      ║
╚═══════════════════════════════════════════════════════════╝
    """)


def interactive_mode(api_key: str):
    """대화형 모드"""
    processor = ParallelImageProcessor(api_key)

    while True:
        print("\n" + "="*50)
        print("모드 선택:")
        print("  1. 텍스트 → 이미지 생성")
        print("  2. 이미지 + 프롬프트 → 이미지 편집 (단일)")
        print("  3. 이미지 + 프롬프트 → 이미지 편집 (병렬, 폴더)")
        print("  4. 이미지 + 프롬프트 → 이미지 편집 (병렬, 파일 목록)")
        print("  q. 종료")
        print("="*50)

        choice = input("\n선택: ").strip()

        if choice == "q":
            print("프로그램을 종료합니다.")
            break

        prompt = input("프롬프트 입력: ").strip()
        if not prompt:
            print("프롬프트가 필요합니다.")
            continue

        output_dir = input("출력 폴더 (기본: ./output): ").strip() or "./output"
        image_size = input("이미지 크기 (1K/2K/4K, 기본: 2K): ").strip() or "2K"

        task_id = f"task_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        if choice == "1":
            # 텍스트 → 이미지
            task = ProcessingTask(
                task_id=task_id,
                task_type=TaskType.TEXT_TO_IMAGE,
                prompt=prompt,
                output_dir=output_dir,
                image_size=image_size
            )

        elif choice == "2":
            # 단일 이미지 편집
            image_path = input("참조 이미지 경로: ").strip()
            if not os.path.exists(image_path):
                print(f"파일을 찾을 수 없습니다: {image_path}")
                continue

            group = ReferenceImageGroup(slot=1, images=[image_path])
            task = ProcessingTask(
                task_id=task_id,
                task_type=TaskType.IMAGE_TO_IMAGE,
                prompt=prompt,
                reference_groups=[group],
                output_dir=output_dir,
                image_size=image_size
            )

        elif choice == "3":
            # 폴더 기반 병렬 처리
            folder_path = input("참조 이미지 폴더 경로 (slot1/, slot2/, ... 구조): ").strip()
            groups = create_reference_groups_from_folders(folder_path)

            if not groups:
                print("참조 이미지를 찾을 수 없습니다.")
                continue

            print(f"발견된 슬롯: {[g.slot for g in groups]}")

            task = ProcessingTask(
                task_id=task_id,
                task_type=TaskType.IMAGE_TO_IMAGE,
                prompt=prompt,
                reference_groups=groups,
                output_dir=output_dir,
                image_size=image_size
            )

        elif choice == "4":
            # 파일 목록 기반 병렬 처리
            print("이미지 파일 경로를 입력하세요 (빈 줄로 종료):")
            files = []
            while True:
                file_path = input("  > ").strip()
                if not file_path:
                    break
                if os.path.exists(file_path):
                    files.append(file_path)
                else:
                    print(f"    파일 없음: {file_path}")

            if not files:
                print("유효한 이미지 파일이 없습니다.")
                continue

            images_per_slot = int(input("슬롯당 이미지 수 (기본: 1): ").strip() or "1")
            groups = create_reference_groups_from_files(files, images_per_slot)

            task = ProcessingTask(
                task_id=task_id,
                task_type=TaskType.IMAGE_TO_IMAGE,
                prompt=prompt,
                reference_groups=groups,
                output_dir=output_dir,
                image_size=image_size
            )

        else:
            print("잘못된 선택입니다.")
            continue

        # 작업 실행
        print("\n처리 중...")
        result = asyncio.run(processor.process_task(task))

        print("\n" + "="*50)
        print("결과:")
        print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
        print("="*50)


def batch_mode(
    api_key: str,
    prompt: str,
    input_path: str,
    output_dir: str = "./output",
    image_size: str = "2K",
    mode: str = "folder"
):
    """배치 모드"""
    processor = ParallelImageProcessor(api_key)
    task_id = f"batch_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    if mode == "folder":
        groups = create_reference_groups_from_folders(input_path)
    elif mode == "files":
        # input_path를 콤마로 분리
        files = [f.strip() for f in input_path.split(",") if f.strip()]
        groups = create_reference_groups_from_files(files)
    else:
        # 텍스트 → 이미지
        groups = []

    task_type = TaskType.IMAGE_TO_IMAGE if groups else TaskType.TEXT_TO_IMAGE

    task = ProcessingTask(
        task_id=task_id,
        task_type=task_type,
        prompt=prompt,
        reference_groups=groups,
        output_dir=output_dir,
        image_size=image_size
    )

    result = asyncio.run(processor.process_task(task))
    return result


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Seedream 4.5 병렬 이미지 처리 도구",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
예시:
  # 대화형 모드
  python seedream_parallel.py --api-key YOUR_KEY

  # 텍스트 → 이미지
  python seedream_parallel.py --api-key YOUR_KEY --prompt "a cat" --mode text

  # 폴더 기반 병렬 처리
  python seedream_parallel.py --api-key YOUR_KEY --prompt "make it blue" \\
      --input ./images --mode folder --output ./results

  # 파일 목록 기반 병렬 처리
  python seedream_parallel.py --api-key YOUR_KEY --prompt "enhance" \\
      --input "img1.png,img2.png,img3.png" --mode files
        """
    )

    parser.add_argument("--api-key", "-k", required=True, help="Seedream API 키")
    parser.add_argument("--prompt", "-p", help="이미지 생성/편집 프롬프트")
    parser.add_argument("--input", "-i", help="입력 경로 (폴더 또는 콤마 구분 파일)")
    parser.add_argument("--output", "-o", default="./output", help="출력 폴더")
    parser.add_argument("--size", "-s", default="2K", choices=["1K", "2K", "4K"], help="이미지 크기")
    parser.add_argument("--mode", "-m", default="interactive",
                       choices=["interactive", "text", "folder", "files"],
                       help="실행 모드")
    parser.add_argument("--provider", default="aimlapi",
                       choices=["aimlapi", "byteplus"],
                       help="API 제공자")

    args = parser.parse_args()

    print_banner()

    if args.mode == "interactive":
        interactive_mode(args.api_key)
    else:
        if not args.prompt:
            print("오류: --prompt 옵션이 필요합니다.")
            sys.exit(1)

        result = batch_mode(
            api_key=args.api_key,
            prompt=args.prompt,
            input_path=args.input or "",
            output_dir=args.output,
            image_size=args.size,
            mode=args.mode
        )

        print("\n최종 결과:")
        print(json.dumps(result, indent=2, ensure_ascii=False, default=str))


if __name__ == "__main__":
    main()
