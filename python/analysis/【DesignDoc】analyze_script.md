# analyze_script.py of DesignDoc

Hayashi Ryohei
last update:2021/10/16
Status:Public

## Goal

渉外CRMで実行されるジョブについて、「金庫顧客数」および「系総顧客数」への依存性を確認する

## Background

割愛

## Overview

統合渉外CRMへの移行に伴い、CPU使用率の増加が更改後どこかでひっ迫する想定となっていた。状況について確認したところ、CPU使用率のひっ迫は確認できなかったが、ジョブの完了時間が遅くなっていること判明した。この時間遅延についてどのような関連性があるのかをある程度明確にする。

## Detailed Design

### Flowchart

```flow
start=>start: start
end=>end: end

process1=>operation: 金庫csvファイルの読み込み
process2=>operation: 顧客数の追記
process3=>operation: リストごとに傾き切片の算出
process4=>operation: csvファイルへ出力

start->process1->process2->process3->process4->end


```

### Detail

- 前提条件
  - 原本csvファイル形式
    - day, job, Ptime, starttime, endtime

1. csvファイルの読み込み
2. 顧客数の追記  
3. job,顧客数のリスト作成
4. job,顧客数のリストごとに傾き・切片の算出
5. 出力

- csvファイルの読み込み
  1. csvファイルを指定して、データの読み込みを行う
- 顧客数の追記
  1. タプルごとの金庫コード取得
  2. 金庫コードごとに適切な顧客数をタプルへ追加
  3. jobから系を取得
  4. 系とdayから適切な総顧客数をタプルへ追加
- job,顧客数のリスト作成
  1. job,顧客数から重複削除したリストを作成する
  2. job,総顧客数から重複削除したリストを作成する
- job,顧客数リストごとに傾き切片を出力する
  1. job,顧客数リストに該当するタプルをPtimeを取得する
  2. 傾き切片を算出し、リストへ追加する
  3. job,総顧客数リストに該当するタプルのPtimeを取得する
  4. 傾き切片を算出し、リストへ追加する
- 出力
  1. jobごとの傾き切片リストを出力する
