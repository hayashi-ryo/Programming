# Nuxt.js

Nuxs.jsの勉強のため、段階を踏んで勉強する。項目は現時点で以下の予定。

1. HTML+CSS
2. javascript
3. JSON
4. Nuxt.js本体

## 参考サイト

[Nuxt.jsに飛びつく前に~Nuxt.jsを習得するための前提技術と、その勉強方法の紹介~](https://qiita.com/newt0/items/763b0c228a8451c68865)

## JavaScriptの第一歩

[URL](https://developer.mozilla.org/ja/docs/Learn/JavaScript/First_steps)

### ウェブ入門

[URL](https://developer.mozilla.org/ja/docs/Learn/Getting_started_with_the_web)

- webサイトの外見について
  - 目的や表現、そのための外見についてあらかじめ考えておくことが重要だ。
- 基本的なフォルダ構成
  - `index.html`サイトの最初のページの内容が基本的にこの形で作成される。
  - `imagesフォルダ`サイトで利用する全ての画像を格納する。
  - `stylesフォルダ`コンテンツのスタイルを設定するためのCSSを格納する。
  - `scriptsフォルダ`サイトに対話機能を適用するためのコードを格納する。
- HTMLの基本
  - タグを使って要素を指定する。
  - 要素にはクラスと呼ばれる属性の値を付与することができる。たとえば`<p class="editor-note">My cat is very grumpy</p>`
  - この情報を使って、スタイル情報などのターゲットを指定することができる。
  - imagesタグのalt属性は、表示不正が発生した場合に表示される内容を指定することができる。
    - すごく簡単に表現すると、説明文
  - リンクは非常に重要な要素。`<a>`で囲ってhrefでリンク先をしているする。
    - hrehは *hypertext reference* の略
- CSSの基本
  - CSSはプログラミング言語でもマークアップ言語でもなく、単なるスタイルシート
  - 構造としては以下のイメージ

    ```css
    p { //selector
      color: red; // property value
      //property
    }
    ```

  - それぞれの要素を組み合わせることで、スタイルを設定する要素を指定し、その要素にどのようなルールを与えるのかを明確化する。
