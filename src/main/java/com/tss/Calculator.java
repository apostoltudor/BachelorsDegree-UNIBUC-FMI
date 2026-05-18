package com.tss;

/**
 * in clasa calculator avem metoda principala supusa testarii unitare
 * calculateGrade primeste 3 paramentri: score, bonus si extraCredit - respectov
 * punctajul de baza, un punctaj suplimentar si un boolean
 * noi testam algoritmul de calcul al notelor pentru a ne asigura ca deciziile,
 * buclele si rezultatele sunt corecte
 * 
 * din punct de vedere structural (white box testing) metoda are 2 conditii
 * compuse cu || si cu &&, o bucla si 6 decizii
 * 
 * erorile ce pot aparea sunt:
 * erori de frontiera: atunci cand programatul foloseste > in loc de >= la
 * limite
 * erori de flux: conditia pentru extraCredit nu adauga corect bonusul sau
 * ocoleste verificarea
 * erori logice compuse: evaluarea gresita a conditiei (score < 0 || score >
 * 100)
 * mutanti: modificarea constantelor (ex: +5 devine +6, plafonul 105 devine 106)
 *
 * limitele reprezinta punctele critice unde se schimba comportamentul:
 * 1. limitele domeniului de intrare pentru score:
 * - limita inferioara: 0 (testam -1, 0, 1)
 * - limita superioara: 100 (testam 99, 100, 101)
 * 2. limitele de trecere intre note:
 * - pragul 60 (F vs D): testam 59, 60, 61
 * - pragul 70 (D vs C): testam 69, 70, 71
 * - pragul 80 (C vs B): testam 79, 80, 81
 * - pragul 90 (B vs A / A+): testam 89, 90, 91
 * 3. limita artificiala de plafonare:
 * - plafonul maxim: 105 (testam 104, 105, 120)
 */
public class Calculator {

    /**
     * algoritmul are urmatorii pasi:
     * valideaza parametrul score
     * adauga bonusul la score daca exista
     * plafoneaza totalul la 105 (optional)
     * itereaza printr-o lista de praguri de note de la cel mai mare la cel mai mic
     * si verifica daca e A+
     * returneaza nota corespunzatoare
     * daca niciun prag nu a fost atins, returneaza F
     * 
     * 
     * @param score       punctajul de baza
     * @param bonus       puncte bonus suplimentare
     * @param extraCredit daca studentul beneficiaza de credit suplimentar (+5
     *                    puncte)
     * @return nota finala
     * @throws IllegalArgumentException daca score nu este in intervalul [0, 100]
     */
    public static String calculateGrade(int score, int bonus, boolean extraCredit) {

        // verificam daca score este in intervalul [0,100]
        if (score < 0 || score > 100) {
            throw new IllegalArgumentException("Score must be between 0 and 100");
        }

        // daca extraCredit == true, totalul creste cu +5 puncte extra
        int total;
        if (extraCredit) {
            total = score + bonus + 5;
        } else {
            total = score + bonus;
        }

        // daca totalul depaseste 105 puncte, se limiteaza la 105.
        if (total > 105) {
            total = 105;
        }
        String[] grades = { "A", "B", "C", "D" };
        int[] thresholds = { 90, 80, 70, 60 };

        for (int i = 0; i < thresholds.length; i++) {
            if (total >= thresholds[i]) {

                if (thresholds[i] == 90 && extraCredit) {
                    return "A+";
                }
                return grades[i];
            }
        }

        // daca bucla s-a epuizat fara sa gaseasca un prag potrivit,
        // inseamna ca totalul este sub 60 => nota este "F".
        // aceasta este calea de baza (Circuit 1) din testarea circuitelor independente
        return "F";
    }
}
