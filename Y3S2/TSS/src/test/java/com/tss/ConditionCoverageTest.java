package com.tss;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;


@DisplayName("Testare Structurala: Acoperire la Nivel de Conditie / MC/DC")
public class ConditionCoverageTest {

    // =====================================================
    // MC/DC PENTRU DECIZIA D1: (score < 0 || score > 100)
    // Operator OR cu 2 conditii individuale.
    //
    // Pentru a demonstra independenta fiecarei conditii:
    // - Schimbam o singura conditie si observam ca decizia se schimba
    // - Celelalte conditii raman la aceeasi valoare (constante)
    // =====================================================

    /**
     * Testele MC/DC pentru decizia compusa D1 (OR).
     * Testam 3 combinatii care demonstreaza efectul independent
     * al fiecarei conditii asupra rezultatului deciziei.
     */
    @Nested
    @DisplayName("D1: MC/DC pentru (score < 0 || score > 100)")
    class D1_MCDC {

        @Test
        @DisplayName("t1: C1=FALSE, C2=TRUE → D1=TRUE (score=101 demonstreaza efectul C2)")
        void t1_c1False_c2True() {
            // t1: score=101 => C1=(101<0)=FALSE, C2=(101>100)=TRUE => D1=TRUE
            // Pereche cu t3 pentru C2: in t3 C2=FALSE si D1=FALSE, aici C2=TRUE si D1=TRUE
            // => C2 influenteaza independent decizia D1
            assertThrows(IllegalArgumentException.class, () ->
                Calculator.calculateGrade(101, 0, false));
        }

        @Test
        @DisplayName("t2: C1=TRUE, C2=FALSE → D1=TRUE (score=-1 demonstreaza efectul C1)")
        void t2_c1True_c2False() {
            // t2: score=-1 => C1=(-1<0)=TRUE, C2=(-1>100)=FALSE => D1=TRUE
            // Pereche cu t3 pentru C1: in t3 C1=FALSE si D1=FALSE, aici C1=TRUE si D1=TRUE
            // => C1 influenteaza independent decizia D1
            assertThrows(IllegalArgumentException.class, () ->
                Calculator.calculateGrade(-1, 0, false));
        }

        @Test
        @DisplayName("t3: C1=FALSE, C2=FALSE → D1=FALSE (score=50, executie normala)")
        void t3_c1False_c2False() {
            // t3: score=50 => C1=(50<0)=FALSE, C2=(50>100)=FALSE => D1=FALSE
            // Aceasta este baza de comparatie: cand ambele conditii sunt FALSE,
            // decizia globala este FALSE => executia continua normal
            assertEquals("F", Calculator.calculateGrade(50, 0, false));
        }
    }

    // =====================================================
    // MC/DC PENTRU DECIZIA D6: (thresholds[i] == 90 && extraCredit)
    // Operator AND cu 2 conditii individuale.
    //
    // Pentru AND, avem nevoie de:
    // - TRUE && TRUE => TRUE (baza)
    // - TRUE && FALSE => FALSE (demonstreaza efectul C4)
    // - FALSE && TRUE => FALSE (demonstreaza efectul C3)
    // =====================================================

    /**
     * Testele MC/DC pentru decizia compusa D6 (AND).
     * Demonstram ca fiecare conditie individuala influenteaza independent
     * rezultatul deciziei compuse.
     */
    @Nested
    @DisplayName("D6: MC/DC pentru (thresholds[i] == 90 && extraCredit)")
    class D6_MCDC {

        @Test
        @DisplayName("t4: C3=TRUE, C4=TRUE → D6=TRUE (total>=90, extra=true → A+)")
        void t4_c3True_c4True() {
            // t4: score=90, extra=true => total=95, prag=90
            // C3=(90==90)=TRUE, C4=(extra)=TRUE => D6=TRUE => return "A+"
            // Aceasta este baza: ambele conditii TRUE => decizia TRUE
            assertEquals("A+", Calculator.calculateGrade(90, 0, true));
        }

        @Test
        @DisplayName("t5: C3=TRUE, C4=FALSE → D6=FALSE (total>=90, extra=false → A)")
        void t5_c3True_c4False() {
            // t5: score=95, extra=false => total=95, prag=90
            // C3=(90==90)=TRUE, C4=(extra)=FALSE => D6=FALSE => return "A"
            // Pereche cu t4 pentru C4: singura schimbare e C4 (TRUE→FALSE)
            // si decizia se schimba (TRUE→FALSE) => C4 influenteaza independent
            assertEquals("A", Calculator.calculateGrade(95, 0, false));
        }

        @Test
        @DisplayName("t6: C3=FALSE, C4=TRUE → D6=FALSE (total in [80,90), extra=true → B)")
        void t6_c3False_c4True() {
            // t6: score=77, extra=true => total=77+5=82, prag=80 (nu 90!)
            // C3=(80==90)=FALSE, C4=(extra)=TRUE => D6=FALSE => return "B"
            // Pereche cu t4 pentru C3: singura schimbare e C3 (TRUE→FALSE)
            // si decizia se schimba (TRUE→FALSE) => C3 influenteaza independent
            assertEquals("B", Calculator.calculateGrade(77, 0, true));
        }
    }

    // =====================================================
    // CONDITII SIMPLE (FIECARE IA TRUE SI FALSE)
    // Pentru deciziile simple (o singura conditie), este suficient
    // sa demonstram ca iau atat TRUE cat si FALSE.
    // Acesta completeaza acoperirea la nivel de conditie.
    // =====================================================

    /**
     * Verificare suplimentara: fiecare conditie simpla din program
     * ia atat valoarea TRUE cat si FALSE.
     * Aceasta sectiune acopera deciziile D2, D3, D4 si D5 la nivel de conditie.
     */
    @Nested
    @DisplayName("Conditii simple: fiecare ia TRUE si FALSE")
    class ConditiiSimple {

        @Test
        @DisplayName("extraCredit = TRUE")
        void extraCreditTrue() {
            // D2 conditia extraCredit ia valoarea TRUE
            // score=65, extra=true => total=70 => nota C
            assertEquals("C", Calculator.calculateGrade(65, 0, true));
        }

        @Test
        @DisplayName("extraCredit = FALSE")
        void extraCreditFalse() {
            // D2 conditia extraCredit ia valoarea FALSE
            // score=65, extra=false => total=65 => nota D
            assertEquals("D", Calculator.calculateGrade(65, 0, false));
        }

        @Test
        @DisplayName("total > 105 = TRUE")
        void totalPeste105True() {
            // D3 conditia (total > 105) ia valoarea TRUE
            // total = 100+20 = 120 > 105 => se plafoneaza la 105 => nota A
            assertEquals("A", Calculator.calculateGrade(100, 20, false));
        }

        @Test
        @DisplayName("total > 105 = FALSE")
        void totalPeste105False() {
            // D3 conditia (total > 105) ia valoarea FALSE
            // total = 75 nu depaseste 105 => ramane neschimbat => nota C
            assertEquals("C", Calculator.calculateGrade(75, 0, false));
        }

        @Test
        @DisplayName("total >= thresholds[i] = TRUE (la prima iteratie)")
        void totalPestePragTrue() {
            // D5 conditia (total >= thresholds[i]) ia valoarea TRUE
            // total=95 >= thresholds[0]=90 => potrivire gasita => nota A
            assertEquals("A", Calculator.calculateGrade(95, 0, false));
        }

        @Test
        @DisplayName("total >= thresholds[i] = FALSE (total sub toate pragurile)")
        void totalSubToatePragurile() {
            // D5 conditia (total >= thresholds[i]) ia valoarea FALSE la TOATE iteratiile
            // total=20 < 60 < 70 < 80 < 90 => niciun prag nu e atins => nota F
            assertEquals("F", Calculator.calculateGrade(20, 0, false));
        }
    }
}
