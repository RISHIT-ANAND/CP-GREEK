public class MultiplicationTable {
    public static void main(String[] args) {
        int n = 5; // Change this to the desired number for which you want the multiplication table.
        System.out.println("Multiplication Table for " + n + ":");
        printMultiplicationTable(n, 1);
    }

    public static void printMultiplicationTable(int n, int i) {
        if (i <= 10) {
            System.out.println(n + " x " + i + " = " + (n * i));
            printMultiplicationTable(n, i + 1);
        }
    }
}
