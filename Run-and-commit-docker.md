**Docker 실행**

```shell
docker run -i -t -v /Users/kimyewon/Documents/sample:/sample mlearn:init
```



**scikit-learn 라이브러리 설치**

```
pip install -U scikit-learn scipy matplotlib scikit-image
```

**pandas 설치**

```
pip install pandas
```





**기존에 있던 도커 컨테이너에 덮어쓰기**

`exit` 으로 도커 밖으로 나온 후,

```
docker ps -a
```

위 명령어를 입력하면 최근에 사용한 도커의 목록이 나옴. 이때 앞서 설치한 라이브러리가 있는 도커의 ID를 복사한 후 commit 명령어 실행

```
docker commit <ID> mlearn:init
```





**다시 도커 실행**

```
docker run -i -t -v /Users/kimyewon/Documents/sample:/sample mlearn:init /bin/bash
```



