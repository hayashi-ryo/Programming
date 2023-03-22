# ベースイメージ:タグ名
FROM ubuntu:jammy-20230308

RUN apt update && \
  apt install -y gcc make git binutils libc6-dev && \
  apt-get update && \
  apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
  && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8
