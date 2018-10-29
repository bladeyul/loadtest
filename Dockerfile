FROM centos:new
MAINTAINER bladeyul fryfish@126.com

WORKDIR /home
RUN curl https://www.python.org/ftp/python/3.6.6/Python-3.6.6.tgz -O
RUN tar zxvf Python-3.6.6.tgz && cd Python-3.6.6
RUN yum install -y gcc cc make zlib* openssl openssl-devel openssh git
RUN ./configure --prefix=/usr/python
RUN make && make install
RUN ln -s /usr/python/bin/python3 /usr/bin/python3
RUN ln -s /usr/python/bin/pip3.6 /usr/bin/pip3

WORKDIR /home
RUN git clone --recursive https://github.com/pytorch/pytorch
RUN cd pytorch && python3 setup.py install

RUN pip3 install opencv-python
RUN pip3 install tensorflow

USER algorithm






