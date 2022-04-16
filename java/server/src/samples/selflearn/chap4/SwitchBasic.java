
public class SwitchBasic {
    public static void main(String args[]) {
        String rank = "甲";

        switch (rank) {
            case "甲":
                System.out.println("大変良いです。");
                break;

            case "乙":
                System.out.println("良いです。");
                break;

            case "丙":
                System.out.println("がんばりましょう。");
                break;

            default:
                break;
        }
    }
}
