package service;

import model.Materie;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class MaterieService {
    private static MaterieService instance;

    private MaterieService() {
        creareTabela();
    }

    public static MaterieService getInstance() {
        if (instance == null) {
            instance = new MaterieService();
        }
        return instance;
    }

    private Connection conectare() throws SQLException {
        return DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "1qaz2wsx");
    }

    public void creareTabela() {
        String sql = "CREATE TABLE IF NOT EXISTS materii (" +
                "id INT PRIMARY KEY AUTO_INCREMENT, " +
                "denumire VARCHAR(100) NOT NULL, " +
                "profesor_id INT, " +
                "FOREIGN KEY (profesor_id) REFERENCES profesori(id)" +
                ")";
        try (Connection conn = conectare();
             Statement stmt = conn.createStatement()) {
            stmt.execute(sql);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void adaugaMaterie(Materie materie) {
        String sql = "INSERT INTO materii (denumire, profesor_id) VALUES (?, ?)";
        try (Connection conn = conectare();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(1, materie.getDenumire());
            pstmt.setInt(2, materie.getProfesorId());
            pstmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public List<Materie> afiseazaMaterii() {
        List<Materie> lista = new ArrayList<>();
        String sql = "SELECT * FROM materii";
        try (Connection conn = conectare();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
            while (rs.next()) {
                int id = rs.getInt("id");
                String denumire = rs.getString("denumire");
                int profesorId = rs.getInt("profesor_id");
                lista.add(new Materie(id, denumire, profesorId));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return lista;
    }

    public void actualizeazaDenumire(int id, String denumireNoua) {
        String sql = "UPDATE materii SET denumire = ? WHERE id = ?";
        try (Connection conn = conectare();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(1, denumireNoua);
            pstmt.setInt(2, id);
            pstmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void stergeMateriiCuProfesor(int profesorId) {
        String sql = "DELETE FROM materii WHERE profesor_id = ?";
        try (Connection conn = conectare();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setInt(1, profesorId);
            int count = pstmt.executeUpdate();
            System.out.println("Au fost sterse " + count + " materii ale profesorului cu id " + profesorId);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
