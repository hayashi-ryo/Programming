public class ifElse {
    public static void main(String[] args) {
        var i = 100;
        if (i > 50) {
            System.out.println("変数は50より大きいです");
        } else if (i > 30) {
            System.out.println("変数は30より大きく、50以下です");
        } else {
            System.out.println("変数は30以下です");
        }
    }
}