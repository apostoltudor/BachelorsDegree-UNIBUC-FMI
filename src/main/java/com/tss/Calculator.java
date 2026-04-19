package com.tss;

public class Calculator {

    // calculeaza nota finala
    public static String calculateGrade(int score, int bonus, boolean extraCredit) {

        // validare scor usor
        if (score < 0 || score > 100) {
            throw new IllegalArgumentException("Score must be between 0 and 100");
        }

        // stabilim cate puncte luam
        int total;
        if (extraCredit) {
            total = score + bonus + 5;
        } else {
            total = score + bonus;
        }

        // plafonam nota maxima
        if (total > 105) {
            total = 105;
        }

        // preluam notele si pragurile
        String[] grades = {"A", "B", "C", "D"};
        int[] thresholds = {90, 80, 70, 60};

        // impartim spre baremul corect
        for (int i = 0; i < thresholds.length; i++) {
            if (total >= thresholds[i]) {
                // intra pe nota maxima
                if (thresholds[i] == 90 && extraCredit) {
                    return "A+";
                }
                return grades[i];
            }
        }

        // ai picat 
        return "F";
    }
}
