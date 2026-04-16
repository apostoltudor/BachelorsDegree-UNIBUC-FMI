package com.tss;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/**
 * Testare functionala — Partitionare in clase de echivalenta.
 *
 * Strategia:
 * Domeniul de intrare este impartit in clase de echivalenta (grupuri de valori
 * care ar trebui sa produca acelasi comportament). Se testeaza un singur
 * reprezentant din fiecare clasa.
 *
 * Clase de echivalenta identificate:
 *
 * PARAMETRU score:
 *   CE1: score invalid negativ        (score < 0)         → IllegalArgumentException
 *   CE2: score valid, nota F           (0 <= score < 60)   → "F"
 *   CE3: score valid, nota D           (60 <= score < 70)  → "D"
 *   CE4: score valid, nota C           (70 <= score < 80)  → "C"
 *   CE5: score valid, nota B           (80 <= score < 90)  → "B"
 *   CE6: score valid, nota A           (90 <= score <= 100) → "A"
 *   CE7: score invalid prea mare       (score > 100)       → IllegalArgumentException
 *
 * PARAMETRU bonus:
 *   CE8: bonus = 0                     → nu influenteaza totalul
 *   CE9: bonus > 0                     → creste totalul
 *
 * PARAMETRU extraCredit:
 *   CE10: extraCredit = false          → totalul este score + bonus
 *   CE11: extraCredit = true           → totalul este score + bonus + 5
 *   CE12: extraCredit = true si total >= 90 → "A+"
 */
@DisplayName("Testare Functionala: Partitionare in Clase de Echivalenta")
public class EquivalencePartitioningTest {

    // =========================================================================
    // CE1: Score invalid — negativ
    // =========================================================================
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

    // =========================================================================
    // CE7: Score invalid — prea mare
    // =========================================================================
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

    // =========================================================================
    // CE2: Score valid → nota F (total < 60)
    // =========================================================================
    @Test
    @DisplayName("CE2: score = 30, bonus = 0, extraCredit = false → F")
    void scoreValidNotaF() {
        assertEquals("F", Calculator.calculateGrade(30, 0, false));
    }

    // =========================================================================
    // CE3: Score valid → nota D (60 <= total < 70)
    // =========================================================================
    @Test
    @DisplayName("CE3: score = 65, bonus = 0, extraCredit = false → D")
    void scoreValidNotaD() {
        assertEquals("D", Calculator.calculateGrade(65, 0, false));
    }

    // =========================================================================
    // CE4: Score valid → nota C (70 <= total < 80)
    // =========================================================================
    @Test
    @DisplayName("CE4: score = 75, bonus = 0, extraCredit = false → C")
    void scoreValidNotaC() {
        assertEquals("C", Calculator.calculateGrade(75, 0, false));
    }

    // =========================================================================
    // CE5: Score valid → nota B (80 <= total < 90)
    // =========================================================================
    @Test
    @DisplayName("CE5: score = 85, bonus = 0, extraCredit = false → B")
    void scoreValidNotaB() {
        assertEquals("B", Calculator.calculateGrade(85, 0, false));
    }

    // =========================================================================
    // CE6: Score valid → nota A (total >= 90, fara extraCredit)
    // =========================================================================
    @Test
    @DisplayName("CE6: score = 95, bonus = 0, extraCredit = false → A")
    void scoreValidNotaA() {
        assertEquals("A", Calculator.calculateGrade(95, 0, false));
    }

    // =========================================================================
    // CE8: Bonus = 0 (nu influenteaza totalul)
    // =========================================================================
    @Test
    @DisplayName("CE8: score = 50, bonus = 0, extraCredit = false → F (bonus nu schimba)")
    void bonusZero() {
        assertEquals("F", Calculator.calculateGrade(50, 0, false));
    }

    // =========================================================================
    // CE9: Bonus > 0 (creste totalul, poate schimba nota)
    // =========================================================================
    @Test
    @DisplayName("CE9: score = 58, bonus = 5, extraCredit = false → D (bonus ridica de la F la D)")
    void bonusSchimbaNotaDeLaFLaD() {
        // total = 58 + 5 = 63 → D
        assertEquals("D", Calculator.calculateGrade(58, 5, false));
    }

    // =========================================================================
    // CE10: extraCredit = false
    // =========================================================================
    @Test
    @DisplayName("CE10: score = 70, bonus = 0, extraCredit = false → C")
    void extraCreditFalse() {
        assertEquals("C", Calculator.calculateGrade(70, 0, false));
    }

    // =========================================================================
    // CE11: extraCredit = true (adauga +5)
    // =========================================================================
    @Test
    @DisplayName("CE11: score = 65, bonus = 0, extraCredit = true → C (65+5=70)")
    void extraCreditTrue() {
        // total = 65 + 0 + 5 = 70 → C
        assertEquals("C", Calculator.calculateGrade(65, 0, true));
    }

    // =========================================================================
    // CE12: extraCredit = true si total >= 90 → A+
    // =========================================================================
    @Test
    @DisplayName("CE12: score = 88, bonus = 0, extraCredit = true → A+ (88+5=93>=90, extra=true)")
    void extraCreditTrueCuAPlus() {
        // total = 88 + 0 + 5 = 93 >= 90 si extraCredit=true → A+
        assertEquals("A+", Calculator.calculateGrade(88, 0, true));
    }
}
