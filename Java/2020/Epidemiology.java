// J2

import java.util.Scanner;

public class Epidemiology {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int target = scanner.nextInt();
        int infected = scanner.nextInt();
        int daily = scanner.nextInt();
        
        scanner.close();
        
        int days = 0;

        int previnfected = infected;
        while (infected <= target) {
            infected += (previnfected * daily);
            days++;
            previnfected *= daily;
        }

        System.out.println(days);
    }
}