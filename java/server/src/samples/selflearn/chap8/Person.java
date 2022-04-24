public class Person {
    // フィールド
    /*
     * よくない書き方
     * public String name;
     * public int age;
     */
    // 良い書き方は以下のようにpirvateとした上で
    public String name;
    public int age;

    /*
     * // 以下のようにgetter/setterを定義する
     * public String getName() {
     * return this.name;
     * }
     * 
     * public void setName(String name) {
     * this.name = name;
     * }
     * 
     * public int getAge() {
     * return this.name;
     * }
     * 
     * public void setAge(int age) {
     * if (age <= 0) {
     * throw new IllegalArgumentException("年齢は0より大きい数を指定してください");
     * }
     * this.age = age;
     * }
     * 
     * // コンストラクタ
     * public Person(String name, int age) {
     * this.name = name;
     * this.age = age;
     * }
     */
    // メソッド
    public String show() {
        return String.format("%s(%d歳)です。", this.name, this.age);
    }
}