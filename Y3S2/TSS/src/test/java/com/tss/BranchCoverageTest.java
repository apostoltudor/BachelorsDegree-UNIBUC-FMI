package com.tss;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;


@DisplayName("Testare Structurala: Acoperire la Nivel de Decizie/Ramura (Branch Coverage)")
public class BranchCoverageTest {

    // =====================================================
    // D1: VALIDARE SCORE — if (score < 0 || score > 100)
    // Trebuie sa testam ambele ramuri: exceptie si executie normala.
    // =====================================================

    /**
     * Testeaza ambele ramuri ale deciziei D1 (validare score).
     * D1 TRUE: score invalid => se arunca exceptie
     * D1 FALSE: score valid => se continua executia normal
     */
    @Nested
    @DisplayName("D1: Validare score")
    class D1_ValidareScore {

        @Test
        @DisplayName("D1 TRUE: score = -1 → exceptie")
        void d1True() {
            // D1 TRUE: score=-1 face conditia (score < 0) TRUE
            // Se intra pe ramura TRUE a deciziei si se arunca exceptie
            assertThrows(IllegalArgumentException.class, () ->
                Calculator.calculateGrade(-1, 0, false));
        }

        @Test
        @DisplayName("D1 FALSE: score = 50 → executie normala (F)")
        void d1False() {
            // D1 FALSE: score=50 face ambele conditii FALSE
            // (50 < 0 este FALSE si 50 > 100 este FALSE)
            // Se intra pe ramura FALSE si se continua executia
            assertEquals("F", Calculator.calculateGrade(50, 0, false));
        }
    }

    // =====================================================
    // D2: EXTRA CREDIT — if (extraCredit)
    // Trebuie sa testam: extraCredit=true si extraCredit=false
    // =====================================================

    /**
     * Testeaza ambele ramuri ale deciziei D2 (extra credit).
     * Folosim aceleasi valori pentru score si bonus, schimband doar extraCredit,
     * pentru a izola efectul acestui parametru asupra totalului.
     */
    @Nested
    @DisplayName("D2: Extra credit")
    class D2_ExtraCredit {

        @Test
        @DisplayName("D2 TRUE: extraCredit = true → total include +5")
        void d2True() {
            // D2 TRUE: extraCredit=true => total = 65 + 0 + 5 = 70 => nota C
            // Se demonstreaza ca ramura TRUE adauga +5 la total
            assertEquals("C", Calculator.calculateGrade(65, 0, true));
        }

        @Test
        @DisplayName("D2 FALSE: extraCredit = false → total fara +5")
        void d2False() {
            // D2 FALSE: extraCredit=false => total = 65 + 0 = 65 => nota D
            // Aceeasi valoare de score, dar fara extra => nota diferita!
            // Aceasta diferenta (C vs D) demonstreaza ca ambele ramuri sunt testate
            assertEquals("D", Calculator.calculateGrade(65, 0, false));
        }
    }

    // =====================================================
    // D3: LIMITARE TOTAL — if (total > 105)
    // Trebuie sa testam: total care depaseste 105 si total normal.
    // =====================================================

    /**
     * Testeaza ambele ramuri ale deciziei D3 (plafonare la 105).
     */
    @Nested
    @DisplayName("D3: Limitarea totalului la 105")
    class D3_LimitareTotal {

        @Test
        @DisplayName("D3 TRUE: total = 120 → se limiteaza la 105")
        void d3True() {
            // D3 TRUE: total = 100+20 = 120, conditia (120 > 105) este TRUE
            // Totalul se limiteaza la 105 => nota A
            assertEquals("A", Calculator.calculateGrade(100, 20, false));
        }

        @Test
        @DisplayName("D3 FALSE: total = 75 → ramane 75")
        void d3False() {
            // D3 FALSE: total = 75, conditia (75 > 105) este FALSE
            // Totalul ramane neschimbat => nota C
            assertEquals("C", Calculator.calculateGrade(75, 0, false));
        }
    }

    // =====================================================
    // D4: BUCLA FOR — conditia i < thresholds.length
    // TRUE = se intra/continua in bucla, FALSE = se iese din bucla.
    // =====================================================

    /**
     * Testeaza ambele ramuri ale conditiei buclei D4.
     * D4 TRUE: gasim o nota in bucla (bucla se executa partial)
     * D4 FALSE: parcurgem toata bucla fara match (bucla se epuizeaza, se returneaza F)
     */
    @Nested
    @DisplayName("D4: Bucla for (intrare si iesire)")
    class D4_BuclaFor {

        @Test
        @DisplayName("D4 TRUE: se intra in bucla si se gaseste nota A")
        void d4TrueGaseste() {
            // D4 TRUE: bucla se executa si la prima iteratie gaseste potrivire
            // total=95 >= 90 (prag 90) => return "A"
            assertEquals("A", Calculator.calculateGrade(95, 0, false));
        }

        @Test
        @DisplayName("D4 FALSE: se parcurge toata bucla fara match → F")
        void d4FalseEpuizare() {
            // D4 FALSE: total=30, sub toate pragurile (90, 80, 70, 60)
            // Bucla se parcurge complet, la final i=4 >= 4 (length) => D4 devine FALSE
            // Se returneaza "F" dupa bucla
            assertEquals("F", Calculator.calculateGrade(30, 0, false));
        }
    }

    // =====================================================
    // D5: VERIFICARE PRAG — if (total >= thresholds[i])
    // TRUE = totalul depaseste pragul curent, FALSE = nu il atinge.
    // =====================================================

    /**
     * Testeaza ambele ramuri ale deciziei D5 (comparare cu pragul).
     * D5 TRUE: totalul >= pragul curent => se returneaza nota
     * D5 FALSE: totalul < pragul curent => se trece la urmatoarea iteratie
     *
     * Nota: la score=85, D5 este FALSE la i=0 (85 < 90) si TRUE la i=1 (85 >= 80),
     * demonstrand ambele ramuri in aceeasi executie.
     */
    @Nested
    @DisplayName("D5: Verificare prag in bucla")
    class D5_VerificarePrag {

        @Test
        @DisplayName("D5 TRUE: total = 85 >= 80 → B")
        void d5True() {
            // D5 TRUE: la iteratia i=1, total=85 >= thresholds[1]=80 => return "B"
            assertEquals("B", Calculator.calculateGrade(85, 0, false));
        }

        @Test
        @DisplayName("D5 FALSE: total = 85 < 90, se trece la urmatorul prag")
        void d5False() {
            // D5 FALSE: la iteratia i=0, total=85 < thresholds[0]=90 => se continua bucla
            // Acest test demonstreaza ca D5 poate fi FALSE (totalul nu atinge pragul)
            assertEquals("B", Calculator.calculateGrade(85, 0, false));
        }
    }

    // =====================================================
    // D6: CONDITIA A+ — if (thresholds[i] == 90 && extraCredit)
    // TRUE = nota A+, FALSE = nota normala din array.
    // =====================================================

    /**
     * Testeaza ambele ramuri ale deciziei D6 (conditia compusa pentru A+).
     * D6 TRUE: pragul este 90 SI extraCredit este true => return "A+"
     * D6 FALSE: pragul este 90 DAR extraCredit este false => return "A"
     *
     * Nota: la branch coverage testam doar decizia globala (TRUE/FALSE),
     * nu conditiile individuale. Pentru acelea se foloseste MC/DC (ConditionCoverageTest).
     */
    @Nested
    @DisplayName("D6: Conditia A+ (compusa)")
    class D6_ConditiaAPlus {

        @Test
        @DisplayName("D6 TRUE: total >= 90 si extraCredit = true → A+")
        void d6True() {
            // D6 TRUE: prag=90 (i=0) si extraCredit=true => ambele conditii sunt TRUE
            // Conditia compusa AND este TRUE => return "A+"
            assertEquals("A+", Calculator.calculateGrade(90, 0, true));
        }

        @Test
        @DisplayName("D6 FALSE: total >= 90 dar extraCredit = false → A")
        void d6False() {
            // D6 FALSE: prag=90 (i=0) dar extraCredit=false
            // Conditia compusa AND este FALSE (una din conditii e false)
            // Se returneaza grades[0] = "A" in loc de "A+"
            assertEquals("A", Calculator.calculateGrade(95, 0, false));
        }
    }
}
