# LinuC学習用環境の構築

LinuC level2勉強のための環境を整備する

## 構成概要

- イメージ
  - centos7のdocker環境を導入する
- フォルダ構成

``` dir
LinuC
└──docker_image
    ├──Dockerfile
    ├──docker-compose.yml
    └──data:マウントフォルダ
```

### 実施内容

### 環境構築

1. dockerイメージのビルド
   1. dockerfileの作成s
   2. ビルド命令の実行
        `docker build --rm -t local/c7-systemd .`
        `docker images`
2. docker起動設定
   1. docker-composer.ymlの作成
   2. 起動コマンドを実行
        `docker-compose up`
3. アクセス
4. その他コマンド