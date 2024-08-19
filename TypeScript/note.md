# TypeScript 学習記録

TypeScriptについて学習した内容を記録していく

## 開発環境

Docker環境にNode.jsをインストールして、その上で開発を行っていく方針

### Docker 情報

Ubuntuをdockerとして起動し、必要なパッケージはその中にインストールしていく

#### フォルダ構成

docker
  ├──Dockerfile
  ├──docker-compose.yml
  └──data:マウントフォルダ

#### 環境構築

1. dockerイメージのビルド
   1. Dockerfileの作成
   2. ビルド命令の実行
    `docker build --rm -t yytypescript .`
    `docker images`
2. docker起動設定

## サバイバルTypeScript

基本的な内容は[サバイバルTypeScript](https://typescriptbook.jp/)を元に実施していく。追加で学習した内容や記録しておきたい事項は、新しい項を作成して記録する。

> メモ: node のバージョンが古くて猫画像シュミレータが作成できなかったので以下コマンドでアップグレードを実施した。
> npm install -g n // パッケージのインストール
> n lts // ltsバージョンのインストール
> n prume // 以前のバージョンの削除
