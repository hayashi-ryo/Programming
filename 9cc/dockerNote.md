# 9cc開発環境

9cc開発環境構成をメモする

## 構成概要

- イメージ
  - Ubuntu開発環境上でgccを導入する
- フォルダ構成

```dir
docker
├-Dockerfile
├-docker-compose.yml
└-data：マウントフォルダ

```

## 　環境構築

1. dockerイメージのビルド
   1. Dockerfileの作成
   2. ビルド実行
      `docker build -t 9cc .`
2. docker-compose.ymlの作成
3. dockerの起動
  `docker-compose up -d`
