# chapter8

オブジェクト指向

- カプセル化
- 継承
- ポリモーフィズム

## 内容

- カプセル化
  - 基本は「利用者に関係ないものは提示しない」こと
    - 利用者に使ってほしい機能だけ参照させ、それ以外の内部的な機能は解放しない
    - 以下の例ではフィールドをpublicで定義しているが、そのようなオブジェクトの内部領域はpublicではなくprivateとすべき領域となる

  ```java
  public class Person {
    // フィールド
    public String name;
    public int age;

    // コンストラクタ
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // メソッド
        public String show() {
            return String.format("%s(%d歳)です。", this.name, this.age);
        }
    }
  ```

- 継承
  - もとになるクラスのメンバーを引き継ぎながら、新しい機能の追加／元の機能の上書きを行う
