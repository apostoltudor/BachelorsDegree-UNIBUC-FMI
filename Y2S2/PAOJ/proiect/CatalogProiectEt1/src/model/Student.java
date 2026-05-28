package model;

public class Student {
    private int id;
    private String nume;
    private String prenume;
    private String grupa;

    public Student(int id, String nume, String prenume, String grupa) {
        this.id = id;
        this.nume = nume;
        this.prenume = prenume;
        this.grupa = grupa;
    }

    public int getId() { return id; }
    public String getNume() { return nume; }
    public String getPrenume() { return prenume; }
    public String getGrupa() { return grupa; }

    public void setNume(String nume) { this.nume = nume; }
    public void setPrenume(String prenume) { this.prenume = prenume; }
    public void setGrupa(String grupa) { this.grupa = grupa; }

    @Override
    public String toString() {
        return "Student{id=" + id + ", nume='" + nume + "', prenume='" + prenume + "', grupa='" + grupa + "'}";
    }
}