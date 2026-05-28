package model;

public class Inscriere {
    private int id;
    private int studentId;
    private int materieId;

    public Inscriere(int id, int studentId, int materieId) {
        this.id = id;
        this.studentId = studentId;
        this.materieId = materieId;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getStudentId() {
        return studentId;
    }

    public void setStudentId(int studentId) {
        this.studentId = studentId;
    }

    public int getMaterieId() {
        return materieId;
    }

    public void setMaterieId(int materieId) {
        this.materieId = materieId;
    }

    @Override
    public String toString() {
        return "Inscriere{" +
                "id=" + id +
                ", studentId=" + studentId +
                ", materieId=" + materieId +
                '}';
    }
}