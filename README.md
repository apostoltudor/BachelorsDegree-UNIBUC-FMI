# T3 – Testare Unitară în Java

## 1. Descrierea Proiectului

Acest proiect implementează o suită de teste unitare în Java pentru o aplicație simulată, ca parte a temei **T3 - Testare Unitară**. Obiectivul principal a fost proiectarea testelor aplicând strategii de testare funcțională (Black-Box), testare structurală (White-Box) și validarea calității testelor prin Mutation Testing folosind uneltele specifice precum JUnit 5, JaCoCo și PIT.

Proiectul a fost configurat utilizând ecosistemul Maven.

## 2. Configurația Sistemului (Software & Hardware)

**Configurație Software:**

- **Limbaj:** Java 11 (sau superior)
- **Management și Build:** Apache Maven 3.9.x
- **Testare Unitară:** JUnit 5 (versiunea 5.10.2)
- **Code Coverage:** JaCoCo Engine (versiunea 0.8.12)
- **Mutation Testing:** PITest (versiunea 1.16.1)

**Configurație Hardware & Mediu:**

- **Mediu Execuție:** Local Machine (macOS Tahoe 26.0.1 / MacBook Air M2)
- **IDE Utilizat:** VS Code

## 3. Arhitectura și Logica

Clasa testată este `Calculator.java`, mai exact metoda de calcul a notelor: `calculateGrade(int score, int bonus, boolean extraCredit)`.
Pentru a satisface toate cerințele impuse, fluxul metodei a fost special elaborat astfel încât să conțină:

- **Structuri decizionale de bază:** `if` / `if-else`
- **Condiții compuse / decizii complexe:** `if (score < 0 || score > 100)`, `if (thresholds[i] == 90 && extraCredit)`
- **O instrucțiune repetitivă:** `for` loop iterând printr-un array de praguri predefinite de la 100 până la nota de trecere.

## 4. Strategii de Testare Implementate

Suitele de testare se împart în 3 abordări majore:

**A. Testare Funcțională (Black-Box)**

- **Partiționarea în clase de echivalență (`EquivalencePartitioningTest`):** Parametrii de intrare au fost divizați în intervale de clase invalide (ex: sub 0 sau peste 100) și clase valide (fiecare tip de notă în funcție de range-ul ei).
- **Analiza Valorilor de Frontieră (`BoundaryValueTest`):** Testarea la limite (sub prag, exact pe prag, imediat deasupra pragului) pentru intervalele notelor (60, 70, 80, 90 și valoarea limită fixată 105).

**B. Testare Structurală (White-Box)**

- **Acoperire la Nivel de Instrucțiune (`StatementCoverageTest`):** Ne-am asigurat că fiecare linie de cod se execută cel puțin o dată.
- **Acoperire la Nivel de Decizie/Ramură (`BranchCoverageTest`):** Fiecare ramură din Graful Fluxului de Control a fost atinsă de setul de teste.
- **Acoperire la Nivel de Condiție și MC/DC (`ConditionCoverageTest`):** Verificare la nivel atomic al predicatelor logice complexe, dovedind efectul izolat al fiecărei expresii care intră într-un `if` AND/OR.
- **Testarea Circuitelor Independente (`IndependentCircuitsTest`):** Bazat pe complexitatea ciclomatică McCabe (*V(G) = 5*), unde am derivat 5 căi total independente din CFG și am scris câte un test dedicat pentru fiecare drum fundamental parcurs de cod.

**C. Testare bazată pe mutanți (Mutation Testing)**

- S-a utilizat pluginul PITest pentru generarea de buguri forțate pe cod.
- Mutanții "supraviețuitori" au fost atent analizați, iar noi am adăugat teste dedicate în `MutationKillerTest` strict pentru omorârea mutanților de ordin unu ce nu puteau fi prinși prin acoperirea clasică.

## 5. Fragmente de Cod Relevante

**A. Logica principală supusă testelor (`Calculator.java`)**

```java
public static String calculateGrade(int score, int bonus, boolean extraCredit) {
    if (score < 0 || score > 100) {
        throw new IllegalArgumentException("Score must be between 0 and 100");
    }
    // ... stabilire total / aplicare bonus / limitare 105
    for (int i = 0; i < thresholds.length; i++) {
        if (total >= thresholds[i]) {
            if (thresholds[i] == 90 && extraCredit) {
                return "A+";
            }
            return grades[i];
        }
    }
    return "F";
}
```

**B. Fragment din Acoperirea Condițiilor - MC/DC (`ConditionCoverageTest.java`)**

```java
@Test
@DisplayName("t1: C1=FALSE, C2=TRUE → D1=TRUE (score=101 demonstreaza efectul C2)")
void t1_c1False_c2True() {
    assertThrows(IllegalArgumentException.class, () ->
        Calculator.calculateGrade(101, 0, false));
}
```

**C. Test Suplimentar creat pentru prinderea unui Mutant (`MutationKillerTest.java`)**

```java
// Mutantul ascundea modificarea lui +5 (extra) in +6
@Test
@DisplayName("score=64, bonus=0, extra=true → D (nu C cum ar da mutantul +6)")
void killMutant2_precizieExtraCreditLaPrag70() {
    // Normal:  total = 64 + 0 + 5 = 69 → D
    // Mutant:  total = 64 + 0 + 6 = 70 → C (DIFERIT!)
    assertEquals("D", Calculator.calculateGrade(64, 0, true));
}
```

## 6. Rezultate Experimentale și Interpretare

**Acoperirea Codului (Code Coverage cu JaCoCo):**
Datorită testelor noastre riguroase structurale, am atins:

- **100% Branch Coverage** (toate ramificațiile acoperite)
- **94% Line Coverage** (o anumită linie `throw` nu a putut fi atinsă la un branch absolut, dar overall toate deciziile sunt testate)

<img width="1014" height="369" alt="jacoco" src="https://github.com/user-attachments/assets/aca42f9d-a52e-412f-b037-7de309265f57" />


**Analiza Mutanților (PITest):**
A fost înregistrat un **Mutation Score de 87%**. Din cei 39 de mutanți generați, ambele suite reușesc să identifice 34 de tipuri de defecte inserate.
Cei 5 mutanți "supraviețuitori" lăsați în raport subliniază conceptul de **Mutanți Echivalenți**:

- Mutantul a modificat de exemplu `105` în `106` pe if-ul `if (total > 105)`. E absolut echivalent matematic pentru că testul continuă la filtrul `>= 90` și returnează oricum nota A. Am adăugat documentarea specifică a acestora fix în clasă ca exemple de mutații invizibile.

<img width="811" height="455" alt="pitest" src="https://github.com/user-attachments/assets/00f9198e-27bc-4729-9fdc-c2cb3bf0d121" />


## 7. Capturi de Ecran doveditoare

- Execuția testelor (88/88 passed):
  <img width="1002" height="199" alt="junit" src="https://github.com/user-attachments/assets/2a75a7dc-5aed-45f9-90bf-89b86f63e5cb" />

- Diagrama Grafului de Control al Fluxului (CFG) generată în diagrams.net pe baza codului pentru complexitatea ciclomatică:
  <img width="1626" height="741" alt="diagrama_tss 22 30 32" src="https://github.com/user-attachments/assets/1b2ed5ec-0487-4562-8c92-f4856a8d2fc4" />


## 8. Demonstrație Video

https://youtu.be/s8MJVBEvsTY

## 9. Raport Utilizare Asistenți AI


## Bibliografie

1. Junit 5 User Guide. Disponibil la: https://junit.org/junit5/docs/current/user-guide/
2. JaCoCo Documentation. Disponibil la: https://www.jacoco.org/jacoco/
3. PITest Mutation testing system. Disponibil la: https://pitest.org/
4. Google, Gemini, https://gemini.google.com/, Data generării: Aprilie 2026.
