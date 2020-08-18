// J1

import java.util.Scanner;

public class DogTreats {
    public static void main(final String[] args) {
        final Scanner scanner = new Scanner(System.in);

        final int small = scanner.nextInt();
        final int medium = scanner.nextInt();
        final int large = scanner.nextInt();

        final int happiness = small + (2 * medium) + (3 * large);

        System.out.println(happiness >= 10?"happy":"sad");
        scanner.close();
        
    }
}