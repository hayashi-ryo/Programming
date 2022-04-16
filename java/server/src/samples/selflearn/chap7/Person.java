public class Person {
    public String name = "初期男";
    public int age = 20;

    // コンストラクター
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String show() {
        return String.format("%s (%d歳）です。", this.name, this.age);
    }
}