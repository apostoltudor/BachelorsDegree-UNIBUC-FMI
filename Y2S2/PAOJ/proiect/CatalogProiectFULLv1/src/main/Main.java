package main;

import model.*;
import service.CatalogService;

public class Main {
    public static void main(String[] args) {
        CatalogService service = new CatalogService();

        int idCounter = (int) (System.currentTimeMillis() % 10000);

        Student s1 = new Student(idCounter++, "Ion", "Pop", "Grupa1");
        StudentMaster sm1 = new StudentMaster(idCounter++, "Maria", "Ionescu", "Grupa2", "TemaMaster");
        service.adaugaStudent(s1);
        service.adaugaStudent(sm1);

        Materie m1 = new Materie(idCounter++, "Programare", 6);
        Materie m2 = new Materie(idCounter++, "Baze de date", 5);
        service.adaugaMaterie(m1);
        service.adaugaMaterie(m2);

        Profesor p1 = new Profesor(idCounter++, "Ana", "Marin", "Informatica");
        service.adaugaProfesor(p1);

        Nota n1 = new Nota(idCounter++, s1.getId(), m1.getId(), 8.5);
        Nota n2 = new Nota(idCounter++, sm1.getId(), m2.getId(), 9.0);
        service.adaugaNota(n1);
        service.adaugaNota(n2);

        Student s1Updated = new Student(s1.getId(), "Ion", "Popescu", "Grupa1");
        service.actualizeazaStudent(s1Updated);

        Materie m1Updated = new Materie(m1.getId(), "Programare Avansată", 7);
        service.actualizeazaMaterie(m1Updated);

        Profesor p1Updated = new Profesor(p1.getId(), "Ana", "Marin", "Matematică");
        service.actualizeazaProfesor(p1Updated);

        Nota n1Updated = new Nota(n1.getId(), s1.getId(), m1.getId(), 9.5);
        service.actualizeazaNota(n1Updated);

        System.out.println("Studenți:");
        for (Student s : service.getStudenti()) {
            System.out.println(s);
        }

        System.out.println("\nMaterii:");
        for (Materie m : service.getMaterii()) {
            System.out.println(m);
        }

        System.out.println("\nProfesori:");
        for (Profesor p : service.getProfesori()) {
            System.out.println(p);
        }

        System.out.println("\nNote:");
        for (Nota n : service.getNote()) {
            System.out.println(n);
        }

        service.stergeStudent(sm1.getId());
        System.out.println("\nStudenți după ștergere:");
        for (Student s : service.getStudenti()) {
            System.out.println(s);
        }
    }
}