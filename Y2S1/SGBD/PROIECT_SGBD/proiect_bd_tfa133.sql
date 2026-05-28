CREATE SEQUENCE seq_departamente
START WITH 1
INCREMENT BY 1
NOCACHE;

CREATE SEQUENCE seq_functii
START WITH 1
INCREMENT BY 1
NOCACHE;

CREATE SEQUENCE seq_angajati
START WITH 1
INCREMENT BY 1
NOCACHE;

CREATE SEQUENCE seq_istoric_angajati
START WITH 1
INCREMENT BY 1
NOCACHE;

CREATE SEQUENCE seq_clienti
START WITH 1
INCREMENT BY 1
NOCACHE;

CREATE SEQUENCE seq_locatii
START WITH 1
INCREMENT BY 1
NOCACHE;

CREATE SEQUENCE seq_materiale
START WITH 1
INCREMENT BY 1
NOCACHE;

CREATE SEQUENCE seq_echipamente
START WITH 1
INCREMENT BY 1
NOCACHE;

CREATE SEQUENCE seq_tip_serviciu
START WITH 1
INCREMENT BY 1
NOCACHE;

CREATE SEQUENCE seq_servicii
START WITH 1
INCREMENT BY 1
NOCACHE;

CREATE SEQUENCE seq_programari
START WITH 1
INCREMENT BY 1
NOCACHE;



--DEPARTAMENTE

CREATE TABLE DEPARTAMENTE (
    id_departament INT PRIMARY KEY,
    nume_departament VARCHAR(50) NOT NULL,
    manager VARCHAR(100) NOT NULL
);

INSERT INTO DEPARTAMENTE (id_departament, nume_departament, manager) VALUES
(seq_departamente.NEXTVAL, 'Curatenie Rezidentiala', 'Zarzalin Marius');
INSERT INTO DEPARTAMENTE (id_departament, nume_departament, manager) VALUES
(seq_departamente.NEXTVAL, 'Curatenie Comerciala', 'Jelea Dana');
INSERT INTO DEPARTAMENTE (id_departament, nume_departament, manager) VALUES
(seq_departamente.NEXTVAL, 'Curatenie Industriala', 'Motan Andrei');
INSERT INTO DEPARTAMENTE (id_departament, nume_departament, manager) VALUES
(seq_departamente.NEXTVAL, 'Curatenie pentru Evenimente', 'Sandu Fanel');
INSERT INTO DEPARTAMENTE (id_departament, nume_departament, manager) VALUES
(seq_departamente.NEXTVAL, 'Curatenie dupa Constructii', 'Lupu George');
INSERT INTO DEPARTAMENTE (id_departament, nume_departament, manager) VALUES
(seq_departamente.NEXTVAL, 'Management', 'Apostol Tudor');

DESCRIBE DEPARTAMENTE;
SELECT * FROM DEPARTAMENTE;





--FUNCTII

CREATE TABLE FUNCTII (
    id_functie INT PRIMARY KEY,
    nume_functie VARCHAR(50) NOT NULL,
    id_departament INT NOT NULL,
    regim_lucru VARCHAR(50) NOT NULL,
    FOREIGN KEY (id_departament) REFERENCES DEPARTAMENTE(id_departament)
);

INSERT INTO FUNCTII (id_functie, nume_functie, id_departament, regim_lucru) VALUES
(seq_functii.NEXTVAL, 'Manager', 6, 'Full-time');
INSERT INTO FUNCTII (id_functie, nume_functie, id_departament, regim_lucru) VALUES
(seq_functii.NEXTVAL, 'Curatator de resedinte', 1, 'Part-time');
INSERT INTO FUNCTII (id_functie, nume_functie, id_departament, regim_lucru) VALUES
(seq_functii.NEXTVAL, 'Curatator pentru centre comerciale', 2, 'Full-time');
INSERT INTO FUNCTII (id_functie, nume_functie, id_departament, regim_lucru) VALUES
(seq_functii.NEXTVAL, 'Curatator pentru evenimente', 4, 'Part-time');
INSERT INTO FUNCTII (id_functie, nume_functie, id_departament, regim_lucru) VALUES
(seq_functii.NEXTVAL, 'Curatator dupa constructii', 5, 'Full-time');
INSERT INTO FUNCTII (id_functie, nume_functie, id_departament, regim_lucru) VALUES
(seq_functii.NEXTVAL, 'Curatator pentru industriale', 3, 'Full-time');

DESCRIBE FUNCTII;
SELECT * FROM FUNCTII;





--ANGAJATI

CREATE TABLE ANGAJATI (
    id_angajat INT PRIMARY KEY,
    nume VARCHAR(50) NOT NULL,
    prenume VARCHAR(50) NOT NULL,
    data_nastere DATE NOT NULL,
    id_functie INT NOT NULL,
    id_departament INT NOT NULL,
    salariu DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_functie) REFERENCES FUNCTII(id_functie),
    FOREIGN KEY (id_departament) REFERENCES DEPARTAMENTE(id_departament)
);

INSERT INTO ANGAJATI (id_angajat, nume, prenume, data_nastere, id_functie, id_departament, salariu) VALUES
(seq_angajati.NEXTVAL, 'Apostol', 'Tudor', '25-FEB-04', 1, 6, 10000.00);
INSERT INTO ANGAJATI (id_angajat, nume, prenume, data_nastere, id_functie, id_departament, salariu) VALUES
(seq_angajati.NEXTVAL, 'Zarzalin', 'Marius', '02-MAY-99', 1, 6, 4000.00);
INSERT INTO ANGAJATI (id_angajat, nume, prenume, data_nastere, id_functie, id_departament, salariu) VALUES
(seq_angajati.NEXTVAL, 'Jelea', 'Dana', '01-AUG-70', 1, 6, 6000.00);
INSERT INTO ANGAJATI (id_angajat, nume, prenume, data_nastere, id_functie, id_departament, salariu) VALUES
(seq_angajati.NEXTVAL, 'Motan', 'Andrei', '20-JAN-01', 1, 6, 5000.00);
INSERT INTO ANGAJATI (id_angajat, nume, prenume, data_nastere, id_functie, id_departament, salariu) VALUES
(seq_angajati.NEXTVAL, 'Sandu', 'Fanel', '31-DEC-80', 1, 6, 4000.00);
INSERT INTO ANGAJATI (id_angajat, nume, prenume, data_nastere, id_functie, id_departament, salariu) VALUES
(seq_angajati.NEXTVAL, 'Lupu', 'George', '03-OCT-03', 1, 6, 5500.00);
INSERT INTO ANGAJATI (id_angajat, nume, prenume, data_nastere, id_functie, id_departament, salariu) VALUES
(seq_angajati.NEXTVAL, 'Nita', 'Ionut', '05-JAN-04', 2, 1, 1800.00);
INSERT INTO ANGAJATI (id_angajat, nume, prenume, data_nastere, id_functie, id_departament, salariu) VALUES
(seq_angajati.NEXTVAL, 'Sandu', 'Emilian', '02-NOV-66', 3, 2, 3200.00);
INSERT INTO ANGAJATI (id_angajat, nume, prenume, data_nastere, id_functie, id_departament, salariu) VALUES
(seq_angajati.NEXTVAL, 'Petre', 'Adrian', '29-FEB-00', 4, 4, 2200.00);
INSERT INTO ANGAJATI (id_angajat, nume, prenume, data_nastere, id_functie, id_departament, salariu) VALUES
(seq_angajati.NEXTVAL, 'Ilie', 'Ana-Maria', '05-FEB-98', 5, 5, 3000.00);
INSERT INTO ANGAJATI (id_angajat, nume, prenume, data_nastere, id_functie, id_departament, salariu) VALUES
(seq_angajati.NEXTVAL, 'Necula', 'Claudia', '17-APR-2006', 6, 3, 2900.00);

DESCRIBE ANGAJATI;
SELECT * FROM ANGAJATI;







--ISTORIC_ANGAJATI

CREATE TABLE ISTORIC_ANGAJATI (
    id_istoric INT PRIMARY KEY,
    id_angajat INT NOT NULL,
    data_angajare DATE NOT NULL,
    data_plecare DATE,
    FOREIGN KEY (id_angajat) REFERENCES ANGAJATI(id_angajat)
);

INSERT INTO ISTORIC_ANGAJATI (id_istoric, id_angajat, data_angajare, data_plecare) VALUES
(seq_istoric_angajati.NEXTVAL, 1, '01-MAR-22', NULL);
INSERT INTO ISTORIC_ANGAJATI (id_istoric, id_angajat, data_angajare, data_plecare) VALUES
(seq_istoric_angajati.NEXTVAL, 2, '05-MAY-23', NULL);
INSERT INTO ISTORIC_ANGAJATI (id_istoric, id_angajat, data_angajare, data_plecare) VALUES
(seq_istoric_angajati.NEXTVAL, 3, '19-JUL-23', NULL);
INSERT INTO ISTORIC_ANGAJATI (id_istoric, id_angajat, data_angajare, data_plecare) VALUES
(seq_istoric_angajati.NEXTVAL, 4, '13-JUN-23', NULL);
INSERT INTO ISTORIC_ANGAJATI (id_istoric, id_angajat, data_angajare, data_plecare) VALUES
(seq_istoric_angajati.NEXTVAL, 5, '05-MAY-23', NULL);
INSERT INTO ISTORIC_ANGAJATI (id_istoric, id_angajat, data_angajare, data_plecare) VALUES
(seq_istoric_angajati.NEXTVAL, 6, '03-JUL-23', NULL);
INSERT INTO ISTORIC_ANGAJATI (id_istoric, id_angajat, data_angajare, data_plecare) VALUES
(seq_istoric_angajati.NEXTVAL, 7, '05-MAR-24', NULL);
INSERT INTO ISTORIC_ANGAJATI (id_istoric, id_angajat, data_angajare, data_plecare) VALUES
(seq_istoric_angajati.NEXTVAL, 8, '25-FEB-24', NULL);
INSERT INTO ISTORIC_ANGAJATI (id_istoric, id_angajat, data_angajare, data_plecare) VALUES
(seq_istoric_angajati.NEXTVAL, 9, '29-JAN-24', NULL);
INSERT INTO ISTORIC_ANGAJATI (id_istoric, id_angajat, data_angajare, data_plecare) VALUES
(seq_istoric_angajati.NEXTVAL, 10, '27-DEC-23', NULL);
INSERT INTO ISTORIC_ANGAJATI (id_istoric, id_angajat, data_angajare, data_plecare) VALUES
(seq_istoric_angajati.NEXTVAL, 11, '18-JAN-23', NULL);

DESCRIBE ISTORIC_ANGAJATI;
SELECT * FROM ISTORIC_ANGAJATI;







--CLIENTI

CREATE TABLE CLIENTI (
    id_client INT PRIMARY KEY,
    nume_client VARCHAR(100) NOT NULL,
    telefon VARCHAR(15) NOT NULL,
    email VARCHAR(100) NOT NULL
);

INSERT INTO CLIENTI (id_client, nume_client, telefon, email) VALUES
(seq_clienti.NEXTVAL, 'Maria Gabriela', '0790367926', 'maria.gabriela@gmail.com');
INSERT INTO CLIENTI (id_client, nume_client, telefon, email) VALUES
(seq_clienti.NEXTVAL, 'Kaufland Sud', '0706413686', 'kaufland.sud@yahoo.com');
INSERT INTO CLIENTI (id_client, nume_client, telefon, email) VALUES
(seq_clienti.NEXTVAL, 'Darius Events', '0755437962', 'dariusevents@gmail.com');
INSERT INTO CLIENTI (id_client, nume_client, telefon, email) VALUES
(seq_clienti.NEXTVAL, 'Ant Constructions', '0784736501', 'ant.constructions@outlook.com');
INSERT INTO CLIENTI (id_client, nume_client, telefon, email) VALUES
(seq_clienti.NEXTVAL, 'Rosca SRL', '0798521470', 'rosca.confectii@yahoo.com');

DESCRIBE CLIENTI;
SELECT * FROM CLIENTI;





--LOCATII

CREATE TABLE LOCATII (
    id_locatie INT PRIMARY KEY,
    judet VARCHAR(50) NOT NULL,
    localitate VARCHAR(50) NOT NULL,
    adresa VARCHAR(100) NOT NULL
);

INSERT INTO LOCATII (id_locatie, judet, localitate, adresa) VALUES
(seq_locatii.NEXTVAL, 'Bucuresti', 'Sectorul 4', 'Drumul Dealul Bradului, Nr. 89, Bl. D7');
INSERT INTO LOCATII (id_locatie, judet, localitate, adresa) VALUES
(seq_locatii.NEXTVAL, 'Vrancea', 'Focsani', 'Str. Binelui, Nr. 204-206');
INSERT INTO LOCATII (id_locatie, judet, localitate, adresa) VALUES
(seq_locatii.NEXTVAL, 'Ilfov', 'Tunari', 'Str. Biruintei, Nr. 74');
INSERT INTO LOCATII (id_locatie, judet, localitate, adresa) VALUES
(seq_locatii.NEXTVAL, 'Bucuresti', 'Sectorul 6', 'Bvd. Iuliu Maniu, Nr. 479');
INSERT INTO LOCATII (id_locatie, judet, localitate, adresa) VALUES
(seq_locatii.NEXTVAL, 'Vrancea', 'Focsani', 'Str. Marasesti, Nr. 56-58');

DESCRIBE LOCATII;
SELECT * FROM LOCATII;







--MATERIALE

CREATE TABLE MATERIALE (
    id_material INT PRIMARY KEY,
    nume_material VARCHAR(50) NOT NULL,
    cantitate INT NOT NULL
);

INSERT INTO MATERIALE (id_material, nume_material, cantitate) VALUES
(seq_materiale.NEXTVAL, 'Detergenti', 544);
INSERT INTO MATERIALE (id_material, nume_material, cantitate) VALUES
(seq_materiale.NEXTVAL, 'Saci menajeri', 1139);
INSERT INTO MATERIALE (id_material, nume_material, cantitate) VALUES
(seq_materiale.NEXTVAL, 'Prosoape ', 300);
INSERT INTO MATERIALE (id_material, nume_material, cantitate) VALUES
(seq_materiale.NEXTVAL, 'Saci pentru aspiratoare', 2048);
INSERT INTO MATERIALE (id_material, nume_material, cantitate) VALUES
(seq_materiale.NEXTVAL, 'Manusi', 4066);

DESCRIBE MATERIALE;
SELECT * FROM MATERIALE;






--ECHIPAMENTE

CREATE TABLE ECHIPAMENTE (
    id_echipament INT PRIMARY KEY,
    nume_echipament VARCHAR(50) NOT NULL,
    stare VARCHAR(50) NOT NULL
);

INSERT INTO ECHIPAMENTE (id_echipament, nume_echipament, stare) VALUES
(seq_echipamente.NEXTVAL, 'Aspiratoare', 'Nou');
INSERT INTO ECHIPAMENTE (id_echipament, nume_echipament, stare) VALUES
(seq_echipamente.NEXTVAL, 'Masini de spalat podele', 'Uzat');
INSERT INTO ECHIPAMENTE (id_echipament, nume_echipament, stare) VALUES
(seq_echipamente.NEXTVAL, 'Mopuri', 'Nou');
INSERT INTO ECHIPAMENTE (id_echipament, nume_echipament, stare) VALUES
(seq_echipamente.NEXTVAL, 'Maturi', 'Uzat');
INSERT INTO ECHIPAMENTE (id_echipament, nume_echipament, stare) VALUES
(seq_echipamente.NEXTVAL, 'Echipament de protectie', 'Nou');
INSERT INTO ECHIPAMENTE (id_echipament, nume_echipament, stare) VALUES
(seq_echipamente.NEXTVAL, 'Aparat de spalat cu presiune', 'Aproape nou');
INSERT INTO ECHIPAMENTE (id_echipament, nume_echipament, stare) VALUES
(seq_echipamente.NEXTVAL, 'Scari', 'Buna');
INSERT INTO ECHIPAMENTE (id_echipament, nume_echipament, stare) VALUES
(seq_echipamente.NEXTVAL, 'Carucioare de curatenie', 'Buna');

DESCRIBE ECHIPAMENTE;
SELECT * FROM ECHIPAMENTE;






--TIP_SERVICIU

CREATE TABLE TIP_SERVICIU (
    id_tip_serviciu INT PRIMARY KEY,
    nume_tip VARCHAR(50) NOT NULL
);

INSERT INTO TIP_SERVICIU (id_tip_serviciu, nume_tip) VALUES
(seq_tip_serviciu.NEXTVAL, 'Zilnic');
INSERT INTO TIP_SERVICIU (id_tip_serviciu, nume_tip) VALUES
(seq_tip_serviciu.NEXTVAL, 'Saptamanal');
INSERT INTO TIP_SERVICIU (id_tip_serviciu, nume_tip) VALUES
(seq_tip_serviciu.NEXTVAL, 'Lunar');
INSERT INTO TIP_SERVICIU (id_tip_serviciu, nume_tip) VALUES
(seq_tip_serviciu.NEXTVAL, 'Dupa client');
INSERT INTO TIP_SERVICIU (id_tip_serviciu, nume_tip) VALUES
(seq_tip_serviciu.NEXTVAL, 'Dimineata si seara');

DESCRIBE TIP_SERVICIU;
SELECT * FROM TIP_SERVICIU;






--SERVICII

CREATE TABLE SERVICII (
    id_serviciu INT PRIMARY KEY,
    nume_serviciu VARCHAR(50) NOT NULL,
    id_tip_serviciu INT NOT NULL,
    pret DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_tip_serviciu) REFERENCES TIP_SERVICIU(id_tip_serviciu)
);

INSERT INTO SERVICII (id_serviciu, nume_serviciu, id_tip_serviciu, pret) VALUES
(seq_servicii.NEXTVAL, 'Curatenie profunda', 3, 250.00);
INSERT INTO SERVICII (id_serviciu, nume_serviciu, id_tip_serviciu, pret) VALUES
(seq_servicii.NEXTVAL, 'Curatenie zilnica', 1, 300.00);
INSERT INTO SERVICII (id_serviciu, nume_serviciu, id_tip_serviciu, pret) VALUES
(seq_servicii.NEXTVAL, 'Curatenie inainte si dupa', 5, 400.00);
INSERT INTO SERVICII (id_serviciu, nume_serviciu, id_tip_serviciu, pret) VALUES
(seq_servicii.NEXTVAL, 'Curatenie finala de santier', 4, 800.00);
INSERT INTO SERVICII (id_serviciu, nume_serviciu, id_tip_serviciu, pret) VALUES
(seq_servicii.NEXTVAL, 'Curatenie industriala', 2, 500.00);


DESCRIBE SERVICII;
SELECT * FROM SERVICII;






--PROGRAMARI

CREATE TABLE PROGRAMARI (
    id_programare INT PRIMARY KEY,
    id_client INT NOT NULL,
    id_locatie INT NOT NULL,
    data_ora TIMESTAMP NOT NULL,
    FOREIGN KEY (id_client) REFERENCES CLIENTI(id_client),
    FOREIGN KEY (id_locatie) REFERENCES LOCATII(id_locatie)
);

INSERT INTO PROGRAMARI (id_programare, id_client, id_locatie, data_ora) VALUES
(seq_programari.NEXTVAL, 1, 1, TO_TIMESTAMP ('09-FEB-24 07:00:00', 'DD-MON-RR HH24:MI:SS'));
INSERT INTO PROGRAMARI (id_programare, id_client, id_locatie, data_ora) VALUES
(seq_programari.NEXTVAL, 2, 2, TO_TIMESTAMP ('22-MAR-24 18:00:00', 'DD-MON-RR HH24:MI:SS'));
INSERT INTO PROGRAMARI (id_programare, id_client, id_locatie, data_ora) VALUES
(seq_programari.NEXTVAL, 3, 3, TO_TIMESTAMP ('29-MAR-24 06:30:00', 'DD-MON-RR HH24:MI:SS'));
INSERT INTO PROGRAMARI (id_programare, id_client, id_locatie, data_ora) VALUES
(seq_programari.NEXTVAL, 4, 4, TO_TIMESTAMP ('30-APR-24 15:30:00', 'DD-MON-RR HH24:MI:SS'));
INSERT INTO PROGRAMARI (id_programare, id_client, id_locatie, data_ora) VALUES
(seq_programari.NEXTVAL, 5, 5, TO_TIMESTAMP ('19-MAR-24 21:00:00', 'DD-MON-RR HH24:MI:SS'));

DESCRIBE PROGRAMARI;
SELECT * FROM PROGRAMARI;





--ANGAJATI_SERVICII

CREATE TABLE ANGAJATI_SERVICII (
    id_angajat INT,
    id_serviciu INT,
    PRIMARY KEY (id_angajat, id_serviciu),
    FOREIGN KEY (id_angajat) REFERENCES ANGAJATI(id_angajat),
    FOREIGN KEY (id_serviciu) REFERENCES SERVICII(id_serviciu)
);

INSERT INTO ANGAJATI_SERVICII (id_angajat, id_serviciu) VALUES
(1, 1);
INSERT INTO ANGAJATI_SERVICII (id_angajat, id_serviciu) VALUES
(2, 2);
INSERT INTO ANGAJATI_SERVICII (id_angajat, id_serviciu) VALUES
(3, 3);
INSERT INTO ANGAJATI_SERVICII (id_angajat, id_serviciu) VALUES
(4, 4);
INSERT INTO ANGAJATI_SERVICII (id_angajat, id_serviciu) VALUES
(5, 5);
INSERT INTO ANGAJATI_SERVICII (id_angajat, id_serviciu) VALUES
(1, 2);
INSERT INTO ANGAJATI_SERVICII (id_angajat, id_serviciu) VALUES
(2, 3);
INSERT INTO ANGAJATI_SERVICII (id_angajat, id_serviciu) VALUES
(3, 4);
INSERT INTO ANGAJATI_SERVICII (id_angajat, id_serviciu) VALUES
(4, 5);
INSERT INTO ANGAJATI_SERVICII (id_angajat, id_serviciu) VALUES
(5, 1);

DESCRIBE ANGAJATI_SERVICII;
SELECT * FROM ANGAJATI_SERVICII;






--MATERIALE_SERVICII

CREATE TABLE MATERIALE_SERVICII (
    id_material INT,
    id_serviciu INT,
    PRIMARY KEY (id_material, id_serviciu),
    FOREIGN KEY (id_material) REFERENCES MATERIALE(id_material),
    FOREIGN KEY (id_serviciu) REFERENCES SERVICII(id_serviciu)
);

INSERT INTO MATERIALE_SERVICII (id_material, id_serviciu) VALUES
(1, 1);
INSERT INTO MATERIALE_SERVICII (id_material, id_serviciu) VALUES
(2, 2);
INSERT INTO MATERIALE_SERVICII (id_material, id_serviciu) VALUES
(3, 3);
INSERT INTO MATERIALE_SERVICII (id_material, id_serviciu) VALUES
(4, 4);
INSERT INTO MATERIALE_SERVICII (id_material, id_serviciu) VALUES
(5, 5);
INSERT INTO MATERIALE_SERVICII (id_material, id_serviciu) VALUES
(1, 2);
INSERT INTO MATERIALE_SERVICII (id_material, id_serviciu) VALUES
(2, 3);
INSERT INTO MATERIALE_SERVICII (id_material, id_serviciu) VALUES
(3, 4);
INSERT INTO MATERIALE_SERVICII (id_material, id_serviciu) VALUES
(4, 5);
INSERT INTO MATERIALE_SERVICII (id_material, id_serviciu) VALUES
(5, 1);

DESCRIBE MATERIALE_SERVICII;
SELECT * FROM MATERIALE_SERVICII;







--ECHIPAMENTE_SERVICII

CREATE TABLE ECHIPAMENTE_SERVICII (
    id_echipament INT,
    id_serviciu INT,
    PRIMARY KEY (id_echipament, id_serviciu),
    FOREIGN KEY (id_echipament) REFERENCES ECHIPAMENTE(id_echipament),
    FOREIGN KEY (id_serviciu) REFERENCES SERVICII(id_serviciu)
);

INSERT INTO ECHIPAMENTE_SERVICII (id_echipament, id_serviciu) VALUES
(1, 1);
INSERT INTO ECHIPAMENTE_SERVICII (id_echipament, id_serviciu) VALUES
(2, 2);
INSERT INTO ECHIPAMENTE_SERVICII (id_echipament, id_serviciu) VALUES
(3, 3);
INSERT INTO ECHIPAMENTE_SERVICII (id_echipament, id_serviciu) VALUES
(4, 4);
INSERT INTO ECHIPAMENTE_SERVICII (id_echipament, id_serviciu) VALUES
(5, 5);
INSERT INTO ECHIPAMENTE_SERVICII (id_echipament, id_serviciu) VALUES
(1, 2);
INSERT INTO ECHIPAMENTE_SERVICII (id_echipament, id_serviciu) VALUES
(2, 3);
INSERT INTO ECHIPAMENTE_SERVICII (id_echipament, id_serviciu) VALUES
(3, 4);
INSERT INTO ECHIPAMENTE_SERVICII (id_echipament, id_serviciu) VALUES
(4, 5);
INSERT INTO ECHIPAMENTE_SERVICII (id_echipament, id_serviciu) VALUES
(5, 1);

DESCRIBE ECHIPAMENTE_SERVICII;
SELECT * FROM ECHIPAMENTE_SERVICII;






--PROGRAMARI_SERVICII

CREATE TABLE PROGRAMARI_SERVICII (
    id_programare INT,
    id_serviciu INT,
    PRIMARY KEY (id_programare, id_serviciu),
    FOREIGN KEY (id_programare) REFERENCES PROGRAMARI(id_programare),
    FOREIGN KEY (id_serviciu) REFERENCES SERVICII(id_serviciu)
);

INSERT INTO PROGRAMARI_SERVICII (id_programare, id_serviciu) VALUES
(1, 1);
INSERT INTO PROGRAMARI_SERVICII (id_programare, id_serviciu) VALUES
(2, 2);
INSERT INTO PROGRAMARI_SERVICII (id_programare, id_serviciu) VALUES
(3, 3);
INSERT INTO PROGRAMARI_SERVICII (id_programare, id_serviciu) VALUES
(4, 4);
INSERT INTO PROGRAMARI_SERVICII (id_programare, id_serviciu) VALUES
(5, 5);
INSERT INTO PROGRAMARI_SERVICII (id_programare, id_serviciu) VALUES
(1, 2);
INSERT INTO PROGRAMARI_SERVICII (id_programare, id_serviciu) VALUES
(2, 3);
INSERT INTO PROGRAMARI_SERVICII (id_programare, id_serviciu) VALUES
(3, 4);
INSERT INTO PROGRAMARI_SERVICII (id_programare, id_serviciu) VALUES
(4, 5);
INSERT INTO PROGRAMARI_SERVICII (id_programare, id_serviciu) VALUES
(5, 1);

DESCRIBE PROGRAMARI_SERVICII;
SELECT * FROM PROGRAMARI_SERVICII;


drop sequence seq_departamente;
drop sequence seq_functii;
drop sequence seq_angajati;
drop sequence seq_istoric_angajati;
drop sequence seq_clienti;
drop sequence seq_locatii;
drop sequence seq_materiale;
drop sequence seq_echipamente;
drop sequence seq_tip_serviciu;
drop sequence seq_servicii;
drop sequence seq_programari;
drop table ISTORIC_ANGAJATI;
drop table PROGRAMARI_SERVICII;
drop table ECHIPAMENTE_SERVICII;
drop table MATERIALE_SERVICII;
drop table ANGAJATI_SERVICII;
drop table SERVICII;
drop table TIP_SERVICIU;
drop table MATERIALE;
drop table ECHIPAMENTE;
drop table PROGRAMARI;
drop table CLIENTI;
drop table LOCATII;
drop table ANGAJATI;
drop table FUNCTII;
drop table DEPARTAMENTE;


SELECT 
    a.nume AS Nume_Angajat,
    a.prenume AS Prenume_Angajat,
    d.nume_departament AS Departament,
    f.nume_functie AS Functie,
    a.salariu AS Salariu
FROM 
    ANGAJATI a
    INNER JOIN DEPARTAMENTE d ON a.id_departament = d.id_departament
    INNER JOIN FUNCTII f ON a.id_functie = f.id_functie
WHERE 
    a.salariu > (
        SELECT AVG(a2.salariu)
        FROM ANGAJATI a2
        WHERE a2.id_functie IN (
            SELECT f2.id_functie
            FROM FUNCTII f2
            WHERE f2.id_departament = (
                SELECT d2.id_departament
                FROM DEPARTAMENTE d2
                WHERE d2.id_departament = d.id_departament
            )
        )
    )
ORDER BY 
    a.salariu DESC;



SELECT c.nume_client, COUNT(p.id_programare) AS numar_programari 
FROM CLIENTI c 
LEFT JOIN (SELECT id_client, id_programare FROM PROGRAMARI) p ON c.id_client = p.id_client 
GROUP BY c.nume_client;



SELECT d.nume_departament, COUNT(a.id_angajat) AS numar_angajati 
FROM ANGAJATI a 
JOIN DEPARTAMENTE d ON a.id_departament = d.id_departament 
GROUP BY d.nume_departament 
HAVING AVG(a.salariu) > (SELECT AVG(a2.salariu) 
        				FROM ANGAJATI a2 
);




SELECT e.nume_echipament, NVL(e.stare, 'Necunoscut') AS stare, DECODE (NVL( e.stare, 'Necunoscut'),
'Nou', 'Nefolosit', 'Uzat', 'Stare precara', 'Aproape nou', 'Testat', 'Necunoscut', 'Stare necunoscuta') AS descriere_stare 
FROM ECHIPAMENTE e 
ORDER BY e.nume_echipament;






WITH AngajatiVarsta AS (SELECT id_angajat, nume, prenume, data_nastere, EXTRACT(YEAR FROM SYSDATE) - EXTRACT(YEAR FROM data_nastere) AS varsta 
                        FROM ANGAJATI) 
SELECT a.nume || ' ' || a.prenume AS nume_complet, TO_CHAR(a.data_nastere, 'DD-MON-YYYY') AS data_nastere_formatata, a.varsta,  
CASE  
WHEN a.varsta < 18 THEN 'Minor' 
WHEN a.varsta BETWEEN 18 AND 65 THEN 'Adult' 
ELSE 'Senior' 
END AS descriere_varsta 
FROM AngajatiVarsta a;





UPDATE PROGRAMARI
SET data_ora = data_ora + INTERVAL '7' DAY
WHERE id_locatie IN (
    SELECT id_locatie
    FROM LOCATII
    WHERE localitate = 'Focsani'
);




UPDATE ECHIPAMENTE 
SET stare = 'Uzat' 
WHERE id_echipament IN ( SELECT id_echipament 
    				FROM SERVICII 
    				WHERE pret > (SELECT AVG(pret) FROM SERVICII) 
);





UPDATE MATERIALE 
SET cantitate = cantitate - 10 
WHERE id_material IN ( SELECT id_material 
                        FROM SERVICII 
                        WHERE id_serviciu IN ( SELECT id_serviciu 
                                                FROM PROGRAMARI_SERVICII 
                                                WHERE id_programare IN ( SELECT id_programare 
                                                                            FROM PROGRAMARI 
                                                                            WHERE id_locatie = ( SELECT id_locatie  
                                                                                                    FROM LOCATII  
                                                                                                        WHERE localitate = 'Sectorul 6') 
) 
) 
);


commit;








CREATE VIEW VIZUALIZARE_ANGAJATI_COMPLEXA AS 
SELECT a.id_angajat, a.nume || ' ' || a.prenume AS nume_complet, f.nume_functie, d.nume_departament, a.salariu, NVL(p.numar_programari, 0) AS numar_programari 
FROM  ANGAJATI a 
JOIN  FUNCTII f ON a.id_functie = f.id_functie 
JOIN  DEPARTAMENTE d ON a.id_departament = d.id_departament 
LEFT JOIN  
    (SELECT ans.id_angajat, COUNT(ps.id_programare) AS numar_programari 
     FROM ANGAJATI_SERVICII ans 
     JOIN PROGRAMARI_SERVICII ps ON ans.id_serviciu = ps.id_serviciu 
     GROUP BY ans.id_angajat) p ON a.id_angajat = p.id_angajat;




SELECT * FROM VIZUALIZARE_ANGAJATI_COMPLEXA 
WHERE numar_programari > 1;


INSERT INTO VIZUALIZARE_ANGAJATI_COMPLEXA (id_angajat, nume_complet, nume_functie, nume_departament, salariu, numar_programari) 
VALUES (999, 'Popescu Ion', 'Manager', 'Curatenie', 5000, 3);

select s.nume_serviciu, count(e.nume_echipament) as numar_echipamente
from SERVICII s
join ECHIPAMENTE_SERVICII es on s.id_serviciu = es.id_serviciu
left join ECHIPAMENTE e on es.id_echipament = e.id_echipament
group by s.nume_serviciu;


UPDATE ANGAJATI
SET salariu = salariu * 2.05
WHERE id_departament = (
    SELECT id_departament
    FROM (
        SELECT id_departament
        FROM ANGAJATI
        GROUP BY id_departament
        ORDER BY AVG(salariu) DESC
    )
    WHERE ROWNUM = 1
);

UPDATE ANGAJATI
SET salariu = salariu * 2.05
WHERE id_departament IN (
    SELECT id_departament
    FROM ANGAJATI
    GROUP BY id_departament
    HAVING AVG(salariu) > (
        SELECT AVG(salariu)
        FROM ANGAJATI
    )
);



--serviciile cu cel mai mare numar de programari folosind clauza having


with max_programari as (select max(count(s.id_serviciu))
                            from SERVICII s
                            join PROGRAMARI_SERVICII ps on s.id_serviciu = ps.id_serviciu
                            join PROGRAMARI p on ps.id_programare = p.id_programare
                            group by s.id_serviciu
                            )
select q.nume_serviciu
from SERVICII q
group by q.nume_serviciu
having (select count(s.id_serviciu)
        from SERVICII s
        join PROGRAMARI_SERVICII ps on s.id_serviciu = ps.id_serviciu
        join PROGRAMARI p on ps.id_programare = p.id_programare
        where q.nume_serviciu = s.nume_serviciu
        group by s.id_serviciu)
        = (select * from max_programari);








create table ANGAJATI_SERVICII2(
id_serviciu int,
id_angajat int,
primary key(id_serviciu, id_angajat),
foreign key (id_serviciu) references SERVICII(id_serviciu),
foreign key (id_angajat) references ANGAJATI(id_angajat));

describe ANGAJATI_SERVICII2;




--exercitiul cu angajati pe scurt
--lmd