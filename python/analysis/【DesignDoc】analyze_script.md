# analyze_script.py of DesignDoc

Hayashi Ryohei
last update:2021/10/16
Status:Draft

## Goal

渉外CRMで実行されるジョブについて、「金庫顧客数」および「系総顧客数」への依存性を確認する

## Background

割愛

## Overview

統合渉外CRMへの移行に伴い、CPU使用率の増加が更改後どこかでひっ迫する想定となっていた。状況について確認したところ、CPU使用率のひっ迫は確認できなかったが、ジョブの完了時間が遅くなっていること判明した。処理時間遅延について、顧客数への依存性と現行システムにおける最遅処理時間との関連を分析する。

## Detailed Design

### Flowchart

```flow
start=>start: start
end=>end: end

process1=>operation: csvファイルの読み込み
process2=>operation: 回帰分析の実行
process3=>operation: csvファイルへ出力

start->process1->process2->process3->end

```

### Detail

- 前提条件
  - 原本csvファイル形式
    - day, job, Ptime, starttime, endtime, WD, kokyaku, kokyaku_total

1. csvファイルの読み込み
2. 重回帰分析の実行  
3. csvファイルへの出力  

- csvファイルの読み込み
  1. csvファイルを指定して、データの読み込みを行う  
- 重回帰分析の実行
  1. 目的変数：Ptime(処理時間)とする
  2. 説明変数：kokyaku, kokyaku_total, WDとする
  3. 条件に従って重回帰分析を実行する
- 出力
  1. 重回帰分析結果をファイル出力する
