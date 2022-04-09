# java練習

javaの開発・勉強を行うために、docker環境の構築を行う

## 構成概要

- イメージ
  - docker環境にopenjdkを導入する
- フォルダ構成

``` dir
java
├──docker
│   └──Dockerfile
├──docker-compose.yml
└──server
    └──src
        └──samples
            ├──mylib
            └──selfleatn
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
