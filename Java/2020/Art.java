import java.util.Arrays;
import java.util.Scanner;

public class Art {
    public static int[] getCoords(String line) {
        String[] nums = line.split(",");
        int[] coords = new int[2];

        for(int i = 0; i < 2; i++) {
            coords[i] = Integer.parseInt(nums[i]);
        }
        
        return coords;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        final int num_coords = scanner.nextInt();
        
        int[] xvals = new int[num_coords];
        int[] yvals = new int[num_coords];

        for (int i = 0; i < num_coords; i++) {
            int[] coords = getCoords(scanner.next());
            xvals[i] = coords[0];
            yvals[i] = coords[1];
        }

        Arrays.sort(xvals);
        Arrays.sort(yvals);

        System.out.println(Integer.toString(xvals[0] - 1) + "," + Integer.toString(yvals[0] - 1));
        System.out.println(Integer.toString(xvals[num_coords - 1] + 1) + "," + Integer.toString(yvals[num_coords - 1] + 1));

    }
}