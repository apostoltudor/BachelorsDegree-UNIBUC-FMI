public class ex1 {

    // 1. Enum pentru statusurile comenzii
    public enum OrderStatus {
        PLACED,
        SHIPPED,
        DELIVERED,
        CANCELLED
    }

    // 2. Clasa Order
    public static class Order {
        private int id;
        private OrderStatus status;

        // Constructor
        public Order(int id) {
            this.id = id;
            this.status = OrderStatus.PLACED; // implicit o comandă e plasată
        }

        // Metodă pentru schimbarea statusului
        public void shipOrder() {
            this.status = OrderStatus.SHIPPED;
        }

        public void deliverOrder() {
            this.status = OrderStatus.DELIVERED;
        }

        public void cancelOrder() {
            this.status = OrderStatus.CANCELLED;
        }

        // Metodă pentru afișarea statusului
        public void printStatus() {
            System.out.println("Order #" + id + " is currently: " + status);
        }
    }

    // 3. Main pentru testare
    public static void main(String[] args) {
        Order o1 = new Order(101);
        o1.printStatus();         // PLACED
        o1.shipOrder();           // schimbă în SHIPPED
        o1.printStatus();         // SHIPPED
        o1.deliverOrder();        // schimbă în DELIVERED
        o1.printStatus();         // DELIVERED

        Order o2 = new Order(102);
        o2.cancelOrder();
        o2.printStatus();         // CANCELLED
    }
}
