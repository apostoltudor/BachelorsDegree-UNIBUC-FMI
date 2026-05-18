# T3 – Testare Unitară în Java

## Cuprins
- [Despre proiect](#despre-proiect)
- [Mediu de lucru](#mediu-de-lucru)
- [Logica aplicației](#logica-aplicației)
- [Cum am testat](#cum-am-testat)
- [Rezultate](#rezultate)
- [Dovezi](#dovezi)
- [Video](#video)
- [Raport AI](#raport-ai)
- [Bibliografie](#bibliografie)

## Despre proiect
Acest proiect este tema T3 de testare unitară. Am construit teste automate pentru o aplicație simplă care transformă un punctaj într-o notă finală.

Scopul a fost să verificăm aplicația din trei unghiuri:
- testare funcțională, adică verificăm ce rezultat se întoarce pentru diferite valori de intrare;
- testare structurală, adică urmărim ce părți din cod sunt executate;
- mutation testing, adică verificăm dacă testele prind greșeli introduse intenționat în cod.

## Mediu de lucru

### Software
- Java 11 sau superior
- Apache Maven 3.9.x
- JUnit 5.10.2
- JaCoCo 0.8.12
- PITest 1.16.1

### Hardware și IDE
- MacBook Air M2
- macOS Tahoe 26.0.1
- VS Code

## Logica aplicației
Metoda testată este `calculateGrade(int score, int bonus, boolean extraCredit)`.

Fluxul ei conține:
- o verificare de început pentru scor invalid;
- o ramură pentru `extraCredit`;
- o limitare a totalului la 105;
- o buclă care compară totalul cu pragurile notelor.

## Cum am testat

### 1. Testare funcțională
Am verificat dacă metoda returnează nota corectă pentru valori diferite de intrare.

### 2. Testare structurală
Am urmărit codul pe mai multe niveluri:
- `StatementCoverageTest` pentru a executa fiecare instrucțiune importantă;
- `BranchCoverageTest` pentru a trece prin ramurile principale ale codului;
- `ConditionCoverageTest` pentru a verifica părțile din condițiile compuse;
- `IndependentCircuitsTest` pentru a acoperi drumuri diferite și importante prin program.

### 3. Mutation testing
Am folosit PITest pentru a vedea dacă testele detectează modificări mici și greșite din cod.

## Graful de control

![Graf CFG calculateGrade](image/graf.png)

Legenda nodurilor:
- 1 = validare score
- 2 = excepție pentru scor invalid
- 3 = după validare și decizie extraCredit
- 4 = total cu +5
- 5 = total fără +5
- 6 = verificare total > 105
- 7 = plafonare la 105
- 8 = inițializări înainte de buclă
- 9 = condiția buclei
- 10 = verificare prag
- 11 = verificare A+
- 12 = return A+
- 13 = return nota curentă
- 14 = i++
- 15 = return F

### BranchCoverageTest

```java
void d1True() {
  assertThrows(IllegalArgumentException.class, () ->
    Calculator.calculateGrade(-1, 0, false));
}
```
Noduri activate: **1, 2**
Explicație: scorul este invalid și testul intră direct pe ramura de excepție.

```java
void d1False() {
  assertEquals("F", Calculator.calculateGrade(50, 0, false));
}
```
Noduri activate: **15**
Explicație: scorul este valid, iar rezultatul final este `F`.

```java
void d2True() {
  assertEquals("C", Calculator.calculateGrade(65, 0, true));
}
```
Noduri activate: **4, 13**
Explicație: `extraCredit = true` activează ramura cu bonus.

```java
void d2False() {
  assertEquals("D", Calculator.calculateGrade(65, 0, false));
}
```
Noduri activate: **5, 13**
Explicație: fără `extraCredit`, metoda folosește ramura normală.

```java
void d3True() {
  assertEquals("A", Calculator.calculateGrade(100, 20, false));
}
```
Noduri activate: **7, 13**
Explicație: totalul trece de 105 și se aplică plafonarea.

```java
void d3False() {
  assertEquals("C", Calculator.calculateGrade(75, 0, false));
}
```
Noduri activate: **13**
Explicație: totalul rămâne sub plafon și merge direct la nota finală.

```java
void d4TrueGaseste() {
  assertEquals("A", Calculator.calculateGrade(95, 0, false));
}
```
Noduri activate: **13**
Explicație: prima comparație din buclă găsește nota `A`.

```java
void d4FalseEpuizare() {
  assertEquals("F", Calculator.calculateGrade(30, 0, false));
}
```
Noduri activate: **15**
Explicație: nicio condiție din buclă nu este adevărată, deci se ajunge la `F`.

```java
void d5True() {
  assertEquals("B", Calculator.calculateGrade(85, 0, false));
}
```
Noduri activate: **10, 13**
Explicație: totalul trece de pragul 80 și se întoarce `B`.

```java
void d5False() {
  assertEquals("B", Calculator.calculateGrade(85, 0, false));
}
```
Noduri activate: **10, 14**
Explicație: prima comparație e falsă, deci se trece la următorul prag.

```java
void d6True() {
  assertEquals("A+", Calculator.calculateGrade(90, 0, true));
}
```
Noduri activate: **11, 12**
Explicație: pragul 90 și `extraCredit = true` duc la `A+`.

```java
void d6False() {
  assertEquals("A", Calculator.calculateGrade(95, 0, false));
}
```
Noduri activate: **11, 13**
Explicație: pragul este atins, dar fără `extraCredit` se întoarce `A`.

### ConditionCoverageTest și IndependentCircuitsTest
- **Acoperire la nivel de condiții și MC/DC:** verificăm fiecare parte din condițiile scrise în `if`.
  - Exemplu: la `score < 0 || score > 100`, testăm separat `score = -1` și `score = 101`.
- **Testarea circuitelor independente:** am ales 5 drumuri diferite prin cod și am scris câte un test pentru fiecare.
  - Exemplu: un test merge pe drumul cu excepție, iar altul merge pe drumul care duce la `A+`.

### MutationTesting
- PITest a generat mutanți în cod.
- Testele dedicate din `MutationKillerTest` au fost făcute ca să prindă acele greșeli.

## Rezultate

### Code coverage
- 100% Branch Coverage
- 94% Line Coverage

### Mutation score
- Mutation Score: 87%
- 34 mutanți au fost omorâți din 39 generați

## Dovezi
- Execuția testelor: 88/88 passed
- Diagrama CFG a fost generată pe baza metodei `calculateGrade`
- Capturi de ecran pentru JaCoCo și PITest sunt incluse în proiect

## Video
https://youtu.be/s8MJVBEvsTY

## Raport AI

Această secțiune poate fi completată cu scurtă descriere despre cum au fost folosiți asistenții AI în realizarea proiectului.

## Bibliografie
1. JUnit 5 User Guide: https://junit.org/junit5/docs/current/user-guide/
2. JaCoCo Documentation: https://www.jacoco.org/jacoco/
3. PITest Documentation: https://pitest.org/
4. Google Gemini: https://gemini.google.com/
