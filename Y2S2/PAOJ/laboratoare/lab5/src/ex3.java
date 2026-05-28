// Clasa excepției personalizate
class InvalidGradeException extends Exception {
    public InvalidGradeException(String message) {
        super(message);  // transmite mesajul clasei Exception
    }
}

public class ex3 {
    // Metodă care validează o notă
    public static void validateGrade(int grade) throws InvalidGradeException {
        if (grade < 1 || grade > 10) {
            throw new InvalidGradeException("Nota trebuie să fie între 1 și 10. Ai introdus: " + grade);
        } else {
            System.out.println("Nota este validă: " + grade);
        }
    }

    public static void main(String[] args) {
        try {
            validateGrade(9);   // OK
            validateGrade(0);   // INVALID → aruncă excepție
        } catch (InvalidGradeException e) {
            System.out.println("A apărut o eroare: " + e.getMessage());
        }
    }
}
