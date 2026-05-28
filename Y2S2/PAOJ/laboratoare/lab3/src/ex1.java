public class ex1 {
    public static class MathUtil{

        int multiply(int a, int b){
            return a*b;
        }
        double multiply(double a, double b, double c){
            return a*b*c;
        }
        int multiply(int[] values){
            int a = 1;
            for(int x : values){
                a = a * x;
            }
            return a;
        }
    }

    public static void main(String[] args){
        System.out.println(new MathUtil().multiply(2,3));
        System.out.println(new MathUtil().multiply(2,3, 5.2));
        int[] x = {1, 2, 3, 4, 5};
        System.out.println(new MathUtil().multiply(x));
    }
}