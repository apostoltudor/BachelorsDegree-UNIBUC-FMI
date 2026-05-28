public class ex3 {
    public class Persoana {
        private String nume;
        private int varsta;
        private double[] venit;
        private static int nrPersoane;
        private int id;
//constructor implicit
        public Persoana(){
            this.nume = "Necunoscut";
            this.varsta = 0;
            this.venit = new double[12];
            nrPersoane++;
            this.id = nrPersoane;
        }
//constructor parametrizat
        public Persoana(String nume, int varsta, double[] venit){
            this.nume = nume;
            this.varsta = varsta;
            this.venit = venit;
            nrPersoane++;
            this.id = nrPersoane;
        }
//constructor de copiere
        public Persoana(Persoana other) {
            this.nume = other.nume;
            this.varsta = other.varsta;

            //deep copy la array
            this.venit = new double[12];
            for (int i = 0; i < 12; i++) {
                this.venit[i] = other.venit[i];
            }
        }


    }

}
