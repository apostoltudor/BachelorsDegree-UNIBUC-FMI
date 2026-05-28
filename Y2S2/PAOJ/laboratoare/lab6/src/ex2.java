public class ex2 {
    public enum Currency {
        EUR(4.95),
        USD(4.6),
        GBP(5.7);

        private final double exchangeRate;

        // Constructorul este privat implicit la enum
        Currency(double rate) {
            this.exchangeRate = rate;
        }

        public double convertToRON(double amount) {
            return amount * exchangeRate;
        }

        public double getExchangeRate() {
            return exchangeRate;
        }
    }

    public static void main(String[] args) {
        double amountInUSD = 100;
        double ronValue = Currency.USD.convertToRON(amountInUSD);
        System.out.println(amountInUSD + " USD în RON = " + ronValue);

        System.out.println("Curs GBP: " + Currency.GBP.getExchangeRate());
    }
}
