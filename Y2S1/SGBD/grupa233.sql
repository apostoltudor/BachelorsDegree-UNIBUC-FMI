--09.10.2024

--4
select * from (
    select t.category, 
           count(distinct t.title_id) as numar_titluri,
           count(r.copy_id) as numar_exemplare
    from title t
    join rental r on t.title_id = r.title_id
    group by t.category
    order by count(r.copy_id) desc
)
where rownum = 1;

--5
select t.title_id, count(tc.copy_id) as exemplare_disponibile
from title t
join title_copy tc on t.title_id = tc.title_id
where tc.status = 'AVAILABLE'
group by t.title_id
order by t.title_id;

--16.10.2024

--E1
DECLARE
    numar number(3) := 100;
    mesaj1 varchar2(255) := 'text 1';
    mesaj2 varchar2(255) := 'text 2';
BEGIN
    DECLARE
        numar number(3) := 1;
        mesaj1 varchar2(255) := 'text 2';
        mesaj2 varchar2(255) := 'text 3';
    BEGIN
        numar := numar + 1;
        mesaj2 := mesaj2 || ' adaugat in sub-bloc';

        DBMS_OUTPUT.PUT_LINE('Valoarea variabilelor in sub-bloc:');
        DBMS_OUTPUT.PUT_LINE('numar (sub-bloc) = ' || numar);
        DBMS_OUTPUT.PUT_LINE('mesaj1 (sub-bloc) = ' || mesaj1);
        DBMS_OUTPUT.PUT_LINE('mesaj2 (sub-bloc) = ' || mesaj2);
    END;

    numar := numar + 1;
    mesaj1 := mesaj1 || ' adaugat un blocul principal';
    mesaj2 := mesaj2 || ' adaugat in blocul principal';

    DBMS_OUTPUT.PUT_LINE('Valoarea variabilelor dupa executia sub-blocului:');
    DBMS_OUTPUT.PUT_LINE('numar (bloc principal) = ' || numar);
    DBMS_OUTPUT.PUT_LINE('mesaj1 (bloc principal) = ' || mesaj1);
    DBMS_OUTPUT.PUT_LINE('mesaj2 (bloc principal) = ' || mesaj2);
END;
/

--E3
DECLARE
    v_nume VARCHAR2(50) := '&nume_membru';
    v_numar_filme NUMBER;
BEGIN
    SELECT COUNT(DISTINCT title_id)
    INTO v_numar_filme
    FROM rental r
    JOIN member m ON r.member_id = m.member_id
    WHERE m.last_name = v_nume;

    IF v_numar_filme > 0 THEN
        DBMS_OUTPUT.PUT_LINE('Numărul de filme împrumutate de ' || v_nume || ' este: ' || v_numar_filme);
    ELSE
        DBMS_OUTPUT.PUT_LINE('Nu există niciun membru cu numele ' || v_nume);
    END IF;
END;
/

--E4
DECLARE
    v_nume VARCHAR2(50) := '&nume_membru';
    v_numar_filme NUMBER;
    v_total_filme NUMBER := (SELECT COUNT(*) FROM title);
BEGIN
    SELECT COUNT(DISTINCT title_id)
    INTO v_numar_filme
    FROM rental r
    JOIN member m ON r.member_id = m.member_id
    WHERE m.last_name = v_nume;

    IF v_numar_filme / v_total_filme > 0.75 THEN
        DBMS_OUTPUT.PUT_LINE('Categoria 1 (a împrumutat mai mult de 75% din titlurile existente)');
    ELSIF v_numar_filme / v_total_filme > 0.5 THEN
        DBMS_OUTPUT.PUT_LINE('Categoria 2 (a împrumutat mai mult de 50% din titlurile existente)');
    ELSIF v_numar_filme / v_total_filme > 0.25 THEN
        DBMS_OUTPUT.PUT_LINE('Categoria 3 (a împrumutat mai mult de 25% din titlurile existente)');
    ELSE
        DBMS_OUTPUT.PUT_LINE('Categoria 4 (altfel)');
    END IF;
END;
/


SET SERVEROUTPUT ON

--6
DECLARE
    v_dep departments.department_name%TYPE;
    v_numar_angajati NUMBER;
BEGIN
    SELECT department_name, COUNT(*) as numar_angajati
    INTO v_dep, v_numar_angajati
    FROM employees e
    JOIN departments d ON e.department_id = d.department_id
    GROUP BY department_name
    HAVING COUNT(*) = (SELECT MAX(COUNT(*))
                       FROM employees
                       GROUP BY department_id);

    DBMS_OUTPUT.PUT_LINE('Departamentul cu cei mai mulți angajați este: ' || v_dep);
    DBMS_OUTPUT.PUT_LINE('Numărul de angajați în acest departament este: ' || v_numar_angajati);
END;
/


--23.10.2024


--2 a)
DECLARE 
  TYPE emp_record IS RECORD  
        (cod employees.employee_id%TYPE,  
         salariu employees.salary%TYPE,  
         job employees.job_id%TYPE); 
  v_ang emp_record; 
BEGIN 
  v_ang.cod:=700; 
  v_ang.salariu:= 9000; 
  v_ang.job:='SA_MAN'; 
  DBMS_OUTPUT.PUT_LINE ('Angajatul cu codul '|| v_ang.cod ||  
    ' si jobul ' || v_ang.job || ' are salariul ' ||  v_ang.salariu); 
END; 
/

--b)
DECLARE 
  TYPE emp_record IS RECORD  
        (cod employees.employee_id%TYPE,  
         salariu employees.salary%TYPE,  
         job employees.job_id%TYPE); 
  v_ang emp_record;
BEGIN 
 SELECT employee_id, salary, job_id 
 INTO   v_ang 
 FROM   employees 
 WHERE  employee_id = 101; 
 DBMS_OUTPUT.PUT_LINE ('Angajatul cu codul '|| v_ang.cod ||  
    ' si jobul ' || v_ang.job || ' are salariul ' ||  v_ang.salariu); 
END; 
/ 

--c)

create table emp_233ta as select* from employees;

DECLARE 
  TYPE emp_record IS RECORD  
        (cod employees.employee_id%TYPE,  
         salariu employees.salary%TYPE,  
         job employees.job_id%TYPE); 
  v_ang emp_record;

BEGIN 
 DELETE FROM emp_233ta 
 WHERE employee_id=100 
 RETURNING employee_id, salary, job_id INTO v_ang; 
  
 DBMS_OUTPUT.PUT_LINE ('Angajatul cu codul '|| v_ang.cod ||  
    ' si jobul ' || v_ang.job || ' are salariul ' ||  v_ang.salariu); 
END; 
/ 

ROLLBACK;

--3
DECLARE 
 v_ang1     employees%ROWTYPE; 
 v_ang2     employees%ROWTYPE; 
BEGIN 
-- sterg angajat 100 si mentin in variabila linia stearsa 
   DELETE FROM emp_233ta     WHERE employee_id = 100     RETURNING employee_id, first_name, last_name, email, phone_number, 
             hire_date, job_id, salary, commission_pct, manager_id, 
             department_id  
   INTO v_ang1; 
 
-- inserez in tabel linia stearsa 
   INSERT INTO emp_233ta 
   VALUES v_ang1; 
 
-- sterg angajat 101  
   DELETE FROM emp_233ta    WHERE employee_id = 101;
   
   -- obtin datele din tabelul employees 
   SELECT * 
   INTO   v_ang2 
   FROM   employees 
   WHERE  employee_id = 101; 
 
-- inserez o linie oarecare in emp_233ta 
   INSERT INTO emp_233ta 
   VALUES(1000,'FN','LN','E',null,sysdate, 'AD_VP',1000, null,100,90); 
 
-- modific linia adaugata anterior cu valorile variabilei v_ang2 
   UPDATE emp_233ta 
   SET    ROW = v_ang2 
   WHERE  employee_id = 1000; 
 END; 
/ 

set serveroutput on

--4
DECLARE 
  TYPE tablou_indexat IS TABLE OF NUMBER INDEX BY PLS_INTEGER; 
  t    tablou_indexat; 
BEGIN 
-- punctul a 
  FOR i IN 1..10 LOOP 
    t(i):=i; 
  END LOOP; 
  DBMS_OUTPUT.PUT('Tabloul are ' || t.COUNT ||' elemente: '); 
  FOR i IN t.FIRST..t.LAST LOOP 
      DBMS_OUTPUT.PUT(t(i) || ' ');  
  END LOOP; 
  DBMS_OUTPUT.NEW_LINE; 
 
-- punctul b 
  FOR i IN 1..10 LOOP 
    IF i mod 2 = 1 THEN t(i):=null;  
    END IF; 
  END LOOP; 
  DBMS_OUTPUT.PUT('Tabloul are ' || t.COUNT ||' elemente: ');
  FOR i IN t.FIRST..t.LAST LOOP 
      DBMS_OUTPUT.PUT(nvl(t(i), 0) || ' ');  
  END LOOP; 
  DBMS_OUTPUT.NEW_LINE; 
 
-- punctul c 
  t.DELETE(t.first);   t.DELETE(5,7); 
  t.DELETE(t.last); 
  DBMS_OUTPUT.PUT_LINE('Primul element are indicele ' || t.first || 
         ' si valoarea ' || nvl(t(t.first),0)); 
  DBMS_OUTPUT.PUT_LINE('Ultimul element are indicele ' || t.last || 
         ' si valoarea ' || nvl(t(t.last),0)); 
  DBMS_OUTPUT.PUT('Tabloul are ' || t.COUNT ||' elemente: '); 
  FOR i IN t.FIRST..t.LAST LOOP 
     IF t.EXISTS(i) THEN  
        DBMS_OUTPUT.PUT(nvl(t(i), 0)|| ' ');  
     END IF; 
  END LOOP; 
  DBMS_OUTPUT.NEW_LINE; 
 
-- punctul d 
  t.delete; 
  DBMS_OUTPUT.PUT_LINE('Tabloul are ' || t.COUNT ||' elemente.'); 
END; 
/

--5
DECLARE 
  TYPE tablou_indexat IS TABLE OF emp_233ta%ROWTYPE  
                      INDEX BY BINARY_INTEGER; 
  t    tablou_indexat; 
BEGIN 
-- stergere din tabel si salvare in tablou  
   DELETE FROM emp_233ta     WHERE  ROWNUM<= 2 
   RETURNING employee_id, first_name, last_name, email, phone_number, 
             hire_date, job_id, salary, commission_pct, manager_id, 
             department_id  
   BULK COLLECT INTO t; 
 
--afisare elemente tablou 
  DBMS_OUTPUT.PUT_LINE (t(1).employee_id ||' ' || t(1).last_name); 
  DBMS_OUTPUT.PUT_LINE (t(2).employee_id ||' ' || t(2).last_name); 
 
--inserare cele 2 linii in tabel 
  INSERT INTO emp_233ta VALUES t(1);   INSERT INTO emp_233ta VALUES t(2); 
  END; 
/ 

--6

DECLARE 
  TYPE tablou_imbricat IS TABLE OF NUMBER; 
  t    tablou_imbricat := tablou_imbricat(); 
BEGIN 
-- punctul a 
  FOR i IN 1..10 LOOP 
     t.extend;  
     t(i):=i; 
  END LOOP; 
  DBMS_OUTPUT.PUT('Tabloul are ' || t.COUNT ||' elemente: '); 
   
  FOR i IN t.FIRST..t.LAST LOOP 
      DBMS_OUTPUT.PUT(t(i) || ' ');  
  END LOOP; 
  DBMS_OUTPUT.NEW_LINE;
  
  -- punctul b 
  FOR i IN 1..10 LOOP 
    IF i mod 2 = 1 THEN t(i):=null;  
    END IF; 
  END LOOP; 
  DBMS_OUTPUT.PUT('Tabloul are ' || t.COUNT ||' elemente: ');   FOR i IN t.FIRST..t.LAST LOOP 
      DBMS_OUTPUT.PUT(nvl(t(i), 0) || ' ');  
  END LOOP; 
  DBMS_OUTPUT.NEW_LINE; 
 
-- punctul c 
  t.DELETE(t.first);   t.DELETE(5,7); 
  t.DELETE(t.last); 
  DBMS_OUTPUT.PUT_LINE('Primul element are indicele ' || t.first || 
         ' si valoarea ' || nvl(t(t.first),0)); 
  DBMS_OUTPUT.PUT_LINE('Ultimul element are indicele ' || t.last || 
         ' si valoarea ' || nvl(t(t.last),0)); 
  DBMS_OUTPUT.PUT('Tabloul are ' || t.COUNT ||' elemente: '); 
  FOR i IN t.FIRST..t.LAST LOOP 
     IF t.EXISTS(i) THEN  
        DBMS_OUTPUT.PUT(nvl(t(i), 0)|| ' ');  
     END IF; 
  END LOOP; 
  DBMS_OUTPUT.NEW_LINE; 
 
-- punctul d 
  t.delete; 
  DBMS_OUTPUT.PUT_LINE('Tabloul are ' || t.COUNT ||' elemente.'); 
END; 
/

--7
DECLARE 
  TYPE tablou_imbricat IS TABLE OF CHAR(1); 
  t tablou_imbricat := tablou_imbricat('m', 'i', 'n', 'i', 'm'); 
  i INTEGER; 
BEGIN 
  i := t.FIRST; 
  WHILE i <= t.LAST LOOP 
    DBMS_OUTPUT.PUT(t(i)); 
    i := t.NEXT(i); 
  END LOOP; 
  DBMS_OUTPUT.NEW_LINE; 
   
  i := t.LAST; 
  WHILE i >= t.FIRST LOOP 
    DBMS_OUTPUT.PUT(t(i)); 
    i := t.PRIOR(i);
      END LOOP; 
  DBMS_OUTPUT.NEW_LINE; 
 
  t.delete(2);  
  t.delete(4); 
 
  i := t.FIRST; 
  WHILE i <= t.LAST LOOP 
    DBMS_OUTPUT.PUT(t(i)); 
    i := t.NEXT(i); 
  END LOOP; 
  DBMS_OUTPUT.NEW_LINE; 
   
  i := t.LAST; 
  WHILE i >= t.FIRST LOOP 
    DBMS_OUTPUT.PUT(t(i)); 
    i := t.PRIOR(i); 
  END LOOP; 
  DBMS_OUTPUT.NEW_LINE; 
 
END; 
/

--8
DECLARE 
  TYPE vector IS VARRAY(20) OF NUMBER; 
  t    vector:= vector(); 
BEGIN 
-- punctul a 
  FOR i IN 1..10 LOOP 
     t.extend; t(i):=i; 
  END LOOP; 
  DBMS_OUTPUT.PUT('Tabloul are ' || t.COUNT ||' elemente: '); 
  FOR i IN t.FIRST..t.LAST LOOP 
      DBMS_OUTPUT.PUT(t(i) || ' ');  
  END LOOP; 
  DBMS_OUTPUT.NEW_LINE; 
-- punctul b 
  FOR i IN 1..10 LOOP 
    IF i mod 2 = 1 THEN t(i):=null; 
    END IF; 
  END LOOP; 
  DBMS_OUTPUT.PUT('Tabloul are ' || t.COUNT ||' elemente: ');   FOR i IN t.FIRST..t.LAST LOOP 
      DBMS_OUTPUT.PUT(nvl(t(i), 0) || ' ');  
  END LOOP; 
  DBMS_OUTPUT.NEW_LINE; 
 
-- punctul c 
-- metodele DELETE(n), DELETE(m,n) nu sunt valabile pentru vectori!!!   
-- din vectori nu se pot sterge elemente individuale!!! 
 
-- punctul d 
  t.delete; 
  DBMS_OUTPUT.PUT_LINE('Tabloul are ' || t.COUNT ||' elemente.'); 
END; 
/

--9
CREATE OR REPLACE TYPE subordonati_233ta AS VARRAY(10) OF NUMBER(4); 
/ 
CREATE TABLE manageri_233ta (cod_mgr NUMBER(10), 
                           nume VARCHAR2(20), 
                           lista subordonati_233ta); 
 
DECLARE  
  v_sub   subordonati_233ta:= subordonati_233ta(100,200,300); 
  v_lista manageri_233ta.lista%TYPE; 
BEGIN 
  INSERT INTO manageri_233ta 
  VALUES (1, 'Mgr 1', v_sub); 
 
  INSERT INTO manageri_233ta 
  VALUES (2, 'Mgr 2', null); 
   
  INSERT INTO manageri_233ta 
  VALUES (3, 'Mgr 3', subordonati_233ta(400,500)); 
   
  SELECT lista 
  INTO   v_lista 
  FROM   manageri_233ta 
  WHERE  cod_mgr=1; 
   
  FOR j IN v_lista.FIRST..v_lista.LAST loop 
       DBMS_OUTPUT.PUT_LINE (v_lista(j)); 
  END LOOP; 
END; 
/ 

SELECT * FROM manageri_233ta;


DROP TABLE  manageri_233ta; 
DROP TYPE subordonati_233ta;

--10
CREATE TABLE emp_test_233ta AS  
      SELECT employee_id, last_name FROM employees 
      WHERE ROWNUM <= 2; 
 
CREATE OR REPLACE TYPE tip_telefon_233ta IS TABLE OF VARCHAR(12); 
/ 
 
ALTER TABLE emp_test_233ta 
ADD (telefon tip_telefon_233ta)  
NESTED TABLE telefon STORE AS tabel_telefon_233ta; 
 
INSERT INTO emp_test_233ta  
VALUES (500, 'XYZ',tip_telefon_233ta('074XXX', '0213XXX', '037XXX')); 
 
UPDATE emp_test_233ta 
SET    telefon = tip_telefon_233ta('073XXX', '0214XXX') 
WHERE  employee_id=100; 
 
SELECT  a.employee_id, b.* 
FROM    emp_test_233ta a, TABLE (a.telefon) b; 
 
DROP TABLE emp_test_233ta; 
DROP TYPE  tip_telefon_233ta;

--11
--v1
DECLARE 
  TYPE tip_cod IS VARRAY(5) OF NUMBER(3); 
  coduri tip_cod := tip_cod(205,206);  
BEGIN 
  FOR i IN coduri.FIRST..coduri.LAST  LOOP 
    DELETE FROM emp_233ta 
    WHERE  employee_id = coduri (i); 
  END LOOP; 
END;  
/ 
SELECT employee_id FROM emp_233ta; 
ROLLBACK;
--v2
DECLARE 
  TYPE tip_cod IS VARRAY(20) OF NUMBER; 
  coduri tip_cod := tip_cod(205,206); 
BEGIN 
  FORALL i IN coduri.FIRST..coduri.LAST 
    DELETE FROM emp_233ta 
    WHERE  employee_id = coduri (i); 
END; 
/ 
SELECT employee_id FROM emp_233ta; 
ROLLBACK;

set serveroutput on

--30.10.2024

--1
DECLARE
  v_nr    number(4); 
  v_nume  departments.department_name%TYPE; 
  CURSOR c IS 
    SELECT department_name nume, COUNT(employee_id) nr   
    FROM   departments d, employees e 
    WHERE  d.department_id=e.department_id(+)  
    GROUP BY department_name;  
BEGIN 
  OPEN c; 
  LOOP 
      FETCH c INTO v_nume,v_nr; 
      EXIT WHEN c%NOTFOUND; 
      IF v_nr=0 THEN 
         DBMS_OUTPUT.PUT_LINE('In departamentul '|| v_nume|| 
                           ' nu lucreaza angajati'); 
      ELSIF v_nr=1 THEN 
           DBMS_OUTPUT.PUT_LINE('In departamentul '|| v_nume|| 
                           ' lucreaza un angajat'); 
      ELSE 
         DBMS_OUTPUT.PUT_LINE('In departamentul '|| v_nume|| 
                           ' lucreaza '|| v_nr||' angajati'); 
     END IF; 
 END LOOP; 
 CLOSE c; 
END;
/

--2
DECLARE 
  TYPE   tab_nume IS TABLE OF departments.department_name%TYPE; 
  TYPE   tab_nr IS TABLE OF NUMBER(4); 
  t_nr   tab_nr; 
  t_nume tab_nume; 
  CURSOR c IS 
    SELECT department_name nume, COUNT(employee_id) nr   
    FROM   departments d, employees e 
    WHERE  d.department_id=e.department_id(+) 
    GROUP BY department_name;  
BEGIN 
  OPEN c; 
  FETCH c  BULK COLLECT INTO t_nume, t_nr; 
  CLOSE c; 
  FOR i IN t_nume.FIRST..t_nume.LAST LOOP 
      IF t_nr(i)=0 THEN 
         DBMS_OUTPUT.PUT_LINE('In departamentul '|| t_nume(i)|| 
                           ' nu lucreaza angajati'); 
      ELSIF t_nr(i)=1 THEN 
           DBMS_OUTPUT.PUT_LINE('In departamentul '||t_nume(i)|| 
                           ' lucreaza un angajat'); 
      ELSE 
         DBMS_OUTPUT.PUT_LINE('In departamentul '|| t_nume(i)|| 
                           ' lucreaza '|| t_nr(i)||' angajati'); 
     END IF; 
  END LOOP; 
END; 
/

--3
DECLARE 
  CURSOR c IS 
    SELECT department_name nume, COUNT(employee_id) nr  
    FROM   departments d, employees e 
    WHERE  d.department_id=e.department_id(+) 
    GROUP BY department_name;  
BEGIN 
  FOR i in c LOOP 
      IF i.nr=0 THEN 
         DBMS_OUTPUT.PUT_LINE('In departamentul '|| i.nume|| 
                           ' nu lucreaza angajati'); 
      ELSIF i.nr=1 THEN 
           DBMS_OUTPUT.PUT_LINE('In departamentul '|| i.nume || 
                           ' lucreaza un angajat'); 
      ELSE 
         DBMS_OUTPUT.PUT_LINE('In departamentul '|| i.nume|| 
                           ' lucreaza '|| i.nr||' angajati'); 
     END IF; 
 END LOOP; 
END; 
/ 

--4
BEGIN 
  FOR i in (SELECT department_name nume, COUNT(employee_id) nr  
            FROM   departments d, employees e 
            WHERE  d.department_id=e.department_id(+) 
            GROUP BY department_name) LOOP 
      IF i.nr=0 THEN 
         DBMS_OUTPUT.PUT_LINE('In departamentul '|| i.nume|| 
                           ' nu lucreaza angajati'); 
      ELSIF i.nr=1 THEN 
           DBMS_OUTPUT.PUT_LINE('In departamentul '|| i.nume || 
                           ' lucreaza un angajat'); 
      ELSE 
         DBMS_OUTPUT.PUT_LINE('In departamentul '|| i.nume|| 
                           ' lucreaza '|| i.nr||' angajati'); 
     END IF; 
 END LOOP; END; 
/ 
--5
DECLARE 
  v_cod    employees.employee_id%TYPE; 
  v_nume   employees.last_name%TYPE; 
  v_nr     NUMBER(4); 
  CURSOR c IS 
    SELECT   sef.employee_id cod, MAX(sef.last_name) nume,  
             count(*) nr 
    FROM     employees sef, employees ang 
    WHERE    ang.manager_id = sef.employee_id 
    GROUP BY sef.employee_id 
    ORDER BY nr DESC; 
BEGIN 
  OPEN c; 
    LOOP 
      FETCH c INTO v_cod,v_nume,v_nr; 
      EXIT WHEN c%ROWCOUNT>3 OR c%NOTFOUND; 
      DBMS_OUTPUT.PUT_LINE('Managerul '|| v_cod ||  
                           ' avand numele ' || v_nume ||  
                           ' conduce ' || v_nr||' angajati'); 
    END LOOP; 
  CLOSE c; 
END; 
/

--6
DECLARE 
  CURSOR c IS 
    SELECT   sef.employee_id cod, MAX(sef.last_name) nume,  
             count(*) nr 
    FROM     employees sef, employees ang 
    WHERE    ang.manager_id = sef.employee_id 
    GROUP BY sef.employee_id 
    ORDER BY nr DESC; 
BEGIN 
  FOR i IN c LOOP 
      EXIT WHEN c%ROWCOUNT>3 OR c%NOTFOUND; 
      DBMS_OUTPUT.PUT_LINE('Managerul '|| i.cod ||  
                           ' avand numele ' || i.nume ||  
                           ' conduce '|| i.nr||' angajati'); 
  END LOOP; 
END; 
/

--7
DECLARE 
  top number(1):= 0;  
BEGIN 
  FOR i IN (SELECT   sef.employee_id cod, MAX(sef.last_name) nume,  
                     count(*) nr 
            FROM     employees sef, employees ang 
            WHERE    ang.manager_id = sef.employee_id 
            GROUP BY sef.employee_id 
            ORDER BY nr DESC)  
  LOOP 
      DBMS_OUTPUT.PUT_LINE('Managerul '|| i.cod ||  
                           ' avand numele ' || i.nume ||  
                           ' conduce '|| i.nr||' angajati'); 
      Top := top+1; 
      EXIT WHEN top=3; 
  END LOOP; 
END; 
/

--8
DECLARE 
  v_x     number(4) := &p_x; 
  v_nr    number(4); 
  v_nume  departments.department_name%TYPE;
  CURSOR c (paramentru NUMBER) IS 
    SELECT department_name nume, COUNT(employee_id) nr   
    FROM   departments d, employees e 
    WHERE  d.department_id=e.department_id 
    GROUP BY department_name 
    HAVING COUNT(employee_id)> paramentru;  
BEGIN 
  OPEN c(v_x); 
  LOOP 
      FETCH c INTO v_nume,v_nr; 
      EXIT WHEN c%NOTFOUND; 
      DBMS_OUTPUT.PUT_LINE('In departamentul '|| v_nume|| 
                           ' lucreaza '|| v_nr||' angajati'); 
 END LOOP;  CLOSE c; 
END; 
/ 
 
DECLARE 
 v_x     number(4) := &p_x; 
 CURSOR c (paramentru NUMBER) IS 
    SELECT department_name nume, COUNT(employee_id) nr  
    FROM   departments d, employees e 
    WHERE  d.department_id=e.department_id 
    GROUP BY department_name 
    HAVING COUNT(employee_id)> paramentru;  
BEGIN 
  FOR i in c(v_x) LOOP 
     DBMS_OUTPUT.PUT_LINE('In departamentul '|| i.nume|| 
                           ' lucreaza '|| i.nr||' angajati'); 
  END LOOP; END; 
/ 
 
DECLARE 
 v_x     number(4) := &p_x; 
 BEGIN 
  FOR i in (SELECT department_name nume, COUNT(employee_id) nr  
            FROM   departments d, employees e 
            WHERE  d.department_id=e.department_id 
            GROUP BY department_name  
            HAVING COUNT(employee_id)> v_x)  
  LOOP 
     DBMS_OUTPUT.PUT_LINE('In departamentul '|| i.nume|| 
                           ' lucreaza '|| i.nr||' angajati'); 
END LOOP; END; 
/

--9
SELECT last_name, hire_date, salary 
FROM   emp_233_at 
WHERE  TO_CHAR(hire_date, 'yyyy') = 2000; 
 
DECLARE 
  CURSOR c IS 
    SELECT * 
    FROM   emp_233_at 
    WHERE  TO_CHAR(hire_date, 'YYYY') = 2000 
    FOR UPDATE OF salary NOWAIT; 
BEGIN 
  FOR i IN c  LOOP 
    UPDATE  emp_233_at 
    SET     salary= salary+1000 
    WHERE CURRENT OF c; 
  END LOOP; 
END; 
/ 
 
SELECT last_name, hire_date, salary 
FROM   emp_233_at 
WHERE  TO_CHAR(hire_date, 'yyyy') = 2000; 
 
ROLLBACK;

--10
--v1
BEGIN 
  FOR v_dept IN (SELECT department_id, department_name 
                 FROM   departments 
                 WHERE department_id IN (10,20,30,40)) 
  LOOP 
    DBMS_OUTPUT.PUT_LINE('-------------------------------------'); 
    DBMS_OUTPUT.PUT_LINE ('DEPARTAMENT '||v_dept.department_name); 
    DBMS_OUTPUT.PUT_LINE('-------------------------------------'); 
    FOR v_emp IN (SELECT last_name 
                  FROM    employees 
                  WHERE  department_id = v_dept.department_id) 
    LOOP 
       DBMS_OUTPUT.PUT_LINE (v_emp.last_name); 
    END LOOP; 
  END LOOP; 
END; 
/
--v2
DECLARE 
  TYPE refcursor IS REF CURSOR; 
  CURSOR c_dept IS 
    SELECT department_name,  
           CURSOR (SELECT last_name  
                   FROM   employees e 
                   WHERE  e.department_id = d.department_id) 
    FROM   departments d 
    WHERE  department_id IN (10,20,30,40); 
  v_nume_dept   departments.department_name%TYPE; 
  v_cursor      refcursor; 
  v_nume_emp    employees.last_name%TYPE; 
BEGIN 
  OPEN c_dept; 
  LOOP 
    FETCH c_dept INTO v_nume_dept, v_cursor; 
    EXIT WHEN c_dept%NOTFOUND; 
    DBMS_OUTPUT.PUT_LINE('-------------------------------------'); 
    DBMS_OUTPUT.PUT_LINE ('DEPARTAMENT '||v_nume_dept); 
    DBMS_OUTPUT.PUT_LINE('-------------------------------------'); 
    LOOP 
      FETCH v_cursor INTO v_nume_emp; 
      EXIT WHEN v_cursor%NOTFOUND; 
      DBMS_OUTPUT.PUT_LINE (v_nume_emp); 
    END LOOP; 
  END LOOP; 
  CLOSE c_dept; 
END; 
/

--11
DECLARE 
  TYPE      emp_tip IS REF CURSOR RETURN employees%ROWTYPE; 
  -- sau  
  -- TYPE   emp_tip IS REF CURSOR; 
   
  v_emp     emp_tip; 
  v_optiune NUMBER := &p_optiune; 
  v_ang    employees%ROWTYPE; 
BEGIN 
   IF v_optiune = 1 THEN 
     OPEN v_emp FOR SELECT *  
                    FROM employees; 
   ELSIF v_optiune = 2 THEN 
     OPEN v_emp FOR  SELECT *  
                     FROM employees  
                     WHERE salary BETWEEN 10000 AND 20000; 
   ELSIF v_optiune = 3 THEN 
     OPEN v_emp FOR SELECT *  
                    FROM employees  
                    WHERE TO_CHAR(hire_date, 'YYYY') = 2000; 
   ELSE 
      DBMS_OUTPUT.PUT_LINE('Optiune incorecta');   
   END IF; 
    
   LOOP 
      FETCH v_emp into v_ang; 
      EXIT WHEN v_emp%NOTFOUND; 
      DBMS_OUTPUT.PUT_LINE(v_ang.last_name); 
   END LOOP; 
    
   DBMS_OUTPUT.PUT_LINE('Au fost procesate '||v_emp%ROWCOUNT  
                        || ' linii'); 
   CLOSE v_emp; 
END; 
/

--12
DECLARE 
  TYPE  empref IS REF CURSOR;  
  v_emp empref; 
  v_nr  INTEGER := &n; 
BEGIN 
  OPEN v_emp FOR  
    'SELECT employee_id, salary, commission_pct ' || 
    'FROM employees WHERE salary > :bind_var' 
     USING v_nr;  -- introduceti liniile corespunzatoare rezolvarii problemei 
END; 
/


--06.11.2024


set serveroutput on

--lab pl/sql 1

--10
create table zile_233_at (
    id int,
    data date,
    nume_zi varchar2(20)
);

DECLARE 
  contor  NUMBER(6) := 1; 
  v_data  DATE; 
  maxim   NUMBER(2) := LAST_DAY(SYSDATE)-SYSDATE; 
BEGIN 
  LOOP 
    v_data := sysdate+contor; 
    INSERT INTO zile_233_at 
    VALUES (contor,v_data,to_char(v_data,'Day')); 
    contor := contor + 1; 
    EXIT WHEN contor > maxim; 
  END LOOP; 
END; 
/ 

desc zile_233_at;

select * from zile_233_at;

rollback;

--bonus

declare
    cursor zile_cursor is
        select data
        from zile_233_at;
    contor number := 0;
begin
    for zi in zile_cursor loop
        contor := contor + 1;
        if mod(to_number(to_char(zi.data, 'DD')), 2) = 0 then
            dbms_output.put_line(to_char(zi.data, 'DD-MON-YY') || ' are loc ' || to_char(zi.data, 'fmDay')); -- Use 'fmDay' to remove padding
        end if;
    end loop;
end;
/

--13

--v1
declare
    i        positive := 1;
    max_loop constant positive := 10;
begin
    loop
        i := i + 1;
        if i > max_loop then
            dbms_output.put_line('in loop i=' || i);
            goto urmator;
        end if;
    end loop;
    <<urmator>>
    i := 1;
    dbms_output.put_line('dupa loop i=' || i);
end;
/

--v2
DECLARE 
  i        POSITIVE:=1; 
  max_loop CONSTANT POSITIVE:=10; 
BEGIN 
  i:=1; 
  LOOP 
    i:=i+1; 
    DBMS_OUTPUT.PUT_LINE('in loop i=' || i); 
    EXIT WHEN i>max_loop; 
  END LOOP; 
  i:=1; 
  DBMS_OUTPUT.PUT_LINE('dupa loop i=' || i); 
END; 
/

--lab pl/sql 2

--10

CREATE TABLE emp_test_233_at AS  
      SELECT employee_id, last_name FROM employees 
      WHERE ROWNUM <= 2; 
 
CREATE OR REPLACE TYPE tip_telefon_233_at IS TABLE OF VARCHAR(12); 
/ 
 
ALTER TABLE emp_test_233_at 
ADD (telefon tip_telefon_233_at)  
NESTED TABLE telefon STORE AS tabel_telefon_233_at; 
 
INSERT INTO emp_test_233_at  
VALUES (500, 'XYZ',tip_telefon_233_at('074XXX', '0213XXX', '037XXX')); 
 
UPDATE emp_test_233_at 
SET    telefon = tip_telefon_233_at('073XXX', '0214XXX') 
WHERE  employee_id=100; 
 
SELECT  a.employee_id, b.* 
FROM    emp_test_233_at a, TABLE (a.telefon) b; 
 
DROP TABLE emp_test_233_at; 
DROP TYPE  tip_telefon_233_at;

--11

--v1
DECLARE 
  TYPE tip_cod IS VARRAY(5) OF NUMBER(3); 
  coduri tip_cod := tip_cod(205,206);  
BEGIN 
  FOR i IN coduri.FIRST..coduri.LAST  LOOP 
    DELETE FROM emp_233_at 
    WHERE  employee_id = coduri (i); 
  END LOOP; 
END;  
/ 
SELECT employee_id FROM emp_233_at; 
ROLLBACK;

--v2
DECLARE 
  TYPE tip_cod IS VARRAY(20) OF NUMBER; 
  coduri tip_cod := tip_cod(205,206); 
BEGIN 
  FORALL i IN coduri.FIRST..coduri.LAST 
    DELETE FROM emp_233_at 
    WHERE  employee_id = coduri (i); 
END; 
/ 
SELECT employee_id FROM emp_233_at; 
ROLLBACK;

--e2

create or replace type tip_orase_233_at is table of varchar2(50);
/
create table excursie_233_at (
    cod_excursie number(4)
    denumire varchar2(20)
    orase tip_orase_233_at
    status varchar2(20)
)nested table orase store as tabel_orase_233_at;


--04.12.2024


set serveroutput on

rollback;

--ex1
CREATE OR REPLACE PACKAGE pachet1_233_at AS 
   FUNCTION  f_numar(v_dept departments.department_id%TYPE)  
        RETURN NUMBER; 
   FUNCTION  f_suma(v_dept departments.department_id%TYPE)  
        RETURN NUMBER; 
END pachet1_233_at; 
/ 

CREATE OR REPLACE PACKAGE BODY pachet1_233_at AS 
   FUNCTION  f_numar(v_dept  departments.department_id%TYPE)  
      RETURN NUMBER IS numar NUMBER; 
   BEGIN 
      SELECT COUNT(*)INTO numar 
      FROM   employees 
      WHERE  department_id =v_dept; 
   RETURN numar; 
   END f_numar;
      FUNCTION  f_suma (v_dept  departments.department_id%TYPE)  
      RETURN NUMBER IS 
      suma NUMBER; 
   BEGIN 
      SELECT SUM(salary+salary*NVL(commission_pct,0)) 
      INTO suma 
      FROM employees 
      WHERE department_id =v_dept; 
   RETURN suma; 
   END f_suma; 
END pachet1_233_at; 
/


SELECT pachet1_233_at.f_numar(80) 
FROM DUAL; 
SELECT pachet1_233_at.f_suma(80) 
FROM DUAL;


BEGIN 
  DBMS_OUTPUT.PUT_LINE('numarul de salariati este '|| 
                        pachet1_233_at.f_numar(80)); 
  DBMS_OUTPUT.PUT_LINE('suma alocata este '|| 
                        pachet1_233_at.f_suma(80)); 
END; 
/

--ex2
create table dept_233_at as select * from departments;

create table emp_233_at as select * from employees;

create sequence sec_233_at
start with 1
increment by 1;


CREATE OR REPLACE PACKAGE pachet2_233_at AS 
   PROCEDURE p_dept (v_codd dept_233_at.department_id%TYPE, 
                     v_nume dept_233_at.department_name%TYPE, 
                     v_manager dept_233_at.manager_id%TYPE, 
                     v_loc dept_233_at.location_id%TYPE); 
   PROCEDURE p_emp (v_first_name emp_233_at.first_name%TYPE, 
                 v_last_name emp_233_at.last_name%TYPE, 
                 v_email emp_233_at.email%TYPE, 
                 v_phone_number emp_233_at.phone_number%TYPE:=NULL,  
                 v_hire_date emp_233_at.hire_date%TYPE :=SYSDATE,      
                 v_job_id emp_233_at.job_id%TYPE,         
                 v_salary   emp_233_at.salary%TYPE :=0,       
                 v_commission_pct emp_233_at.commission_pct%TYPE:=0, 
                 v_manager_id emp_233_at.manager_id%TYPE,    
                 v_department_id emp_233_at.department_id%TYPE); 
  FUNCTION exista (cod_loc dept_233_at.location_id%TYPE,  
                   manager dept_233_at.manager_id%TYPE)  
  RETURN NUMBER; 
END pachet2_233_at; 
/
 
CREATE OR REPLACE PACKAGE BODY pachet2_233_at AS 
 
FUNCTION exista(cod_loc dept_233_at.location_id%TYPE,  
                manager dept_233_at.manager_id%TYPE) 
 RETURN NUMBER  IS  
      rezultat NUMBER:=1; 
      rez_cod_loc NUMBER; 
      rez_manager NUMBER; 
 BEGIN 
    SELECT count(*) INTO   rez_cod_loc 
    FROM   locations 
    WHERE  location_id = cod_loc; 
     
    SELECT count(*) INTO   rez_manager 
    FROM   emp_233_at 
    WHERE  employee_id = manager; 
     
    IF rez_cod_loc=0 OR rez_manager=0 THEN  
         rezultat:=0;      
    END IF; 
RETURN rezultat; 
END; 
 
PROCEDURE p_dept(v_codd dept_233_at.department_id%TYPE, 
                 v_nume dept_233_at.department_name%TYPE, 
                 v_manager dept_233_at.manager_id%TYPE, 
                 v_loc dept_233_at. location_id%TYPE) IS 
BEGIN 
   IF exista(v_loc, v_manager)=0 THEN  
       DBMS_OUTPUT.PUT_LINE('Nu s-au introdus date coerente pentru 
tabelul dept_233_at'); 
   ELSE 
     INSERT INTO dept_233_at 
          (department_id,department_name,manager_id,location_id) 
     VALUES (v_codd, v_nume, v_manager, v_loc); 
   END IF; 
 END p_dept; 
 
PROCEDURE p_emp 
(v_first_name emp_233_at.first_name%TYPE, 
 v_last_name emp_233_at.last_name%TYPE, 
 v_email emp_233_at.email%TYPE, 
 v_phone_number emp_233_at.phone_number%TYPE:=null,  
 v_hire_date emp_233_at.hire_date%TYPE :=SYSDATE,      
 v_job_id emp_233_at.job_id%TYPE,         
 v_salary emp_233_at.salary %TYPE :=0,
 v_commission_pct emp_233_at.commission_pct%TYPE:=0, 
 v_manager_id emp_233_at.manager_id%TYPE,    
 v_department_id  emp_233_at.department_id%TYPE) 
AS 
 BEGIN 
     INSERT INTO emp_233_at 
     VALUES (sec_233_at.NEXTVAL, v_first_name, v_last_name, v_email, 
            v_phone_number,v_hire_date, v_job_id, v_salary, 
            v_commission_pct, v_manager_id,v_department_id); 
END p_emp; 
END pachet2_233_at; 
/


EXECUTE pachet2_233_at.p_dept(50,'Economic',200,2000); 
 
SELECT * FROM dept_233_at WHERE department_id=50; 
 
EXECUTE pachet2_233_at.p_emp('f','l','e',v_job_id=>'j', 
                          v_manager_id=>200,v_department_id=>50); 
 
SELECT * FROM emp_233_at WHERE job_id='j'; 
 
ROLLBACK;


BEGIN 
   pachet2_233_at.p_dept(50,'Economic',99,2000); 
   pachet2_233_at.p_emp('f','l','e',v_job_id=>'j',v_manager_id=>200, 
                     v_department_id=>50); 
END; 
/ 
 
SELECT * FROM emp_233_at WHERE job_id='j'; 
ROLLBACK;

--ex3

CREATE  OR REPLACE PACKAGE pachet3_233_at AS 
   CURSOR c_emp(nr NUMBER) RETURN employees%ROWTYPE;  
   FUNCTION  f_max  (v_oras  locations.city%TYPE) RETURN NUMBER; 
END pachet3_233_at; 
/ 
 
CREATE OR REPLACE PACKAGE BODY pachet3_233_at AS 
 
CURSOR c_emp(nr NUMBER) RETURN employees%ROWTYPE   
      IS 
      SELECT *  
      FROM employees  
      WHERE salary >= nr;  
 
FUNCTION  f_max (v_oras  locations.city%TYPE) RETURN NUMBER  IS 
      maxim  NUMBER; 
BEGIN 
     SELECT  MAX(salary)  
     INTO    maxim   
     FROM    employees e, departments d, locations l 
     WHERE   e.department_id=d.department_id  
             AND d.location_id=l.location_id  
             AND UPPER(city)=UPPER(v_oras); 
    RETURN  maxim; 
END f_max; 
END pachet3_233_at; 
/ 
 
DECLARE 
  oras    locations.city%TYPE:= 'Toronto'; 
  val_max NUMBER; 
  lista   employees%ROWTYPE; 
BEGIN 
   val_max:=  pachet3_233_at.f_max(oras); 
   FOR v_cursor IN pachet3_233_at.c_emp(val_max) LOOP 
      DBMS_OUTPUT.PUT_LINE(v_cursor.last_name||' '|| 
                           v_cursor.salary);    
   END LOOP; 
END; 
/


--ex4
CREATE OR REPLACE  PACKAGE pachet4_233_at IS 
  PROCEDURE p_verific  
      (v_cod employees.employee_id%TYPE, 
       v_job   employees.job_id%TYPE); 
  CURSOR c_emp RETURN employees%ROWTYPE;   
END pachet4_233_at; 
/ 
 
CREATE OR REPLACE PACKAGE BODY pachet4_233_at IS 
 
CURSOR c_emp  RETURN employees%ROWTYPE  IS 
       SELECT * 
       FROM   employees; 
 
PROCEDURE p_verific(v_cod   employees.employee_id%TYPE, 
                    v_job   employees.job_id%TYPE) 
IS 
  gasit BOOLEAN:=FALSE; 
  lista employees%ROWTYPE; 
BEGIN 
  OPEN c_emp; 
  LOOP 
    FETCH c_emp INTO lista; 
    EXIT WHEN c_emp%NOTFOUND; 
    IF lista.employee_id=v_cod  AND lista.job_id=v_job    
       THEN  gasit:=TRUE; 
    END IF; 
  END LOOP; 
  CLOSE c_emp; 
  IF gasit=TRUE THEN  
     DBMS_OUTPUT.PUT_LINE('combinatia data exista'); 
  ELSE   
     DBMS_OUTPUT.PUT_LINE('combinatia data nu exista'); 
  END IF; 
END p_verific; 
END pachet4_233_at; 
/ 
    
EXECUTE pachet4_233_at.p_verific(200,'AD_ASST');

--tema 8

set serveroutput on

--tema 9





