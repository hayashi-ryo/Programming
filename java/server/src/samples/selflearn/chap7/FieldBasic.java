import java.security.Permissions;

public class FieldBasic {
    public String firstName;
    public String lastName;

    public static void main(String[] args) {
        var p1 = new Person();
        p1.name = "山田太郎";
        p1.age = 30;

        var p2 = new Person();
        p2.name = "鈴木花子";
        p2.age = 25;

        var p3 = new Person();

        System.out.printf("%s（%d歳）\n", p1.name, p1.age);
        System.out.printf("%s（%d歳）\n", p2.name, p2.age);
        System.out.printf("%s（%d歳）\n", p3.name, p3.age);

        var p4 = new Person();
        p4.name = "佐藤大輝";
        p4.age = 15;
        System.out.println(p4.show());
    }
}