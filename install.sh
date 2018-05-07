#!/usr/bin/env bash
ln -s $(pwd)/uni-launch.desktop ~/.local/share/applications/
sudo mkdir /opt/unilauncher/
sudo ln -s $(pwd)/app.py /opt/unilauncher/
sudo chmod +x /opt/unilauncher/app.py
xdg-mime default uni-launch.desktop x-scheme-handler/remmina
xdg-mime default uni-launch.desktop x-scheme-handler/ssh
