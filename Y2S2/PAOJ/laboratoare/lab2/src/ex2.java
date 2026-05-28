import java.util.Arrays;

public class ex2 {
    public static void main(String[] args){
        int[][] array = new int[3][];
        array = new int[][]{{1,2,3}, {4,5}, {6,7,8,9}};
        for(int i=0;i<array.length;i++){
            for(int j=0;j<array[i].length;j++){
                System.out.print(array[i][j] + " ");
            }
            System.out.println();
        }

        System.out.println();

        for(int[] x : array){
            for(int y : x){
                System.out.print(y + " ");
            }
            System.out.println();
        }
    }
}
