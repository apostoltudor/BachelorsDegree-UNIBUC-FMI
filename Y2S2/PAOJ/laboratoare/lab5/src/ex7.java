import java.util.*;

public class ex7 {
    public static class Product {
        private int id;
        private String name;
        private double price;

        public Product(int id, String name, double price) {
            this.id = id;
            this.name = name;
            this.price = price;
        }

        public int getId() {
            return id;
        }

        public String getName() {
            return name;
        }

        public double getPrice() {
            return price;
        }

        @Override
        public String toString() {
            return "Product{id=" + id + ", name='" + name + "', price=" + price + "}";
        }
    }

    public static void main(String[] args) {
        List<Product> produse = new ArrayList<>();

        // Adăugăm produse în listă
        produse.add(new Product(1, "Laptop", 3200.50));
        produse.add(new Product(2, "Telefon", 1800.00));
        produse.add(new Product(3, "Monitor", 950.99));
        produse.add(new Product(4, "Tastatură", 250.00));

        // Afișare inițială
        System.out.println("Produse inițiale:");
        for (Product p : produse) {
            System.out.println(p);
        }

        // Sortare după preț
        produse.sort(new Comparator<Product>() {
            @Override
            public int compare(Product a, Product b) {
                return Double.compare(a.getPrice(), b.getPrice());
            }
        });

        // Afișare cu Iterator
        System.out.println("\nProduse sortate după preț:");
        Iterator<Product> it = produse.iterator();
        while (it.hasNext()) {
            Product p = it.next();
            System.out.println(p);
        }
    }
}
