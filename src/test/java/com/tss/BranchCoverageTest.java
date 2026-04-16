package com.tss;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/**
 * Testare structurala — Acoperire la nivel de decizie/ramura (Branch/Decision Coverage).
 *
 * Strategia:
 * Fiecare decizie (ramura) din metoda calculateGrade trebuie sa ia
 * atat valoarea TRUE cat si valoarea FALSE cel putin o data.
 *
 * Deciziile identificate:
 *
 * D1: if (score < 0 || score > 100)
 *     TRUE  → throw exception
 *     FALSE → continua executia normala
 *
 * D2: if (extraCredit)
 *     TRUE  → total = score + bonus + 5
 *     FALSE → total = score + bonus
 *
 * D3: if (total > 105)
 *     TRUE  → total = 105
 *     FALSE → total ramine neschimbat
 *
 * D4: conditia for: i < thresholds.length
 *     TRUE  → se intra in bucla
 *     FALSE → se iese din bucla (se ajunge la return "F")
 *
 * D5: if (total >= thresholds[i])
 *     TRUE  → se intra in bloc (verifica A+, sau returneaza nota)
 *     FALSE → se continua bucla
 *
 * D6: if (thresholds[i] == 90 && extraCredit)
 *     TRUE  → return "A+"
 *     FALSE → return grades[i]
 */
@DisplayName("Testare Structurala: Acoperire la Nivel de Decizie/Ramura (Branch Coverage)")
public class BranchCoverageTest {

    // =========================================================================
    // D1: if (score < 0 || score > 100) — TRUE si FALSE
    // =========================================================================
    @Nested
    @DisplayName("D1: Validare score")
    class D1_ValidareScore {

        @Test
        @DisplayName("D1 TRUE: score = -1 → exceptie")
        void d1True() {
            assertThrows(IllegalArgumentException.class, () ->
                Calculator.calculateGrade(-1, 0, false));
        }

        @Test
        @DisplayName("D1 FALSE: score = 50 → executie normala (F)")
        void d1False() {
            assertEquals("F", Calculator.calculateGrade(50, 0, false));
        }
    }

    // =========================================================================
    // D2: if (extraCredit) — TRUE si FALSE
    // =========================================================================
    @Nested
    @DisplayName("D2: Extra credit")
    class D2_ExtraCredit {

        @Test
        @DisplayName("D2 TRUE: extraCredit = true → total include +5")
        void d2True() {
            // score=65, bonus=0, extra=true → total=70 → C
            assertEquals("C", Calculator.calculateGrade(65, 0, true));
        }

        @Test
        @DisplayName("D2 FALSE: extraCredit = false → total fara +5")
        void d2False() {
            // score=65, bonus=0, extra=false → total=65 → D
            assertEquals("D", Calculator.calculateGrade(65, 0, false));
        }
    }

    // =========================================================================
    // D3: if (total > 105) — TRUE si FALSE
    // =========================================================================
    @Nested
    @DisplayName("D3: Limitarea totalului la 105")
    class D3_LimitareTotal {

        @Test
        @DisplayName("D3 TRUE: total = 120 → se limiteaza la 105")
        void d3True() {
            // score=100, bonus=20, extra=false → total=120 → capped 105 → A
            assertEquals("A", Calculator.calculateGrade(100, 20, false));
        }

        @Test
        @DisplayName("D3 FALSE: total = 75 → ramane 75")
        void d3False() {
            // score=75, bonus=0, extra=false → total=75 → C
            assertEquals("C", Calculator.calculateGrade(75, 0, false));
        }
    }

    // =========================================================================
    // D4: conditia for: i < thresholds.length — TRUE si FALSE
    // =========================================================================
    @Nested
    @DisplayName("D4: Bucla for (intrare si iesire)")
    class D4_BuclaFor {

        @Test
        @DisplayName("D4 TRUE: se intra in bucla si se gaseste nota A")
        void d4TrueGaseste() {
            assertEquals("A", Calculator.calculateGrade(95, 0, false));
        }

        @Test
        @DisplayName("D4 FALSE: se parcurge toata bucla fara match → F")
        void d4FalseEpuizare() {
            // total=30, nu se potriveste nici un prag → bucla se termina → F
            assertEquals("F", Calculator.calculateGrade(30, 0, false));
        }
    }

    // =========================================================================
    // D5: if (total >= thresholds[i]) — TRUE si FALSE
    // =========================================================================
    @Nested
    @DisplayName("D5: Verificare prag in bucla")
    class D5_VerificarePrag {

        @Test
        @DisplayName("D5 TRUE: total = 85 >= 80 → B")
        void d5True() {
            assertEquals("B", Calculator.calculateGrade(85, 0, false));
        }

        @Test
        @DisplayName("D5 FALSE: total = 85 < 90, se trece la urmatorul prag")
        void d5False() {
            // La prima iteratie (prag 90): 85 < 90 → FALSE, se continua
            // La a doua iteratie (prag 80): 85 >= 80 → TRUE → B
            assertEquals("B", Calculator.calculateGrade(85, 0, false));
        }
    }

    // =========================================================================
    // D6: if (thresholds[i] == 90 && extraCredit) — TRUE si FALSE
    // =========================================================================
    @Nested
    @DisplayName("D6: Conditia A+ (compusa)")
    class D6_ConditiaAPlus {

        @Test
        @DisplayName("D6 TRUE: total >= 90 si extraCredit = true → A+")
        void d6True() {
            // score=90, bonus=0, extra=true → total=95 → A+
            assertEquals("A+", Calculator.calculateGrade(90, 0, true));
        }

        @Test
        @DisplayName("D6 FALSE: total >= 90 dar extraCredit = false → A")
        void d6False() {
            // score=95, bonus=0, extra=false → total=95, thresholds[0]==90 dar extra=false → A
            assertEquals("A", Calculator.calculateGrade(95, 0, false));
        }
    }
}
