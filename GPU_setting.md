# GPU setting 방법 
[세욱 guide](https://docs.google.com/document/d/1vLYF9af7_VTs4RBzEhbzpAEofuTNHjTgIF5yIIiqyZY/edit#)

[연구실 guide](http://kdd.snu.ac.kr/wiki/index.php/GUIDE:GPU)



### 상식

GPU를 돌리기에 앞서 나의 gpu 머신이 어떤 graphic driver와 호환되는지 알아야한다. 

graphic driver는 cuda기반 programming으로 돌아가기 때문에, graph driver와 호환이 맞는 cuda, cudnn 등을 깔아야하며, tensorflow-gpu 역시 



### cuda
[버전에 맞는게 뭔지 확인](https://linuxconfig.org/how-to-install-the-nvidia-drivers-on-ubuntu-18-04-bionic-beaver-linux)
sudo apt-get update
sudo apt install ubuntu-drivers-common
ubuntu-drivers devices

사이트에서 unbuntu 버전에 맞게 다운로드 받고, 버전에 맞는 cuda deb 파일을 다운받아 설치   
cuda version check `$ nvcc --version`

---

# CUDA, Nvidia

[참고1](http://cslab.jbnu.ac.kr/board/bbs/board.php?bo_table=libfaq&wr_id=226) [참고2](https://tavris.tistory.com/24)이 글을 먼저 읽어보기

deb 파일로 설치하면, Nvidia graphics driver 도 install 됨(run 파일은 아님)

### PRE-INSTALLATION ACTIONS

기존에 설치되어 있는 것들을 제거하는 과정. 설치되어 있는가를 확인하려면

```bash
$ apt list --installed | grep nvidia
$ apt list --installed | grep cuda
```

제거하는 명령어:

```bash
$ sudo apt-get --purge remove '^cuda.*'
$ sudo apt-get --purge remove '^nvidia.*'
```

apt로 설치되지 않는 것들은 다음과 같이 제거해야 한다.

```bash
$ sudo /usr/local/cuda/bin/uninstall_cuda_X.Y.pl
$ sudo /usr/bin/nvidia-uninstall
```

마지막으로 제대로 제거되었는지 확인한다

```bash
$ ls -d /usr/local/cuda*
```



### Installation

* [cuda-toollkit-archieve](https://developer.nvidia.com/cuda-toolkit-archive) 에서 원하는 version > Linux > x86_64 > Ubuntu   버전 선택 > deb (network 로 골라야한다. local 로 하면 안됨) 에서 설치 파일 다운로드 후, sudo apt-get install cuda 를 제외한 적혀 있는 명령어 실행 

* 주의: sudo apt-get install cuda 를 실행하면 원하는 버전이 아니라 최신 버전으로 설치되는 문제가 있다. 따라서,

```bash
$ dpkg -l | grep cuda     # verify the version
$ sudo apt-get install cuda-X.X.XX     # input the version 
# e.g., sudo apt-get install cuda-X.X.XX
```

※ **이때, 사용하고자 하는 tensorflow-gpu 버전에 맞는 CUDA, cuDNN을 설치해야한다.   또한 이때 gpu 의 hardware에 맞는 CUDA, cuDNN 버전을 설치해야하므로 버전 체크 과정 필요**

[tensorflow gpu 지원 안내](https://www.tensorflow.org/install/gpu) (성욱 컴퓨터 기준으로 작성)  의 링크를 들어가서, **소프트웨어 요구사항** 읽어보기   

- [NVIDIA® GPU 드라이버](https://www.nvidia.com/drivers) - CUDA 10.0에는 410.x 이상이 필요합니다.

  - 내가 쓰는 gpu는  GTX 1060 6gb 따라서, 위의 link를 통해  hardware에 맞는 그래픽 드라이버를 검색해보면, 다음과 같이 나옴

    **LINUX X64 (AMD64/EM64T) DISPLAY DRIVER**

    | Version:          | 430.34       |
    | ----------------- | ------------ |
    | Release Date:     | 2019.7.9     |
    | Operating System: | Linux 64-bit |
    | Language:         | English (US) |
    | File Size:        | 105.05 MB    |
    
  - cpu architecture check  ```$ dpkg -s libc6 | grep Arch ```
  
  따라서, ~~CUDA 10.0 설치가능!!~~ (그런데, 설치 해보면 로그인 lock 현상 발생! 따라서, cuda 9.0 을 설치 하겠다. 또한,  그래픽 드라이버는 CUDA 를 deb로 깔면 자동으로 깔리므로 따로 설치할 필요없다.)

- [CUDA® Toolkit](https://developer.nvidia.com/cuda-toolkit-archive) - TensorFlow는 CUDA 10.0을 지원합니다(TensorFlow 1.13.0 이상).

  - [cuda-toollkit-archieve](https://developer.nvidia.com/cuda-toolkit-archive) 에서 원하는 version > Linux > x86_64 > Ubuntu   버전 선택 > deb (network 로 골라야한다. local 로 하면 안됨) 에서 설치 파일 다운로드 후, sudo apt-get install cuda 를 제외한 적혀 있는 명령어 실행 

  - ~~`$ sudo apt-get install cuda-10.0` 이라고 하면됨~~

  - `$ sudo apt-get install cuda-9.0` 이라고 하면됨

  - 설치 후 아마 재부팅을 요구할 것이다. 필요하면 재부팅한다.
    `$ sudo reboot`

  - RTX 계열은 CUDA 10이상을 설치하자
    tensorflow가 cuda10에서도 libcublas9.0을 찾는 경우가 존재하는데, 이 경우
    sudo apt-get install cuda-libraries-9-0
    명령어를 통해 해결할 수 있다.

    ** POST-INSTALLATION ACTIONS**
    ~/.bashrc 에 다음 lines 추가

    ```shell
    # cuda
    export CUDA_HOME=/usr/local/cuda
    export PATH=$CUDA_HOME/bin:$PATH
    export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH
    ```

  

  ---

  # [cuDNN SDK](https://developer.nvidia.com/cudnn)(7.4.1 이상)

  - [cuDNN link](https://developer.nvidia.com/cudnn) 에 들어가서 설치된 CUDA version 에 적합한 cuDNN vX.X.X Library for Linux 를 다운 받는다.
    다음 명령어 실행
    tar -xzvf cudnn-X.X-linux-x64-vX.tgz
    sudo cp cuda/include/cudnn.h /usr/local/cuda/include
    sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64
    sudo chmod a+r /usr/local/cuda/include/cudnn.h





**CUDA Toolkit 9.0 **



설치 파일 다운로드: https://developer.nvidia.com/cuda-90-download-archive?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1604&target_type=deblocalcd ~/Downloadssudo dpkg -i cuda-*

터미널에 뜨는 sudo apt-key add ... 명령어를 복붙 

sudo apt update

sudo apt install cuda

gedit ~/.bashrc맨 아래에 다음 내용 추가

export PATH=/usr/local/cuda-9.0/bin${PATH:+:${PATH}}

export LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}

재부팅

재부팅 후 설치 확인

cat /proc/driver/nvidia/version nvcc -Vnvidia-smi

------



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

------



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



------



**pip**

$ sudo apt install python-pip



------



**virtualenv**

$ pip install virtualenv