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
