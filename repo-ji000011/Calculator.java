public class Calculator {
private double value1;
private double value2;
public Calculator(double v1, double v2) {
value1 = v1;
value2 = v2;
}
public void setValue(double v1, double v2) {
value1 = v1;
value2 = v2;
}
public double sum() {
return value1 + value2;
}
public double difference() {
return value1 - value2;
}
public static void main(String[] args) {
Calculator c = new Calculator(0,0);
c.setValue(3, 4);
System.out.println("sum " + c.sum());
System.out.println("diffrence " + c.difference());
}
}
