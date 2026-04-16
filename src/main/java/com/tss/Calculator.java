package com.tss;

/**
 * Calculator de note pentru studenti.
 *
 * Aceasta clasa contine metoda calculateGrade care determina nota finala
 * a unui student pe baza scorului brut, punctelor bonus si creditului suplimentar.
 *
 * Constrangeri indeplinite conform cerintelor profesoarei:
 * - Minim 3 parametri: score, bonus, extraCredit
 * - Instructiune repetitiva: bucla for
 * - if cu else: blocul if (extraCredit) ... else ...
 * - if fara else: if (score < 0 || score > 100),  if (total > 105), if (total >= thresholds[i])
 * - Conditie simpla: if (extraCredit), if (total > 105)
 * - Conditie compusa: if (score < 0 || score > 100), if (thresholds[i] == 90 && extraCredit)
 */
public class Calculator {

    /**
     * Calculeaza nota finala sub forma de eticheta (label) pe baza scorului,
     * punctelor bonus si eligibilitatii pentru credit suplimentar.
     *
     * Reguli de calcul:
     * - Daca extraCredit este true, se adauga 5 puncte la total
     * - Daca extraCredit este false, totalul este scor + bonus
     * - Totalul este limitat la maxim 105
     * - Nota este determinata pe baza pragurilor: 90->A, 80->B, 70->C, 60->D, altfel F
     * - Daca totalul >= 90 SI extraCredit este true, nota este A+
     *
     * @param score       scorul brut al examenului (interval valid: 0-100)
     * @param bonus       puncte bonus (interval valid: 0-20)
     * @param extraCredit daca studentul este eligibil pentru credit suplimentar (+5 puncte)
     * @return eticheta notei: "A+", "A", "B", "C", "D" sau "F"
     * @throws IllegalArgumentException daca score nu este in intervalul [0, 100]
     */
    public static String calculateGrade(int score, int bonus, boolean extraCredit) {

        // Validare score — if FARA else, conditie COMPUSA (||)
        if (score < 0 || score > 100) {
            throw new IllegalArgumentException("Score must be between 0 and 100");
        }

        // Calculul totalului — if CU else, conditie SIMPLA
        int total;
        if (extraCredit) {
            total = score + bonus + 5;
        } else {
            total = score + bonus;
        }

        // Limitarea totalului — if FARA else, conditie SIMPLA
        if (total > 105) {
            total = 105;
        }

        // Determinarea notei — instructiune REPETITIVA (for)
        String[] grades = {"A", "B", "C", "D"};
        int[] thresholds = {90, 80, 70, 60};

        for (int i = 0; i < thresholds.length; i++) {
            if (total >= thresholds[i]) {
                // Conditie COMPUSA (&&) — if FARA else
                if (thresholds[i] == 90 && extraCredit) {
                    return "A+";
                }
                return grades[i];
            }
        }

        return "F";
    }
}
