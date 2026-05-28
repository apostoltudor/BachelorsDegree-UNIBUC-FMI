package model;

public class Nota {
    private int id;
    private int studentId;
    private int materieId;
    private double valoare;

    public Nota(int id, int studentId, int materieId, double valoare) {
        this.id = id;
        this.studentId = studentId;
        this.materieId = materieId;
        this.valoare = valoare;
    }

    public int getId() {
        return id;
    }

    public int getStudentId() {
        return studentId;
    }

    public int getMaterieId() {
        return materieId;
    }

    public double getValoare() {
        return valoare;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setStudentId(int studentId) {
        this.studentId = studentId;
    }

    public void setMaterieId(int materieId) {
        this.materieId = materieId;
    }

    public void setValoare(double valoare) {
        this.valoare = valoare;
    }

    @Override
    public String toString() {
        return "Nota{id=" + id +
                ", studentId=" + studentId +
                ", materieId=" + materieId +
                ", valoare=" + valoare + "}";
    }
}
