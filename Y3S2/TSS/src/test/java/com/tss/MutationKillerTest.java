package com.tss;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;


@DisplayName("Mutation Testing: Teste suplimentare pentru omorarea mutantilor")
public class MutationKillerTest {

    // =====================================================
    // MUTANT #2: Constanta +5 inlocuita cu +6 (INLINE_CONSTS)
    //
    // PITest a generat un mutant care inlocuieste constanta 5 cu 6
    // in instructiunea: total = score + bonus + 5
    // Mutantul devine: total = score + bonus + 6
    //
    // Pentru a omori acest mutant, avem nevoie de un test unde
    // diferenta de 1 punct (5 vs 6) schimba nota finala.
    // Aceasta inseamna sa alegem un score care face ca totalul sa fie
    // exact pe un prag cu +5 dar sa treaca pragul cu +6.
    //
    // Exemplu: score=64, bonus=0, extra=true
    //   Program original: total = 64 + 0 + 5 = 69 → nota D (69 < 70)
    //   Mutant (+6):      total = 64 + 0 + 6 = 70 → nota C (70 >= 70)
    //   Rezultatele difera (D ≠ C) => mutantul este OMORAT!
    //
    // Conditii de omorare (conform cursului):
    //   Reachability: instructiunea total=score+bonus+5 se executa (extra=true) ✓
    //   State infection: totalul este 69 in loc de 70, stari diferite ✓
    //   State propagation: nota finala D ≠ C, diferenta se propaga la output ✓
    // =====================================================

    @Nested
    @DisplayName("Kill Mutant #2: Constanta +5 extraCredit (linia 46)")
    class KillMutant2_ExtraCredit5 {

        @Test
        @DisplayName("score=64, bonus=0, extra=true → D (nu C cum ar da mutantul +6)")
        void killMutant2_precizieExtraCreditLaPrag70() {
            // Normal:  total = 64 + 0 + 5 = 69 → D (sub pragul 70)
            // Mutant:  total = 64 + 0 + 6 = 70 → C (pe pragul 70 — DIFERIT!)
            // Acest test omoara mutantul deoarece D != C
            assertEquals("D", Calculator.calculateGrade(64, 0, true));
        }

        @Test
        @DisplayName("score=74, bonus=0, extra=true → C (nu B cum ar da mutantul +6)")
        void killMutant2_precizieExtraCreditLaPrag80() {
            // Normal:  total = 74 + 5 = 79 → C (sub pragul 80)
            // Mutant:  total = 74 + 6 = 80 → B (pe pragul 80 — DIFERIT!)
            assertEquals("C", Calculator.calculateGrade(74, 0, true));
        }

        @Test
        @DisplayName("score=84, bonus=0, extra=true → B (nu A cum ar da mutantul +6)")
        void killMutant2_precizieExtraCreditLaPrag90() {
            // Normal:  total = 84 + 5 = 89 → B (sub pragul 90)
            // Mutant:  total = 84 + 6 = 90 → A (pe pragul 90 — DIFERIT!)
            assertEquals("B", Calculator.calculateGrade(84, 0, true));
        }
    }

    // =====================================================
    // MUTANT #5: Constanta thresholds.length modificata (INLINE_CONSTS)
    //
    // PITest a generat un mutant care modifica lungimea array-ului
    // in conditia buclei for: i < thresholds.length
    // Daca lungimea devine mai mica, bucla nu parcurge toate pragurile.
    // Daca lungimea devine mai mare, se produce ArrayIndexOutOfBounds.
    //
    // Pentru a omori acest mutant, avem nevoie de teste care cer ca
    // bucla sa parcurga TOATE cele 4 iteratii (sa ajunga la pragul 60).
    // Daca mutantul reduce lungimea, bucla se opreste devreme si
    // nu gaseste pragul 60, returnand F in loc de D, sau crapa.
    // =====================================================

    @Nested
    @DisplayName("Kill Mutant #5: Constanta lungime array (linia 57)")
    class KillMutant5_LungimeArray {

        @Test
        @DisplayName("score=50, bonus=0, extra=false → F (mutantul ar crapa cu ArrayIndexOutOfBounds)")
        void killMutant5_totalSubToatePragurile() {
            // total=50 => bucla parcurge TOATE cele 4 praguri (90,80,70,60)
            // fara sa gaseasca match => returneaza F
            // Daca mutantul mareste lungimea => ar accesa thresholds[4] => ArrayIndexOutOfBounds
            assertEquals("F", Calculator.calculateGrade(50, 0, false));
        }

        @Test
        @DisplayName("score=30, bonus=0, extra=false → F (verifica ca bucla se termina corect)")
        void killMutant5_buclaSeFinalizeaza() {
            // total=30 => inca sub toate pragurile, bucla epuizata complet
            // Confirma ca bucla parcurge toate cele 4 iteratii si se termina normal
            assertEquals("F", Calculator.calculateGrade(30, 0, false));
        }
    }

    // =====================================================
    // MUTANTI ECHIVALENTI — nu pot fi omorati de niciun test
    //
    // Conform cursului: "Un mutant M se numeste echivalent daca el se
    // comporta identic cu programul P pentru ORICE date de intrare."
    //
    // "Determinarea mutantilor echivalenti poate fi un proces foarte complex –
    // principala problema practica a tehnicii mutation testing."
    //
    // In proiectul nostru, PITest a generat cativa mutanti pe care
    // nu putem sa ii omoram deoarece sunt echivalenti. Ii documentam aici
    // cu teste demonstrative care arata ca mutatia nu schimba comportamentul.
    // =====================================================

    @Nested
    @DisplayName("Documentare mutanti echivalenti (teste demonstrative)")
    class MutantiEchivalenti {

        @Test
        @DisplayName("Mutant echiv. #1: total>105 vs total>=105 — total=105 nu e afectat")
        void mutantEchivalent1_conditionalBoundary() {
            // Mutantul schimba conditia de la (total > 105) la (total >= 105)
            // Singura diferenta ar fi la total=105:
            //   Original: 105 > 105 este FALSE => total ramane 105
            //   Mutant:   105 >= 105 este TRUE => total se seteaza la 105
            // Dar total era deja 105! Deci setarea nu schimba nimic.
            // Rezultat: identic in ambele cazuri => MUTANT ECHIVALENT
            assertEquals("A", Calculator.calculateGrade(100, 5, false));
        }

        @Test
        @DisplayName("Mutant echiv. #3/#4: 105→106 — nu schimba nota (106>=90 → A)")
        void mutantEchivalent3_4_inlineConst106() {
            // Mutantul schimba plafonul de la 105 la 106
            // Original: total=120 se plafoneaza la 105 => 105 >= 90 => A
            // Mutant:   total=120 se plafoneaza la 106 => 106 >= 90 => A
            // Nota finala este identica (A) => MUTANT ECHIVALENT
            // Plafonul 105 vs 106 nu schimba nota deoarece ambele sunt peste pragul 90
            assertEquals("A", Calculator.calculateGrade(100, 20, false));
        }

        @Test
        @DisplayName("Mutant echiv. #6: if eliminat — totalul nelimitat tot da A")
        void mutantEchivalent6_removeConditional() {
            // Mutantul elimina complet conditia if (total > 105)
            // Original: total=120 se plafoneaza la 105 => A
            // Mutant:   total ramane 120 (fara plafonare) => 120 >= 90 => tot A
            // In practica, orice total > 90 produce nota A (sau A+ cu extra)
            // Deci eliminarea plafonarii nu schimba nota finala => MUTANT ECHIVALENT
            assertEquals("A", Calculator.calculateGrade(100, 20, false));
        }
    }

    // =====================================================
    // TESTE DE PRECIZIE SUPLIMENTARE
    //
    // Aceste teste ofera o acoperire suplimentara pentru a confirma
    // ca diferite combinatii ale celor 3 parametri produc rezultate corecte.
    // Ele ajuta la omorarea mutantilor care modifica operatori sau constante
    // in locuri unde alte teste nu au suficienta precizie.
    // =====================================================

    @Nested
    @DisplayName("Teste de precizie suplimentare")
    class TestePrecizie {

        @Test
        @DisplayName("Precizie: toate notele in ordine crescatoare a totalului")
        void precizieToateNotele() {
            // Parcurgem sistematic toate clasele de echivalenta ale notelor
            // cu valori care nu sunt pe frontiera, pentru a confirma stabilitatea
            assertEquals("F", Calculator.calculateGrade(50, 0, false));  // total=50 < 60
            assertEquals("D", Calculator.calculateGrade(60, 0, false));  // total=60, pe pragul D
            assertEquals("C", Calculator.calculateGrade(70, 0, false));  // total=70, pe pragul C
            assertEquals("B", Calculator.calculateGrade(80, 0, false));  // total=80, pe pragul B
            assertEquals("A", Calculator.calculateGrade(90, 0, false));  // total=90, pe pragul A
            assertEquals("A+", Calculator.calculateGrade(90, 0, true)); // total=95, A+ cu extra
        }

        @Test
        @DisplayName("Precizie: bonus schimba categoria notei")
        void precizieBonusSchimbaCategoria() {
            // Demonstram ca parametrul bonus poate muta totalul de la o clasa la alta
            assertEquals("F", Calculator.calculateGrade(58, 0, false));  // 58 => F (sub 60)
            assertEquals("D", Calculator.calculateGrade(58, 2, false));  // 58+2=60 => D
            assertEquals("C", Calculator.calculateGrade(58, 12, false)); // 58+12=70 => C
        }

        @Test
        @DisplayName("Precizie: score=0 este valid si returneaza F")
        void score0Valid() {
            // Verifica ca score=0 (limita inferioara) nu produce exceptie
            // si returneaza corect nota F (total=0 < 60)
            assertDoesNotThrow(() -> Calculator.calculateGrade(0, 0, false));
            assertEquals("F", Calculator.calculateGrade(0, 0, false));
        }

        @Test
        @DisplayName("Precizie: score=100 este valid si returneaza A")
        void score100Valid() {
            // Verifica ca score=100 (limita superioara) nu produce exceptie
            // si returneaza corect nota A (total=100 >= 90)
            assertDoesNotThrow(() -> Calculator.calculateGrade(100, 0, false));
            assertEquals("A", Calculator.calculateGrade(100, 0, false));
        }
    }
}
