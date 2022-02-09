import java.util.Scanner;

public class S2 {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    // take the number of pieces
    int numPieces = scanner.nextInt();

    double totalArea = 0.0;

    // make a new array with the number of heights and widths
    int[] heights = new int[numPieces + 1];
    int[] widths = new int[numPieces];

    for (int i = 0; i < numPieces + 1; i++) {
      heights[i] = scanner.nextInt(); // take in integer input
    }

    // take in inputs for the widths
    for (int i = 0; i < numPieces; i++) {
      widths[i] = scanner.nextInt(); // take in integer input
    }

    // heights: {2, 3, 6, 2}
    // widths: {4, 1, 1}

    // loop through each piece
    for (int i = 0; i < numPieces; i++) {
      // i = 0
      double area = ((heights[i] + heights[i + 1]) / 2.0) *
                    widths[i];      // calculating the area
      totalArea = totalArea + area; // adding the area to the total area
    }

    if (totalArea % 1 == 0) {
      System.out.println((int)totalArea);
    } else {
      System.out.println(totalArea);
    }

    scanner.close();
  }
}
