# Excel 2 json
![sheetImage](https://lh3.ggpht.com/e3oZddUHSC6EcnxC80rl_6HbY94sM63dn6KrEXJ-C4GIUN-t1XM0uYA_WUwyhbIHmVMH=w300)   

Google OAuth로 인증하고 drive의 text resource 를 가져와서 json 으로 변환해주는 내부 툴.

   
## 🛠 Setup
### 1. 프로젝트 만들고 api 활성화 하기
1. [Create project](https://developers.google.com/workspace/guides/create-project)
2. [Enable api](https://developers.google.com/workspace/guides/enable-apis) 에서 sheet api 활성화

### 2. Create credential 
1. [Google cloud platform console](https://console.developers.google.com/home) 열고
2. APIs & Services > Credentials 접근
3. OAuth client ID 만들기
4. Application type > Desktop application
5. 이름 -> Beflex i18n converter
6. 위 설정들 마치고 만든 OAuth client json 파일 다운로드
7. 본 프로젝트의 lib 폴더 안에 credentials.json 으로 저장
   
[참고 자료](https://developers.google.com/workspace/guides/create-credentials#oauth-client-id)
   
### 3. Install google client library
> pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
   
## 🧑‍💻 How to use?
1. python 가상환경을 사용하기 위해 terminal 에 해당 프로젝트 경로에 접근
2. ```. venv/bin/activate``` 명령으로 가상환경 활성화
3. ```python3 lib/main.py``` 로 실행
4. 구글 로그인
5. 프로젝트 i18n 폴더 경로 기재 (경로 변경을 원할 경우, asset 폴더 안의 **flutter_project_resource_path.txt** 내용 변경하면 됨)
6. 기재한 프로젝트 i18n 경로로 변환된 파일 저장됨.
