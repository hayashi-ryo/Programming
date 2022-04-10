public class test {
    public static void main(String[] args) {

        // append
        var builder = new StringBuilder();
        for (var i = 0; i < 100000; i++) {
            builder.append("いろは");
        }
        var result = builder.toString();
    }
}