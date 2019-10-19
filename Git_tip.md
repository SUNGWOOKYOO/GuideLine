# Git 사용법 tip

### 기존 remote repository 제거 

```shell 
$ git remote remove origin
```

### untracted file과 directory 제거 방법 [link](https://blog.outsider.ne.kr/1164)
```shell
# 지우기전에 어떤 것들이 지워질지 확인 가능  
$ git clean -fd --dry -run   
# file과 directory를 모두 지음
$ git clean -fd 
```



### 현재 branch를 master branch로 바꾸기 [link](http://egloos.zum.com/YSocks/v/511600)

```shell
# current branch list
# * master
# * branch
git checkout branch 
git merge --strategy=ours master
git checkout master
git merge branch 
```

