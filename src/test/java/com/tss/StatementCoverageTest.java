package com.tss;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/**
 * Testare structurala — Acoperire la nivel de instructiune (Statement Coverage).
 *
 * Strategia:
 * Fiecare instructiune (linie de cod) din metoda calculateGrade trebuie
 * executata cel putin o data. Se identifica blocurile de cod si se aleg
 * date de test care forteaza executia fiecarui bloc.
 *
 * Instructiunile din calculateGrade si testele care le acopera:
 *
 * Linie  | Instructiune                                    | Acoperita de test
 * -------|------------------------------------------------|------------------
 *   1    | if (score < 0 || score > 100) throw ...         | testExceptieScoreInvalid
 *   2    | int total;                                      | toate testele valide
 *   3    | if (extraCredit) total = score + bonus + 5      | testExtraCreditTrue
 *   4    | else total = score + bonus                      | testExtraCreditFalse
 *   5    | if (total > 105) total = 105                    | testLimitareTotal105
 *   6    | for (int i = 0; i < thresholds.length; i++)     | toate testele valide
 *   7    | if (total >= thresholds[i])                     | testNotaA, testNotaB, etc.
 *   8    | if (thresholds[i] == 90 && extraCredit) → A+    | testNotaAPlus
 *   9    | return grades[i]                                | testNotaA, testNotaB, etc.
 *  10    | return "F"                                      | testNotaF
 */
@DisplayName("Testare Structurala: Acoperire la Nivel de Instructiune (Statement Coverage)")
public class StatementCoverageTest {

    @Test
    @DisplayName("Instructiunea throw — score invalid triggereaza exceptia")
    void testExceptieScoreInvalid() {
        // Acopera: if (score < 0 || score > 100) throw new IllegalArgumentException
        assertThrows(IllegalArgumentException.class, () ->
            Calculator.calculateGrade(-5, 0, false));
    }

    @Test
    @DisplayName("Ramura extraCredit = true — total = score + bonus + 5")
    void testExtraCreditTrue() {
        // Acopera: if (extraCredit) → total = score + bonus + 5
        // score=80, bonus=0, extra=true → total = 85 → B
        assertEquals("B", Calculator.calculateGrade(80, 0, true));
    }

    @Test
    @DisplayName("Ramura extraCredit = false — total = score + bonus")
    void testExtraCreditFalse() {
        // Acopera: else → total = score + bonus
        // score=75, bonus=0, extra=false → total = 75 → C
        assertEquals("C", Calculator.calculateGrade(75, 0, false));
    }

    @Test
    @DisplayName("Limitarea totalului la 105 — total > 105 devine 105")
    void testLimitareTotal105() {
        // Acopera: if (total > 105) total = 105
        // score=100, bonus=20, extra=false → total = 120 → capped 105 → A
        assertEquals("A", Calculator.calculateGrade(100, 20, false));
    }

    @Test
    @DisplayName("Nota A+ — conditie compusa thresholds[i]==90 && extraCredit")
    void testNotaAPlus() {
        // Acopera: if (thresholds[i] == 90 && extraCredit) return "A+"
        // score=90, bonus=0, extra=true → total = 95 → A+
        assertEquals("A+", Calculator.calculateGrade(90, 0, true));
    }

    @Test
    @DisplayName("Nota A — total >= 90, fara extraCredit")
    void testNotaA() {
        // Acopera: return grades[i] cand i=0 (thresholds[0]=90)
        assertEquals("A", Calculator.calculateGrade(95, 0, false));
    }

    @Test
    @DisplayName("Nota B — total >= 80 si < 90")
    void testNotaB() {
        // Acopera: return grades[i] cand i=1 (thresholds[1]=80)
        assertEquals("B", Calculator.calculateGrade(85, 0, false));
    }

    @Test
    @DisplayName("Nota C — total >= 70 si < 80")
    void testNotaC() {
        // Acopera: return grades[i] cand i=2 (thresholds[2]=70)
        assertEquals("C", Calculator.calculateGrade(70, 0, false));
    }

    @Test
    @DisplayName("Nota D — total >= 60 si < 70")
    void testNotaD() {
        // Acopera: return grades[i] cand i=3 (thresholds[3]=60)
        assertEquals("D", Calculator.calculateGrade(60, 0, false));
    }

    @Test
    @DisplayName("Nota F — total < 60, bucla se epuizeaza")
    void testNotaF() {
        // Acopera: return "F" (dupa iesirea din bucla for)
        assertEquals("F", Calculator.calculateGrade(30, 0, false));
    }
}
