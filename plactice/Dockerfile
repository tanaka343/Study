FROM ubuntu:20.04
USER root

#コンテナイメージ作成時
RUN apt update
RUN apt install -y python3.9
RUN apt install -y python3-pip

#リモート上のファイルは扱えないローカルのみ
COPY requirements.txt .
RUN python3.9 -m pip install -r requirements.txt

ENV SITE_DOMAIN=vtuber.sapu.com

WORKDIR /var

#ウェブ上からでもコピー可能
ADD https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data .

#コンテナ実行時に同時に動かしたいシェルコマンド
# ENTRYPOINT [ "executable" ]
