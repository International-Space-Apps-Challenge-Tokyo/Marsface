# coding: utf-8
import os
from fabric.api import local, sudo, cd, lcd



"""
大前提:fabric, pip, source code一式

やること:
アプリが利用するするライブラリをインストール


beautifulsoup
ipython
numpy,scipy,pandas
matplotlib
tornado
<mecab一式>

"""
def install_build():
    local("sudo apt-get install build-essential")

def install_bs():
    local("sudo pip install beautifulsoup")


def install_mathpkgs():

    local("sudo apt-get install python-numpy")
    local("sudo apt-get install python-scipy")
    local("sudo pip install numpy")
    local("sudo pip install scipy")
    local("sudo pip install pandas")
    local("sudo pip install httplib2")
    local("sudo pip install ujson")
    local("sudo pip install boost_python")

def install_matplotlib():
    local("sudo apt-get install python-matplotlib")


def install_ipython():
    local("sudo pip install ipython")
    local("sudo pip install pyzmq")
    local("sudo pip install jinja2")
    local("sudo pip install tornado --upgrade")
    
def install_caffe():
    local("sudo sudo apt-get install libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libboost-all-dev libhdf5-serial-dev")

def install_google_logging():
    local("wget https://google-glog.googlecode.com/files/glog-0.3.3.tar.gz")
    local("tar zxvf glog-0.3.3.tar.gz")
    with lcd("glog-0.3.3"):
        local("pwd")
        local("./configure")
        local("make")
        local("sudo make install")
    


def demo1_deploy():
#    install_build()
#    install_bs()
#    install_mathpkgs()
#    install_matplotlib()
#    install_ipython()
#    install_caffe()
    install_google_logging()
