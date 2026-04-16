package com.tss;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/**
 * Testare structurala — Circuite independente (Complexitate ciclomatica McCabe).
 *
 * Strategia:
 * Se construieste Graful Fluxului de Control (CFG) al metodei calculateGrade,
 * se calculeaza complexitatea ciclomatica V(G) = e - n + 2,
 * si se identifica setul de baza al circuitelor independente.
 * Se scrie cate un test pentru fiecare circuit.
 *
 * =========================================================================
 * GRAFUL FLUXULUI DE CONTROL (CFG)
 * =========================================================================
 *
 * Noduri:
 *   N1:  START / Intrare metoda
 *   N2:  if (score < 0 || score > 100)
 *   N3:  throw IllegalArgumentException           [ramura TRUE a N2]
 *   N4:  if (extraCredit)
 *   N5:  total = score + bonus + 5                 [ramura TRUE a N4]
 *   N6:  total = score + bonus                     [ramura FALSE a N4]
 *   N7:  if (total > 105)
 *   N8:  total = 105                               [ramura TRUE a N7]
 *   N9:  for (i = 0; i < thresholds.length; i++)   [conditia buclei]
 *   N10: if (total >= thresholds[i])
 *   N11: if (thresholds[i] == 90 && extraCredit)
 *   N12: return "A+"                               [ramura TRUE a N11]
 *   N13: return grades[i]                          [ramura FALSE a N11]
 *   N14: return "F"                                [iesire bucla]
 *
 * Arce (e = 17):
 *   N1→N2, N2→N3, N2→N4, N4→N5, N4→N6, N5→N7, N6→N7,
 *   N7→N8, N7→N9, N8→N9, N9→N10, N9→N14,
 *   N10→N11, N10→N9(back), N11→N12, N11→N13
 *
 * n = 14 noduri, e = 17 arce (incluzand arcul implicit N10→N9 cand
 * conditia e FALSE si se trece la urmatoarea iteratie)
 *
 * ATENTIE: Intr-un CFG real, N10→N9(back) cand total < thresholds[i],
 *          si N9→N14 cand i >= thresholds.length.
 *
 * =========================================================================
 * COMPLEXITATE CICLOMATICA
 * =========================================================================
 *
 * V(G) = e - n + 2 = 17 - 14 + 2 = 5
 *
 * Alternativ: V(G) = numar de decizii + 1 = 4 + 1 = 5
 * (Decizii: N2, N4, N7, N9/N10, N11 — dar N9 si N10 pot fi grupate)
 *
 * =========================================================================
 * SETUL DE BAZA AL CIRCUITELOR INDEPENDENTE
 * =========================================================================
 *
 * Circuit 1 (Calea de baza — cale directa cu nota F):
 *   N1 → N2 → N4(FALSE) → N6 → N7(FALSE) → N9 → N9(exit) → N14
 *   Date: score=30, bonus=0, extra=false → F
 *
 * Circuit 2 (Deviatie: exceptie la validare):
 *   N1 → N2 → N3
 *   Date: score=-1, bonus=0, extra=false → exception
 *
 * Circuit 3 (Deviatie: extraCredit = true):
 *   N1 → N2 → N4(TRUE) → N5 → N7(FALSE) → N9 → N10(TRUE) → N11(FALSE) → N13
 *   Date: score=80, bonus=0, extra=true → B (total=85)
 *
 * Circuit 4 (Deviatie: total > 105, capped):
 *   N1 → N2 → N4(FALSE) → N6 → N7(TRUE) → N8 → N9 → N10(TRUE) → N11(FALSE) → N13
 *   Date: score=100, bonus=20, extra=false → A (total=120→105)
 *
 * Circuit 5 (Deviatie: A+ - conditia compusa true):
 *   N1 → N2 → N4(TRUE) → N5 → N7(FALSE) → N9 → N10(TRUE) → N11(TRUE) → N12
 *   Date: score=90, bonus=0, extra=true → A+ (total=95)
 *
 * =========================================================================
 */
@DisplayName("Testare Structurala: Circuite Independente (McCabe V(G) = 5)")
public class IndependentCircuitsTest {

    @Test
    @DisplayName("Circuit 1: Calea de baza — extraCredit=false, total<60 → F")
    void circuit1_caleaDeBaza() {
        // N1 → N2(F) → N4(F) → N6 → N7(F) → N9 → [bucla epuizata] → N14
        // score=30, bonus=0, extra=false → total=30 → F
        assertEquals("F", Calculator.calculateGrade(30, 0, false));
    }

    @Test
    @DisplayName("Circuit 2: Deviatie exceptie — score invalid")
    void circuit2_exceptie() {
        // N1 → N2(T) → N3 (throw)
        // score=-1 → exception
        assertThrows(IllegalArgumentException.class, () ->
            Calculator.calculateGrade(-1, 0, false));
    }

    @Test
    @DisplayName("Circuit 3: Deviatie extraCredit=true, nota B")
    void circuit3_extraCreditTrue() {
        // N1 → N2(F) → N4(T) → N5 → N7(F) → N9 → N10(T) → N11(F) → N13
        // score=80, bonus=0, extra=true → total=85 → B
        assertEquals("B", Calculator.calculateGrade(80, 0, true));
    }

    @Test
    @DisplayName("Circuit 4: Deviatie total>105 capped, nota A")
    void circuit4_totalCapped() {
        // N1 → N2(F) → N4(F) → N6 → N7(T) → N8 → N9 → N10(T) → N11(F) → N13
        // score=100, bonus=20, extra=false → total=120→105 → A
        assertEquals("A", Calculator.calculateGrade(100, 20, false));
    }

    @Test
    @DisplayName("Circuit 5: Deviatie A+ (conditia compusa true)")
    void circuit5_aPlus() {
        // N1 → N2(F) → N4(T) → N5 → N7(F) → N9 → N10(T) → N11(T) → N12
        // score=90, bonus=0, extra=true → total=95 → A+
        assertEquals("A+", Calculator.calculateGrade(90, 0, true));
    }
}
