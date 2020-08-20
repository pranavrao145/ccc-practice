// J2

import java.util.Scanner;

public class OccupyParking {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int count = 0;
        int spaces = scanner.nextInt();
        
        String row1 = scanner.next();
        String row2 = scanner.next();

        for (int i = 0; i < spaces; i++) {
            if (row1.charAt(i) == 'C' && row2.charAt(i) == 'C') count++;
        }
        
        System.out.println(count);

        scanner.close();
        
    }    
}