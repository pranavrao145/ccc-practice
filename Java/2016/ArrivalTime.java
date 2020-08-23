// J4

import java.util.Arrays;
import java.util.Scanner;

public class ArrivalTime {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String input = scanner.next();

        int[] time = Arrays.stream(input.split(":")).mapToInt(Integer::parseInt).toArray();

        int left = time[0] * 60 + time[1];

        int arrived = left;

        for (int minute = left; minute < left + 120; minute++) {
            if (arrived >= 420 && arrived < 600 || arrived >= 900 && arrived < 1140) arrived += 2;
            else arrived++;

            if (arrived == 1400) arrived = 0;
        }

        int hours = 0, minutes = 0;

        while (arrived >= 60) {
            arrived -= 60;
            hours++;
            if (arrived < 60) break;
        }

        minutes = arrived;

        String hours1, minutes1;

        if (hours < 10) hours1 = "0" + Integer.toString(hours); else hours1 = Integer.toString(hours);
        if (minutes < 10) minutes1 = "0" + Integer.toString(minutes); else minutes1 = Integer.toString(minutes);

        System.out.println(hours1 + ":" + minutes1);
        
        scanner.close();
    }
}