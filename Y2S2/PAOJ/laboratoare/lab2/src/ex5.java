import java.util.Arrays;

public class ex5 {
    public static class Student implements Comparable<Student>{

        @Override
        public int compareTo(Student altStudent){
            return Double.compare(this.medie, altStudent.medie);
        }

        private String nume;
        private int varsta;
        private double medie;

        //constructor implicit
        public Student(){
            this.nume = "Necunoscut";
            this.varsta = -1;
            this.medie = -1;
        }

        //constructor parametrizat
        public Student(String nume, int varsta, double medie){
            this.nume = nume;
            this.varsta = varsta;
            this.medie = medie;
        }

        //getteri
        public String getNume(){
            return nume;
        }
        public int getVarsta(){
            return varsta;
        }
        public double getMedie(){
            return medie;
        }

        //setteri
        public void setNume(String nume){
            this.nume = nume;
        }
        public void setVarsta(int varsta){
            this.varsta = varsta;
        }
        public void setMedie(double medie){
            this.medie = medie;
        }

        public static void afisareStudenti(Student[] studenti) {
            for (Student s : studenti) {
                System.out.println(s.getNume() + ", " + s.getVarsta() + ", " + s.getMedie());
            }
        }

    }

    public static void main(String[] args){
        Student[] studenti = new Student[5];
        studenti[0] = new Student("Ion", 20, 3.5);
        studenti[1] = new Student("Andrei", 21, 4.0);
        studenti[2] = new Student("Maria", 22, 3.0);
        studenti[3] = new Student("Vasile", 23, 3.7);
        studenti[4] = new Student("Gigel", 24, 2.5);
        Arrays.sort(studenti);
        Student.afisareStudenti(studenti);
    }
}
