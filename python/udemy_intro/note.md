# python勉強ノート

udemy講座の勉強用ノート

## 概要

コードは全てdocker配下に配置する

### 備忘

実行環境
    docker
IDE
    pycharm

- docker 起動コマンド
    'docker run --name JupyterNote -v /Users/hayashir/work/4_Programming/git/Programmig/python/docker_JupyterNote:/notebook -p 8888:8888 --rm -it continuumio/anaconda3'
- notebook 起動コマンド
    `jupyter notebook --ip 0.0.0.0 --allow-root --no-browser --NotebookApp.disable_check_xsrf=True  --NotebookApp.token='' --NotebookApp.password=''`

### 内容

