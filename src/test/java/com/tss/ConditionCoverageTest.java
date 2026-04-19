package com.tss;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

// testare structurala - acoperim mcdc
@DisplayName("Testare Structurala: Acoperire la Nivel de Conditie / MC/DC")
public class ConditionCoverageTest {

    // testare conditie eroare
    @Nested
    @DisplayName("D1: MC/DC pentru (score < 0 || score > 100)")
    class D1_MCDC {

        @Test
        @DisplayName("t1: C1=FALSE, C2=TRUE → D1=TRUE (score=101 demonstreaza efectul C2)")
        void t1_c1False_c2True() {
            // score=101 → score<0 este FALSE, score>100 este TRUE → exceptie
            assertThrows(IllegalArgumentException.class, () ->
                Calculator.calculateGrade(101, 0, false));
        }

        @Test
        @DisplayName("t2: C1=TRUE, C2=FALSE → D1=TRUE (score=-1 demonstreaza efectul C1)")
        void t2_c1True_c2False() {
            assertThrows(IllegalArgumentException.class, () ->
                Calculator.calculateGrade(-1, 0, false));
        }

        @Test
        @DisplayName("t3: C1=FALSE, C2=FALSE → D1=FALSE (score=50, executie normala)")
        void t3_c1False_c2False() {
            assertEquals("F", Calculator.calculateGrade(50, 0, false));
        }
    }

    // testare conditie a plus
    @Nested
    @DisplayName("D6: MC/DC pentru (thresholds[i] == 90 && extraCredit)")
    class D6_MCDC {

        @Test
        @DisplayName("t4: C3=TRUE, C4=TRUE → D6=TRUE (total>=90, extra=true → A+)")
        void t4_c3True_c4True() {
            assertEquals("A+", Calculator.calculateGrade(90, 0, true));
        }

        @Test
        @DisplayName("t5: C3=TRUE, C4=FALSE → D6=FALSE (total>=90, extra=false → A)")
        void t5_c3True_c4False() {
            assertEquals("A", Calculator.calculateGrade(95, 0, false));
        }

        @Test
        @DisplayName("t6: C3=FALSE, C4=TRUE → D6=FALSE (total in [80,90), extra=true → B)")
        void t6_c3False_c4True() {
            assertEquals("B", Calculator.calculateGrade(77, 0, true));
        }
    }

    // testare celalalte if uri
    @Nested
    @DisplayName("Conditii simple: fiecare ia TRUE si FALSE")
    class ConditiiSimple {

        @Test
        @DisplayName("extraCredit = TRUE")
        void extraCreditTrue() {
            assertEquals("C", Calculator.calculateGrade(65, 0, true));
        }

        @Test
        @DisplayName("extraCredit = FALSE")
        void extraCreditFalse() {
            assertEquals("D", Calculator.calculateGrade(65, 0, false));
        }

        @Test
        @DisplayName("total > 105 = TRUE")
        void totalPeste105True() {
            assertEquals("A", Calculator.calculateGrade(100, 20, false));
        }

        @Test
        @DisplayName("total > 105 = FALSE")
        void totalPeste105False() {
            assertEquals("C", Calculator.calculateGrade(75, 0, false));
        }

        @Test
        @DisplayName("total >= thresholds[i] = TRUE (la prima iteratie)")
        void totalPestePragTrue() {
            assertEquals("A", Calculator.calculateGrade(95, 0, false));
        }

        @Test
        @DisplayName("total >= thresholds[i] = FALSE (total sub toate pragurile)")
        void totalSubToatePragurile() {
            assertEquals("F", Calculator.calculateGrade(20, 0, false));
        }
    }
}
