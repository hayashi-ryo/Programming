public class InheritBasic {
    public static void main(String[] args) {
        var bp = new BuisinessPerson();
        bp.name = "山田太郎";
        bp.age = 30;

        System.out.println(bp.show());
        System.out.println(bp.work());
    }
}