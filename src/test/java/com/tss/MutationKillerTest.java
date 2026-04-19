package com.tss;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

// teste aditionale impuse pit test 
@DisplayName("Mutation Testing: Teste suplimentare pentru omorarea mutantilor")
public class MutationKillerTest {

    // omoram mutanti gasiti manual
    @Nested
    @DisplayName("Kill Mutant #2: Constanta +5 extraCredit (linia 46)")
    class KillMutant2_ExtraCredit5 {

        @Test
        @DisplayName("score=64, bonus=0, extra=true → D (nu C cum ar da mutantul +6)")
        void killMutant2_precizieExtraCreditLaPrag70() {
            // Normal:  total = 64 + 0 + 5 = 69 → D
            // Mutant:  total = 64 + 0 + 6 = 70 → C (DIFERIT!)
            // Acest test omoara mutantul deoarece D != C
            assertEquals("D", Calculator.calculateGrade(64, 0, true));
        }

        @Test
        @DisplayName("score=74, bonus=0, extra=true → C (nu B cum ar da mutantul +6)")
        void killMutant2_precizieExtraCreditLaPrag80() {
            assertEquals("C", Calculator.calculateGrade(74, 0, true));
        }

        @Test
        @DisplayName("score=84, bonus=0, extra=true → B (nu A cum ar da mutantul +6)")
        void killMutant2_precizieExtraCreditLaPrag90() {
            assertEquals("B", Calculator.calculateGrade(84, 0, true));
        }
    }

    // validare array constant break point
    @Nested
    @DisplayName("Kill Mutant #5: Constanta lungime array (linia 57)")
    class KillMutant5_LungimeArray {

        @Test
        @DisplayName("score=50, bonus=0, extra=false → F (mutantul ar crapa cu ArrayIndexOutOfBounds)")
        void killMutant5_totalSubToatePragurile() {
            assertEquals("F", Calculator.calculateGrade(50, 0, false));
        }

        @Test
        @DisplayName("score=30, bonus=0, extra=false → F (verifica ca bucla se termina corect)")
        void killMutant5_buclaSeFinalizeaza() {
            assertEquals("F", Calculator.calculateGrade(30, 0, false));
        }
    }

    // listare erori de test echivalente
    @Nested
    @DisplayName("Documentare mutanti echivalenti (teste demonstrative)")
    class MutantiEchivalenti {

        @Test
        @DisplayName("Mutant echiv. #1: total>105 vs total>=105 — total=105 nu e afectat")
        void mutantEchivalent1_conditionalBoundary() {
            assertEquals("A", Calculator.calculateGrade(100, 5, false));
        }

        @Test
        @DisplayName("Mutant echiv. #3/#4: 105→106 — nu schimba nota (106>=90 → A)")
        void mutantEchivalent3_4_inlineConst106() {
            assertEquals("A", Calculator.calculateGrade(100, 20, false));
        }

        @Test
        @DisplayName("Mutant echiv. #6: if eliminat — totalul nelimitat tot da A")
        void mutantEchivalent6_removeConditional() {
            assertEquals("A", Calculator.calculateGrade(100, 20, false));
        }
    }

    // teste extra
    @Nested
    @DisplayName("Teste de precizie suplimentare")
    class TestePrecizie {

        @Test
        @DisplayName("Precizie: toate notele in ordine crescatoare a totalului")
        void precizieToateNotele() {
            assertEquals("F", Calculator.calculateGrade(50, 0, false));
            assertEquals("D", Calculator.calculateGrade(60, 0, false));
            assertEquals("C", Calculator.calculateGrade(70, 0, false));
            assertEquals("B", Calculator.calculateGrade(80, 0, false));
            assertEquals("A", Calculator.calculateGrade(90, 0, false));
            assertEquals("A+", Calculator.calculateGrade(90, 0, true));
        }

        @Test
        @DisplayName("Precizie: bonus schimba categoria notei")
        void precizieBonusSchimbaCategoria() {
            assertEquals("F", Calculator.calculateGrade(58, 0, false));
            assertEquals("D", Calculator.calculateGrade(58, 2, false));
            assertEquals("C", Calculator.calculateGrade(58, 12, false));
        }

        @Test
        @DisplayName("Precizie: score=0 este valid si returneaza F")
        void score0Valid() {
            assertDoesNotThrow(() -> Calculator.calculateGrade(0, 0, false));
            assertEquals("F", Calculator.calculateGrade(0, 0, false));
        }

        @Test
        @DisplayName("Precizie: score=100 este valid si returneaza A")
        void score100Valid() {
            assertDoesNotThrow(() -> Calculator.calculateGrade(100, 0, false));
            assertEquals("A", Calculator.calculateGrade(100, 0, false));
        }
    }
}
