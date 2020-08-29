// J1

import java.util.Scanner;

public class SpeedFinesAreNotFine {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter the speed limit: ");
        int limit = scanner.nextInt();

        System.out.print("Enter the speed of the car: ");
        int speed = scanner.nextInt();

        if(speed - limit  < 1) System.out.println("Congratulations, you are within the speed limit!");
        else if (speed - limit < 21) System.out.println("You are speeding and your fine is $100.");
        else if (speed - limit < 31) System.out.println("You are speeding and your fine is $270.");
        else System.out.println("You are speeding and your fine is $500.");

        scanner.close();
    }
    
}