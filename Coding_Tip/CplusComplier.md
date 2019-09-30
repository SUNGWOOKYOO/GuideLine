# C++ code Complie Tip

## G++ Complier 

`g++ -std=[standard] [filename]` 을 하면 `./a.out` 생성 

```shell
# example
$ g++ -std=C++11 main.cpp 
$ ./a.out 
```



### Library

```c++
// 미리 컴파일된 헤더는 한번 제거하고 complie 해보자
# include <limits.h> // INT_MAX 등이 정의됨 
# include <algorithm> // reduce_shuffle() 등이 정의
# include <math.h> // floor() 등이 정의
```



## Sublime Text 

[Tutorial](https://jeonghakhur.gitbooks.io/sublime-text3/content/) [한글 Tutorial](https://www.opentutorials.org/module/406/3595)

### Sublime Text editor를 사용한 G++ complie

[blog 설명 link](https://miracleyoo.tistory.com/m/15)



### Sublime Text 단축기 지정

[기본 단축키 설명과 그림](https://codedragon.tistory.com/7211)

상단 **Preferences 탭** → **Key Bindings - User** 항목을 열어 다음의 코드를 추가해준다.

```shell
# 기존에 ctrl+shift+f로 설정된 shortcut이 있다면 자동으로 overriding된다.
[
	{
		"keys": ["ctrl+shift+f"], 
		"command": "reindent", 
		"args": {"single_line": false}
	}
]
```



### Sublime Text 깨끗히 삭제하는 법

[설명 link](https://dev-strender.github.io/articles/2018-06/reinstallation-of-sublime-text-3)

**프로그램 추가/제거** 로 검색한 후, 거기에서 다시 서브라임을 검색한 후 제거

```shell
C: > 사용자 > 사용자이름 > AppData > Roaming 에 있는 Sublime Text 폴더 제거
C: > 사용자 > 사용자이름 > AppData > Local 에 있는 Sublime Text 폴더 제거
```

