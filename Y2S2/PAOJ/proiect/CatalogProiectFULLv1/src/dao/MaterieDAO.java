package dao;

import model.Materie;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class MaterieDAO {
    private Connection connection;

    public MaterieDAO() {
        try {
            connection = DriverManager.getConnection("jdbc:sqlite:catalog.db");
            Statement statement = connection.createStatement();
            statement.execute("CREATE TABLE IF NOT EXISTS materie (id INTEGER PRIMARY KEY, nume TEXT, credite INTEGER)");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void create(Materie materie) {
        try {
            PreparedStatement ps = connection.prepareStatement("INSERT INTO materie (id, nume, credite) VALUES (?, ?, ?)");
            ps.setInt(1, materie.getId());
            ps.setString(2, materie.getNume());
            ps.setInt(3, materie.getCredite());
            ps.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public Materie read(int id) {
        try {
            PreparedStatement ps = connection.prepareStatement("SELECT * FROM materie WHERE id = ?");
            ps.setInt(1, id);
            ResultSet rs = ps.executeQuery();
            if (rs.next()) {
                return new Materie(rs.getInt("id"), rs.getString("nume"), rs.getInt("credite"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    public void update(Materie materie) {
        try {
            PreparedStatement ps = connection.prepareStatement("UPDATE materie SET nume = ?, credite = ? WHERE id = ?");
            ps.setString(1, materie.getNume());
            ps.setInt(2, materie.getCredite());
            ps.setInt(3, materie.getId());
            ps.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void delete(int id) {
        try {
            PreparedStatement ps = connection.prepareStatement("DELETE FROM materie WHERE id = ?");
            ps.setInt(1, id);
            ps.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public List<Materie> getAll() {
        List<Materie> materii = new ArrayList<>();
        try {
            Statement statement = connection.createStatement();
            ResultSet rs = statement.executeQuery("SELECT * FROM materie");
            while (rs.next()) {
                materii.add(new Materie(rs.getInt("id"), rs.getString("nume"), rs.getInt("credite")));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return materii;
    }
}