import java.util.TreeMap;
import java.util.Map;

public class MapTree {
    public static void main(String[] args) {
        var data = new TreeMap<String, String>(Map.of("Rose", "バラ",
                "Sunflower", "ひまわり", "Morinig Glory", "あさがお"));
        for (var key : data.keySet()) {
            System.out.println(key);
        }
    }
}