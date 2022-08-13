FROM local/c7-systemd
# jdk11の導入
ADD ./jdk/openjdk-11+28_linux-x64_bin.tar.gz /opt/jdk/
ENV PATH /opt/jdk/jdk-11/bin:$PATH
# cbcコンパイラの導入
RUN mkdir -p /work/tmp
ADD ./cbc/cbc-1.0.tar.gz /work/tmp/
#RUN /work/tmp/cbc-1.0/install.sh
#ENV PATH /usr/local/cbc/bin/cbc:$PATH