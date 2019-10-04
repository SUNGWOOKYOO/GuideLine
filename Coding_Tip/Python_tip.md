# 파이썬 소스코드가 실행되는 방식과 import의 동작 원리

이 [link](https://soooprmx.com/archives/2897) 를 보면  설명을 볼 수 있다.   

요약  

다음과 같은 파일이 있다고 하자. 

```python
# gcd.py
def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    return gcd(b, a % b)


x, y = [int(n) for n in input("두 수를 입력하세요:").split()[:2]]
g = gcd(x, y)
print("%d와 %d의 최대 공약수는 %d 입니다." % (x, y, g))
​```
```

그리고, 다른 py 파일에서 

```python
import gcd
​````
```

를  수행하는 시점에 해당 소스코드 내용이 모두 실행됨.



따라서, 모듈로 동작할때와 주 실행 프로그램으로 동작할 때를 구분한다. 

```
def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    return gcd(b, a % b)


if __name__ == '__main__':
    x, y = [int(n) for n in input("두 수를 입력하세요:").split()[:2]]
    g = gcd(x, y)
    print("%d와 %d의 최대 공약수는 %d 입니다." % (x, y, g))

​```
```

이렇게 gcd.py를 만들어 놓으면, 

python gcd.py 를 할때만 `__main__`  밑부분이 실행됨





# Tip

### path join하는법

os.path.join(<base directory>, <추가할 디렉토리 이름>)  

### 리눅스 실행결과를 파일로 저장 
리눅스에서 프로그램 실행했을때 화면에 뿌려지는 결과를 파일로 저장하는건 " > "  
예를 들어 실행 파일명이 `hello.py` 이고, 저장하고 싶은 파일명이 result.txt 인 경우  
`$ python hello.py > result.txt `  
화면 보면서 파일로 저장하는건 `$ python hello.py | tee result.txt`    
[출처](https://bumsei.tistory.com/381)
