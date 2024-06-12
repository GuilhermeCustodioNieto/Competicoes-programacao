import java.util.*;

public class jogo {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int numLinhas = scan.nextInt();
        int numPassos = scan.nextInt();

        int[][] matriz = new int[numLinhas][numLinhas];


        // resetando a matriz
        for (int i =0; i<numLinhas; i++){
            for (int j = 0; j < matriz[i].length; j++) {
                matriz[i][j] = 0;
            }
        }

        // populando matriz
        for (int i = 0; i < matriz.length; i++) {
            String valores = scan.next();
            int[] valoresInt = repartirValores(valores);

            for (int j = 0; j < matriz[i].length; j++) {
                matriz[i][j] = valoresInt[j];
            }


        }

        // Processamento
        for(int i=0; i<numPassos; i++){

        }



        pegarAoRedor(matriz, 2, 1);

    }

   public static int[] repartirValores(String valores){
        int[] listaValores = new int[valores.length()];

       for (int i = 0; i < valores.length(); i++) {
           if(valores.charAt(i) == '0'){
               listaValores[i] = 0;
           }else if(valores.charAt(i) == '1'){
               listaValores[i] = 1;
           }
       }

       return listaValores;
   }

   public static void imprimirMatriz(int[][] matriz){
       for (int i = 0; i < matriz.length; i++) {
           for (int j = 0; j < matriz[i].length; j++) {
               System.out.print(matriz[i][j] + ", ");
           }

           System.out.println();
       }
   }

   public static int[] pegarAoRedor(int[][] matriz, int linhaValor, int colunaValor){
        int[] matrizRetorno = new int[8];

       int contadorRetorno = 0;

       for (int i = colunaValor - 1; i < colunaValor + 2; i++) {
           matrizRetorno[contadorRetorno] = matriz[linhaValor - 1][i];

           contadorRetorno++;
       }


       for (int i = colunaValor - 1; i < colunaValor + 2; i++) {
           if(i != colunaValor) {
               matrizRetorno[contadorRetorno] = matriz[linhaValor][i];

               contadorRetorno++;
           }
       }


       for (int i = colunaValor - 1; i < colunaValor + 2; i++) {
           matrizRetorno[contadorRetorno] = matriz[linhaValor + 1][i];

           contadorRetorno++;
       }
       return matrizRetorno;
   }





}
