package com.tss;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

// testare structurala - executam fiecare instructiune
@DisplayName("Testare Structurala: Acoperire la Nivel de Instructiune (Statement Coverage)")
public class StatementCoverageTest {

    // testare eroare
    @Test
    @DisplayName("Instructiunea throw — score invalid triggereaza exceptia")
    void testExceptieScoreInvalid() {
        // Acopera: if (score < 0 || score > 100) throw new IllegalArgumentException
        assertThrows(IllegalArgumentException.class, () ->
            Calculator.calculateGrade(-5, 0, false));
    }

    // testare ramura adevarat extra
    @Test
    @DisplayName("Ramura extraCredit = true — total = score + bonus + 5")
    void testExtraCreditTrue() {
        // Acopera: if (extraCredit) → total = score + bonus + 5
        // score=80, bonus=0, extra=true → total = 85 → B
        assertEquals("B", Calculator.calculateGrade(80, 0, true));
    }

    // testare ramura fals extra
    @Test
    @DisplayName("Ramura extraCredit = false — total = score + bonus")
    void testExtraCreditFalse() {
        assertEquals("C", Calculator.calculateGrade(75, 0, false));
    }

    // testare decizie limitare
    @Test
    @DisplayName("Limitarea totalului la 105 — total > 105 devine 105")
    void testLimitareTotal105() {
        assertEquals("A", Calculator.calculateGrade(100, 20, false));
    }

    // nota maxima
    @Test
    @DisplayName("Nota A+ — conditie compusa thresholds[i]==90 && extraCredit")
    void testNotaAPlus() {
        assertEquals("A+", Calculator.calculateGrade(90, 0, true));
    }

    // nota a
    @Test
    @DisplayName("Nota A — total >= 90, fara extraCredit")
    void testNotaA() {
        assertEquals("A", Calculator.calculateGrade(95, 0, false));
    }

    // nota b
    @Test
    @DisplayName("Nota B — total >= 80 si < 90")
    void testNotaB() {
        assertEquals("B", Calculator.calculateGrade(85, 0, false));
    }

    // nota c
    @Test
    @DisplayName("Nota C — total >= 70 si < 80")
    void testNotaC() {
        assertEquals("C", Calculator.calculateGrade(70, 0, false));
    }

    // nota d
    @Test
    @DisplayName("Nota D — total >= 60 si < 70")
    void testNotaD() {
        assertEquals("D", Calculator.calculateGrade(60, 0, false));
    }

    // nota de picare
    @Test
    @DisplayName("Nota F — total < 60, bucla se epuizeaza")
    void testNotaF() {
        assertEquals("F", Calculator.calculateGrade(30, 0, false));
    }
}
