# SSH 란 ?

[기본 설명 link](https://jimnong.tistory.com/713)

**요약**

```shell
# ssh 가 구동되고 있는지 확인한다.
$ dpkg -l |grep openssh
$ sudo apt-get update 
$ sudo apt-get install openssh-server
# openssh-server가 설치되었나 확인한다.
$ dpkg -l |grep openssh
```



**에러발생시**

openssh  설치 과정에서 에러 발생할 수 있다. [stack overflow](https://askubuntu.com/questions/914428/unmet-dependencies-when-trying-to-install-r-base/965162)

따라서,  다음과 같은 업데이트를 통해 해결하였다. 

```shell
$ sudo apt install --fix-broken
$ sudo apt-get update
$ sudo apt-get upgrade
```



# SSH 연결하기

```shell
# ssh 서비스 시작
$ sudo service ssh start
# 서비스가 실행 중인지 확인
$ service --status-all |grep +
# ssh 서비스가 점유 하고있는 포트번호 확인
$ sudo netstat -antp
```



### Putty 를 통해 접속하기

[영문 설명 링크](https://itsfoss.com/putty-linux/)

```shell
$ sudo add-apt-repository universee
$ sudo apt update
$ sudo apt install putty
# putty를 실행한다
$ putty
```

putty를 실행한 뒤 , 세션에 연결하고자하는 ip를 호스트에 추가하여 접속한다.



### Window에서 원격으로 GUI 사용하기

xming이라는 프로그램과 putty를 이용하여 GUI를 원격으로 구동시킬 수 있다. [설명 link](https://talkingaboutme.tistory.com/entry/Linux-X11-Forwarding-using-PuTTY)

 Xming을 설치 후에, putty의 Configuration> Connection>  SSH > X11 에서 X11 forwarding에 체크를 해주면 사용가능 한 것 같다.



### Putty 에서 F1, F2, .. . 등이 작동이 안될때

Change Setting > Keyboard > xterm R6 를 선택하여 사용한다. [link](https://ttend.tistory.com/274)

