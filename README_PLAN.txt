================================================================================
PLAN CONTINUT README.md — T3 Testare Unitara in Java
================================================================================

README-ul va fi documentatia principala a proiectului. Trebuie sa contina
urmatoarele sectiuni (conform cerintelor din PDF-ul temei):

================================================================================
1. TITLU SI INFORMATII GENERALE
================================================================================
- Titlul proiectului: "T3 — Testare Unitara in Java"
- Membrii echipei (nume, prenume, grupa)
- Link repository GitHub
- Materia: TSS (Testarea Sistemelor Software), FMI, an 2025-2026

================================================================================
2. DESCRIEREA CLASEI DE TESTAT
================================================================================
- Prezentarea clasei Calculator si a metodei calculateGrade
- Explicarea parametrilor (score, bonus, extraCredit)
- Explicarea logicii de calcul a notei
- Evidentierea constructiilor din cod care satisfac cerintele:
  * 3 parametri
  * instructiune repetitiva (for)
  * if cu else, if fara else
  * conditie simpla, conditie compusa
- Bucata de cod a metodei (snippet)

================================================================================
3. STRATEGII DE TESTARE FUNCTIONALA (Blackbox)
================================================================================
3.1 Partitionare in clase de echivalenta
    - Tabel cu clasele de echivalenta identificate (CE1-CE12)
    - Explicatie: de ce aceste clase?
    - Screenshot-uri cu rularea testelor (JUnit verde/rosu)

3.2 Analiza valorilor de frontiera (BVA)
    - Tabel cu pragurile si valorile testate (prag-1, prag, prag+1)
    - Diagrama frontierelor
    - Screenshot-uri cu rularea testelor

================================================================================
4. STRATEGII DE TESTARE STRUCTURALA (Whitebox)
================================================================================
4.1 Graful Fluxului de Control (CFG)
    - DIAGRAMA CFG a metodei calculateGrade (facuta cu diagrams.net)
      * Nodurile etichetate N1-N14
      * Arcele numerotate
      * IMPORTANT: profesoara cere diagrame facute cu tool-uri, NU fotografiate!
    - Explicarea nodurilor si arcelor

4.2 Acoperire la nivel de instructiune (Statement Coverage)
    - Tabel: instructiune -> test care o acopera
    - Screenshot raport JaCoCo (instructions coverage)

4.3 Acoperire la nivel de decizie/ramura (Branch/Decision Coverage)
    - Tabel: decizie -> ramura TRUE/FALSE -> test
    - Screenshot raport JaCoCo (branch coverage)

4.4 Acoperire la nivel de conditie — MC/DC
    - Tabele MC/DC pentru fiecare decizie compusa:
      * D1: score < 0 || score > 100
      * D6: thresholds[i] == 90 && extraCredit
    - Explicarea influentei independente a fiecarei conditii
    - Screenshot-uri

4.5 Circuite independente (Complexitate ciclomatica McCabe)
    - Calculul V(G) = e - n + 2
    - Lista circuitelor independente (setul de baza)
    - Tabel: circuit -> cale prin noduri -> date de test -> rezultat
    - Referinta la CFG

================================================================================
5. MUTATION TESTING CU PIT
================================================================================
- Explicarea mutation testing (ce sunt mutantii, cum sunt generati)
- Operatorii de mutatie folositi de PIT
- Screenshot raport PIT (mutation score initial)
- Tabel cu mutantii generati:
  * Mutantul (operatorul + linia)
  * Status: killed / survived / equivalent
- Identificarea a CEL PUTIN 2 mutanti neechivalenti ramasi in viata
- Analiza: de ce au supravietuit?
- Testele suplimentare scrise pentru a-i omori
- Screenshot raport PIT dupa adaugarea testelor suplimentare
- Calculul mutation score: MS(T) = D / (D + L)

================================================================================
6. CONFIGURATIA TEHNICA
================================================================================
- Configuratia hardware (procesor, RAM, OS)
- Configuratia software:
  * Versiune Java (11)
  * Versiune JUnit (5.10.2)
  * Versiune JaCoCo (0.8.12)
  * Versiune PIT (1.16.1)
  * Build tool: Maven
  * IDE: IntelliJ IDEA (versiune)
- Captura de ecran cu structura proiectului in IDE

================================================================================
7. COMPARATIE REZULTATE / TOOL-URI (TABEL)
================================================================================
- Tabel comparativ:
  | Strategie           | Nr. teste | Coverage atins | Tool folosit |
  |---------------------|-----------|----------------|--------------|
  | Statement coverage  | ...       | 100%           | JaCoCo       |
  | Branch coverage     | ...       | 100%           | JaCoCo       |
  | Condition coverage  | ...       | MC/DC complet  | Manual       |
  | Mutation testing    | ...       | MS=xx%         | PIT          |
- Interpretari: ce strategie a fost cea mai eficienta?

================================================================================
8. RAPORT FOLOSIRE AI
================================================================================
ATENTIE: Aceasta sectiune este OBLIGATORIE conform cerintelor!

- Tool-ul AI folosit (ex: ChatGPT, Claude, GitHub Copilot)
- Prompt-urile date (copiate exact)
- Raspunsurile primite (cod generat de AI)
- Comparatie: suita PROPRIE de teste vs. testele AUTO-GENERATE
  * Tabel: test propriu vs. test AI → diferente
  * Ce a generat AI-ul bine?
  * Ce a ratat AI-ul?
- Screenshot-uri cu rularea codului autogenerat
- Interpretare si concluzii
- Referinte bibliografice (cu data generarii)

================================================================================
9. REFERINTE BIBLIOGRAFICE
================================================================================
Format cerut:
[1] Prenume, Nume, Titlu articol/carte, URL/Editura, Data accesarii
[2] OpenAI, ChatGPT, https://chatgpt.com/, Data generarii: ...
[3] etc.

Referinte de inclus:
- Cursurile TSS (Sorina Predut)
- Documentatia JUnit 5: https://junit.org/junit5/docs/current/user-guide/
- Documentatia JaCoCo: https://www.jacoco.org/jacoco/trunk/doc/
- Documentatia PIT: https://pitest.org
- Mathur, Aditya P., "Foundations of Software Testing"
- Tool-urile AI folosite

================================================================================
10. VIDEO DEMO (link)
================================================================================
- Link YouTube/Stream cu demo-ul:
  * Prezentarea codului in IDE
  * Rularea testelor JUnit (verde)
  * Generarea si prezentarea raportului JaCoCo
  * Generarea si prezentarea raportului PIT
  * Explicarea unui mutant omorat si a unuia echivalent
