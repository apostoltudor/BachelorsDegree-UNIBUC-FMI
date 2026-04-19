package com.tss;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

// testare functionala - partitionare in clase de echivalenta
@DisplayName("Testare Functionala: Partitionare in Clase de Echivalenta")
public class EquivalencePartitioningTest {

    // scor negativ
    @Nested
    @DisplayName("CE1: Score negativ (invalid)")
    class ScoreNegativ {

        @Test
        @DisplayName("score = -5, bonus = 0, extraCredit = false → exceptie")
        void scoreNegativ() {
            assertThrows(IllegalArgumentException.class, () ->
                Calculator.calculateGrade(-5, 0, false));
        }

        @Test
        @DisplayName("score = -100, bonus = 10, extraCredit = true → exceptie")
        void scoreNegativMare() {
            assertThrows(IllegalArgumentException.class, () ->
                Calculator.calculateGrade(-100, 10, true));
        }
    }

    // scor peste suta
    @Nested
    @DisplayName("CE7: Score peste 100 (invalid)")
    class ScorePeste100 {

        @Test
        @DisplayName("score = 101, bonus = 0, extraCredit = false → exceptie")
        void scorePeste100() {
            assertThrows(IllegalArgumentException.class, () ->
                Calculator.calculateGrade(101, 0, false));
        }

        @Test
        @DisplayName("score = 200, bonus = 5, extraCredit = true → exceptie")
        void scoreFoarteMare() {
            assertThrows(IllegalArgumentException.class, () ->
                Calculator.calculateGrade(200, 5, true));
        }
    }

    // pici clasa
    @Test
    @DisplayName("CE2: score = 30, bonus = 0, extraCredit = false → F")
    void scoreValidNotaF() {
        assertEquals("F", Calculator.calculateGrade(30, 0, false));
    }

    // la limita trecerii
    @Test
    @DisplayName("CE3: score = 65, bonus = 0, extraCredit = false → D")
    void scoreValidNotaD() {
        assertEquals("D", Calculator.calculateGrade(65, 0, false));
    }

    // nota medie
    @Test
    @DisplayName("CE4: score = 75, bonus = 0, extraCredit = false → C")
    void scoreValidNotaC() {
        assertEquals("C", Calculator.calculateGrade(75, 0, false));
    }

    // nota buna
    @Test
    @DisplayName("CE5: score = 85, bonus = 0, extraCredit = false → B")
    void scoreValidNotaB() {
        assertEquals("B", Calculator.calculateGrade(85, 0, false));
    }

    // foarte bine
    @Test
    @DisplayName("CE6: score = 95, bonus = 0, extraCredit = false → A")
    void scoreValidNotaA() {
        assertEquals("A", Calculator.calculateGrade(95, 0, false));
    }

    // fara bonus
    @Test
    @DisplayName("CE8: score = 50, bonus = 0, extraCredit = false → F (bonus nu schimba)")
    void bonusZero() {
        assertEquals("F", Calculator.calculateGrade(50, 0, false));
    }

    // bonus te salveaza
    @Test
    @DisplayName("CE9: score = 58, bonus = 5, extraCredit = false → D (bonus ridica de la F la D)")
    void bonusSchimbaNotaDeLaFLaD() {
        assertEquals("D", Calculator.calculateGrade(58, 5, false));
    }

    // fara puncte extra
    @Test
    @DisplayName("CE10: score = 70, bonus = 0, extraCredit = false → C")
    void extraCreditFalse() {
        assertEquals("C", Calculator.calculateGrade(70, 0, false));
    }

    // puncte extra
    @Test
    @DisplayName("CE11: score = 65, bonus = 0, extraCredit = true → C (65+5=70)")
    void extraCreditTrue() {
        assertEquals("C", Calculator.calculateGrade(65, 0, true));
    }

    // nota maxima
    @Test
    @DisplayName("CE12: score = 88, bonus = 0, extraCredit = true → A+ (88+5=93>=90, extra=true)")
    void extraCreditTrueCuAPlus() {
        assertEquals("A+", Calculator.calculateGrade(88, 0, true));
    }
}
