public class concatString {
    public static void main(String[] args) {
        var result = "";
        for (var i = 0; i < 100000; i++) {
            result += "いろは";
        }
    }
}
