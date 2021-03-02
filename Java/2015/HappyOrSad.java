import java.util.Scanner;

public class HappyOrSad {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String sentence = scanner.nextLine();

        int happyFaces = sentence.split(":-\\)").length - 1;
        int sadFaces = sentence.split(":-\\(").length - 1;

        if (happyFaces > sadFaces) System.out.println("happy");
        else if (sadFaces > happyFaces) System.out.println("sad");
        else System.out.println("none");
    }
}
