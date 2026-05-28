--28.02.24


select *
from employees
where employee_id=107;

describe departments;

select employee_id, first_name || ' ' || last_name "Numele complet", job_id, hire_date, salary*12"ANNUAL SALARY"
from employees;

describe jobs;
desc employees;

select employee_id, salary sal     --ordinea e mereu: from --> where --> select --> order by,   select e mreu penultimul si order by ultimul
from employees
where salary>10000
and employee_id <150
order by sal desc;   --"order by 2 desc"; 2 fiind a 2-a coloana (salary), daca era 1, era dupa prima coloana (employee_id)

select 1+2
from dual;     --dual e tabel de tip dummy

select to_char(sysdate, 'DAY/MONTH/YEAR')
from dual;

alter session set nls_language=Romanian;

select employee_id,to_char(hire_date, 'Month'), to_char(Hire_Date, 'MONTH'), commission_pct 
from employees
order by commission_pct desc;

alter session set nls_language=American;

describe employees

select employee_id,to_char(hire_date, 'Month') "Luna", to_char(Hire_Date, 'MONTH') "LUNA", nvl(commission_pct, 0) "Comision"
from employees
order by 4 desc;


--06.03.24


select last_name, first_name
from employees
where last_name like 'A%' or first_name like 'A%';

select last_name, first_name
from employees
where last_name like '__A%';

select last_name, first_name
from employees
where lower(last_name) like '__a%';   --nu mai e case sensitive

select last_name, first_name
from employees
where upper(last_name) like '__A%';    --lfl ca mai sus

select last_name, first_name, department_id, manager_id
from employees
where (upper(last_name) like '%L%L%') and (department_id=30 or manager_id=102);    --and-ul leaga mai rapid decat or (se folosesc paranteze pentru exprimare)

select last_name, first_name, job_id, salary
from employees
where (lower(job_id) like '%clerk%' or lower(job_id) like '%rep%') and (salary not in (3200, 2700, 2500, 3100, 6200));

select first_name ||' '|| last_name ||' castiga '|| salary ||' lunar dar doreste '|| salary*3 "Salariu ideal"
from employees;

select initcap(first_name) "PRENUME", upper(last_name) "NUME", lenght(last_name) "LUNGIME NUME"
from employees
where last_name like 'J%' or last_name like 'M%' or substr(last_name, 3,3)='A';
order by lenght(last_name) desc;


--13.03.24


select last_name, first_name, nvl2(to_char(manager_id),'Are manager','Nu are manager')
from employees;

select e.*, d.*
from employees e, departments d;

select e.*, d.*
from employees e join departments d on e.department_id=d.department_id;

select e.last_name ||' '|| e.first_name, d.department_name, e.department_id
from employees e join departments d on e.department_id=d.department_id;

select j.*, l.*, c.*
from jobs j, location l, countries c;

select e.last_name||' '|| e.first_name||' '||j.job_title
from jobs j join employees e on e.job_id=j.job_id 
join departaments d on e.department_id=d.department_id 
join locations l on d.location_id =l.location_id 
join countries c on l.country_id=c.country_id 
where e.manager_id=100;

select e.last_name||' '|| e.first_name||' '||j.job_title
from jobs j join employees e using(job_id) 
join departaments d using(department_id) 
join locations l using(location_id) 
join countries c using(country_id) 
where e.manager_id=100;

select j.job_title, e.salary, j.max_salary
from jobs j, employees e
where j.max_salary<e.salary
and e.employee_id=100;

select *
from jobs
where max_salary<(select salary from employees where employee_id=100);

select first_name, hire_date
from employees
where hire_date>(select hire_date from employees where last_name='Gates');

select first_name
from employees e
where department_id in (select distinct..);

describe employees;


--20.03.24


select employee_id, last_name, e.department_id, department_name
from employees e, departments d
where e.department_id=d.department_id;

--select e.employee_id, e.last_name, e.department_id, e.department_name
--from employees e join department d on (e.department_id = d.department_id)

select employee_id, last_name, e.department_id, department_name
from employees e, departments d
where e.department_id(+)=d.department_id;  --dep fara angajati

--UNION all uneste ambele, cu tot cu duplicate

select employee_id, last_name, e.department_id, department_name
from employees e, departments d
where e.department_id=d.department_id(+);  --angajati fara dep

select employee_id, last_name, e.department_id, department_name
from employees e full outer join departments d on (e.department_id = d.department_id);

select c.country_id, d.location_id, e.department_id, employee_id
from employees e, departments d, countries c, locations l
where l.country_id(+)=c.country_id
and d.location_id(+)=l.location_id
and e.department_id(+)=d.department_id;

select l.city, d.department_name, dep
from locations l, departments d
where l.location_id(+)=d.location_id
order by dep desc;

select d.department_id
from departments d
where lower(d.department_name) like '%re%'
union
select e.department_id
from employees e
where upper(e.job_id) like '%SA_REP%'
and department_id is not null;

select d.department_id
from departments d
minus
select e.department_id
from employees e;

select last_name, salary
from employees
where department_id=any
(select department_id      --subcereri
from employees             --subcereri
where last_name='King')    --subcereri
and last_name != 'King';   --subcereri


--10.04.24


SELECT last_name, department_id, salary
FROM employees
WHERE (department_id, salary) IN 
(
SELECT department_id, salary 
FROM employees 
WHERE commission_pct IS NOT NULL
);

-- Ex 8: S? se afi?eze numele, departamentul, salariul ?i job-ul tuturor angaja?ilor al c?ror 
--salariu ?i comision coincid cu salariul ?i comisionul unui angajat din Oxford.

Select last_name, department_id, salary, job_id
From employees
where (salary, commission_pct) in
(select salary, commission_pct
from employees e, departments d, locations l
where l.location_id = d.location_id
and d.department_id = e.department_id
and l.city like 'Oxford');

-- Ex 7) Scrie?i o cerere pentru a afi?a numele, numele departamentului ?i salariul angaja?ilor 
-- care nu câ?tig? comision, dar al c?ror ?ef direct câ?tig? comision.

select e.last_name, e.department_id, e.salary 
from employees e, departments d
where e.department_id = d.department_id
and e.commission_pct is not null
and e.manager_id in (select employee_id
from employees 
where commission_pct is not null);

select min(salary)
from employees; --afiseaza doar salariul minim, nu si cati employees au salariul minim

select e.last_name, e.department_id, e.salary
from employees e
where e.salary = (select min(salary) from employees);


--17.04.24


select employee_id, last_name, department_id, salary
from employees
where (department_id, salary) in (select department_id, max(salary)
                                from employees
                                group by department_id)
order by department_id;

select e.employee_id, e.last_name, e.department_id, e.salary
from employees e
where e.salary=(select max(salary)
                from employees b
                where b.department_id=e.department_id)
order by department_id;

select count(*)
from employees;

select count(employee_id)
from employees;

select count(department_id)
from employees; --arata cu unul mai putin deoarece managerul nu are departament

select department_id, count(employee_id)
from employees
group by department_id;

select avg(commission_pct)
from employees;

select medie as sum(commission_pct)/count(employee_id)
from employees;   --gresit

select max(salary) MAXIM, min(salary) MINIM, sum(salary) TOTAL, round(avg(salary)) MEDIE,
        floor(avg(salary)) med, avg(salary), round(avg(salary),2)
from employees;

select j.job_id, job_title, min(salary) MINIM, max(salary) MAXIM, sum(salary) TOTAL, round(avg(salary)),
    count (employee_id) NR_ANG
from employees e, jobs j
where e.job_id = j.job_id
group by j.job_id, job_title;

select max(numar)
from (select job_id, count(*) NUMAR
     from employees
      group by job_id) JOBURI;
      
select job_id, max(count(*)) numar_maxim  --la super-agregari nu pot afisa alta coloana
from employees
group by job_id;    --gresit

select max(count(*)) numar_maxim
from employees
group by job_id;

select e.job_id, job_title, count(*) numar
from employees e, jobs j
where e.job_id = j.job_id
group by e.job_id, job_title
having count(*) = (select max(count(*)) numar_maxim
                    from employees
                    group by job_id);
           
select *
from employees
where job_id in
                (select e.job_id
                from employees e
                group by e.job_id
                having count(*) = (select max(count(*)) numar_maxim
                       from employees
                       group by job_id)
                );
                
select employee_id, manager_id
from employees;

select distinct manager_id
from employees
where manager_id is not null
order by 1;

select *
from employees
where employee_id in (select manager_id 
                        from employees);
                        
select count(distinct manager_id)
from employees;

select count(distinct manager_id)
from employees
where manager_id is not null;

select max(salary)-min(salary) DIFERENTA, department_id DEPT_ID, count(*) NR_ANG_DIN_DEPT
from employees
group by department_id;

select d.department_name NUME_DEP, l.city LOCATIE, count(e.employee_id) NR_ANG, round(avg(e.salary)) SALARIU_MEDIU
from employees e
join departments d on e.department_id = d.department_id
join locations l on l.location_id =  d.location_id
group by d.department_name, l.city;


--24.04.24


select e.department_id, round(avg(e.salary))
from employees e
group by e.department_id;

select max(roung(avg(salary)))
from employees e
group by e.department_id;

select d.department_id, d.department_name, round(avg(e.salary)), min(e.salary)
from employees e, departments d
where e.department_id=d.department_id
group by d.department_id, d.department_id
having avg(e.salary)= (select max(avg(salary))
                        from employees e
                        group by e.department_id);
                        

with
aux as (select d.department_id, d.department_name, round(avg(e.salary)) media
        from employees e, departments d
        where e.department_id=d.department_id
        group  by d.department_id, d.department_name)
select max(media) maxim
from aux;

with
aux as (select d.department_id, d.department_name, round(avg(e.salary)) media
        from employees e, departments d
        where e.department_id=d.department_id
        group  by d.department_id, d.department_name),
tab_maximul as (
                select max(media) col_maxim
                from aux)
select *
from aux
where media = (select col_maxim from tab_maximul);

select *
from employees
where department_id in (select d.department_id
                        from employees e, departments d
                        where e.department_id=d.department_id
                        group by d.department_id, d.department_name
                        having round(avg(e.salary)) = (select max(round(avg(salary)))
                                                        from employees e, departments d
                                                        where e.department_id=d.department_id
                                                        group by e.department_id));

select d.department_id , d.department_name, count(e.employee_id)
from employees e
join departments d on e.department_id = d.department_id
group by d.department_id, d.department_name
having count(e.employee_id)<4;

select d.department_id , d.department_name, count(e.employee_id)
from employees e
join departments d on e.department_id = d.department_id
group by d.department_id, d.department_name
having count(e.employee_id) = (select max(count(e.employee_id))
                                from employees e
                                group by department_id);
              
select count(*)
from (
select d.department_id , d.department_name, count(e.employee_id)
from employees e
join departments d on e.department_id = d.department_id
group by d.department_id, d.department_name
having count(e.employee_id)<4);

--v1
select job_id, nvl(sum(decode(department_id, 30, salary)), 0) Dep30,
nvl(sum(decode(department_id, 50, salary)), 0) Dep50,
nvl(sum(decode(department_id, 80, salary)), 0) Dep80,
nvl(sum(salary), 0) Total
from employees
group by job_id
order by 1;

select count(employee_id) TOTAL
sum(decode(to_char(hire_date,'yyyy'), 1997, 1, 0)) "AN 1997",
sum(decode(to_char(hire_date,'yyyy'), 1998, 1, 0)) "AN 1998",
sum(decode(to_char(hire_date,'yyyy'), 1999, 1, 0)) "AN 1999",
sum(decode(to_char(hire_date,'yyyy'), 2000, 1, 0)) "AN 2000"
from employees;


--15.05.24


SELECT last_name, salary, aux.department_id, aux.department_name, round(aux.media), numar
FROM employees e, (select dd.department_name, avg(salary) as media, count(*) as numar
                    from departments dd, employees ee
                    join employees ee on dd.department_id=ee.department_id
                    where dd.department_id=ee.department_id
                    group by dd.department_name, dd.department_id) as aux
WHERE salary > (SELECT AVG(salary)
FROM employees
WHERE department_id = e.department_id)
AND e.department_id=aux.department_id;

SELECT last_name, salary, department_id,
        (SELECT round(avg(salary))
        from employees
        where department_id = e.department_id) Media,
        (select department_name
        from departments
        where department_id = e.department_id) nr_ang
from employees e
where salary > (select avg(salary)
                from employees
                where department_id = e.department_id)
order by media desc;

select d.department_name, e.last_name
from departments d, employees e
where e.department_id = d.department_id
and e.hire_date = (select min(f.hire_date)
                    from employees f
                    where f.department_id = e.department_id)
order by d.department_name ASC;

with emp_min_hd as(select min(e2.hire_date) as data_ang, e2.department_id
        from employees e2
        group by department_id)
select d.department_name, e.last_name
from employees e, emp_min_hd aux, departments d
where aux.department_id = e.department_id
and e.department_id = d.department_id;

select l.location_id, l.city
from locations l
where exists(select 'x'
            from departments d
            where d.location_id = l.location_id);
            
select d.department_id, d.department_name
from departments d
where not exists(select 'x'
            from employees e
            where d.department_id = e.department_id);
            
with subordonati as(select e.last_name
                    from employees e
                    where e.manager_id = (select e2.employee_id
                                            from employees e2
                                             where e2.first_name = 'Steven'
                                             and e2.last_name = 'King'))
with vechime as (select min(hire_date) as maxim
                    from subordonati)
select *
from subordonati
where hire_date = (select maxim from vechime)
;


--22.05.24


select sum(salary) as SUMA
from employees
where job_id like 'S%';

select avg(e.salary), e.department_id
from employees e, departments
where e.department_id = (select d.department_id
                        from employees d
                        where d.salary=max(salary));
                        
select job_id, avg(salary) as avg_salary
from employees
group by job_id
order by avg_salary asc
fetch first 14 rows only;

with sal_14 as (select *
                from (select avg(salary) medie
                        from employees
                        group by job_id
                        order by medie asc
                    )
                where rownum <=14),
joburi as (select job_id, avg(salary)
            from employees
            group by job_id
            having avg(salary) in (select medie from sal_14)
            order by avg(salary))
select *
from employees
where job_id in (select job_id
                    from joburi);

--I

select employee_id, last_name, salary, department_id
from employees
where employee_id = &p_cod;

--III

set verify on;

DEFINE p_cod;

select employee_id, last_name, salary, department_id
from employees
where employee_id = &p_cod;

UNDEFINE p_cod;

--III

DEFINE p_cod=100;
SELECT employee_id, last_name, salary, department_id
FROM employees
WHERE employee_id = &&p_cod;

UNDEFINE p_cod;

--IV

ACCEPT p_cod PROMPT “cod= “;

SELECT employee_id, last_name, salary, department_id
FROM employees
WHERE employee_id = &p_cod;


accept variabila prompt "Selectati id-ul unui angajat:";
select last_name as NUME, department_id as ID_DEPARTAMENT, salary*12 as SALARIU_ANUAL
from employees
where employee_id = &variabila;
undefine variabila;

select &p_coloana, department_id
from &p_tabel
where &p_where
order by &p_coloana;

accept oras prompt "Selectati locatia:";
select e.last_name, e.first_name, e.job_id, e.salary, d.department_name
from employees e
join departments d on d.department_id = e.department_id
join locations l on l.location_id = d.location_id
where upper(city) = upper('&oras');
undefine oras;