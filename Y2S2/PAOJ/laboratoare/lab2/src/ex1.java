import java.util.Arrays;

public class ex1{
    public static void main(String[] args){
        int[] array = new int[10];
        for (int i = 0;i<10;i++){
            array[i] = i;
        }
        for(int i=0;i<10;i++){
            System.out.print(array[i] + " ");
        }
        System.out.println();

        System.out.println(Arrays.toString(array));

        for( int x : array){
            System.out.print(x + " ");
        }
    }
}