package dao;

import model.Nota;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class NotaDAO {
    private Connection connection;

    public NotaDAO() {
        try {
            connection = DriverManager.getConnection("jdbc:sqlite:catalog.db");
            Statement statement = connection.createStatement();
            statement.execute("CREATE TABLE IF NOT EXISTS nota (id INTEGER PRIMARY KEY, studentId INTEGER, materieId INTEGER, valoare REAL)");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void create(Nota nota) {
        try {
            PreparedStatement ps = connection.prepareStatement("INSERT INTO nota (id, studentId, materieId, valoare) VALUES (?, ?, ?, ?)");
            ps.setInt(1, nota.getId());
            ps.setInt(2, nota.getStudentId());
            ps.setInt(3, nota.getMaterieId());
            ps.setDouble(4, nota.getValoare());
            ps.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public Nota read(int id) {
        try {
            PreparedStatement ps = connection.prepareStatement("SELECT * FROM nota WHERE id = ?");
            ps.setInt(1, id);
            ResultSet rs = ps.executeQuery();
            if (rs.next()) {
                return new Nota(rs.getInt("id"), rs.getInt("studentId"), rs.getInt("materieId"), rs.getDouble("valoare"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    public void update(Nota nota) {
        try {
            PreparedStatement ps = connection.prepareStatement("UPDATE nota SET studentId = ?, materieId = ?, valoare = ? WHERE id = ?");
            ps.setInt(1, nota.getStudentId());
            ps.setInt(2, nota.getMaterieId());
            ps.setDouble(3, nota.getValoare());
            ps.setInt(4, nota.getId());
            ps.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void delete(int id) {
        try {
            PreparedStatement ps = connection.prepareStatement("DELETE FROM nota WHERE id = ?");
            ps.setInt(1, id);
            ps.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public List<Nota> getAll() {
        List<Nota> note = new ArrayList<>();
        try {
            Statement statement = connection.createStatement();
            ResultSet rs = statement.executeQuery("SELECT * FROM nota");
            while (rs.next()) {
                note.add(new Nota(rs.getInt("id"), rs.getInt("studentId"), rs.getInt("materieId"), rs.getDouble("valoare")));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return note;
    }
}