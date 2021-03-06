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



### git add, git commit 취소 

[korean blog](https://gmlwjd9405.github.io/2018/05/25/git-add-cancle.html)

**add 취소 **

 실수로 git add * 명령을 사용하여 모든 파일을 Staging Area에 넣은 경우,
Staging Area(git add 명령 수행한 후의 상태)에 넣은 파일을 빼고 싶을 때가 있다.

뒤에 파일명이 없으면 add한 파일 전체를 취소한다.
file.txt 파일을 Unstaged 상태로 변경해보자.

`$ git reset HEAD [file]` 명령어를 통해 git add를 취소할 수 있다.

```shell
# CONTRIBUTING.md 파일을 Unstage로 변경한다.
$ git reset HEAD file.txt
Unstaged changes after reset:
M	file.txt
```

**commit 취소**

`$ git reset HEAD^` 명령어를 통해 git commit을 취소할 수 있다.

```shell
$ git reset HEAD^
```



### 원격저장소 다루기 

[생활코딩 블로그](https://cjh5414.github.io/get-git-remote-branch/)

**push**

 로컬 저장소의 branch 를 push 하고싶은 경우, 다음과 같은 명령 사용

* `$ git checkout [experiment branch]`

* `$ git push [원격저장소 이름] [원격저장소에 만들 branch 이름]`

```shell
# 먼저 push하고싶은 로컬 저장소로 checkout을 한 후,
$ git checkout exp
# 원격저장소에 새로운 branch를 push한다.
$ git push origin exp
```



**pull**

*  `$ git checkout -t [원격저장소 이름]`

`-t` 옵션과 `원격 저장소의 branch 이름`을 입력하면 로컬의 동일한 이름의 branch를 생성하면서 해당 branch로 checkout을 한다.

만약 branch 이름을 변경하여 가져오고 싶다면 `$ git checkout -b [생성할 branch 이름] [원격 저장소의 branch 이름]` 처럼 사용하면 된다.

```shell
# 원격 저장소를 업데이트 한후 
$ git remote update 
# 원격 저장소와 로컬 저장소의 branch 목록을 확인한다.
$ git branch -a
# 원격 저장소의 브랜치를 로컬 저장소로 그대로 가져온다.
$ git checkout -t origin/exp
```



### 원격 저장소 특정 브랜치만 지우기

```shell
$ git push <remote_name> --delete <branch_name>
```

