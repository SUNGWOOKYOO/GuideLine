# GPU setting 방법 
[guide](https://docs.google.com/document/d/1vLYF9af7_VTs4RBzEhbzpAEofuTNHjTgIF5yIIiqyZY/edit#)

[연구실 guide](http://kdd.snu.ac.kr/wiki/index.php/GUIDE:GPU)

### cuda
[버전에 맞는게 뭔지 확인](https://linuxconfig.org/how-to-install-the-nvidia-drivers-on-ubuntu-18-04-bionic-beaver-linux)
sudo apt-get update
sudo apt install ubuntu-drivers-common
ubuntu-drivers devices

사이트에서 unbuntu 버전에 맞게 다운로드 받고, 버전에 맞는 cuda deb 파일을 다운받아 설치   
cuda version check `$ nvcc --version`

---

## CUDA Installation

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
  
  따라서, CUDA 10.0 설치가능!! (그래픽 드라이버는 CUDA 를 deb로 깔면 자동으로 깔리므로 따로 설치할 필요없다.)

- [CUDA® Toolkit](https://developer.nvidia.com/cuda-toolkit-archive) - TensorFlow는 CUDA 10.0을 지원합니다(TensorFlow 1.13.0 이상).

  - [cuda-toollkit-archieve](https://developer.nvidia.com/cuda-toolkit-archive) 에서 원하는 version > Linux > x86_64 > Ubuntu   버전 선택 > deb (network 로 골라야한다. local 로 하면 안됨) 에서 설치 파일 다운로드 후, sudo apt-get install cuda 를 제외한 적혀 있는 명령어 실행 

  - `$ sudo apt-get install cuda-10.0` 이라고 하면됨

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

- [cuDNN SDK](https://developer.nvidia.com/cudnn)(7.4.1 이상)

  - [cuDNN link](https://developer.nvidia.com/cudnn) 에 들어가서 설치된 CUDA version 에 적합한 cuDNN vX.X.X Library for Linux 를 다운 받는다.
    다음 명령어 실행
    tar -xzvf cudnn-X.X-linux-x64-vX.tgz
    sudo cp cuda/include/cudnn.h /usr/local/cuda/include
    sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64
    sudo chmod a+r /usr/local/cuda/include/cudnn.h