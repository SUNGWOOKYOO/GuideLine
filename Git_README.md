# 기존 remote repository 제거 
$ git remote remove origin

### untracted file과 directory 제거 방법 [link](https://blog.outsider.ne.kr/1164)
$ git clean -fd --dry -run   
지우기전에 어떤 것들이 지워질지 확인 가능  
$ git clean -fd 
file과 directory를 모두 지음

