# linux 를 다루는데 필요한 tip 

### 환경변수 추가 후 적용하는 코드 

환경변수를 추가하는 file은 보통 `~/.bashrc` 파일이다. 

따라서, `gedit ~/.bashrc` 를 실행 후, 아나콘다 가상환경을 activate 하기 위한 path를 적어논다고하면, 

`export PATH="/home/kddlab/anaconda3/etc/profile.d/conda.sh"` 와 같이 적을수 있고, 

적은 후에 shell script에서 
```shell
# 이렇게 command line을 치면 적용이 완료됨.
$ source ~/.bashrc 
```



### 파일에 대한 alias 를 설정하기

`~/.bashrc`파일에 alias를 설정해두면 파일에 직접가지 않더라도 바로 실행할 수 있게 된다. 

따라서, `gedit ~/.bashrc` 를 실행 후, pycharm을 실행하기 위한 alias를 만든다고하면,

다음의 예시와 같은 line을 추가 할 수 있다.

`alias pycharm="/home/kddlab/Downloads/pycharm-community-2019.2.2/bin/pycharm.sh"` 

```shell
# 바뀐 변수를 적용을 시킨뒤
$ source ~/.bashrc
# 실행하면 sh ~/pycharm.sh 와 같은 효과를 볼 수 있다.
$ pycharm 
```



### 바로가기 만들기
```shell
ln -s [path]
```



### sudo apt-get update 에러시

다음과 같은 명령어를 한 후, 다시 시도해본다. [stack overflow](https://askubuntu.com/questions/760574/sudo-apt-get-update-failes-due-to-hash-sum-mismatch)

```shell
$ sudo apt-get clean
$ sudo rm -r /var/lib/apt/lists/*
```

 update, upgrade, autoremove 를 번갈아 가면서 하다보면 해결되는 경우가 많다.

```shell
$ sudo apt-get update
```

