package com.tss;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

// testare structurala - acoperim toate ramurile
@DisplayName("Testare Structurala: Acoperire la Nivel de Decizie/Ramura (Branch Coverage)")
public class BranchCoverageTest {

    // ramuri aruncare exceptie
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

    // ramuri puncte bonus
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
            assertEquals("D", Calculator.calculateGrade(65, 0, false));
        }
    }

    // ramuri maxim permis
    @Nested
    @DisplayName("D3: Limitarea totalului la 105")
    class D3_LimitareTotal {

        @Test
        @DisplayName("D3 TRUE: total = 120 → se limiteaza la 105")
        void d3True() {
            assertEquals("A", Calculator.calculateGrade(100, 20, false));
        }

        @Test
        @DisplayName("D3 FALSE: total = 75 → ramane 75")
        void d3False() {
            assertEquals("C", Calculator.calculateGrade(75, 0, false));
        }
    }

    // ramuri verificare bucla
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
            assertEquals("F", Calculator.calculateGrade(30, 0, false));
        }
    }

    // ramuri gasire prag
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
            assertEquals("B", Calculator.calculateGrade(85, 0, false));
        }
    }

    // ramuri validare a plus
    @Nested
    @DisplayName("D6: Conditia A+ (compusa)")
    class D6_ConditiaAPlus {

        @Test
        @DisplayName("D6 TRUE: total >= 90 si extraCredit = true → A+")
        void d6True() {
            assertEquals("A+", Calculator.calculateGrade(90, 0, true));
        }

        @Test
        @DisplayName("D6 FALSE: total >= 90 dar extraCredit = false → A")
        void d6False() {
            assertEquals("A", Calculator.calculateGrade(95, 0, false));
        }
    }
}
