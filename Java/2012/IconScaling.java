// J3

import java.util.Scanner;

public class IconScaling {
    
    private static int scaling;

    public static String scaleLine(String line) {
        String newstring = "";
        for(int i = 0; i < line.length(); i++) {
            newstring += new String(new char[scaling]).replace("\0", Character.toString(line.charAt(i)));
        }

        return newstring;
    }
    public static void main(String[] args) {
        String[] icon = {"*x*", " xx", "* *"};

        Scanner scanner = new Scanner(System.in);

        scaling = scanner.nextInt();

        for (String line : icon) {
            for (int g = 0; g < scaling; g++) {
                System.out.println(scaleLine(line));
            }
        }

        scanner.close();
        
    }
}