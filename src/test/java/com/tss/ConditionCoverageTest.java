package com.tss;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/**
 * Testare structurala — Acoperire la nivel de conditie si MC/DC
 * (Modified Condition/Decision Coverage).
 *
 * Strategia:
 * Fiecare conditie INDIVIDUALA dintr-o decizie compusa trebuie sa ia atat
 * valoarea TRUE cat si valoarea FALSE, si fiecare conditie trebuie sa
 * influenteze independent decizia din care face parte.
 *
 * =========================================================================
 * Decizia D1: score < 0 || score > 100
 *   Conditii individuale: C1 = (score < 0), C2 = (score > 100)
 *
 *   Tabel MC/DC pentru OR:
 *   Test | C1      | C2      | D1 (C1||C2) | Efect demonstrat
 *   t1   | FALSE   | TRUE    | TRUE        | C2 influenteaza D1
 *   t2   | TRUE    | FALSE   | TRUE        | C1 influenteaza D1
 *   t3   | FALSE   | FALSE   | FALSE       | (baza)
 *
 *   t2 si t3 demonstreaza efectul independent al C1
 *   t1 si t3 demonstreaza efectul independent al C2
 * =========================================================================
 *
 * =========================================================================
 * Decizia D6: thresholds[i] == 90 && extraCredit
 *   Conditii individuale: C3 = (thresholds[i] == 90), C4 = (extraCredit)
 *
 *   Tabel MC/DC pentru AND:
 *   Test | C3      | C4      | D6 (C3&&C4) | Efect demonstrat
 *   t4   | TRUE    | TRUE    | TRUE        | (baza)
 *   t5   | TRUE    | FALSE   | FALSE       | C4 influenteaza D6
 *   t6   | FALSE   | TRUE    | FALSE       | C3 influenteaza D6
 *
 *   t4 si t5 demonstreaza efectul independent al C4
 *   t4 si t6 demonstreaza efectul independent al C3
 * =========================================================================
 */
@DisplayName("Testare Structurala: Acoperire la Nivel de Conditie / MC/DC")
public class ConditionCoverageTest {

    // =========================================================================
    // D1: score < 0 || score > 100 — MC/DC
    // =========================================================================
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
            // score=-1 → score<0 este TRUE, score>100 este FALSE → exceptie
            assertThrows(IllegalArgumentException.class, () ->
                Calculator.calculateGrade(-1, 0, false));
        }

        @Test
        @DisplayName("t3: C1=FALSE, C2=FALSE → D1=FALSE (score=50, executie normala)")
        void t3_c1False_c2False() {
            // score=50 → score<0 este FALSE, score>100 este FALSE → continua
            assertEquals("F", Calculator.calculateGrade(50, 0, false));
        }

        // Nota: t1 si t3 dovedesc ca C2 influenteaza independent D1
        //       t2 si t3 dovedesc ca C1 influenteaza independent D1
    }

    // =========================================================================
    // D6: thresholds[i] == 90 && extraCredit — MC/DC
    // =========================================================================
    @Nested
    @DisplayName("D6: MC/DC pentru (thresholds[i] == 90 && extraCredit)")
    class D6_MCDC {

        @Test
        @DisplayName("t4: C3=TRUE, C4=TRUE → D6=TRUE (total>=90, extra=true → A+)")
        void t4_c3True_c4True() {
            // score=90, bonus=0, extra=true → total=95, thresholds[0]=90 → C3=T, C4=T → A+
            assertEquals("A+", Calculator.calculateGrade(90, 0, true));
        }

        @Test
        @DisplayName("t5: C3=TRUE, C4=FALSE → D6=FALSE (total>=90, extra=false → A)")
        void t5_c3True_c4False() {
            // score=95, bonus=0, extra=false → total=95, thresholds[0]=90 → C3=T, C4=F → A
            assertEquals("A", Calculator.calculateGrade(95, 0, false));
        }

        @Test
        @DisplayName("t6: C3=FALSE, C4=TRUE → D6=FALSE (total in [80,90), extra=true → B)")
        void t6_c3False_c4True() {
            // score=77, bonus=0, extra=true → total=82
            // La iteratia i=0: thresholds[0]=90, 82<90 → C5 false, nu se ajunge la D6
            // La iteratia i=1: thresholds[1]=80, 82>=80 → C5 true, dar thresholds[1]!=90
            //   → C3=FALSE → D6=FALSE → return "B"
            assertEquals("B", Calculator.calculateGrade(77, 0, true));
        }

        // Nota: t4 si t5 dovedesc ca C4 (extraCredit) influenteaza independent D6
        //       t4 si t6 dovedesc ca C3 (thresholds[i]==90) influenteaza independent D6
    }

    // =========================================================================
    // Conditii simple — se asigura ca iau si TRUE si FALSE
    // =========================================================================
    @Nested
    @DisplayName("Conditii simple: fiecare ia TRUE si FALSE")
    class ConditiiSimple {

        @Test
        @DisplayName("extraCredit = TRUE")
        void extraCreditTrue() {
            assertEquals("C", Calculator.calculateGrade(65, 0, true)); // total=70
        }

        @Test
        @DisplayName("extraCredit = FALSE")
        void extraCreditFalse() {
            assertEquals("D", Calculator.calculateGrade(65, 0, false)); // total=65
        }

        @Test
        @DisplayName("total > 105 = TRUE")
        void totalPeste105True() {
            assertEquals("A", Calculator.calculateGrade(100, 20, false)); // total=120→105
        }

        @Test
        @DisplayName("total > 105 = FALSE")
        void totalPeste105False() {
            assertEquals("C", Calculator.calculateGrade(75, 0, false)); // total=75
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
