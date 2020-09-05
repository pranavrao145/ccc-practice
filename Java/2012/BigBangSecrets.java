// J4

import java.util.Scanner;

public class BigBangSecrets {
    public static void main(String[] args) {
        String alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        StringBuilder builder = new StringBuilder();

        Scanner scanner = new Scanner(System.in);

        int k = scanner.nextInt();
        String word = scanner.next();

        for (int i = 0; i < word.length(); i++) {
            int index = alpha.indexOf(word.charAt(i));
            int shift = ((3 * (i + 1)) + k) % 26;

            if (shift < index)
                builder.append(alpha.charAt(index - shift));
            else {
                int newshift = shift - index;
                if (newshift == 0)
                    builder.append(alpha.charAt(0));
                else
                    builder.append(alpha.charAt(alpha.length() - newshift));
            }
        }

        System.out.println(builder);

        scanner.close();
    }
}
