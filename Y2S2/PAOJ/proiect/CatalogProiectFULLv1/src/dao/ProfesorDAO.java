package dao;

import model.Profesor;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class ProfesorDAO {
    private Connection connection;

    public ProfesorDAO() {
        try {
            connection = DriverManager.getConnection("jdbc:sqlite:catalog.db");
            Statement statement = connection.createStatement();
            statement.execute("CREATE TABLE IF NOT EXISTS profesor (id INTEGER PRIMARY KEY, nume TEXT, prenume TEXT, departament TEXT)");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void create(Profesor profesor) {
        try {
            PreparedStatement ps = connection.prepareStatement("INSERT INTO profesor (id, nume, prenume, departament) VALUES (?, ?, ?, ?)");
            ps.setInt(1, profesor.getId());
            ps.setString(2, profesor.getNume());
            ps.setString(3, profesor.getPrenume());
            ps.setString(4, profesor.getDepartament());
            ps.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public Profesor read(int id) {
        try {
            PreparedStatement ps = connection.prepareStatement("SELECT * FROM profesor WHERE id = ?");
            ps.setInt(1, id);
            ResultSet rs = ps.executeQuery();
            if (rs.next()) {
                return new Profesor(rs.getInt("id"), rs.getString("nume"), rs.getString("prenume"), rs.getString("departament"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    public void update(Profesor profesor) {
        try {
            PreparedStatement ps = connection.prepareStatement("UPDATE profesor SET nume = ?, prenume = ?, departament = ? WHERE id = ?");
            ps.setString(1, profesor.getNume());
            ps.setString(2, profesor.getPrenume());
            ps.setString(3, profesor.getDepartament());
            ps.setInt(4, profesor.getId());
            ps.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void delete(int id) {
        try {
            PreparedStatement ps = connection.prepareStatement("DELETE FROM profesor WHERE id = ?");
            ps.setInt(1, id);
            ps.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public List<Profesor> getAll() {
        List<Profesor> profesori = new ArrayList<>();
        try {
            Statement statement = connection.createStatement();
            ResultSet rs = statement.executeQuery("SELECT * FROM profesor");
            while (rs.next()) {
                profesori.add(new Profesor(rs.getInt("id"), rs.getString("nume"), rs.getString("prenume"), rs.getString("departament")));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return profesori;
    }
}