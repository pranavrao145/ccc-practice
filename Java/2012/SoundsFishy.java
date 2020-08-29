// J2

import java.util.Scanner;

public class SoundsFishy {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] measurements = new int[4];

        for(int i = 0; i < 4; i++) measurements[i] = scanner.nextInt();
        
        scanner.close();

        if (measurements[0] < measurements[1] && measurements[1] < measurements[2] && measurements[2] < measurements[3]) System.out.println("Fish Rising");
        else if (measurements[0] > measurements[1] && measurements[1] > measurements[2] && measurements[2] > measurements[3]) System.out.println("Fish Diving");
        else if (measurements[0] == measurements[1] && measurements[1] == measurements[2] && measurements[2] == measurements[3]) System.out.println("Constant Depth");
        else System.out.println("No Fish");


    }    
}