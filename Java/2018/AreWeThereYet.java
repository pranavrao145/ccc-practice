//J3

import java.util.Scanner;

public class AreWeThereYet {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[] d = new int[4];

        for (int i = 0; i < 4; i++) {
            d[i] = scanner.nextInt();
        }

        scanner.close();

        System.out.println(0 + " " + d[0] + " " + (d[0] + d[1]) + " "  + (d[0] + d[1] + d[2]) + " " + (d[0] + d[1] + d[2] + d[3]));
        System.out.println(d[0] + " " + 0 + " " + d[1] + " " + (d[1] + d[2]) + " " + (d[1] + d[2] + d[3]));
        System.out.println((d[0] + d[1]) + " " + d[1] + " " + 0 + " " + d[2] + " " + (d[2] + d[3]));
        System.out.println((d[0] + d[1] + d[2]) + " " + (d[1] + d[2]) + " " + d[2] + " " + 0 + " " + d[3]);
        System.out.println((d[0] + d[1] + d[2] + d[3]) + " " + (d[1] + d[2] + d[3]) + " " + (d[2] + d[3]) + " " + d[3] + " " + 0);
    }    
}