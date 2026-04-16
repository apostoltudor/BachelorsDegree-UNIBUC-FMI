package com.tss;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/**
 * Teste suplimentare pentru omorarea mutantilor — Mutation Testing cu PIT.
 *
 * =========================================================================
 * CONTEXT
 * =========================================================================
 * Dupa rularea PIT cu operatorii DEFAULTS + INLINE_CONSTS + REMOVE_INCREMENTS
 * (FARA aceasta clasa de teste), au fost generati 39 de mutanti.
 * Din acestia, 33 au fost omorati de suitele:
 *   - EquivalencePartitioningTest
 *   - BoundaryValueTest
 *   - StatementCoverageTest
 *   - BranchCoverageTest
 *   - ConditionCoverageTest
 *   - IndependentCircuitsTest
 *
 * Au supravietuit 6 mutanti (Mutation Score = 33/39 = 85%):
 *
 * =========================================================================
 * MUTANTII SUPRAVIETUITORI (inainte de aceasta clasa)
 * =========================================================================
 *
 * 1. Linia 52: ConditionalsBoundaryMutator — "total > 105" → "total >= 105"
 *    ANALIZA: MUTANT ECHIVALENT
 *    Daca total == 105, atunci "total >= 105" ar fi true, si total ar fi setat
 *    la 105 (identic cu valoarea sa actuala). Rezultatul este identic.
 *    Nu poate fi omorat — il documentam ca echivalent.
 *
 * 2. Linia 46: InlineConstantMutator — "+5" → "+6" (extraCredit bonus)
 *    ANALIZA: MUTANT NEECHIVALENT
 *    Daca extraCredit=true si score+bonus+5 vs score+bonus+6 duc la
 *    note diferite, il putem omori.
 *    TEST: score=85, bonus=0, extra=true → total ar fi 90 (normal) vs 91 (mutant)
 *    Ambii dau A/A+, dar daca score=55, bonus=0, extra=true:
 *    Normal: 55+0+5=60 → D | Mutant: 55+0+6=61 → D (la fel!)
 *    Mai bine: score=65, bonus=0, extra=true: Normal: 70→C | Mutant: 71→C (la fel!)
 *    Solutie: score=85, bonus=0, extra=true: Normal: 90→A+ | Mutant: 91→A+
 *    Trebuie un caz unde ±1 schimba nota:
 *    score=64, bonus=0, extra=true: Normal: 69→D | Mutant: 70→C ← DIFERIT!
 *
 * 3. Linia 52: InlineConstantMutator — "105" → "106" (conditia if)
 *    ANALIZA: MUTANT NEECHIVALENT
 *    Daca total == 106, programul normal il limiteaza la 105, dar mutantul
 *    il lasa la 106 (106 > 106 e false). Totusi, 106 si 105 dau ambii A.
 *    De fapt e cvasiechivalent deoarece orice total > 100 da nota A.
 *    DOCUMENTAT CA ECHIVALENT in practica.
 *
 * 4. Linia 53: InlineConstantMutator — "105" → "106" (atribuirea total=105)
 *    ANALIZA: MUTANT NEECHIVALENT (cuplat cu #3)
 *    Daca total>105 si se seteaza total=106 in loc de 105, nota ramane A.
 *    Echivalent in practica, deoarece 106>=90 → A, la fel ca 105>=90 → A.
 *    DOCUMENTAT CA ECHIVALENT in practica.
 *
 * 5. Linia 57: InlineConstantMutator — "4" → "5" (numarul de elemente in array)
 *    ANALIZA: MUTANT NEECHIVALENT
 *    Daca numarul de praguri devine 5, bucla ar accesa thresholds[4] care
 *    nu exista → ArrayIndexOutOfBoundsException.
 *    De fapt, PIT muta constanta compilata "4" (nr de elemente) in bytecode.
 *    Dar arrayul are doar 4 elemente, deci for-ul cu length=5 ar crapa.
 *    Totusi, length este proprietatea arrayului, nu constanta. PIT muta
 *    o constanta interna. Trebuie verificat.
 *    TEST: Orice apel valid ar genera crash daca mutantul e activ → se omoara.
 *
 * 6. Linia 52: RemoveConditionalMutator_ORDER_ELSE — eliminarea conditiei
 *    ANALIZA: MUTANT NEECHIVALENT
 *    Daca se elimina if(total>105), totalul nu e limitat niciodata.
 *    Cu total=120, programul normal returneaza A (105>=90), mutantul
 *    returneaza A (120>=90) — la fel!
 *    Echivalent practic, deoarece orice total>105 tot >= 90 → A.
 *    DOCUMENTAT CA ECHIVALENT.
 *
 * =========================================================================
 * STRATEGIE DE OMORARE
 * =========================================================================
 * Mutantul #2 (linia 46: +5→+6) este NEECHIVALENT si poate fi omorat
 * cu un test precis la frontiera.
 *
 * Mutantul #5 (linia 57: 4→5) este NEECHIVALENT — ar cauza o eroare la
 * runtime.
 *
 * Restul mutantilor sunt echivalenti sau cvasi-echivalenti in practica.
 * =========================================================================
 */
@DisplayName("Mutation Testing: Teste suplimentare pentru omorarea mutantilor")
public class MutationKillerTest {

    // =========================================================================
    // MUTANT NEECHIVALENT #2: Linia 46 — "+5" → "+6"
    // Operator: InlineConstantMutator (Substituted 5 with 6)
    // =========================================================================
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
            // Normal:  total = 74 + 0 + 5 = 79 → C
            // Mutant:  total = 74 + 0 + 6 = 80 → B (DIFERIT!)
            assertEquals("C", Calculator.calculateGrade(74, 0, true));
        }

        @Test
        @DisplayName("score=84, bonus=0, extra=true → B (nu A cum ar da mutantul +6)")
        void killMutant2_precizieExtraCreditLaPrag90() {
            // Normal:  total = 84 + 0 + 5 = 89 → B
            // Mutant:  total = 84 + 0 + 6 = 90 → A+ (DIFERIT!)
            assertEquals("B", Calculator.calculateGrade(84, 0, true));
        }
    }

    // =========================================================================
    // MUTANT NEECHIVALENT #5: Linia 57 — "4" → "5" (lungimea array compilata)
    // Operator: InlineConstantMutator (Substituted 4 with 5)
    // =========================================================================
    @Nested
    @DisplayName("Kill Mutant #5: Constanta lungime array (linia 57)")
    class KillMutant5_LungimeArray {

        @Test
        @DisplayName("score=50, bonus=0, extra=false → F (mutantul ar crapa cu ArrayIndexOutOfBounds)")
        void killMutant5_totalSubToatePragurile() {
            // Daca mutantul schimba bucla for sa itereze de 5 ori,
            // la iteratia i=4 ar accesa thresholds[4] → crash
            // Testul nostru verifica ca returneaza "F" fara erori
            assertEquals("F", Calculator.calculateGrade(50, 0, false));
        }

        @Test
        @DisplayName("score=30, bonus=0, extra=false → F (verifica ca bucla se termina corect)")
        void killMutant5_buclaSeFinalizeaza() {
            assertEquals("F", Calculator.calculateGrade(30, 0, false));
        }
    }

    // =========================================================================
    // DOCUMENTAREA MUTANTILOR ECHIVALENTI
    // =========================================================================
    @Nested
    @DisplayName("Documentare mutanti echivalenti (teste demonstrative)")
    class MutantiEchivalenti {

        @Test
        @DisplayName("Mutant echiv. #1: total>105 vs total>=105 — total=105 nu e afectat")
        void mutantEchivalent1_conditionalBoundary() {
            // Mutant: if (total >= 105) total = 105
            // Original: if (total > 105) total = 105
            // Cand total=105: mutantul seteaza total=105 (nicio schimbare)
            // Rezultat identic in ambele cazuri
            assertEquals("A", Calculator.calculateGrade(100, 5, false)); // total=105
        }

        @Test
        @DisplayName("Mutant echiv. #3/#4: 105→106 — nu schimba nota (106>=90 → A)")
        void mutantEchivalent3_4_inlineConst106() {
            // Mutant: total se seteaza la 106 in loc de 105
            // Dar 106 >= 90 → A (identic cu 105 >= 90 → A)
            assertEquals("A", Calculator.calculateGrade(100, 20, false)); // total=120
        }

        @Test
        @DisplayName("Mutant echiv. #6: if eliminat — totalul nelimitat tot da A")
        void mutantEchivalent6_removeConditional() {
            // Mutant: if(total>105) eliminat, total ramane 120
            // Dar 120 >= 90 → A (identic cu 105 >= 90 → A)
            assertEquals("A", Calculator.calculateGrade(100, 20, false));
        }
    }

    // =========================================================================
    // Teste de precizie suplimentare (omoara mutanti subtili)
    // =========================================================================
    @Nested
    @DisplayName("Teste de precizie suplimentare")
    class TestePrecizie {

        @Test
        @DisplayName("Precizie: toate notele in ordine crescatoare a totalului")
        void precizieToateNotele() {
            assertEquals("F", Calculator.calculateGrade(50, 0, false));  // total=50
            assertEquals("D", Calculator.calculateGrade(60, 0, false));  // total=60
            assertEquals("C", Calculator.calculateGrade(70, 0, false));  // total=70
            assertEquals("B", Calculator.calculateGrade(80, 0, false));  // total=80
            assertEquals("A", Calculator.calculateGrade(90, 0, false));  // total=90
            assertEquals("A+", Calculator.calculateGrade(90, 0, true)); // total=95
        }

        @Test
        @DisplayName("Precizie: bonus schimba categoria notei")
        void precizieBonusSchimbaCategoria() {
            assertEquals("F", Calculator.calculateGrade(58, 0, false));  // total=58
            assertEquals("D", Calculator.calculateGrade(58, 2, false));  // total=60
            assertEquals("C", Calculator.calculateGrade(58, 12, false)); // total=70
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
