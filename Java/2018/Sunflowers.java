import java.util.ArrayList;
import java.util.Scanner;

public class Sunflowers {
    private static int[][] plantheights;
    private static int n;

    public static boolean check(int[][] table) {
        boolean flag = true;

        for (int a = 0; a < n - 1; a++) {
            for (int b = 0; b < n; b++) {
                if (table[a][b] < table[a + 1][b]) {
                    ;
                }
                else {
                    flag = false;
                }
            }
        }

        for (int a = 0; a < n; a++) {
            for (int b = 0; b < n -1 ; b++) {
                if (table[a][b] < table[a][b + 1]) {
                    ;
                }
                else {
                    flag = false;
                }
            }
        }

        return flag;
        
    }

    public static int[][] rotate(int[][] table) {
        int[][] newmatrix = new int[n][n];
        for (int a = 0; a < n; a++) {
            for (int b = 0; b < n; b++) {
                newmatrix[a][b] = table[b][n-(a+1)];
            }
        }
        return newmatrix;
    }


    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        n = scanner.nextInt();
        plantheights = new int[n][n];

        // taking input
        for (int a = 0; a < n; a++) {
            for (int b = 0; b < n; b++) {
                plantheights[a][b] = scanner.nextInt();
            }
        }

        while (!check(plantheights)) {
            plantheights = rotate(plantheights);
        }

        for (int i = 0; i < n; i++) {
            for (int g = 0; g < n; g++) {
                if (g != n - 1) System.out.print(plantheights[i][g] + " ");
                else System.out.println(plantheights[i][g]);
            }
        }

    }
}