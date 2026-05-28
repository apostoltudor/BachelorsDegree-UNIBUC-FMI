package service;

import model.Student;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class StudentService {
    private static StudentService instance;
    private Connection conn;

    private StudentService() {
        try {
            conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "1qaz2wsx");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public static StudentService getInstance() {
        if (instance == null) {
            instance = new StudentService();
        }
        return instance;
    }

    public void adaugaStudent(Student student) {
        String sql = "INSERT INTO studenti (nume, prenume, grupa) VALUES (?, ?, ?)";
        try (PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setString(1, student.getNume());
            stmt.setString(2, student.getPrenume());
            stmt.setString(3, student.getGrupa());
            stmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public List<Student> getStudenti() {
        List<Student> lista = new ArrayList<>();
        String sql = "SELECT * FROM studenti";
        try (Statement stmt = conn.createStatement(); ResultSet rs = stmt.executeQuery(sql)) {
            while (rs.next()) {
                int id = rs.getInt("id");
                String nume = rs.getString("nume");
                String prenume = rs.getString("prenume");
                String grupa = rs.getString("grupa");
                lista.add(new Student(id, nume, prenume, grupa));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return lista;
    }

    public void actualizeazaGrupa(int id, String nouaGrupa) {
        String sql = "UPDATE studenti SET grupa = ? WHERE id = ?";
        try (PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setString(1, nouaGrupa);
            stmt.setInt(2, id);
            stmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void stergeStudent(int id) {
        String sql = "DELETE FROM studenti WHERE id = ?";
        try (PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setInt(1, id);
            stmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
