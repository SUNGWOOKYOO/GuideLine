# python for loop visualization 

### tqdm

```python
from tqdm import trange
from time import sleep

# 기본 사용법 
s = 0
for i in trange(10, desc="iteration"):
    s += i
    # sleep(0.01)
```

[stackoverflow](https://stackoverflow.com/questions/42212810/tqdm-in-jupyter-notebook)

```python
import sys
from time import sleep
from tqdm import tqdm

num = 3
with tqdm(total=3, file=sys.stdout) as pbar:
    for i in values:
        pbar.set_description('processed: %d' % (1 + i))
        pbar.update(1)
        sleep(0.1)
```



### progress

