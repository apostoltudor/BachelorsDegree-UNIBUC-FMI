package service;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DatabaseConnection {
    private static final String URL = "jdbc:mysql://localhost:3306/testdb";
    private static final String USER = "root";
    private static final String PASSWORD = "1qaz2wsx";

    private static Connection connection = null;

    private DatabaseConnection() {}

    public static Connection getConnection() {
        if (connection == null) {
            try {
                connection = DriverManager.getConnection(URL, USER, PASSWORD);
                System.out.println("Conexiune realizata cu succes la baza de date.");
            } catch (SQLException e) {
                System.out.println("Eroare la conectarea la baza de date: " + e.getMessage());
            }
        }
        return connection;
    }
}
