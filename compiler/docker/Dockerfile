# ベースイメージ
FROM local/c7-systemd
# jdk17の導入
ADD ./base/jdk-17_linux-aarch64_bin.tar.gz /opt/jdk/
ENV PATH /opt/jdk/jdk-17.0.4/bin:$PATH
# cbcコンパイラの導入
RUN mkdir -p /work/tmp
ADD ./base/cbc-1.0.tar.gz /work/tmp/
#CMD ["/work/tmp/cbc-1.0/install.sh"]
ENV PATH /usr/local/cbc/bin:$PATH