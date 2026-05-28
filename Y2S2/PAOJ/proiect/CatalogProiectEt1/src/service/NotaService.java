package service;

import model.Nota;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class NotaService {
    private static NotaService instance;
    private final Connection conn;

    private NotaService(Connection conn) {
        this.conn = conn;
    }

    public static NotaService getInstance(Connection conn) {
        if (instance == null) {
            instance = new NotaService(conn);
        }
        return instance;
    }

    public void creeazaTabelaNote() {
        String sql = "CREATE TABLE IF NOT EXISTS note (" +
                "id INT PRIMARY KEY AUTO_INCREMENT," +
                "student_id INT," +
                "materie_id INT," +
                "valoare DOUBLE NOT NULL," +
                "FOREIGN KEY (student_id) REFERENCES studenti(id)," +
                "FOREIGN KEY (materie_id) REFERENCES materii(id))";
        try (Statement stmt = conn.createStatement()) {
            stmt.execute(sql);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void adaugaNota(Nota nota) {
        String sql = "INSERT INTO note (student_id, materie_id, valoare) VALUES (?, ?, ?)";
        try (PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setInt(1, nota.getStudentId());
            stmt.setInt(2, nota.getMaterieId());
            stmt.setDouble(3, nota.getValoare());
            stmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public List<Nota> getNote() {
        List<Nota> lista = new ArrayList<>();
        String sql = "SELECT * FROM note";
        try (Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
            while (rs.next()) {
                int id = rs.getInt("id");
                int studentId = rs.getInt("student_id");
                int materieId = rs.getInt("materie_id");
                double valoare = rs.getDouble("valoare");
                lista.add(new Nota(id, studentId, materieId, valoare));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return lista;
    }

    public void actualizeazaNota(int idNota, double nouaValoare) {
        String sql = "UPDATE note SET valoare = ? WHERE id = ?";
        try (PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setDouble(1, nouaValoare);
            stmt.setInt(2, idNota);
            stmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void stergeNota(int idNota) {
        String sql = "DELETE FROM note WHERE id = ?";
        try (PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setInt(1, idNota);
            stmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
