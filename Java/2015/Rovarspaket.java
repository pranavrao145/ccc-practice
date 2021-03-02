import java.util.Scanner;

public class Rovarspaket {
    public static void main(String[] args) {
        String consonants = "bcdfghjklmnpqrstvwxyz";
        String nearestVowel = "aaeeeiiiiooooouuuuuuu";
        String nearestConsonant = "cdfghjklmnpqrstvwxyzz";

        String inputString = new Scanner(System.in).nextLine();
        StringBuilder outputString = new StringBuilder();

        for (char i : inputString.toCharArray()) {
            int index = consonants.indexOf(i);

            if (index > -1) {
                outputString.append(i).append(nearestVowel.charAt(index)).append(nearestConsonant.charAt(index));
            }
            else {
                outputString.append(i);
            }
        }

        System.out.println(outputString.toString());

    }
}
