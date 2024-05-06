## System reqs
***Ubuntu 22.04*** and 
***Needed Nvidia GPU***

## Prerequisites:
I heartly recommend to do this before the next steps:
  1) Install docker: following [this guide](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04), but you can do launching the ***docker_install.sh*** script you can find in ***Scripts*** folder
  2) Now check if you have the right Nvidia drivers on you pc:
       1) Open a terminal and launch ```nvidia-smi -L```
       2) If return something like this: ```GPU 0: NVIDIA GeForce RTX 4090 (UUID: GPU-fa3da260-9c42-828f-981a-f6d7b48d77b3)``` , everything works fine.
       3) If **NOT**... cry... I'm joking, let's install the driver on your pc following this guide [Nvidia driver](https://www.nvidia.it/Download/index.aspx?lang=it)
       
  3) Install Nvidia container toolkit: following [this guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html), but you can do launching the ***nvidia_toolkit_install.sh*** script you can find in ***Scripts*** folder

## How to build the container
Now you can create the container:
  1) Go inside the main cloned folder ***sistemi_subacquei/***
  2) Open a terminal inside this folder *(right-click -> open a terminal inside this folder)*
  3) Build the custom docker image: ```docker build -t sistemi_subacquei_image .``` *(include the endpoint)*
  4) Attach a container to that image: ```docker run -it --user ros --gpus all --network=host --ipc=host -v $PWD/catkin_ws:/home/ros/catkin_ws -v /tmp/.X11-unix:/tmp/.X11-unix:rw --env=DISPLAY -v /dev:/dev --device-cgroup-rule="c : rmw" sistemi_subacquei_image --name container_sistemi_subacquei``` 
  5) Now you are inside the container with ***Ubuntu 18.04 and ROS1 Melodic*** already setup
  6) ***Basic command***:
     1) If you want to exit it and return to your basic system use **CTRL + D**
     2)  If you want to start your container *(use at the start of your pc)*: ```docker start container_sistemi_subacquei```
     3)  If you want to go inside the container from your basic system: ```docker exec -it container_sistemi_subacquei /bin/bash```
     4)  You can use the previous command to enter the container also from every new basic system terminal

