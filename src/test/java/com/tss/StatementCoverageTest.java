package com.tss;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;


@DisplayName("Testare Structurala: Acoperire la Nivel de Instructiune (Statement Coverage)")
public class StatementCoverageTest {

    /**
     * Acopera instructiunea: throw new IllegalArgumentException(...)
     * Aceasta instructiune se executa doar cand D1 este TRUE (score invalid).
     * Fara acest test, instructiunea throw nu ar fi executata niciodata.
     */
    @Test
    @DisplayName("Instructiunea throw — score invalid triggereaza exceptia")
    void testExceptieScoreInvalid() {
        // Acopera: if (score < 0 || score > 100) throw new IllegalArgumentException
        // score=-5 face ca conditia (score < 0) sa fie TRUE => se executa throw
        assertThrows(IllegalArgumentException.class, () ->
            Calculator.calculateGrade(-5, 0, false));
    }

    /**
     * Acopera instructiunea: total = score + bonus + 5
     * Aceasta instructiune se executa doar cand extraCredit este TRUE.
     * Verificam ca ramura TRUE a deciziei D2 este executata.
     */
    @Test
    @DisplayName("Ramura extraCredit = true — total = score + bonus + 5")
    void testExtraCreditTrue() {
        // Acopera: if (extraCredit) → total = score + bonus + 5
        // score=80, bonus=0, extra=true → total = 80+0+5 = 85 => nota B
        assertEquals("B", Calculator.calculateGrade(80, 0, true));
    }

    /**
     * Acopera instructiunea: total = score + bonus (ramura else)
     * Aceasta instructiune se executa cand extraCredit este FALSE.
     */
    @Test
    @DisplayName("Ramura extraCredit = false — total = score + bonus")
    void testExtraCreditFalse() {
        // Acopera ramura else a D2: total = score + bonus (fara +5)
        // score=75, bonus=0, extra=false => total=75 => nota C
        assertEquals("C", Calculator.calculateGrade(75, 0, false));
    }

    /**
     * Acopera instructiunea: total = 105 (plafonarea)
     * Aceasta instructiune se executa doar cand total > 105.
     * Fara acest test, linia de cod total=105 nu ar fi executata niciodata.
     */
    @Test
    @DisplayName("Limitarea totalului la 105 — total > 105 devine 105")
    void testLimitareTotal105() {
        // Acopera: if (total > 105) total = 105
        // score=100, bonus=20 => total=120, dar se limiteaza la 105 => nota A
        assertEquals("A", Calculator.calculateGrade(100, 20, false));
    }

    /**
     * Acopera instructiunea: return "A+"
     * Aceasta instructiune se executa doar cand conditia compusa
     * (thresholds[i] == 90 && extraCredit) este TRUE.
     */
    @Test
    @DisplayName("Nota A+ — conditie compusa thresholds[i]==90 && extraCredit")
    void testNotaAPlus() {
        // Acopera: return "A+" (D6 TRUE)
        // score=90, bonus=0, extra=true => total=95, prag=90, extraCredit=true => A+
        assertEquals("A+", Calculator.calculateGrade(90, 0, true));
    }

    /**
     * Acopera instructiunea: return grades[0] care este "A".
     * Se executa cand totalul >= 90 dar extraCredit este false.
     */
    @Test
    @DisplayName("Nota A — total >= 90, fara extraCredit")
    void testNotaA() {
        // Acopera: return grades[0] = "A" (D6 FALSE, dar D5 TRUE la i=0)
        assertEquals("A", Calculator.calculateGrade(95, 0, false));
    }

    /**
     * Acopera instructiunea: return grades[1] care este "B".
     * Bucla parcurge prima iteratie (prag 90, nu se potriveste),
     * la a doua iteratie (prag 80) gaseste potrivirea.
     */
    @Test
    @DisplayName("Nota B — total >= 80 si < 90")
    void testNotaB() {
        // Acopera: return grades[1] = "B" (iteratia i=1)
        assertEquals("B", Calculator.calculateGrade(85, 0, false));
    }

    /**
     * Acopera instructiunea: return grades[2] care este "C".
     */
    @Test
    @DisplayName("Nota C — total >= 70 si < 80")
    void testNotaC() {
        // Acopera: return grades[2] = "C" (iteratia i=2)
        assertEquals("C", Calculator.calculateGrade(70, 0, false));
    }

    /**
     * Acopera instructiunea: return grades[3] care este "D".
     */
    @Test
    @DisplayName("Nota D — total >= 60 si < 70")
    void testNotaD() {
        // Acopera: return grades[3] = "D" (iteratia i=3)
        assertEquals("D", Calculator.calculateGrade(60, 0, false));
    }

    /**
     * Acopera instructiunea: return "F" (de dupa bucla).
     * Bucla se parcurge complet fara sa gaseasca un prag potrivit,
     * deci totalul este sub 60 si se returneaza nota F.
     */
    @Test
    @DisplayName("Nota F — total < 60, bucla se epuizeaza")
    void testNotaF() {
        // Acopera: return "F" — calea care trece prin toata bucla fara match
        // score=30 => total=30, sub toate pragurile => F
        assertEquals("F", Calculator.calculateGrade(30, 0, false));
    }
}
