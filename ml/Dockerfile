# Start from the NVIDIA Caffe image
FROM nvcr.io/nvidia/caffe:20.03-py3

# Set up some basic environment settings
ENV DEBIAN_FRONTEND=noninteractive

# Update and install dependencies
RUN apt-get update && apt-get install -y \
    git \
    cmake \
    g++ \
    libmysqlclient-dev \
    libboost-dev \
    libboost-all-dev

# Clone SOCI
WORKDIR /
RUN git clone https://github.com/SOCI/soci.git

# Build and install SOCI
WORKDIR /soci
RUN mkdir build && cd build \
    && cmake -DSOCI_MYSQL=ON -DWITH_BOOST=ON .. \
    && make -j$(nproc) && make install

# Set the working directory back to the workspace
WORKDIR /workspace