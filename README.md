# jenkins-pipelines-project
![d](https://user-images.githubusercontent.com/60678531/150051193-cbfe89a0-b1f6-4d8f-aaec-d8d8bfd302f5.png)

----------------------------------------------------------------------------
1. code작업이 다 끝난 후 git commit만하면 Jenkins에서 인식
2. Jenkins에서 Dockerfile를 읽어서 Dokcer Image를 만든다.
3. Docker Container로 배포를 하게된다.
4. 배포가 완료되면 Docker hub를 Image를 push하여 저장한다. 

## Project에 필요한 파일목록
![image](https://user-images.githubusercontent.com/60678531/150052082-88820e82-009a-4ae4-b53d-13ab697dc5e7.png)
1. Docker Image를 만들기 위한 Dockerfile
2. Jenkin에서 인식할 수 있는 Jenkinsfile
3. Dockerfile를 컨테이너로 만들어주는 Docker-compose.yml
4. main.py code가 있는 파이썬 파일
5. requirements.txt main.py에서 사용되는 라이브러리 

## Jenkins
![image](https://user-images.githubusercontent.com/60678531/150054299-1e4226c4-71e8-4bae-90b5-0bfaa4b69b15.png)


# 과정 시각화
## commit 
![image](https://user-images.githubusercontent.com/60678531/150054816-6cc0a577-e9d7-466f-84ca-bb66f9089d7a.png)
## docker container check
![image](https://user-images.githubusercontent.com/60678531/150054899-2a06c49a-9af2-4e7d-a53d-ecf6c3429bd2.png)
## Jenkins 
![image](https://user-images.githubusercontent.com/60678531/150054994-9d97e790-8614-4efe-b8cc-b36cc381180e.png)

![image](https://user-images.githubusercontent.com/60678531/150055028-6a247699-b877-49aa-9bb5-0a75e6f17bbe.png)

## docker ps check
![image](https://user-images.githubusercontent.com/60678531/150055600-c271681b-c449-41f8-8d5b-5f9d4e2e9bbe.png)

## buid deploy check
![image](https://user-images.githubusercontent.com/60678531/150055721-8095642e-b917-4e9c-9f2e-82eac401e142.png)
-----------------------------------------------------
#### code 변경후 자동으로 배포된걸 확인 할 수 있다. 
