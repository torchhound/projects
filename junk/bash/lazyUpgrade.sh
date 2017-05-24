#!/bin/bash

#pacman-key --init
#pacman-key --populate archlinux
#pacman-key --refresh-keys

rm -rf ~/initramfs-linux-fallback.img ~/initramfs-linux-grsec-fallback.img
mv /boot/initramfs-linux-fallback.img ~
mv /boot/initramfs-linux-grsec-fallback.img ~
pacman -Syyu
