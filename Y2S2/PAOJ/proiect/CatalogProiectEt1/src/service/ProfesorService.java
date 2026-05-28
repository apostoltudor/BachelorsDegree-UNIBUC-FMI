package service;

import model.Profesor;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class ProfesorService {
    private final Connection conn;

    public ProfesorService(Connection conn) {
        this.conn = conn;
    }

    public void adaugaProfesor(Profesor profesor) {
        String sql = "INSERT INTO profesori (nume, departament) VALUES (?, ?)";
        try (PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setString(1, profesor.getNume());
            stmt.setString(2, profesor.getDepartament());
            stmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public List<Profesor> getProfesori() {
        List<Profesor> lista = new ArrayList<>();
        String sql = "SELECT * FROM profesori";
        try (Statement stmt = conn.createStatement(); ResultSet rs = stmt.executeQuery(sql)) {
            while (rs.next()) {
                int id = rs.getInt("id");
                String nume = rs.getString("nume");
                String departament = rs.getString("departament");
                lista.add(new Profesor(id, nume, departament));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return lista;
    }

    public void actualizeazaDepartament(int id, String nouDepartament) {
        String sql = "UPDATE profesori SET departament = ? WHERE id = ?";
        try (PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setString(1, nouDepartament);
            stmt.setInt(2, id);
            stmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void stergeProfesor(int id) {
        String sql = "DELETE FROM profesori WHERE id = ?";
        try (PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setInt(1, id);
            stmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
