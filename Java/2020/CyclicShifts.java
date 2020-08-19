// J4

import java.util.Scanner;

public class CyclicShifts {
    public static String[] cyclicShifts(String str) {
        int length = str.length();
        String string = str;
        String[] shifts = new String[length];

        for (int i = 0; i < length; i++) {
            shifts[i] = string;
            string = string.substring(1) + string.charAt(0);
        }

        return shifts;
    }

    public static boolean check(String text, String string) {
        String[] shifts = cyclicShifts(string);
        
        for (String shift : shifts) {
            if(text.contains(shift)) return true;
        }
        
        return false;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        scanner.close();

        String text = scanner.next();
        String string = scanner.next();

        if(check(text, string)) System.out.println("yes"); else System.out.println("no");

        
    }
}