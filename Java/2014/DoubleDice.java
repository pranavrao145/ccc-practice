import java.util.Scanner;

// J3

public class DoubleDice {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n, antonia_points = 100, david_points = 100;

        n = scanner.nextInt();

        int[][] rolls = new int[n][2];

        for (int a = 0; a < n; a++) {
            for (int b = 0; b < 2; b++) {
                rolls[a][b] = scanner.nextInt();
            }
        }

        for (int[] roll : rolls) {
            if(roll[0] < roll[1]) antonia_points -= roll[1];
            else if(roll[1] < roll[0]) david_points -= roll[0];
            else continue;
        }

        if (antonia_points < 0) antonia_points = 0;
        if (david_points < 0) david_points = 0;

        System.out.println(antonia_points);
        System.out.println(david_points);

        scanner.close();
    }
    
}