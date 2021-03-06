<<<<<<< HEAD
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



###  SSH 다른 포트 추가하기

openssh server를 구동시킬때 방화벽에 의해 22번 포트가 막혀있을 수 있다.

따라서,  원격 접속 시 방화벽이 동작하지않는 다른 포트를 열어줄 필요가 있을 때 사용 가능 하다.

[zeta wiki](https://zetawiki.com/wiki/SSH_%ED%8F%AC%ED%8A%B8_%EC%B6%94%EA%B0%80%ED%95%98%EA%B8%B0)

```shell
# 외부 포트도 열어주기
$ gedit /etc/ssh/sshd_config
"""
Port 22 
Port 9999 # 9999 포트 추가
"""

# 9999 port 방화벽 허용 
$ sudo ufw allow 9999
```

sudo ufw allow 22

[ufw 사용법 korean blog](https://webdir.tistory.com/206)



### Linux에서 ssh 를 통해 원격 로그인하기

`ssh -p [포트번호] [로그인이름]@[host ip]`

```shell
# 지정된 포트를 통해 연결
# 접속 후 비밀번호도 입력
$ ssh -p 10022 kddlab@147.46.244.243
```



### ssh 재시작

```shell
$ sudo service ssh restart
=======
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



###  SSH 다른 포트 추가하기

openssh server를 구동시킬때 방화벽에 의해 22번 포트가 막혀있을 수 있다.

따라서,  원격 접속 시 방화벽이 동작하지않는 다른 포트를 열어줄 필요가 있을 때 사용 가능 하다.

[zeta wiki](https://zetawiki.com/wiki/SSH_%ED%8F%AC%ED%8A%B8_%EC%B6%94%EA%B0%80%ED%95%98%EA%B8%B0)

```shell
# 외부 포트도 열어주기
$ gedit /etc/ssh/sshd_config
"""
Port 22 
Port 9999 # 9999 포트 추가
"""

# 9999 port 방화벽 허용 
$ sudo ufw allow 9999
```

sudo ufw allow 22



### Linux에서 ssh 를 통해 원격 로그인하기

`ssh -p [포트번호] [로그인이름]@[host ip]`

```shell
# 지정된 포트를 통해 연결
# 접속 후 비밀번호도 입력
$ ssh -p 10022 kddlab@147.46.244.243
```



### ssh 재시작

```shell
$ sudo service ssh restart
>>>>>>> c9fce03def20851d43b6a1837032d1a4f6389c3a
```