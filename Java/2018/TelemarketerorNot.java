// J1

import java.util.Scanner;

public class TelemarketerorNot {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[] numbers = new int[4];

        for (int i = 0; i < 4; i++) {
            numbers[i] = scanner.nextInt();    
        }

        if ((numbers[0] == 8 || numbers[0] == 9) && (numbers[3] == 8 || numbers[3] == 9) && (numbers[1] == numbers[2])) System.out.println("ignore"); else System.out.println("answer");
    }
    
    scanner.close()
}