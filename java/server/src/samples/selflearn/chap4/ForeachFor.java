public class ForeachFor {
    public static void main(String[] args) {
        var data = new String[] { "梅", "桃", "桜" };
        // 通常
        for (var i = 0; i < data.length; i++) {
            System.out.println(data[i]);
        }
        System.out.println("*************");
        // 拡張For
        for (var value : data) {
            System.out.println(value);
        }
    }
}