first date: 2019-07-03
@ swyoo 

# Anaconda 설치법 
[Anaconda 설치설명 blog](http://taewan.kim/tutorial_manual/dl_pytorch/02/install/linux_env/)
blog를 보고 설치하면 된다.

conda --version
path를 잡지 못한다면, path 설정을 vim ~/.bashrc 에 가서 해주고, source ~/.bashrc 를 통해 적용을 한다. 

which python 했을떄, 
/home/swyoo/anaconda3/bin/python 이렇게 나와야하며, 

conda list  했을때 설치 파일들이 나와야한다. 


### conda 가상환경 
$ conda info --env 명령시, conda environments를 몰수 있다. 

$ conda create -n <가상환경 이름> python=<버전정보>
e.g., conda create -n swyoo python=3.6 을 통해 python3.6 환경에서 작동하는 virtual environment를 구성할 수 있다. 

$ conda env remove -n <가상환경 이름> 
가상환경을 지울수 있다. 

$conda activate <가상환경 이름>
$conda deactivate 

### 가상환경 kernel 적용
가상환경에서 ... [link](https://tech.songyunseop.com/post/2016/09/using-jupyter-inside-virtualenv/)
$ pip install ipykernel  
$ python3 -m ipykernel install --user --name=<가상환경 이름>  
jupyter notebook 접속
Kernel> change kernel> <가상환경 이름>

### 버전에 맞는 modul 설치 
e.g., $ pip install tensorflow-gpu==1.8.0  
만약, downgrade 또는 upgrade를 원한다면,  
$ pip install --upgrade tensorflow-gpu==1.4.0  
이런식으로 사용하면 된다.

