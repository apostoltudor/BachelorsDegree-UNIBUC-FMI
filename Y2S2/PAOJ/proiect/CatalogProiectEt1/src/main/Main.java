package main;

import model.*;
import service.AuditService;
import service.CatalogService;

import java.sql.Connection;
import java.sql.DriverManager;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        try {
            Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "1qaz2wsx");
            CatalogService service = new CatalogService(conn);
            Scanner scanner = new Scanner(System.in);
            boolean running = true;

            while (running) {
                System.out.println("\nMeniu Catalog Academic:");
                System.out.println("1. Adauga student");
                System.out.println("2. Afiseaza studenti");
                System.out.println("3. Actualizeaza student");
                System.out.println("4. Sterge student");
                System.out.println("5. Adauga materie");
                System.out.println("6. Afiseaza materii");
                System.out.println("7. Actualizeaza materie");
                System.out.println("8. Sterge materie");
                System.out.println("9. Adauga profesor");
                System.out.println("10. Afiseaza profesori");
                System.out.println("11. Actualizeaza profesor");
                System.out.println("12. Sterge profesor");
                System.out.println("13. Adauga nota");
                System.out.println("14. Afiseaza note");
                System.out.println("15. Actualizeaza nota");
                System.out.println("16. Sterge nota");
                System.out.println("0. Iesire");
                System.out.print("Alege o optiune: ");

                int optiune = scanner.nextInt();
                scanner.nextLine();

                switch (optiune) {
                    case 1:
                        System.out.print("ID student: ");
                        int idStudent = scanner.nextInt(); scanner.nextLine();
                        System.out.print("Nume: ");
                        String nume = scanner.nextLine();
                        System.out.print("Prenume: ");
                        String prenume = scanner.nextLine();
                        System.out.print("Grupa: ");
                        String grupa = scanner.nextLine();
                        service.adaugaStudent(new Student(idStudent, nume, prenume, grupa));
                        AuditService.getInstance().logActiune("adaugat student");
                        break;
                    case 2:
                        List<Student> studenti = service.getStudenti();
                        for (Student s : studenti) {
                            System.out.println(s);
                        }
                        AuditService.getInstance().logActiune("afisat studenti");
                        break;
                    case 3:
                        System.out.print("ID student de actualizat: ");
                        int idUpdate = scanner.nextInt(); scanner.nextLine();
                        System.out.print("Nume nou: ");
                        String numeNou = scanner.nextLine();
                        System.out.print("Prenume nou: ");
                        String prenumeNou = scanner.nextLine();
                        System.out.print("Grupa noua: ");
                        String grupaNoua = scanner.nextLine();
                        service.actualizeazaStudent(idUpdate, numeNou, prenumeNou, grupaNoua);
                        AuditService.getInstance().logActiune("actualizat student");
                        break;
                    case 4:
                        System.out.print("ID student de sters: ");
                        int idStergere = scanner.nextInt(); scanner.nextLine();
                        service.stergeStudent(idStergere);
                        AuditService.getInstance().logActiune("sters student");
                        break;
                    case 5:
                        System.out.print("ID materie: ");
                        int idMaterie = scanner.nextInt(); scanner.nextLine();
                        System.out.print("Denumire: ");
                        String denumire = scanner.nextLine();
                        System.out.print("ID profesor: ");
                        int profesorId = scanner.nextInt(); scanner.nextLine();
                        service.adaugaMaterie(new Materie(idMaterie, denumire, profesorId));
                        AuditService.getInstance().logActiune("adaugat materie");
                        break;
                    case 6:
                        for (Materie m : service.getMaterii()) {
                            System.out.println(m);
                        }
                        AuditService.getInstance().logActiune("afisat materii");
                        break;
                    case 7:
                        System.out.print("ID materie de actualizat: ");
                        int idUpdateMat = scanner.nextInt(); scanner.nextLine();
                        System.out.print("Denumire noua: ");
                        String denNou = scanner.nextLine();
                        System.out.print("ID nou profesor: ");
                        int profNou = scanner.nextInt(); scanner.nextLine();
                        service.actualizeazaMaterie(idUpdateMat, denNou, profNou);
                        AuditService.getInstance().logActiune("actualizat materie");
                        break;
                    case 8:
                        System.out.print("ID materie de sters: ");
                        int idStergMat = scanner.nextInt(); scanner.nextLine();
                        service.stergeMaterie(idStergMat);
                        AuditService.getInstance().logActiune("sters materie");
                        break;
                    case 9:
                        System.out.print("ID profesor: ");
                        int idProf = scanner.nextInt(); scanner.nextLine();
                        System.out.print("Nume: ");
                        String numeProf = scanner.nextLine();
                        System.out.print("Departament: ");
                        String departament = scanner.nextLine();
                        service.adaugaProfesor(new Profesor(idProf, numeProf, departament));
                        AuditService.getInstance().logActiune("adaugat profesor");
                        break;
                    case 10:
                        for (Profesor p : service.getProfesori()) {
                            System.out.println(p);
                        }
                        AuditService.getInstance().logActiune("afisat profesori");
                        break;
                    case 11:
                        System.out.print("ID profesor de actualizat: ");
                        int idUpdateProf = scanner.nextInt(); scanner.nextLine();
                        System.out.print("Nume nou: ");
                        String numeNouProf = scanner.nextLine();
                        System.out.print("Departament nou: ");
                        String departamentNou = scanner.nextLine();
                        service.actualizeazaProfesor(idUpdateProf, numeNouProf, departamentNou);
                        AuditService.getInstance().logActiune("actualizat profesor");
                        break;
                    case 12:
                        System.out.print("ID profesor de sters: ");
                        int idStergProf = scanner.nextInt(); scanner.nextLine();
                        service.stergeProfesor(idStergProf);
                        AuditService.getInstance().logActiune("sters profesor");
                        break;
                    case 13:
                        System.out.print("ID nota: ");
                        int idNota = scanner.nextInt();
                        System.out.print("ID student: ");
                        int idStudentNota = scanner.nextInt();
                        System.out.print("ID materie: ");
                        int idMaterieNota = scanner.nextInt();
                        System.out.print("Valoare: ");
                        double valoareNota = scanner.nextDouble(); scanner.nextLine();
                        service.adaugaNota(new Nota(idNota, idStudentNota, idMaterieNota, valoareNota));
                        AuditService.getInstance().logActiune("adaugat nota");
                        break;
                    case 14:
                        for (Nota n : service.getNote()) {
                            System.out.println(n);
                        }
                        AuditService.getInstance().logActiune("afisat note");
                        break;
                    case 15:
                        System.out.print("ID nota de actualizat: ");
                        int idUpdateNota = scanner.nextInt();
                        System.out.print("Valoare noua: ");
                        double valoareNoua = scanner.nextDouble(); scanner.nextLine();
                        service.actualizeazaNota(idUpdateNota, valoareNoua);
                        AuditService.getInstance().logActiune("actualizat nota");
                        break;
                    case 16:
                        System.out.print("ID nota de sters: ");
                        int idStergNota = scanner.nextInt(); scanner.nextLine();
                        service.stergeNota(idStergNota);
                        AuditService.getInstance().logActiune("sters nota");
                        break;
                    case 0:
                        running = false;
                        AuditService.getInstance().logActiune("iesire");
                        break;
                    default:
                        System.out.println("Optiune invalida.");
                }
            }

            scanner.close();
            conn.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}