package model;

public class Atribuire {
    private int id;
    private int profesorId;
    private int materieId;

    public Atribuire(int id, int profesorId, int materieId) {
        this.id = id;
        this.profesorId = profesorId;
        this.materieId = materieId;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getProfesorId() {
        return profesorId;
    }

    public void setProfesorId(int profesorId) {
        this.profesorId = profesorId;
    }

    public int getMaterieId() {
        return materieId;
    }

    public void setMaterieId(int materieId) {
        this.materieId = materieId;
    }

    @Override
    public String toString() {
        return "Atribuire{" +
                "id=" + id +
                ", profesorId=" + profesorId +
                ", materieId=" + materieId +
                '}';
    }
}