# window 에서 unbuntu 사용하기 

### 설치
[설치 및 삭제 방법](https://www.howtoinstall.co/en/ubuntu/xenial/byobu?action=remove)

### byobu 사용
[byobu 사용시 발생 문제 stack overflow](https://askubuntu.com/questions/492802/byobu-weird-character)
```shell
$ byobu-config
```
에서 "Toggle Status Notifications", de-selecting "logo", and then pressing "Apply".


### 바로가기 만들기 
ln -s <경로>
e.g., ln -s /mnt/c/Git



## Tip
ctrl + s 누르면 화면이 멈추는데 ctrl + q 를 누르면 풀림  
F6 누르면 byobu 나감  
ctrl + F7 누르면 위로 커서 올려서 볼 수 있음  
ctrl + F6: session 강제종료    

[byobu session 다루기](https://askubuntu.com/questions/196290/name-a-byobu-session)

```shell
# 누가 session을 만들었는지 본다.
$ byobu list-session
# 내 세션을 만든다. 
$ byobu new -s <session_name> 
e.g. $ byobu new -s swyoo
```



## Link

[정리가 잘 되어있는 블로그](https://eungbean.github.io/2018/08/29/gpu-monitor-with-byobu/)
