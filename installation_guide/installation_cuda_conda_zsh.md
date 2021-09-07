# Development environment installation guidelines

This document provides installation commands for
[cuda](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html), [zsh](https://github.com/ohmyzsh/ohmyzsh), [anaconda](https://www.anaconda.com/), [dotfiles](https://github.com/wookayin/dotfiles) on Ubuntu.
The dotfile is provided by [wookayin](https://github.com/wookayin)

## Prerequisites
* Ubuntu >= 16.04
* Download [Anaconda installer](https://www.anaconda.com/products/individual)

## root >>
Install cuda manually following [NVIDIA CUDA Installation Guide for Linux](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html), and then


    sudo apt-cache search nvidia-driver
    sudo apt-get install nvidia-driver-4**
    sudo apt-get install cuda
    sudo apt-get nvidia-cuda-toolkit
    sudo reboot

    sudo apt-get install curl
    sudo apt-get install zsh

## user >>
    chsh -s $(which zsh)
    bash Anaconda3_LATEST.sh
    curl -fsSL https://dotfiles.wook.kr/etc/install | bash
    source /home/USERNAME/anaconda3/bin/activate
    conda init zsh
    dotfile update
