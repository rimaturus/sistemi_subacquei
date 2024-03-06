## How to build the container

docker build -t sistemi_subacquei_image .

docker run -it --user ros --network=host --ipc=host -v $PWD/ros_ws:/home/ros/ros_ws -v /tmp/.X11-unix:/tmp/.X11-unix:rw --env=DISPLAY -v /dev:/dev --device-cgroup-rule="c *:* rmw" sistemi_subacquei_image

