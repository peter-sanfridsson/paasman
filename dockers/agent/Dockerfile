FROM ubuntu:12.04

MAINTAINER paasman

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update

RUN DEBIAN_FRONTEND=noninteractive apt-get install -q -y curl wget
RUN DEBIAN_FRONTEND=noninteractive apt-get install -q -y python
RUN DEBIAN_FRONTEND=noninteractive apt-get install -q -y python-pip
RUN DEBIAN_FRONTEND=noninteractive apt-get install -q -y python-dev

# build things
RUN DEBIAN_FRONTEND=noninteractive apt-get install -q -y libtool autoconf automake uuid-dev build-essential g++ make

# libevent, used by gevent
RUN DEBIAN_FRONTEND=noninteractive apt-get install -q -y libevent-dev

# download the project and place it under paasman
ADD https://github.com/ahlen/paasman/archive/master.tar.gz paasman-src/
RUN cd paasman-src && tar -xzvf master.tar.gz --strip-components 1

RUN cd paasman-src && pip install -r requirements.txt

CMD ["/bin/bash"]