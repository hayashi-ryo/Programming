# コンパイラ勉強用環境の構築

「ふつうのコンパイラを作ろう」の学習用環境を作成する

## 構成概要

- イメージ
  - centos7のdocker環境を導入する
  - centos上にJREを導入する
    - jdk11を導入する
- フォルダ構成

``` dir
compiler
└──docker
    ├──Dockerfile
    ├──docker-compose.yml
    ├──base:必要なベースイメージを格納する
    jdk11のベースイメージを格納する
    ├──cbc:cbcコンパイラのtar.gzを格納する
    └──data:マウントフォルダ。/work/sourceにマウントする
```

### 環境構築

1. dockerイメージのビルド
   1. dockerfileの作成
   2. ビルド命令の実行
    `docker build --rm -t c7-cbc .`
    `docker images`
2. docker起動設定
   1. docker-composer.ymlの作成
   2. 起動コマンドを実行
3. アクセス
