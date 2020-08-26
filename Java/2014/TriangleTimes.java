// J1

import java.util.Scanner;

public class TriangleTimes {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int side1, side2, side3;
        side1 = scanner.nextInt();
        side2 = scanner.nextInt();
        side3 = scanner.nextInt();
        
        scanner.close();

        if (side1 + side2 + side3 != 180) System.out.println("Error");
        else if (side1 == 60 && side2 == 60) System.out.println("Equilateral");
        else if (side1 == side2 || side2 == side3 || side1 == side3 ) System.out.println("Isosceles");
        else System.out.println("Scalene");
    }
}