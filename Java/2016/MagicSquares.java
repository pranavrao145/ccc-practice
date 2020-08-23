// J2

import java.util.Scanner;
import java.util.stream.IntStream;

public class MagicSquares {
    private static int rowsum, colsum;

    public static boolean checkRows(int[][] table) {
        int orgsum = IntStream.of(table[0]).sum();

        for (int i = 0; i < 4; i++) {
            if (IntStream.of(table[i]).sum() != orgsum) return false;
        }

        rowsum = orgsum;
        return true;
    }

    public static boolean checkCols(int[][] table) {
        int orgsum = 0;

            for (int a = 0; a < 4; a++) {
                orgsum += table[a][0];   
            }

            for (int a = 0; a < 4; a++) {
                int sum = 0;
                for (int b = 0; b < 4; b++) {
                    sum += table[b][a];
                }
                if (sum != orgsum) return false;
            }

            colsum = orgsum;
            return true;
    }

    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[][] square = new int[4][4];

        for (int a = 0; a < 4; a++) {
            for (int b = 0; b < 4; b++) {
                square[a][b] = scanner.nextInt();      
            } 
        }

        if (checkCols(square) && checkRows(square) && colsum == rowsum) System.out.println("magic"); else System.out.println("not magic");

        scanner.close();
    }
}