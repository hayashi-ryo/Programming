import javax.swing.text.Document;

import java.lang.Math;

public class PCircle {
    public double radius;

    public PCircle(double radius) {
        this.radius = radius;
    }

    public PCircle() {
        this(1);
    }

    public double getArea() {
        return radius * radius * Math.PI;
    }
}