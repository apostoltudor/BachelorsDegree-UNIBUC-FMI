package dao;

import model.Student;
import model.StudentMaster;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class StudentDAO {
    private Connection connection;

    public StudentDAO() {
        try {
            connection = DriverManager.getConnection("jdbc:sqlite:catalog.db");
            Statement statement = connection.createStatement();
            statement.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY, nume TEXT, prenume TEXT, grupa TEXT, temaMaster TEXT)");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void create(Student student) {
        try {
            PreparedStatement ps;
            if (student instanceof StudentMaster) {
                StudentMaster sm = (StudentMaster) student;
                ps = connection.prepareStatement("INSERT INTO student (id, nume, prenume, grupa, temaMaster) VALUES (?, ?, ?, ?, ?)");
                ps.setInt(1, sm.getId());
                ps.setString(2, sm.getNume());
                ps.setString(3, sm.getPrenume());
                ps.setString(4, sm.getGrupa());
                ps.setString(5, sm.getTemaMaster());
            } else {
                ps = connection.prepareStatement("INSERT INTO student (id, nume, prenume, grupa) VALUES (?, ?, ?, ?)");
                ps.setInt(1, student.getId());
                ps.setString(2, student.getNume());
                ps.setString(3, student.getPrenume());
                ps.setString(4, student.getGrupa());
            }
            ps.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public Student read(int id) {
        try {
            PreparedStatement ps = connection.prepareStatement("SELECT * FROM student WHERE id = ?");
            ps.setInt(1, id);
            ResultSet rs = ps.executeQuery();
            if (rs.next()) {
                String temaMaster = rs.getString("temaMaster");
                if (temaMaster != null && !temaMaster.isEmpty()) {
                    return new StudentMaster(rs.getInt("id"), rs.getString("nume"), rs.getString("prenume"), rs.getString("grupa"), temaMaster);
                } else {
                    return new Student(rs.getInt("id"), rs.getString("nume"), rs.getString("prenume"), rs.getString("grupa"));
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    public void update(Student student) {
        try {
            PreparedStatement ps;
            if (student instanceof StudentMaster) {
                StudentMaster sm = (StudentMaster) student;
                ps = connection.prepareStatement("UPDATE student SET nume = ?, prenume = ?, grupa = ?, temaMaster = ? WHERE id = ?");
                ps.setString(1, sm.getNume());
                ps.setString(2, sm.getPrenume());
                ps.setString(3, sm.getGrupa());
                ps.setString(4, sm.getTemaMaster());
                ps.setInt(5, sm.getId());
            } else {
                ps = connection.prepareStatement("UPDATE student SET nume = ?, prenume = ?, grupa = ?, temaMaster = NULL WHERE id = ?");
                ps.setString(1, student.getNume());
                ps.setString(2, student.getPrenume());
                ps.setString(3, student.getGrupa());
                ps.setInt(4, student.getId());
            }
            ps.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void delete(int id) {
        try {
            PreparedStatement ps = connection.prepareStatement("DELETE FROM student WHERE id = ?");
            ps.setInt(1, id);
            ps.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public List<Student> getAll() {
        List<Student> students = new ArrayList<>();
        try {
            Statement statement = connection.createStatement();
            ResultSet rs = statement.executeQuery("SELECT * FROM student");
            while (rs.next()) {
                String temaMaster = rs.getString("temaMaster");
                if (temaMaster != null && !temaMaster.isEmpty()) {
                    students.add(new StudentMaster(rs.getInt("id"), rs.getString("nume"), rs.getString("prenume"), rs.getString("grupa"), temaMaster));
                } else {
                    students.add(new Student(rs.getInt("id"), rs.getString("nume"), rs.getString("prenume"), rs.getString("grupa")));
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return students;
    }
}