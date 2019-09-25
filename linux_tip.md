# linux 를 다루는데 필요한 tip 

### 환경변수 추가 후 적용하는 코드 

환경변수를 추가하는 file은 보통 `~/.bashrc` 파일이다. 

따라서, gedit ~/.bashrc 를 실행 후, 아나콘다 가상환경을 activate 하기 위한 path를 적어논다고하면, 

`export PATH="/home/kddlab/anaconda3/etc/profile.d/conda.sh"` 와 같이 적을수 있고, 

적은 후에 shell script에서 
```shell
# 이렇게 command line을 치면 적용이 완료됨.
$ source ~/.bashrc 
```

