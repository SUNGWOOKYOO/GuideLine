## 유용한 설정 옵션



### janus (미리 설정된 패키지)[편집](http://kdd.snu.ac.kr/wiki/index.php?title=VIM&action=edit&section=11)

janus: 자주 사용되는 편한 설정을 쉽게 적용할 수 있는 패키지 (https://github.com/carlhuda/janus)

```
sudo apt-get install vim git rake curl -y

curl -L https://bit.ly/janus-bootstrap | bash
```

이것만 하면 다른 설정 없이도 어느 정도 사용 가능

### Colorscheme[편집](http://kdd.snu.ac.kr/wiki/index.php?title=VIM&action=edit&section=12)

터미널에 찍히는 텍스트 색깔에 대한 프리셋을 선택할 수 있다. 설정 방법은 .vimrc 파일에 아래의 명령어를 추가해주면 된다.

```
colorsheme 스킨이름
```

### vimrc[편집](http://kdd.snu.ac.kr/wiki/index.php?title=VIM&action=edit&section=13)

~/.vimrc이 vim 설정 파일이며, 이 파일에 아래 내용을 입력하면 된다. (없으면 새로 만들면 된다)

자주쓰는 설정들은 찾아보면 잘 나오므로, 여기에는 그 외에 쓸만하다고 생각하는 옵션들을 나열하였다.

**참조**) C++ 프로그래밍 환경을 위한 기본 옵션

```
if has("syntax")
   syntax on
endif
set autoindent
set cindent
set nu
set cursorline
```

## 플러그인[편집](http://kdd.snu.ac.kr/wiki/index.php?title=VIM&action=edit&section=14)

[플러그인 모음](https://vimawesome.com/)


VIM에는 플러그인을 추가하여 더 편리한 텍스트 편집환경을 구축할 수 있다. 먼저 Vundle이라는 플러그인 관리자를 설치해서 플러그인 추가를 자유롭게 할 수 있도록 세팅을 할 수 있다. [설치가이드](https://github.com/VundleVim/Vundle.Vim#quick-start)

```
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
```