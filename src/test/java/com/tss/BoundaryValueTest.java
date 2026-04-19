package com.tss;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

// testare functionala - analiza valorilor de frontiera
@DisplayName("Testare Functionala: Analiza Valorilor de Frontiera (BVA)")
public class BoundaryValueTest {

    // testare scor zero
    @Nested
    @DisplayName("Frontiera score: limita inferioara (0)")
    class FrontieraScoreLimitaInferioara {

        @Test
        @DisplayName("score = -1 → exceptie (sub limita inferioara)")
        void scoreMinus1() {
            assertThrows(IllegalArgumentException.class, () ->
                Calculator.calculateGrade(-1, 0, false));
        }

        @Test
        @DisplayName("score = 0 → F (pe limita inferioara)")
        void scoreZero() {
            assertEquals("F", Calculator.calculateGrade(0, 0, false));
        }

        @Test
        @DisplayName("score = 1 → F (deasupra limitei inferioare)")
        void score1() {
            assertEquals("F", Calculator.calculateGrade(1, 0, false));
        }
    }

    // testare suta
    @Nested
    @DisplayName("Frontiera score: limita superioara (100)")
    class FrontieraScoreLimitaSuperioara {

        @Test
        @DisplayName("score = 99 → A (sub limita superioara)")
        void score99() {
            assertEquals("A", Calculator.calculateGrade(99, 0, false));
        }

        @Test
        @DisplayName("score = 100 → A (pe limita superioara)")
        void score100() {
            assertEquals("A", Calculator.calculateGrade(100, 0, false));
        }

        @Test
        @DisplayName("score = 101 → exceptie (deasupra limitei superioare)")
        void score101() {
            assertThrows(IllegalArgumentException.class, () ->
                Calculator.calculateGrade(101, 0, false));
        }
    }

    // limita de trecere
    @Nested
    @DisplayName("Frontiera prag 60 (D vs F)")
    class FrontieraPrag60 {

        @Test
        @DisplayName("total = 59 → F (sub prag)")
        void total59() {
            assertEquals("F", Calculator.calculateGrade(59, 0, false));
        }

        @Test
        @DisplayName("total = 60 → D (pe prag)")
        void total60() {
            assertEquals("D", Calculator.calculateGrade(60, 0, false));
        }

        @Test
        @DisplayName("total = 61 → D (deasupra prag)")
        void total61() {
            assertEquals("D", Calculator.calculateGrade(61, 0, false));
        }
    }

    // limita nota mica
    @Nested
    @DisplayName("Frontiera prag 70 (C vs D)")
    class FrontieraPrag70 {

        @Test
        @DisplayName("total = 69 → D (sub prag)")
        void total69() {
            assertEquals("D", Calculator.calculateGrade(69, 0, false));
        }

        @Test
        @DisplayName("total = 70 → C (pe prag)")
        void total70() {
            assertEquals("C", Calculator.calculateGrade(70, 0, false));
        }

        @Test
        @DisplayName("total = 71 → C (deasupra prag)")
        void total71() {
            assertEquals("C", Calculator.calculateGrade(71, 0, false));
        }
    }

    // limita nota medie
    @Nested
    @DisplayName("Frontiera prag 80 (B vs C)")
    class FrontieraPrag80 {

        @Test
        @DisplayName("total = 79 → C (sub prag)")
        void total79() {
            assertEquals("C", Calculator.calculateGrade(79, 0, false));
        }

        @Test
        @DisplayName("total = 80 → B (pe prag)")
        void total80() {
            assertEquals("B", Calculator.calculateGrade(80, 0, false));
        }

        @Test
        @DisplayName("total = 81 → B (deasupra prag)")
        void total81() {
            assertEquals("B", Calculator.calculateGrade(81, 0, false));
        }
    }

    // limita nota mare
    @Nested
    @DisplayName("Frontiera prag 90 (A vs B)")
    class FrontieraPrag90 {

        @Test
        @DisplayName("total = 89 → B (sub prag)")
        void total89() {
            assertEquals("B", Calculator.calculateGrade(89, 0, false));
        }

        @Test
        @DisplayName("total = 90 → A (pe prag, fara extraCredit)")
        void total90() {
            assertEquals("A", Calculator.calculateGrade(90, 0, false));
        }

        @Test
        @DisplayName("total = 91 → A (deasupra prag, fara extraCredit)")
        void total91() {
            assertEquals("A", Calculator.calculateGrade(91, 0, false));
        }

        @Test
        @DisplayName("total = 90 cu extraCredit → A+ (pe prag, cu extraCredit)")
        void total90CuExtraCredit() {
            assertEquals("A+", Calculator.calculateGrade(85, 0, true));
        }
    }

    // limita puncte maxime
    @Nested
    @DisplayName("Frontiera limitarii total la 105")
    class FrontieraLimitareTotal {

        @Test
        @DisplayName("total = 104 → A (sub limita de cap)")
        void total104() {
            assertEquals("A", Calculator.calculateGrade(100, 4, false));
        }

        @Test
        @DisplayName("total = 105 → A (pe limita de cap)")
        void total105() {
            assertEquals("A", Calculator.calculateGrade(100, 5, false));
        }

        @Test
        @DisplayName("total ar fi 110 dar se limiteaza la 105 → A")
        void totalCapAtLa105() {
            assertEquals("A", Calculator.calculateGrade(100, 10, false));
        }

        @Test
        @DisplayName("total ar fi 125 cu extraCredit, se limiteaza la 105 → A+")
        void totalCapAtCuExtraCredit() {
            assertEquals("A+", Calculator.calculateGrade(100, 20, true));
        }
    }
}
