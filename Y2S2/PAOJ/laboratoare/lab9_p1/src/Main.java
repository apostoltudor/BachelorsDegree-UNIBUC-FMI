public class Main {
    public static void main(String[] args) {
        ProdusService service = new ProdusService();

        // Adăugăm un Produs nou
        Produs produs1 = new Produs(1, "Telefon", 5.0);
        Produs produs2 = new Produs(2, "Laptop", 2678.9);

        service.adaugaProdus(produs1);
        service.adaugaProdus(produs2);


        service.cautaSiActualizeazaProdus("Laptop", 9876.5);

        service.afiseazaProduse();

        // Exemplu de apel
        service.stergeProduseSubPret(15.0);

        // Afișăm toate produsele după actualizare
        service.afiseazaProduse();

    }
}
