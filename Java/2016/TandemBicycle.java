import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class TandemBicycle {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int question = scanner.nextInt();
        int participants = scanner.nextInt();

        ArrayList<Integer> d_speeds = new ArrayList<Integer>();
        ArrayList<Integer> p_speeds = new ArrayList<Integer>();

        for (int i = 0; i < participants; i++) {
            d_speeds.add(scanner.nextInt());
        }

        for (int i = 0; i < participants; i++) {
            p_speeds.add(scanner.nextInt());
        }

        Collections.sort(d_speeds);
        Collections.sort(p_speeds);

        if (question == 2)
            Collections.reverse(p_speeds);

        int total = 0;

        for (int i = 0; i < participants; i++) {
            total += Math.max(d_speeds.get(i), p_speeds.get(i));
        }

        System.out.println(total);
    }
}
