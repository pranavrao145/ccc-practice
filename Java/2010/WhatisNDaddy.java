// J1

import java.util.Scanner;

public class WhatisNDaddy {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int a = scanner.nextInt(), n = 0;

        for (int i = 0; i <= 5; i++) {
            for (int j = 0; j <= i; j++) {
                if (i + j == a)
                    n++;
            }
        }
        System.out.println(n);

        scanner.close();
    }
}