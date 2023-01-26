FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get upgrade -y

# Python
RUN apt-get install -y python3 python3-pip
RUN python3 -m pip install -U setuptools ipython

# OpenCV
RUN apt-get install -y libopencv-dev python3-opencv

# XIMEA
RUN apt-get update --fix-missing
RUN apt-get install -y ca-certificates wget sudo vim
RUN python3 -m pip install matplotlib Pillow numpy
WORKDIR /tmp
RUN wget https://www.ximea.com/downloads/recent/XIMEA_Linux_SP.tgz
RUN tar -xf XIMEA_Linux_SP.tgz && rm XIMEA_Linux_SP.tgz
WORKDIR /tmp/package
RUN ./install -noudev
RUN python3 -m pip install ximea-py

# PCL
RUN apt-get install -y libpcl-dev
RUN apt-get install -y python3-pcl pcl-tools
RUN python3 -m pip install python-pcl

# eCAL
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:ecal/ecal-latest
RUN apt-get update
RUN apt-get install -y python3-ecal5

# ROS2
WORKDIR /tmp
# Set locale
RUN apt update && apt install locales -y
RUN locale-gen en_US en_US.UTF-8
RUN update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
ENV LANG=en_US.UTF-8
# Setup Sources
RUN apt update && apt install curl gnupg2 lsb-release -y
RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(source /etc/os-release && echo $UBUNTU_CODENAME) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null
# Install ROS 2 packages
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install ros-foxy-desktop -y
RUN apt-get install -y ros-foxy-sensor-msgs
# Install Python packages
RUN apt-get install -y python3-argcomplete
RUN pip3 install argcomplete
# Install colcon
RUN apt-get install python3-colcon-common-extensions -y
RUN echo "source /opt/ros/foxy/setup.bash" >> /root/.bashrc
