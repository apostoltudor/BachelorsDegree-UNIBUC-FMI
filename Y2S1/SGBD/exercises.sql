select table_name 
from user_tables;


select p.data_ora from programari p
join programari_servicii ps on p.id_programare = ps.id_programare
join servicii s on s.id_serviciu = ps.id_serviciu
where s.id_serviciu = 2;

set serveroutput on;

declare
    mesaj varchar2(100) := 'Invat pl/sql';
begin
    dbms_output.put_line(mesaj);
end;
/

desc departments;
desc employees;


declare
    nume_dep departments.department_name %type;
begin
    select department_name
    into nume_dep
    from employees e, departments d
    where e.department_id=d.department_id
    group by department_name
    having count(*)=(select max(count(*))
                    from employees
                    group by department_id);
    dbms_output.put_line('departmaenteul '||nume_dep);
end;
/

declare
    vcod employees.employee_id%type := &cod_angajat;
    vsalariu employees.salary%type;
    vbonus employees.salary%type;
begin
    select salary*12 into vsalariu
    from employees
    where employee_id = vcod;
    if vsalariu >= 200001
        then vbonus := 20000;
    elsif vsalariu >= 100001
        then vbonus := 10000;
    else vbonus := 5000;
    end if;
    dbms_output.put_line('salariul este '||vsalariu);
    dbms_output.put_line('bonusul este '||vbonus);
end;
/


--TALENT CU RECORD!!!!
declare
    v_ang1 employees%rowtype;
    v_ang2 employees%rowtype;
begin
    delete from emp_***
    where employee_id = 100
    returning * into v_ang1;
    --inserez in tabel linia abia stearsa
    insert into emp_***
    values v_ang1;
    --sterg anagajatul 101
    delete from emp_***
    where employee_id=101;
    --iau datele din empleoyees
    select * into v_ang2
    from employees
    where employee_id=101;
    --inserez in emp_*** o linie oarecare
    insert into emp_***
    values (1000, 'FN', 'LN', 'E', null, sysdate, 'AD_VP', 1000, null, 100, 90);
    --modific linia adaugata cu valorile variabilei v_ang2
    update emp_***
    set row = v_ang2
    where employee_id = 1000;
end;
/

