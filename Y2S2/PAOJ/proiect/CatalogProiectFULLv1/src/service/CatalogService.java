package service;

import dao.*;
import model.*;
import java.util.List;

public class CatalogService {
    private StudentDAO studentDAO = new StudentDAO();
    private MaterieDAO materieDAO = new MaterieDAO();
    private ProfesorDAO profesorDAO = new ProfesorDAO();
    private NotaDAO notaDAO = new NotaDAO();
    private AuditService auditService = AuditService.getInstance();

    public void adaugaStudent(Student student) {
        studentDAO.create(student);
        auditService.logAction("Adauga Student");
    }

    public Student getStudent(int id) {
        auditService.logAction("Citeste Student");
        return studentDAO.read(id);
    }

    public void actualizeazaStudent(Student student) {
        studentDAO.update(student);
        auditService.logAction("Actualizeaza Student");
    }

    public void stergeStudent(int id) {
        studentDAO.delete(id);
        auditService.logAction("Sterge Student");
    }

    public List<Student> getStudenti() {
        auditService.logAction("Lista Studenti");
        return studentDAO.getAll();
    }

    public void adaugaMaterie(Materie materie) {
        materieDAO.create(materie);
        auditService.logAction("Adauga Materie");
    }

    public Materie getMaterie(int id) {
        auditService.logAction("Citeste Materie");
        return materieDAO.read(id);
    }

    public void actualizeazaMaterie(Materie materie) {
        materieDAO.update(materie);
        auditService.logAction("Actualizeaza Materie");
    }

    public void stergeMaterie(int id) {
        materieDAO.delete(id);
        auditService.logAction("Sterge Materie");
    }

    public List<Materie> getMaterii() {
        auditService.logAction("Lista Materii");
        return materieDAO.getAll();
    }

    public void adaugaProfesor(Profesor profesor) {
        profesorDAO.create(profesor);
        auditService.logAction("Adauga Profesor");
    }

    public Profesor getProfesor(int id) {
        auditService.logAction("Citeste Profesor");
        return profesorDAO.read(id);
    }

    public void actualizeazaProfesor(Profesor profesor) {
        profesorDAO.update(profesor);
        auditService.logAction("Actualizeaza Profesor");
    }

    public void stergeProfesor(int id) {
        profesorDAO.delete(id);
        auditService.logAction("Sterge Profesor");
    }

    public List<Profesor> getProfesori() {
        auditService.logAction("Lista Profesori");
        return profesorDAO.getAll();
    }

    public void adaugaNota(Nota nota) {
        notaDAO.create(nota);
        auditService.logAction("Adauga Nota");
    }

    public Nota getNota(int id) {
        auditService.logAction("Citeste Nota");
        return notaDAO.read(id);
    }

    public void actualizeazaNota(Nota nota) {
        notaDAO.update(nota);
        auditService.logAction("Actualizeaza Nota");
    }

    public void stergeNota(int id) {
        notaDAO.delete(id);
        auditService.logAction("Sterge Nota");
    }

    public List<Nota> getNote() {
        auditService.logAction("Lista Note");
        return notaDAO.getAll();
    }
}