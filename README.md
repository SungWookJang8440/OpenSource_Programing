# 🚀 My Development Profile & API Server
> TADD(Test+AI Driven Development)와 객체지향 리팩토링이 적용된 개인 포트폴리오 웹 서비스 및 API 서버입니다.

## 📸 1. Visual Demonstration
<img width="1887" height="787" alt="Image" src="https://github.com/user-attachments/assets/1d6e12b1-fc28-4a33-9d81-c85195419ee0" />


## 🎯 2. Motivation & Problem
처음에는 단순한 자기소개 텍스트를 반환하는 웹 서버(Mini_project1)로 시작했습니다. 하지만 코드가 복잡해질수록 확장과 유지보수가 어려워지는 문제를 겪었습니다. 
이를 해결하기 위해 **TADD(Test+AI Driven Development)** 방법론과 **객체지향 설계(Strategy Pattern)**를 도입하여 코드 스멜을 제거하고 구조를 개선했습니다. 또한, 협업 생태계를 고려하여 Flasgger와 Sphinx를 활용한 자동화된 문서 환경(Single Source of Truth)을 구축했습니다.

## ✨ 3. Key Features
총 4개의 핵심 라우트로 구성되어 있습니다.
1. **`/` (Home)**: API 서버 접속 환영 메시지 및 메인 화면 렌더링
2. **`/profile` (Profile)**: 개발자(장성욱 - 경북대학교 컴퓨터학부)의 기본 인적 사항 출력
3. **`/skills` (Skills)**: 주력 개발 스택(Python 등) 출력
4. **`/register` (Password API)**: TADD로 개발된 안전한 비밀번호 검증 로직 (8자 이상, 대문자/숫자 포함 여부 검사 및 클라이언트/서버 단 이중 검증)

## 🛠️ 4. Tech Stack & Rationale
* **Python / Flask**: 빠르고 가벼운 백엔드 API 및 웹 서버 구축을 위해 선택했습니다.
* **Pytest**: TDD 방법론을 적용하여 리팩토링 시 코드가 망가지지 않음을 증명하는 안전망(Safety Net)으로 활용했습니다.
* **Flasgger (Swagger)**: API 사용자(클라이언트)를 위한 인터랙티브 API 명세서를 제공하여 DX(Developer Experience)를 향상시켰습니다.
* **Sphinx**: 코드를 유지보수하는 동료 개발자를 위해 Python 코드 내부 구조 문서를 자동화했습니다.

## 🚀 5. Getting Started
```bash
# 1. 저장소 클론
git clone [https://github.com/SungWookJang8440/OpenSource_Programing.git](https://github.com/SungWookJang8440/OpenSource_Programing.git)
cd OpenSource_Programing

# 2. 패키지 설치
pip install -r requirements.txt

# 3. 서버 실행
python app.py