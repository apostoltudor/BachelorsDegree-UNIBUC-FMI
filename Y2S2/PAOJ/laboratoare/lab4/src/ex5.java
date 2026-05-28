public class ex5 {
    public static void main(String[] args){
        String original = "Hello";
        String upper = original.toUpperCase();

        System.out.println("Original: " + original);
        System.out.println("Upper: " + upper);


        StringBuilder sb = new StringBuilder("Salut");
        sb.append(" lume");
        sb.insert(sb.length()-1, ">> ");
        sb.delete(0, 3);

        System.out.println("Rezultat: " + sb);


        StringBuffer sbf = new StringBuffer("Ana");
        sbf.append(" are mere");
        sbf.insert(0, ">> ");
        sbf.delete(0, 3);

        System.out.println("Rezultat: " + sbf);
    }
}
