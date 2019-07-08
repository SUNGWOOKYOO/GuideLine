# 소스 코드 작성 요령

버전에 맞는 library를 사용해야 dependency 문제가 없다.  따라서, 다음과 같은 버전체크와 path를 명시

```python
'''
Created on July 1, 2019
@author: SungWook Yoo 
'''
import tensorflow as tf
from platform import python_version
import os
!type python
print(python_version())
print(tf.__version__)
# path = os.getcwd() + '/Data/ml-1m'
# os.path.join(<base directory>, <추가할 디렉토리 이름>)
path = os.path.join(os.getcwd(), 'Data/ml-1m')
path
```



# jupyter notebook 원격접속 서버 설정 

### prerequsite: juptyer가 설치 되어 있어야한다.

1. config 파일 만들기 

   `$jupyter notebook --generate-config`

   실행결과: `Writing default to : ...# <= 이 디렉토리에 jupyter_notebook_config.py 생성`

   `...` = `/home/swyoo/.jupyter/jupyter_notebook_config.py`

2. ipython으로 비밀번호 설정

   ```python
   $ ipython #실행 후
   In [1]: from notebook.auth import passwd
   In [2]: passwd() 
   #입력하면 pw 입력하라고 뜬다, 그럼 입력해주세요
   Out [2]: '.......' #'...'의 ...은 본인의 패스워드 입니다. <= 복사해주세요!
   #ipython 종료
   exit()
   ```

3. 패스워드를 config하기 

   ```python
   $ vi /your/dir/for/jupyter_notebook_config.py
   
   c.NotebookApp.ip = '내 ip'
   c.NotebookApp.password=u'sha1:....' 
   c.NotebookApp.open_browser = False #원래 True
   ```

4. `$ jupyter notebook ` 실행

### Tip 

vi editor에서 원하는 text 찾을때, 명령어 모드에서  

` :?<검색어> `# 윗방향으로 검색 

`:/<검색어>` # 아랫방향 검색

`n` 누르면 다음 단어

`u` 누르면 이전 되돌리기

`ctrl + F6`  강제종료  나중에 *.swp 폴더도 지워주어야함









