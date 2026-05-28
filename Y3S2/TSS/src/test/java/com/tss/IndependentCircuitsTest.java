package com.tss;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;


@DisplayName("Testare Structurala: Circuite Independente (McCabe V(G) = 5)")
public class IndependentCircuitsTest {

    /**
     * CIRCUIT 1 — Calea de baza (cel mai lung drum fara ramificatii speciale).
     *
     * Parcurs: N1 → N2(FALSE) → N4(FALSE) → N6(FALSE) → N8 → N9 → N10(FALSE) →
     *          N9 → N10(FALSE) → N9 → N10(FALSE) → N9 → N10(FALSE) → N9(FALSE) → N14
     *
     * Toate deciziile iau valoarea FALSE (score valid, fara extra, fara plafonare,
     * totalul sub toate pragurile). Bucla se parcurge complet fara match.
     * Se returneaza nota "F".
     *
     * Acest circuit este fundamentul: celelalte 4 circuite sunt deviatii de la aceasta cale.
     */
    @Test
    @DisplayName("Circuit 1: Calea de baza — extraCredit=false, total<60 → F")
    void circuit1_caleaDeBaza() {
        // N1 → N2(F) → N4(F) → N6(F) → N8 → N9 → [bucla epuizata] → N14
        // score=30, bonus=0, extra=false → total=30 → sub toate pragurile → F
        assertEquals("F", Calculator.calculateGrade(30, 0, false));
    }

    /**
     * CIRCUIT 2 — Deviatie: se ia ramura TRUE la D1 (exceptie).
     *
     * Parcurs: N1 → N2(TRUE) → N3 (throw exception)
     *
     * Fata de Circuitul 1, singura deviatie este ca D1 ia valoarea TRUE
     * in loc de FALSE. Executia se opreste imediat la N3.
     * Aceasta este calea cea mai scurta prin program.
     */
    @Test
    @DisplayName("Circuit 2: Deviatie exceptie — score invalid")
    void circuit2_exceptie() {
        // N1 → N2(TRUE) → N3: score=-1 face D1 TRUE => throw exception
        assertThrows(IllegalArgumentException.class, () ->
            Calculator.calculateGrade(-1, 0, false));
    }

    /**
     * CIRCUIT 3 — Deviatie: se ia ramura TRUE la D2 (extraCredit activ).
     *
     * Parcurs: N1 → N2(FALSE) → N4(TRUE) → N5 → N6(FALSE) → N8 →
     *          N9 → N10(TRUE) → N11(FALSE) → N13 (return "B")
     *
     * Fata de Circuitul 1, deviatia este ca D2 ia valoarea TRUE (extra=true),
     * ceea ce modifica totalul cu +5 si face ca bucla sa gaseasca un prag.
     */
    @Test
    @DisplayName("Circuit 3: Deviatie extraCredit=true, nota B")
    void circuit3_extraCreditTrue() {
        // score=80, bonus=0, extra=true => total=80+5=85
        // Bucla: 85<90 (FALSE la i=0), 85>=80 (TRUE la i=1) => return "B"
        assertEquals("B", Calculator.calculateGrade(80, 0, true));
    }

    /**
     * CIRCUIT 4 — Deviatie: se ia ramura TRUE la D3 (plafonare total).
     *
     * Parcurs: N1 → N2(FALSE) → N4(FALSE) → N6(TRUE) → N7 → N8 →
     *          N9 → N10(TRUE) → N11(FALSE) → N13 (return "A")
     *
     * Fata de Circuitul 1, deviatia este ca D3 ia valoarea TRUE
     * (totalul depaseste 105 si este plafonat), apoi bucla gaseste pragul 90.
     */
    @Test
    @DisplayName("Circuit 4: Deviatie total>105 capped, nota A")
    void circuit4_totalCapped() {
        // score=100, bonus=20 => total=120 > 105 => plafonat la 105
        // Bucla: 105>=90 (TRUE la i=0) => return "A"
        assertEquals("A", Calculator.calculateGrade(100, 20, false));
    }

    /**
     * CIRCUIT 5 — Deviatie: se ia ramura TRUE la D6 (nota A+).
     *
     * Parcurs: N1 → N2(FALSE) → N4(TRUE) → N5 → N6(FALSE) → N8 →
     *          N9 → N10(TRUE) → N11(TRUE) → N12 (return "A+")
     *
     * Fata de Circuitul 3, deviatia suplimentara este ca D6 ia valoarea TRUE
     * (pe langa D2 TRUE). Conditia compusa (prag==90 && extraCredit) este TRUE
     * deoarece totalul ajunge la pragul 90 si extraCredit este activ.
     */
    @Test
    @DisplayName("Circuit 5: Deviatie A+ (conditia compusa true)")
    void circuit5_aPlus() {
        // score=90, bonus=0, extra=true => total=90+5=95
        // Bucla: 95>=90 (TRUE la i=0), prag==90 si extra=true => D6 TRUE => return "A+"
        assertEquals("A+", Calculator.calculateGrade(90, 0, true));
    }
}
