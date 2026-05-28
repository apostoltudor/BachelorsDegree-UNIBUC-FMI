package com.tss;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/**
 * testare functionala - analiza valorilor de frontiera
 *
 * Tehnica de testare functionala (black-box) complementara partitionarii in clase de echivalenta
 *
 * multe erori apar la limitele claselor de echivalenta, de aceea pentru fiecare frontiera se testeaza 3 valori:
 *   - valoarea imediat sub frontiera (off-point inferior)
 *   - valoarea exact pe frontiera (on-point)
 *   - valoarea imediat deasupra frontierei (off-point superior)
 *
 *
 * aceasta tehnica este eficienta deoarece erorile de tip "off-by-one" sunt printre cele mai comune in programare. 
 * testarea boundary value analysis le detecteaza
 */
@DisplayName("Testare Functionala: Analiza Valorilor de Frontiera")
public class BoundaryValueTest {

    // =====================================================
    // FRONTIERA SCORE: LIMITA INFERIOARA (0)
    // Domeniul valid al lui score incepe de la 0.
    // Testam: -1 (invalid), 0 (pe frontiera), 1 (valid).
    // =====================================================

    /**
     * Testeaza frontiera inferioara a parametrului score la valoarea 0.
     * Conform BVA, testam cele 3 puncte critice din jurul frontierei.
     */
    @Nested
    @DisplayName("Frontiera score: limita inferioara (0)")
    class FrontieraScoreLimitaInferioara {

        @Test
        @DisplayName("score = -1 → exceptie (sub limita inferioara)")
        void scoreMinus1() {
            // OFF-POINT INFERIOR: score = -1 este sub frontiera 0
            // Apartine clasei de echivalenta invalide => exceptie
            assertThrows(IllegalArgumentException.class, () ->
                Calculator.calculateGrade(-1, 0, false));
        }

        @Test
        @DisplayName("score = 0 → F (pe limita inferioara)")
        void scoreZero() {
            // ON-POINT: score = 0 este exact pe frontiera
            // Este prima valoare valida => trebuie acceptata (total=0 => F)
            assertEquals("F", Calculator.calculateGrade(0, 0, false));
        }

        @Test
        @DisplayName("score = 1 → F (deasupra limitei inferioare)")
        void score1() {
            // OFF-POINT SUPERIOR: score = 1, imediat deasupra frontierei
            // Confirma ca valorile imediat deasupra frontierei sunt tratate corect
            assertEquals("F", Calculator.calculateGrade(1, 0, false));
        }
    }

    // =====================================================
    // FRONTIERA SCORE: LIMITA SUPERIOARA (100)
    // Domeniul valid al lui score se termina la 100.
    // Testam: 99 (valid), 100 (pe frontiera), 101 (invalid).
    // =====================================================

    /**
     * Testeaza frontiera superioara a parametrului score la valoarea 100.
     */
    @Nested
    @DisplayName("Frontiera score: limita superioara (100)")
    class FrontieraScoreLimitaSuperioara {

        @Test
        @DisplayName("score = 99 → A (sub limita superioara)")
        void score99() {
            // OFF-POINT INFERIOR: score = 99, ultima valoare inainte de frontiera
            // total=99 >= 90 => nota A
            assertEquals("A", Calculator.calculateGrade(99, 0, false));
        }

        @Test
        @DisplayName("score = 100 → A (pe limita superioara)")
        void score100() {
            // ON-POINT: score = 100, exact pe frontiera superioara
            // Ultima valoare valida acceptata de program
            assertEquals("A", Calculator.calculateGrade(100, 0, false));
        }

        @Test
        @DisplayName("score = 101 → exceptie (deasupra limitei superioare)")
        void score101() {
            // OFF-POINT SUPERIOR: score = 101, prima valoare invalida
            // Trece in clasa invalida => exceptie
            assertThrows(IllegalArgumentException.class, () ->
                Calculator.calculateGrade(101, 0, false));
        }
    }

    // =====================================================
    // FRONTIERA PRAG 60: TRECERE INTRE NOTA F SI D
    // Pragul 60 separa nota F (total < 60) de nota D (total >= 60).
    // Testam: total=59 (F), total=60 (D), total=61 (D).
    // =====================================================

    /**
     * Testeaza frontiera pragului 60 care separa nota F de nota D.
     * Aceasta este o eroare clasica off-by-one: daca cineva scrie > in loc de >=,
     * testul total=60 ar detecta greseala.
     */
    @Nested
    @DisplayName("Frontiera prag 60 (D vs F)")
    class FrontieraPrag60 {

        @Test
        @DisplayName("total = 59 → F (sub prag)")
        void total59() {
            // OFF-POINT INFERIOR: total=59, cu 1 sub pragul 60
            // Nu atinge pragul, deci ramane pe nota F
            assertEquals("F", Calculator.calculateGrade(59, 0, false));
        }

        @Test
        @DisplayName("total = 60 → D (pe prag)")
        void total60() {
            // ON-POINT: total=60, exact pe prag
            // Conditia total >= 60 este TRUE => nota D
            assertEquals("D", Calculator.calculateGrade(60, 0, false));
        }

        @Test
        @DisplayName("total = 61 → D (deasupra prag)")
        void total61() {
            // OFF-POINT SUPERIOR: total=61, imediat deasupra pragului
            // Confirma ca nota D se aplica si deasupra frontierei
            assertEquals("D", Calculator.calculateGrade(61, 0, false));
        }
    }

    // =====================================================
    // FRONTIERA PRAG 70: TRECERE INTRE NOTA D SI C
    // =====================================================

    /**
     * Testeaza frontiera pragului 70 care separa nota D de nota C.
     */
    @Nested
    @DisplayName("Frontiera prag 70 (C vs D)")
    class FrontieraPrag70 {

        @Test
        @DisplayName("total = 69 → D (sub prag)")
        void total69() {
            // OFF-POINT INFERIOR: total=69, sub pragul 70 => ramane D
            assertEquals("D", Calculator.calculateGrade(69, 0, false));
        }

        @Test
        @DisplayName("total = 70 → C (pe prag)")
        void total70() {
            // ON-POINT: total=70, exact pe prag => trece la C
            assertEquals("C", Calculator.calculateGrade(70, 0, false));
        }

        @Test
        @DisplayName("total = 71 → C (deasupra prag)")
        void total71() {
            // OFF-POINT SUPERIOR: total=71 => confirma nota C
            assertEquals("C", Calculator.calculateGrade(71, 0, false));
        }
    }

    // =====================================================
    // FRONTIERA PRAG 80: TRECERE INTRE NOTA C SI B
    // =====================================================

    /**
     * Testeaza frontiera pragului 80 care separa nota C de nota B.
     */
    @Nested
    @DisplayName("Frontiera prag 80 (B vs C)")
    class FrontieraPrag80 {

        @Test
        @DisplayName("total = 79 → C (sub prag)")
        void total79() {
            // OFF-POINT INFERIOR: total=79, sub pragul 80 => nota C
            assertEquals("C", Calculator.calculateGrade(79, 0, false));
        }

        @Test
        @DisplayName("total = 80 → B (pe prag)")
        void total80() {
            // ON-POINT: total=80, exact pe prag => nota B
            assertEquals("B", Calculator.calculateGrade(80, 0, false));
        }

        @Test
        @DisplayName("total = 81 → B (deasupra prag)")
        void total81() {
            // OFF-POINT SUPERIOR: total=81 => confirma nota B
            assertEquals("B", Calculator.calculateGrade(81, 0, false));
        }
    }

    // =====================================================
    // FRONTIERA PRAG 90: TRECERE INTRE NOTA B SI A
    // Include si cazul special A+ cand extraCredit = true.
    // =====================================================

    /**
     * Testeaza frontiera pragului 90 care separa nota B de nota A.
     * La acest prag exista si conditia speciala: daca extraCredit=true si
     * total >= 90, nota devine A+ in loc de A.
     */
    @Nested
    @DisplayName("Frontiera prag 90 (A vs B)")
    class FrontieraPrag90 {

        @Test
        @DisplayName("total = 89 → B (sub prag)")
        void total89() {
            // OFF-POINT INFERIOR: total=89, sub pragul 90 => nota B
            assertEquals("B", Calculator.calculateGrade(89, 0, false));
        }

        @Test
        @DisplayName("total = 90 → A (pe prag, fara extraCredit)")
        void total90() {
            // ON-POINT: total=90, exact pe pragul 90, fara extraCredit => nota A
            assertEquals("A", Calculator.calculateGrade(90, 0, false));
        }

        @Test
        @DisplayName("total = 91 → A (deasupra prag, fara extraCredit)")
        void total91() {
            // OFF-POINT SUPERIOR: total=91, confirma nota A fara extra
            assertEquals("A", Calculator.calculateGrade(91, 0, false));
        }

        @Test
        @DisplayName("total = 90 cu extraCredit → A+ (pe prag, cu extraCredit)")
        void total90CuExtraCredit() {
            // ON-POINT cu extraCredit: score=85, extra=true => total=85+5=90
            // Totalul este exact pe prag 90 si extraCredit=true => nota A+ (caz special)
            assertEquals("A+", Calculator.calculateGrade(85, 0, true));
        }
    }

    // =====================================================
    // FRONTIERA PLAFONARE TOTAL LA 105
    // Daca totalul depaseste 105, se limiteaza automat la 105.
    // Testam: total=104, total=105, total>105.
    // =====================================================

    /**
     * Testeaza frontiera plafonarii totalului la valoarea 105.
     * Aceasta frontiera previne ca bonusuri foarte mari sa produca
     * un total nerealist (de ex. 200).
     */
    @Nested
    @DisplayName("Frontiera limitarii total la 105")
    class FrontieraLimitareTotal {

        @Test
        @DisplayName("total = 104 → A (sub limita de cap)")
        void total104() {
            // OFF-POINT INFERIOR: total=100+4=104, sub plafonul 105
            // Totalul ramane neschimbat => nota A
            assertEquals("A", Calculator.calculateGrade(100, 4, false));
        }

        @Test
        @DisplayName("total = 105 → A (pe limita de cap)")
        void total105() {
            // ON-POINT: total=100+5=105, exact pe plafon
            // Conditia total > 105 este FALSE, deci totalul ramane 105 => nota A
            assertEquals("A", Calculator.calculateGrade(100, 5, false));
        }

        @Test
        @DisplayName("total ar fi 110 dar se limiteaza la 105 → A")
        void totalCapAtLa105() {
            // OFF-POINT SUPERIOR: total=100+10=110, depaseste plafonul
            // Totalul este limitat la 105, dar nota ramane A (105 >= 90)
            assertEquals("A", Calculator.calculateGrade(100, 10, false));
        }

        @Test
        @DisplayName("total ar fi 125 cu extraCredit, se limiteaza la 105 → A+")
        void totalCapAtCuExtraCredit() {
            // COMBINATIE: total=100+20+5=125, plafonat la 105
            // 105 >= 90 si extraCredit=true => nota A+
            assertEquals("A+", Calculator.calculateGrade(100, 20, true));
        }
    }
}
