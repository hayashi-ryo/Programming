# python環境の導入

## 目的

- python環境をdockerで構築する

## 概要

- docker上にanacondaをインストールし、JupyterNotebookを動かせるようにする
- 作成までに必要な手順があれば全部かきだしておく

### 手順

1. Dockerのインストール
   1. [参考サイト](https://sukkiri.jp/technologies/virtualizers/docker/docker-mac_install.html)
   2. 参考サイトから適切なCPUのファイルを取得（今回はM1mac用）
   3. Finderから起動
       - この際セキュリティ関連でいくつか確認が発生する
   4. Dockerアカウントを作成する.
2. docker Hubからanacondaをインストール
   1. [参考サイト](https://qiita.com/ku_a_i/items/8c7d91f6e13a5091f51c)
   2. [サイト](https://hub.docker.com/r/continuumio/anaconda3)にアクセスしてコマンドを確認
   3. ターミナルで実行
      `docker pull continuumio/**anaconda3**`
   4. 落としてきたイメージを念の為確認
      `docker images`
   5. dockerを起動
      `docker run -it continuumio/anaconda3:2019.03`
   6. ホストOS側に参照用フォルダを作成
