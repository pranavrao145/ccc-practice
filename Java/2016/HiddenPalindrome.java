// J3

import java.util.ArrayList;
import java.util.Scanner;

public class HiddenPalindrome {

    public static String reverse(String str) {
        StringBuilder builder = new StringBuilder();
        builder.append(str);
        return builder.reverse().toString();
    }

    public static boolean check(String word) {
        return (word.equals(reverse(word)));
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int length = 0;

        String word = scanner.next();

        ArrayList<String> subwords = new ArrayList<String>();

        for (int i = 0; i < word.length() + 1; i++) {
            for (int f = 0; f < word.length() + 1; f++) {
                try {
                String modiword = word.substring(i, f);
                subwords.add(modiword); 
                }
                catch (Exception e) {
                    ;
                }
            }
        }

        for (int i = 0; i < subwords.size(); i++) {
            String subword = subwords.get(i);
            if (check(subword) && subword.length() > length) length = subword.length();
        }

        System.out.println(length);

        scanner.close();
    }    
}