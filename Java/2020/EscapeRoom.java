// J5

import java.util.ArrayList;
import java.util.Scanner;

class Pair {
    int x, y;

    public Pair(int xval, int yval) {
        x = xval;
        y = yval;
    }

}

public class EscapeRoom {

    private static int down, across;
    private static boolean found = false;
    private static ArrayList<Pair> visited = new ArrayList<Pair>();
    private static int[][] matrix;

    public static ArrayList<Pair> factors(int value) {
        ArrayList<Pair> factors = new ArrayList<Pair>();

        for (int i = 1; i < value + 1; i++) {
            if(value % i == 0) {
                if (i <= down && (value / i) <= across) {
                    factors.add(new Pair(i, (int)(value/i)));
                }
            }
        }

        return factors;
    }    

    public static void check(int d, int a) {
        if(d == down && a == across) {
            found = true;
            return;
        }
        ArrayList<Pair> factors = factors(matrix[d-1][a-1]);

        if (!found) {
            for (Pair elem : factors) {
                if(!visited.contains(elem)) {
                    visited.add(elem);
                    check(elem.x, elem.y);
                }
            }
        }
        return;
    }

    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        
        down = scanner.nextInt();
        across = scanner.nextInt();

        matrix = new int[down][across];

        for (int a = 0; a < down; a++) {
            for (int b = 0; b < across; b++) {
                matrix[a][b] = scanner.nextInt();
            }
        }

        check(1, 1);

        if (found) System.out.println("yes"); else System.out.println("no");
        
        scanner.close();
    }
}