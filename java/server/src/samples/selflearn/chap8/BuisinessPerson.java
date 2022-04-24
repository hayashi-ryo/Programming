public class BuisinessPerson extends Person {

    public String work() {
        return String.format("%d歳の%2は働きます。", this.age, this.name);
    }
}