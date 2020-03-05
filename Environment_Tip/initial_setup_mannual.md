**Dependency**

https://www.tensorflow.org/install/source



**CUDA Toolkit 9.0 **



설치 파일 다운로드 deb(local): https://developer.nvidia.com/cuda-90-download-archive?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1604&target_type=deblocalcd 

cd ~/Downloads 

sudo dpkg -i cuda-*

터미널에 뜨는 sudo apt-key add ... 명령어를 복붙 

sudo apt update

sudo apt install cuda

gedit ~/.bashrc맨 아래에 다음 내용 추가

export PATH=/usr/local/cuda-9.0/bin${PATH:+:${PATH}}

export LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}

재부팅

재부팅 후 설치 확인

cat /proc/driver/nvidia/version nvcc -Vnvidia-smi

---



**cuDNN 7.0** 



social ID로 로그인 (google )

설치 파일 링크: https://developer.nvidia.com/rdp/cudnn-download

위 링크에서 cuDNN v7.0.5 for CUDA 9.0 다운로드 ([cuDNN v7.0.5 Library for Linux](https://developer.nvidia.com/compute/machine-learning/cudnn/secure/v7.0.5/prod/9.0_20171129/cudnn-9.0-linux-x64-v7))

cd Downloads

tar xvzf cudnn-9.0-linux-x64-v7.tgz

cd cuda

sudo cp include/cudnn.h /usr/local/cuda-9.0/include

sudo cp lib64/* /usr/local/cuda-9.0/lib64

sudo chmod a+r /usr/local/cuda-9.0/include/cudnn.h /usr/local/cuda-9.0/lib64/libcudnn*

설치 확인

cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2

---



 **Bazel v0.9.0**

우선 oracle JDK-8 설치 필요

Add the java 8 repo to apt-get

```java
$ sudo add-apt-repository ppa:webupd8team/java
이후 Enter
```

Again update the apt-get repo

```java
$ sudo apt-get update
```

Finally install java 8

```java
$ sudo apt-get install oracle-java8-installer
```

오류가 난다면 

sudo apt -get install -f

그래도 오류가 나면

/var/lib/dpkg/info 폴더로가서

sudo rm openjdk-9-*

sudo dpkg --configure -a

이후

sudo apt -get install -f



설치파일 링크 : https://github.com/bazelbuild/bazel/releases/tag/0.9.0

bazel_0.9.0-linux-x86_64.deb 를 받아서 

$ sudo dpkg -i baze

설치됬는지 확인은

bazel version



---



**pip**

$ sudo apt install python-pip



---



**virtualenv**

$ pip install virtualenv

