package com.tss;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

// testare structurala - circuite independente mccabe
@DisplayName("Testare Structurala: Circuite Independente (McCabe V(G) = 5)")
public class IndependentCircuitsTest {

    // testare flux obisnuit eroare
    @Test
    @DisplayName("Circuit 1: Calea de baza — extraCredit=false, total<60 → F")
    void circuit1_caleaDeBaza() {
        // N1 → N2(F) → N4(F) → N6 → N7(F) → N9 → [bucla epuizata] → N14
        // score=30, bonus=0, extra=false → total=30 → F
        assertEquals("F", Calculator.calculateGrade(30, 0, false));
    }

    // testare drum blocant return timpuriu
    @Test
    @DisplayName("Circuit 2: Deviatie exceptie — score invalid")
    void circuit2_exceptie() {
        assertThrows(IllegalArgumentException.class, () ->
            Calculator.calculateGrade(-1, 0, false));
    }

    // testare flux normal nota mare extra
    @Test
    @DisplayName("Circuit 3: Deviatie extraCredit=true, nota B")
    void circuit3_extraCreditTrue() {
        assertEquals("B", Calculator.calculateGrade(80, 0, true));
    }

    // testare limitator puncte bune
    @Test
    @DisplayName("Circuit 4: Deviatie total>105 capped, nota A")
    void circuit4_totalCapped() {
        assertEquals("A", Calculator.calculateGrade(100, 20, false));
    }

    // flux returnare imediata a plus
    @Test
    @DisplayName("Circuit 5: Deviatie A+ (conditia compusa true)")
    void circuit5_aPlus() {
        assertEquals("A+", Calculator.calculateGrade(90, 0, true));
    }
}
