// J1

import java.util.Scanner;

public class TournamentSelection {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int wincount = 0;

        for(int i = 0; i < 6; i++) {
            if(scanner.next().equals('W')) wincount++;
        }

        scanner.close();

        if (wincount == 6 || wincount == 5) {
            System.out.println(1);
        }
        else if (wincount == 4 || wincount == 3) {
            System.out.println(2);
        }
        else if (wincount == 2 || wincount == 1) {
            System.out.println(1);
        }
        else {
            System.out.println(-1);
        }
    }
}