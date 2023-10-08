# Use a base image that has C++ compilers
FROM ubuntu:20.04

# Ensure we are root
USER root

RUN dpkg --configure -a

# Set non-interactive mode for apt (to avoid prompts like tzdata)
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/London  

# Preemptively install Python and fix permissions
RUN apt-get clean && apt-get update \
    && apt-get install -y python3.8 \
    && chmod -R 777 /usr/lib/python3.8/

# Update and install necessary tools
RUN apt-get update && apt-get install -y apt-transport-https ca-certificates gnupg software-properties-common wget

# Add the Kitware repository for CMake
RUN wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null | gpg --dearmor - > /etc/apt/trusted.gpg.d/kitware.gpg
RUN apt-add-repository 'deb https://apt.kitware.com/ubuntu/ focal main'

# Update and upgrade system packages
RUN apt-get update && apt-get upgrade -y

# Install CMake
RUN apt-get install -y cmake

# Install necessary utilities and dependencies
RUN apt-get install -y \
    g++ \
    cmake \
    git \
    libmysqlclient-dev \
    mysql-client \
    libboost-dev

# Set the system timezone
RUN ln -fs /usr/share/zoneinfo/$TZ /etc/localtime && dpkg-reconfigure --frontend noninteractive tzdata

WORKDIR /

# # Copy your project into the Docker container
# COPY . /workspace

RUN ls -al /

# Set the working directory
# Set the working directory to /workspace
WORKDIR /

# Clone the SOCI repo, build and install inside /workspace
RUN git clone https://github.com/SOCI/soci.git

WORKDIR /soci
RUN mkdir build && cd build \
    && cmake -DSOCI_MYSQL=ON -DWITH_BOOST=ON .. \
    && make -j$(nproc) && make install

RUN mkdir /app