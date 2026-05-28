package service;

import model.*;
import java.sql.*;
import java.util.*;

public class CatalogService {
    private Connection conn;

    public CatalogService(Connection conn) {
        this.conn = conn;
    }

    public void adaugaStudent(Student student) {
        try {
            PreparedStatement stmt = conn.prepareStatement("INSERT INTO studenti (id, nume, prenume, grupa) VALUES (?, ?, ?, ?)");
            stmt.setInt(1, student.getId());
            stmt.setString(2, student.getNume());
            stmt.setString(3, student.getPrenume());
            stmt.setString(4, student.getGrupa());
            stmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public List<Student> getStudenti() {
        List<Student> studenti = new ArrayList<>();
        try {
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM studenti");
            while (rs.next()) {
                studenti.add(new Student(rs.getInt("id"), rs.getString("nume"), rs.getString("prenume"), rs.getString("grupa")));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return studenti;
    }

    public void actualizeazaStudent(int id, String nume, String prenume, String grupa) {
        try {
            PreparedStatement stmt = conn.prepareStatement("UPDATE studenti SET nume = ?, prenume = ?, grupa = ? WHERE id = ?");
            stmt.setString(1, nume);
            stmt.setString(2, prenume);
            stmt.setString(3, grupa);
            stmt.setInt(4, id);
            stmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void stergeStudent(int id) {
        try {
            PreparedStatement stmt = conn.prepareStatement("DELETE FROM studenti WHERE id = ?");
            stmt.setInt(1, id);
            stmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void adaugaMaterie(Materie materie) {
        try {
            PreparedStatement stmt = conn.prepareStatement("INSERT INTO materii (id, denumire, profesor_id) VALUES (?, ?, ?)");
            stmt.setInt(1, materie.getId());
            stmt.setString(2, materie.getDenumire());
            stmt.setInt(3, materie.getProfesorId());
            stmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public List<Materie> getMaterii() {
        List<Materie> materii = new ArrayList<>();
        try {
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM materii");
            while (rs.next()) {
                materii.add(new Materie(rs.getInt("id"), rs.getString("denumire"), rs.getInt("profesor_id")));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return materii;
    }

    public void actualizeazaMaterie(int id, String denumire, int profesor_id) {
        try {
            PreparedStatement stmt = conn.prepareStatement("UPDATE materii SET denumire = ?, profesor_id = ? WHERE id = ?");
            stmt.setString(1, denumire);
            stmt.setInt(2, profesor_id);
            stmt.setInt(3, id);
            stmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void stergeMaterie(int id) {
        try {
            PreparedStatement stmt = conn.prepareStatement("DELETE FROM materii WHERE id = ?");
            stmt.setInt(1, id);
            stmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void adaugaProfesor(Profesor profesor) {
        try {
            PreparedStatement stmt = conn.prepareStatement(
                    "INSERT INTO profesori (id, nume, departament) VALUES (?, ?, ?)"
            );
            stmt.setInt(1, profesor.getId());
            stmt.setString(2, profesor.getNume());
            stmt.setString(3, profesor.getDepartament());
            stmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public List<Profesor> getProfesori() {
        List<Profesor> profesori = new ArrayList<>();
        try {
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM profesori");
            while (rs.next()) {
                profesori.add(new Profesor(
                        rs.getInt("id"),
                        rs.getString("nume"),
                        rs.getString("departament")
                ));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return profesori;
    }

    public void actualizeazaProfesor(int id, String nume, String departament) {
        try {
            PreparedStatement stmt = conn.prepareStatement(
                    "UPDATE profesori SET nume = ?, departament = ? WHERE id = ?"
            );
            stmt.setString(1, nume);
            stmt.setString(2, departament);
            stmt.setInt(3, id);
            stmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void stergeProfesor(int id) {
        try {
            PreparedStatement stmt = conn.prepareStatement(
                    "DELETE FROM profesori WHERE id = ?"
            );
            stmt.setInt(1, id);
            stmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void adaugaNota(Nota nota) {
        try {
            PreparedStatement stmt = conn.prepareStatement(
                    "INSERT INTO note (id, student_id, materie_id, valoare) VALUES (?, ?, ?, ?)"
            );
            stmt.setInt(1, nota.getId());
            stmt.setInt(2, nota.getStudentId());
            stmt.setInt(3, nota.getMaterieId());
            stmt.setDouble(4, nota.getValoare());
            stmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public List<Nota> getNote() {
        List<Nota> note = new ArrayList<>();
        try {
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM note");
            while (rs.next()) {
                note.add(new Nota(
                        rs.getInt("id"),
                        rs.getInt("student_id"),
                        rs.getInt("materie_id"),
                        rs.getDouble("valoare")
                ));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return note;
    }

    public void actualizeazaNota(int id, double valoare) {
        try {
            PreparedStatement stmt = conn.prepareStatement(
                    "UPDATE note SET valoare = ? WHERE id = ?"
            );
            stmt.setDouble(1, valoare);
            stmt.setInt(2, id);
            stmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void stergeNota(int id) {
        try {
            PreparedStatement stmt = conn.prepareStatement(
                    "DELETE FROM note WHERE id = ?"
            );
            stmt.setInt(1, id);
            stmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
