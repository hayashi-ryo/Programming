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

### Flowchart regressionAnalysis

```flow
start=>start: start
end=>end: end

process1=>operation: 加工csvファイルの読み込み
process2=>operation: 目的変数・説明変数の定義
process3=>operation: 回帰分析の実行
process4=>operation: 結果出力

start->process1->process2->process3
process3->process4->end
```

### Detail

- 前提条件
  - 原本csvファイル形式
    - day, job, Ptime, starttime, endtime
  - 加工後csvファイル形式
    - day, job, Ptime, starttime, endtime, kokyaku, kokyaku_total, WD

1. CSV_ReadWrite
2. regressionAnalysis  

- regressionAnalysis
  1. 目的変数：Ptime(処理時間)とする
  2. 説明変数：kokyaku, kokyaku_total, WD, coreとする
  3. 条件に従って重回帰分析を実行する
- 出力
  1. 重回帰分析結果をファイル出力する
  2. 出力対象を以下に記載する
     - ジョブごとの回帰係数および標準化回帰係数
     - 切片
     - 決定係数
     - グラフ（そのまま・標準化後）
