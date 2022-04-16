import java.util.HashMap;
import java.util.Map;

public class MapHash {
    public static void main(String[] args) {
        var map = new HashMap<String, String>(Map.of("Rose", "バラ",
                "Sunflower", "ひまわり", "Morinig Glory", "あさがお"));
        System.out.println(map.containsKey("Rose"));
        System.out.println(map.containsValue("ひまわり"));
        System.out.println(map.isEmpty());

        for (var key : map.keySet()) {
            System.out.println(key);
        }

        for (var value : map.values()) {
            System.out.println(value);
        }
    }
}
