// J2

import java.util.Scanner;

public class VoteCount {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int numvotes = scanner.nextInt(), a_count = 0, b_count = 0;

        String votes = scanner.next();

        for (int i = 0; i < numvotes; i++) {
            if (votes.charAt(i) == 'A') a_count++;
            else b_count++;
        }

        scanner.close();

        if (a_count > b_count) System.out.println('A');
        else if (b_count > a_count) System.out.println('B');
        else System.out.println("Tie");
    }
}