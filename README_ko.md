# Okteto Application example with automated github action
적용 사이트 - https://api-sunghoonism.cloud.okteto.net/

## 넘길다;읽기시렁:
---
이 저장소를 포크하고 아래 설명대로 진행하세요.
1. https://cloud.okteto.com 의 settings 메뉴에서 "New Token"을 눌러서 `okteto` Personal Access Token 을 발급 받으세요.
2. 발급받은 `okteto` Personal Acess Token의 값을 사용하여 `OKTETO_TOKEN`이라는 이름으로 Repository secret를 만듭니다.  
   ('포크'한 저장소의 Settings -> Secrets 메뉴에서 "New repository secret" 버튼을 눌러 repository secret을 만들 수 있습니다.)
3. .github/workflows/workflow.yml 파일의 19, 24 줄에 본인의 `okteto` 네임스페이스명을 넣으세요.  
<h3> 이게 다예요! </h3>
<br>

## 기타 설명
---
- `okteto`는 다양한 방법의 빌드 및 배포를 지원하나, 여기서는 docker-compose 파일을 이용한 방법을 사용하였습니다.
- docker-compose의 주석을 해제하여 redis를 이용할 수 도 있습니다.
- 어플리케이션은 fastapi를 활용하여 만들어졌습니다. /docs , /redoc 경로 사용 가능합니다.