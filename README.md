# THISGLOBAL Website Rebuild

## 프로젝트 개요
- **이름**: THISGLOBAL Website
- **목표**: JSolution 레이아웃 구조를 참고하여 THISGLOBAL 웹사이트 재구축
- **주요 기능**: 반응형 디자인, 인터랙티브 슬라이더, 제품 쇼케이스, 문의 폼

## 🌐 URL
- **스테이징 사이트**: https://3000-ie56ezs2g1i5cf0s9r9dx-6532622b.e2b.dev
- **API 상태**: https://3000-ie56ezs2g1i5cf0s9r9dx-6532622b.e2b.dev/api/status
- **원본 사이트**: https://www.thisglobal.kr/
- **참고 사이트**: https://jsolution.kr/

## 📊 섹션 매핑 (JSolution → THISGLOBAL)

### 1. 헤더/내비게이션
- **JSolution 구조**: 드롭다운 메뉴가 있는 데스크톱 내비, 햄버거 메뉴 모바일
- **THISGLOBAL 적용**: 
  - 솔루션 (LED Display, Media Contents, Interactive Signage, TP LED)
  - 제품 (실내 LED, 실외 LED, 투명 LED, 플렉시블 LED)
  - 레퍼런스, 회사소개, 문의하기

### 2. 히어로 섹션
- **JSolution 구조**: 3개 슬라이드 자동 회전 캐러셀 (INNOVATION, INTELLIGENT, INTEGRITY)
- **THISGLOBAL 적용**: 
  - INNOVATION - Beyond of Signage Paradigm
  - INTERACTIVE - The Highest Interactive Signage
  - GLOBAL - LED Display & Media Contents

### 3. 비즈니스 영역
- **JSolution 구조**: 6개 제품 카드 그리드 레이아웃
- **THISGLOBAL 적용**: 
  - LED Display, Media Contents
  - Interactive Signage, TP LED
  - Outdoor Solutions, Rental Service

### 4. 레퍼런스/파트너
- **JSolution 구조**: 파트너 로고 자동 스크롤
- **THISGLOBAL 적용**: 6개 파트너 로고 플레이스홀더 (자동 스크롤)

### 5. 문의 폼
- **JSolution 구조**: 기본 연락 폼
- **THISGLOBAL 적용**: 회사명, 담당자명, 연락처, 이메일, 제목, 내용

### 6. 푸터
- **JSolution 구조**: 다중 컬럼 레이아웃
- **THISGLOBAL 적용**: 회사 정보, 솔루션 링크, 고객지원, 소셜 미디어

## 🎨 디자인 시스템
- **주요 색상**: 
  - Primary: #3039e5 (THISGLOBAL Blue)
  - Secondary: #0a1628 (Dark Navy)
  - Accent: #00d4ff (Cyan)
- **폰트**: Noto Sans KR
- **반응형 브레이크포인트**: 768px (모바일), 1024px (태블릿)

## 🔄 플레이스홀더 교체 가이드

### 이미지 플레이스홀더
위치: `/public/static/images/`

1. **제품 이미지 (600x400px)**
   - `placeholder-led-display.jpg` → LED 디스플레이 제품 이미지
   - `placeholder-media.jpg` → 미디어 콘텐츠 이미지
   - `placeholder-interactive.jpg` → 인터랙티브 사이니지 이미지
   - `placeholder-tp-led.jpg` → TP LED 이미지
   - `placeholder-outdoor.jpg` → 실외 솔루션 이미지
   - `placeholder-rental.jpg` → 렌탈 서비스 이미지

2. **파트너 로고 (200x100px)**
   - `placeholder-logo-1~6.png` → 실제 파트너사 로고

3. **소셜 미디어 이미지**
   - `og-image.jpg` (1200x630px) → OG 태그용 대표 이미지

### 텍스트/정보 교체
1. **회사 정보**
   - 주소: 실제 회사 주소로 교체
   - 전화: 실제 연락처로 교체
   - 이메일: info@thisglobal.kr 또는 실제 이메일

2. **소셜 미디어 링크**
   - Facebook, Instagram, YouTube, LinkedIn 실제 링크

## 🛠 기술 스택
- **프레임워크**: Hono (Cloudflare Workers)
- **스타일링**: Vanilla CSS, Tailwind (CDN)
- **아이콘**: Font Awesome 6.4
- **폰트**: Google Fonts (Noto Sans KR)
- **배포**: Cloudflare Pages
- **개발 서버**: PM2 + Wrangler

## 📦 주요 컴포넌트

### JavaScript 컴포넌트
1. **HeroSlider**: 자동 재생 캐러셀, 수동 컨트롤, 인디케이터
2. **MobileMenu**: 햄버거 메뉴 토글, 서브메뉴 아코디언
3. **ContactForm**: 폼 검증, AJAX 제출, 성공 모달
4. **PartnersSlider**: 무한 스크롤 로고 캐러셀
5. **SmoothScroll**: 앵커 링크 부드러운 스크롤

### CSS 모듈
1. **Header**: 고정 헤더, 드롭다운 메뉴
2. **Hero**: 풀스크린 슬라이더
3. **ProductGrid**: 반응형 카드 그리드
4. **ContactSection**: 폼 + 정보 카드
5. **Footer**: 다중 컬럼 레이아웃

## ✅ 완료된 기능
- ✅ 반응형 헤더/내비게이션 (데스크톱 드롭다운, 모바일 햄버거)
- ✅ 히어로 슬라이더 (자동 재생, 수동 컨트롤)
- ✅ 제품/솔루션 그리드 섹션
- ✅ 파트너 로고 캐러셀
- ✅ 문의 폼 (검증, 피드백)
- ✅ 반응형 푸터
- ✅ 기본 SEO 메타 태그
- ✅ Open Graph 태그

## 🚧 추가 개발 필요
1. 실제 이미지 및 로고 교체
2. 실제 회사 정보 업데이트
3. 백엔드 API 연동 (문의 폼 이메일 전송)
4. 각 제품/솔루션 상세 페이지
5. 다국어 지원 (한/영)
6. 애니메이션 효과 강화
7. 성능 최적화 (이미지 최적화, lazy loading)
8. Google Analytics 통합

## 📝 배포 방법

### 로컬 개발
```bash
cd /home/user/webapp
npm run build
pm2 start ecosystem.config.cjs
```

### Cloudflare Pages 배포
```bash
npm run build
cp -r public/* dist/
npx wrangler pages deploy dist --project-name thisglobal-webapp
```

## 📌 참고사항
- 모든 플레이스홀더 이미지는 실제 THISGLOBAL 콘텐츠로 교체 필요
- 문의 폼은 현재 프론트엔드만 구현 (백엔드 연동 필요)
- 색상 스키마는 THISGLOBAL 브랜드 컬러 (#3039e5) 기반

## 🔗 관련 링크
- [Hono Documentation](https://hono.dev/)
- [Cloudflare Pages](https://pages.cloudflare.com/)
- [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/)

---
최종 업데이트: 2025-08-16