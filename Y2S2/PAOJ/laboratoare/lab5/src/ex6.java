import java.sql.SQLException;

public class ex6 {

    // 1. Interfața
    public interface DatabaseActions {
        void connect() throws IllegalStateException;
        void executeQuery(String query) throws SQLException;
    }

    // 2. Clasa FakeDatabase
    public static class FakeDatabase implements DatabaseActions {
        private boolean online;

        public FakeDatabase(boolean online) {
            this.online = online;
        }

        @Override
        public void connect() {
            if (!online) {
                throw new IllegalStateException("Database is offline. Cannot connect.");
            }
            System.out.println("Connected to the database.");
        }

        @Override
        public void executeQuery(String query) throws SQLException {
            if (query == null || query.trim().isEmpty()) {
                throw new SQLException("Query is invalid (null or empty).");
            }
            System.out.println("Executing query: " + query);
        }
    }

    // 3. Main
    public static void main(String[] args) {
        FakeDatabase db = new FakeDatabase(false); // pornește baza ca offline

        try {
            db.connect(); // va arunca IllegalStateException
            db.executeQuery(""); // nu se execută, pentru că nu ajunge aici
        } catch (IllegalStateException e) {
            System.out.println("Eroare la conectare: " + e.getMessage());
        } catch (SQLException e) {
            System.out.println("Eroare la interogare: " + e.getMessage());
        }

        // Reîncercăm cu baza online
        db = new FakeDatabase(true);
        try {
            db.connect(); // acum funcționează
            db.executeQuery(""); // aruncă SQLException
        } catch (IllegalStateException e) {
            System.out.println("Eroare la conectare: " + e.getMessage());
        } catch (SQLException e) {
            System.out.println("Eroare la interogare: " + e.getMessage());
        }
    }
}
