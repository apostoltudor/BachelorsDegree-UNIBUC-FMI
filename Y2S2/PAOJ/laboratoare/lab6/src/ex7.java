public class ex7 {

    // Interfața Logger
    public interface Logger {
        // Metodă default (poate fi folosită fără a fi suprascrisă)
        default void log(String msg) {
            System.out.println("[LOG] " + msg);
        }

        // Metodă statică (se apelează direct cu numele interfeței)
        static boolean isEmpty(String str) {
            return str == null || str.isEmpty();
        }
    }

    // Clasa care implementează Logger
    public static class ConsoleLogger implements Logger {
        public void processMessage(String mesaj) {
            if (Logger.isEmpty(mesaj)) {
                log("Mesajul este gol sau null.");
            } else {
                log("Mesajul primit: " + mesaj);
            }
        }
    }

    public static void main(String[] args) {
        ConsoleLogger logger = new ConsoleLogger();
        logger.processMessage("Salut!");
        logger.processMessage("");
        logger.processMessage(null);
    }
}
