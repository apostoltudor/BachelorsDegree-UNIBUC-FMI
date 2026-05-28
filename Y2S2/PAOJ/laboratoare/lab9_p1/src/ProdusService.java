import java.sql.*;

public class ProdusService {

    private Connection conn;

    public ProdusService() {
        try {
            conn = DriverManager.getConnection(
                    "jdbc:mysql://localhost:3306/testdb", // numele bazei de date
                    "root",                               // utilizatorul tău MySQL
                    "1qaz2wsx"                             // parola ta
            );
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void adaugaProdus(Produs produs) {
        String sql = "INSERT INTO produse (id, nume, pret) VALUES (?, ?, ?)";

        try (PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setInt(1, produs.getId());
            ps.setString(2, produs.getNume());
            ps.setDouble(3, produs.getPret());
            ps.executeUpdate();
            System.out.println("Produs adăugat cu succes.");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void afiseazaProduse() {
        String sql = "SELECT * FROM produse";

        try (Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            System.out.println("Lista produselor din baza de date:");
            while (rs.next()) {
                int id = rs.getInt("id");
                String nume = rs.getString("nume");
                double pret = rs.getDouble("pret");
                System.out.println("ID: " + id + ", Nume: " + nume + ", Preț: " + pret);
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void stergeProduseSubPret(double pretMinim) {
        String sql = "DELETE FROM produse WHERE pret < ?";

        try (PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setDouble(1, pretMinim);
            int afectate = stmt.executeUpdate();
            System.out.println("Produse șterse: " + afectate);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void createTable() {
        String sql = "CREATE TABLE IF NOT EXISTS produse (" +
                "id INT PRIMARY KEY, " +
                "nume VARCHAR(100), " +
                "pret DOUBLE" +
                ")";
        try (Connection conn = DatabaseConfig.getConnection();
             Statement stmt = conn.createStatement()) {
            stmt.execute(sql);
            System.out.println("Tabela `produse` a fost creată (sau deja exista).");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void addProdus(Produs produs) {
        String sql = "INSERT INTO produse (id, nume, pret) VALUES (?, ?, ?)";
        try (Connection conn = DatabaseConfig.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setInt(1, produs.getId());
            pstmt.setString(2, produs.getNume());
            pstmt.setDouble(3, produs.getPret());
            pstmt.executeUpdate();
            System.out.println("Produsul a fost adăugat cu succes.");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void listProduse() {
        String sql = "SELECT * FROM produse";
        try (Connection conn = DatabaseConfig.getConnection();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
            while (rs.next()) {
                int id = rs.getInt("id");
                String nume = rs.getString("nume");
                double pret = rs.getDouble("pret");
                System.out.println("Produs: " + id + ", " + nume + ", " + pret);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void cautaSiActualizeazaProdus(String nume, double pretNou) {
        String sqlSelect = "SELECT * FROM produse WHERE nume = ?";
        String sqlUpdate = "UPDATE produse SET pret = ? WHERE nume = ?";

        try (PreparedStatement psSelect = conn.prepareStatement(sqlSelect)) {
            psSelect.setString(1, nume);
            ResultSet rs = psSelect.executeQuery();

            if (rs.next()) {
                try (PreparedStatement psUpdate = conn.prepareStatement(sqlUpdate)) {
                    psUpdate.setDouble(1, pretNou);
                    psUpdate.setString(2, nume);
                    int rowsUpdated = psUpdate.executeUpdate();
                    System.out.println("Prețul a fost actualizat pentru produsul \"" + nume + "\".");
                }
            } else {
                System.out.println("Produsul \"" + nume + "\" nu a fost găsit în baza de date.");
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

}
