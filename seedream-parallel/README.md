# Seedream 4.5 Parallel Image Processing Tool

여러 이미지에 동일한 프롬프트를 **병렬로** 적용하는 도구입니다.

## 기능

- **텍스트 → 이미지**: 프롬프트만으로 이미지 생성
- **이미지 → 이미지**: 참조 이미지 + 프롬프트로 이미지 편집/변환
- **병렬 처리**: 최대 5개 슬롯으로 여러 이미지 동시 처리
- **유연한 입력**: 폴더 구조 또는 파일 목록 지원

## 설치

```bash
pip install -r requirements.txt
```

## 사용법

### 1. 대화형 모드 (권장)

```bash
python seedream_parallel.py --api-key YOUR_API_KEY
```

### 2. 텍스트 → 이미지

```bash
python seedream_parallel.py \
  --api-key YOUR_API_KEY \
  --prompt "a beautiful sunset over mountains" \
  --mode text \
  --output ./results
```

### 3. 폴더 기반 병렬 처리

폴더 구조:
```
./images/
  ├── slot1/
  │   ├── image1.png
  │   └── image2.png
  ├── slot2/
  │   └── image3.png
  └── slot3/
      └── image4.png
```

```bash
python seedream_parallel.py \
  --api-key YOUR_API_KEY \
  --prompt "make it look like watercolor painting" \
  --input ./images \
  --mode folder \
  --output ./results
```

### 4. 파일 목록 병렬 처리

```bash
python seedream_parallel.py \
  --api-key YOUR_API_KEY \
  --prompt "enhance the colors" \
  --input "img1.png,img2.png,img3.png,img4.png,img5.png" \
  --mode files \
  --output ./results
```

## 옵션

| 옵션 | 단축 | 설명 | 기본값 |
|------|------|------|--------|
| `--api-key` | `-k` | API 키 (필수) | - |
| `--prompt` | `-p` | 이미지 프롬프트 | - |
| `--input` | `-i` | 입력 경로 | - |
| `--output` | `-o` | 출력 폴더 | `./output` |
| `--size` | `-s` | 이미지 크기 (1K/2K/4K) | `2K` |
| `--mode` | `-m` | 실행 모드 | `interactive` |
| `--provider` | - | API 제공자 | `aimlapi` |

## 슬롯 시스템

참조 이미지를 최대 5개 슬롯으로 나누어 **병렬 처리**할 수 있습니다:

- **슬롯 1~5**: 각 슬롯은 독립적으로 API 호출
- **슬롯당 여러 이미지**: 한 슬롯에 여러 참조 이미지 가능 (최대 14개)
- **동일 프롬프트**: 모든 슬롯에 같은 프롬프트 적용

## Python 코드에서 사용

```python
from seedream_parallel import (
    ParallelImageProcessor,
    ProcessingTask,
    TaskType,
    ReferenceImageGroup
)
import asyncio

# 프로세서 생성
processor = ParallelImageProcessor(
    api_key="YOUR_API_KEY",
    max_concurrent=5
)

# 참조 이미지 그룹 설정
groups = [
    ReferenceImageGroup(slot=1, images=["ref1.png", "ref2.png"]),
    ReferenceImageGroup(slot=2, images=["ref3.png"]),
    ReferenceImageGroup(slot=3, images=["ref4.png"]),
]

# 작업 생성
task = ProcessingTask(
    task_id="my_task",
    task_type=TaskType.IMAGE_TO_IMAGE,
    prompt="transform into anime style",
    reference_groups=groups,
    output_dir="./output",
    image_size="2K"
)

# 실행
result = asyncio.run(processor.process_task(task))
print(result)
```

## API 제공자

현재 지원되는 API 제공자:

- `aimlapi` (기본): https://api.aimlapi.com
- `byteplus`: https://api.byteplus.com

## 라이선스

MIT License
