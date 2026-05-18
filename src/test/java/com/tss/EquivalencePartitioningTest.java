package com.tss;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;


@DisplayName("Testare Functionala: Partitionare in Clase de Echivalenta")
public class EquivalencePartitioningTest {

    // =====================================================
    // CLASE GLOBALE CG1-CG2: Score negativ (clasa individuala S1)
    // Combinat cu diferite clase ale celorlalti parametri
    // pentru a verifica ca exceptia se arunca indiferent de bonus/extra.
    // =====================================================

    /**
     * Clase globale cu score negativ (S1).
     * Testam ca exceptia se produce indiferent de valorile celorlalti parametri.
     * CG1: (S1, B1, E1) si CG2: (S1, B2, E2)
     */
    @Nested
    @DisplayName("Clase globale CG1-CG2: Score negativ (S1, invalid)")
    class ScoreNegativ {

        @Test
        @DisplayName("CG1: (S1, B1, E1) → score=-5, bonus=0, extra=false → exceptie")
        void cg1_scoreNegativ_bonus0_extraFalse() {
            // Clasa globala CG1: combinam S1 (score<0) cu B1 (bonus=0) si E1 (extra=false)
            // Rezultat: exceptie, deoarece score=-5 violeaza domeniul valid [0,100]
            assertThrows(IllegalArgumentException.class, () ->
                Calculator.calculateGrade(-5, 0, false));
        }

        @Test
        @DisplayName("CG2: (S1, B2, E2) → score=-100, bonus=10, extra=true → exceptie")
        void cg2_scoreNegativ_bonusPositiv_extraTrue() {
            // Clasa globala CG2: combinam S1 cu B2 (bonus>0) si E2 (extra=true)
            // Chiar daca bonus si extraCredit sunt nenule, validarea score se face prima
            // Demonstram ca exceptia este independenta de ceilalti parametri
            assertThrows(IllegalArgumentException.class, () ->
                Calculator.calculateGrade(-100, 10, true));
        }
    }

    // =====================================================
    // CLASE GLOBALE CG3-CG4: Score peste 100 (clasa individuala S7)
    // =====================================================

    /**
     * Clase globale cu score peste 100 (S7).
     * CG3: (S7, B1, E1) si CG4: (S7, B2, E2)
     */
    @Nested
    @DisplayName("Clase globale CG3-CG4: Score peste 100 (S7, invalid)")
    class ScorePeste100 {

        @Test
        @DisplayName("CG3: (S7, B1, E1) → score=101, bonus=0, extra=false → exceptie")
        void cg3_scorePeste100_bonus0_extraFalse() {
            // Clasa globala CG3: S7 (score>100) cu B1 si E1
            // score=101 depaseste limita superioara => exceptie
            assertThrows(IllegalArgumentException.class, () ->
                Calculator.calculateGrade(101, 0, false));
        }

        @Test
        @DisplayName("CG4: (S7, B2, E2) → score=200, bonus=5, extra=true → exceptie")
        void cg4_scorePeste100_bonusPositiv_extraTrue() {
            // Clasa globala CG4: S7 cu B2 si E2
            // Demonstram ca exceptia se arunca si cu bonus si extra active
            assertThrows(IllegalArgumentException.class, () ->
                Calculator.calculateGrade(200, 5, true));
        }
    }

    // =====================================================
    // CLASE GLOBALE CG5-CG9: Score valid, bonus=0, extra=false
    // Izoleaza efectul parametrului score (clase individuale S2-S6)
    // prin fixarea celorlalti parametri la valorile neutre (B1, E1).
    // =====================================================

    /**
     * CG5: (S2, B1, E1) — score in [0,59], bonus=0, extra=false → nota F.
     * Reprezentant: score=30 (valoare din mijlocul intervalului S2).
     */
    @Test
    @DisplayName("CG5: (S2, B1, E1) → score=30, bonus=0, extra=false → F")
    void cg5_scoreZonaF() {
        // Clasa globala CG5: izolam parametrul score in zona F
        // total = 30 + 0 = 30, sub pragul 60 => nota F
        assertEquals("F", Calculator.calculateGrade(30, 0, false));
    }

    /**
     * CG6: (S3, B1, E1) — score in [60,69], bonus=0, extra=false → nota D.
     * Reprezentant: score=65.
     */
    @Test
    @DisplayName("CG6: (S3, B1, E1) → score=65, bonus=0, extra=false → D")
    void cg6_scoreZonaD() {
        // Clasa globala CG6: izolam parametrul score in zona D
        // total = 65, in intervalul [60,69] => nota D
        assertEquals("D", Calculator.calculateGrade(65, 0, false));
    }

    /**
     * CG7: (S4, B1, E1) — score in [70,79], bonus=0, extra=false → nota C.
     * Reprezentant: score=75.
     */
    @Test
    @DisplayName("CG7: (S4, B1, E1) → score=75, bonus=0, extra=false → C")
    void cg7_scoreZonaC() {
        // Clasa globala CG7: izolam parametrul score in zona C
        // total = 75, in intervalul [70,79] => nota C
        assertEquals("C", Calculator.calculateGrade(75, 0, false));
    }

    /**
     * CG8: (S5, B1, E1) — score in [80,89], bonus=0, extra=false → nota B.
     * Reprezentant: score=85.
     */
    @Test
    @DisplayName("CG8: (S5, B1, E1) → score=85, bonus=0, extra=false → B")
    void cg8_scoreZonaB() {
        // Clasa globala CG8: izolam parametrul score in zona B
        // total = 85, in intervalul [80,89] => nota B
        assertEquals("B", Calculator.calculateGrade(85, 0, false));
    }

    /**
     * CG9: (S6, B1, E1) — score in [90,100], bonus=0, extra=false → nota A.
     * Reprezentant: score=95.
     */
    @Test
    @DisplayName("CG9: (S6, B1, E1) → score=95, bonus=0, extra=false → A")
    void cg9_scoreZonaA() {
        // Clasa globala CG9: izolam parametrul score in zona A
        // total = 95, peste pragul 90 => nota A
        assertEquals("A", Calculator.calculateGrade(95, 0, false));
    }

    // =====================================================
    // CLASE GLOBALE CG10-CG11: Efectul parametrului bonus
    // Fixam score in zona F si extra=false, variem doar bonus.
    // Demonstram ca bonusul poate schimba clasa globala de output.
    // =====================================================

    /**
     * CG10: (S2, B1, E1) — bonus=0 nu modifica totalul.
     * Totalul ramane egal cu score => nota nu se schimba.
     */
    @Test
    @DisplayName("CG10: (S2, B1, E1) → score=50, bonus=0, extra=false → F (bonus nu schimba)")
    void cg10_bonusZero() {
        // Clasa globala CG10: bonus=0 (clasa individuala B1)
        // total = 50 + 0 = 50 => nota F
        assertEquals("F", Calculator.calculateGrade(50, 0, false));
    }

    /**
     * CG11: (S2, B2, E1) — bonus>0 ridica totalul suficient sa schimbe nota.
     * score=58 cu bonus=5 => total=63 trece de pragul 60 => nota D in loc de F.
     * Aceasta demonstreaza INTERACTIUNEA dintre parametrii score si bonus.
     */
    @Test
    @DisplayName("CG11: (S2, B2, E1) → score=58, bonus=5, extra=false → D (bonus ridica F→D)")
    void cg11_bonusSchimbaCategoria() {
        // Clasa globala CG11: bonus=5 (clasa individuala B2)
        // total = 58 + 5 = 63 >= 60 => nota D (fara bonus ar fi fost F!)
        assertEquals("D", Calculator.calculateGrade(58, 5, false));
    }

    // =====================================================
    // CLASE GLOBALE CG12-CG14: Efectul parametrului extraCredit
    // Demonstram influenta flagului boolean asupra totalului
    // si a notei speciale A+.
    // =====================================================

    /**
     * CG12: (S4, B1, E1) — extraCredit=false, nota ramane C.
     * Aceasta este clasa de referinta pentru comparatie cu CG13.
     */
    @Test
    @DisplayName("CG12: (S4, B1, E1) → score=70, bonus=0, extra=false → C")
    void cg12_extraCreditFalse() {
        // Clasa globala CG12: extra=false (clasa individuala E1)
        // total = 70 + 0 = 70 => nota C
        assertEquals("C", Calculator.calculateGrade(70, 0, false));
    }

    /**
     * CG13: (S3, B1, E2) — extraCredit=true adauga +5 si schimba nota.
     * score=65 fara extra => total=65 => D (CG6)
     * score=65 cu extra  => total=70 => C (CG13)
     * Diferenta C vs D demonstreaza efectul parametrului extraCredit.
     */
    @Test
    @DisplayName("CG13: (S3, B1, E2) → score=65, bonus=0, extra=true → C (65+5=70)")
    void cg13_extraCreditTrue() {
        // Clasa globala CG13: extra=true (clasa individuala E2)
        // total = 65 + 0 + 5 = 70 >= 70 => nota C (cu extra, se ridica de la D la C)
        assertEquals("C", Calculator.calculateGrade(65, 0, true));
    }

    /**
     * CG14: (S5, B1, E2) — extraCredit=true cu total >= 90 produce nota A+.
     * Aceasta este singura clasa globala care produce nota speciala A+.
     * score=88, extra=true => total = 88+5 = 93 >= 90 si extraCredit=true => A+
     */
    @Test
    @DisplayName("CG14: (S5, B1, E2) → score=88, bonus=0, extra=true → A+ (88+5=93)")
    void cg14_extraCreditCuAPlus() {
        // Clasa globala CG14: combinatia care produce nota speciala A+
        // total = 88 + 5 = 93, pragul 90 atins si extraCredit=true => A+
        assertEquals("A+", Calculator.calculateGrade(88, 0, true));
    }
}
