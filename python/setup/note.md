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
      `docker run -it continuumio/anaconda3`
   6. ホストOS側に参照用フォルダを作成
      - フォルダ構成
        - docker_JupyterNote -- data
        - docker_JupyterNote:Ipythonプログラムの格納フォルダ
        - data:参照用データ格納フォルダ
   7. docker_JupyterNoteに移動
   8. dockerを起動
      `docker run --name JupyterNote -v /Users/hayashir/work/4_Programming/git/Programmig/python/docker_JupyterNote:/notebook -p 8888:8888 --rm -it continuumio/anaconda3`
      - 各種オプション
          >  【docker run + オプション(下記) + イメージ】
          >  --name → コンテナ名を指定(なくてもいい)
          >  -v → マウント指定(コロンの左側がローカル側、右側がコンテナ側のpath)
          >  -p → ポート接続(コロンの左側がローカル側、右側がコンテナ側※jupyterは8888)
          >  --rm → コンテナ終了時にコンテナ自動的に削除
          >  --it → ホスト側のターミナルからコンテナ内部の操作
          >  ※^ は長いコマンドの場合に改行の意味を示すコマンド(キャレット)
          >  ※-v "%cd%":/notebook の意味は「ローカル側が未記載≒今のpath(docker_sample)」、
          >  「コンテナ側はnotebookフォルダ」をマウントさせるという意味。
          >  notebookフォルダはデフォルトでは存在しないのでコンテナ側で作成される
   9. Jupyter Notebookを起動
        `jupyter notebook --ip 0.0.0.0 --allow-root --no-browser --NotebookApp.disable_check_xsrf=True  --NotebookApp.token='' --NotebookApp.password=''`
