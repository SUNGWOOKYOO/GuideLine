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
path = os.getcwd() + '/Data/ml-1m'
path
```

