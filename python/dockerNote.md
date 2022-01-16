# python開発

pythonの開発・勉強に必要なことをメモする

## 構成概要

- イメージ
  - docker環境にanacondaを導入する
- フォルダ構成

``` dir
work
├──docker
│   └──yml
└──Github
    └──Programmig
        └──python
            └──docker_image
                 └──anaconda:各種構成情報の格納フォルダ、build/composeはここで実施
                    ├──Dockerfile
                    ├──docker-compose.yml
                    └──data:マウントフォルダ

```

## 実施内容

### 環境構築

1. dockerイメージのビルド
   1. Dockerfileの作成
   2. ビルド命令の実行
        `docker build -t anaconda .`
2. docker起動の作成
   1. docker-compese.ymlの作成
   2. 起動コマンドを実行
        `docker-compose up`
3. ブラウザからアクセス
   1. `http:localhost:8888`
4. 削除系のコマンド
   1. 停止
        `docker-compose stop`
   2. 削除
        `docker-compose down`
