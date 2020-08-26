// J5

import java.util.Scanner;

public class AssigningPartners {
    public static boolean is_balanced(String[] list1, String[] list2) {
        String partner1 = "", partner2 = "";

        for (int i = 0; i < list1.length; i++) {
            if (list1[i] == list2[i])
                return false;
            else
                partner1 = list2[i];

            for (int g = 0; g < list2.length; g++) {
                if (list2[g].equals(list1[i]))
                    partner2 = list1[g];
            }
            if (!partner1.equals(partner2))
                return false;
        }

        return true;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();

        String[] a = new String[n], b = new String[n];

        for (int i = 0; i < a.length; i++) {
            a[i] = scanner.next();
        }
        for (int i = 0; i < b.length; i++) {
            b[i] = scanner.next();
        }

        if (is_balanced(a, b))
            System.out.println("good");
        else
            System.out.println("bad");

        scanner.close();
    }

}