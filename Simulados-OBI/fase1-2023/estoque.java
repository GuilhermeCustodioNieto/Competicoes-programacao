// peça tem tipo e tamanho

// coluna = tamanho
// linha = tipo

// matriz [3][4]

// cada peça é um número

// Quando a peça é vendida, o estoque subtrai a quantidade que for vendida
// se a quantidade de peças for 0, não vamos subtrair

// na primeira linha vamos ver o tasmanho do estoque, sendo tipo e tamanho as entradas

// as proximas entradas são: quahtidadePeca, tipo, tamanho


import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class estoque{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);


        int quantidadeTipo = scan.nextInt();
        int quantidadeTamanho = scan.nextInt();

        int[][] estoque = new int[quantidadeTipo][quantidadeTamanho];


        // leitura linha a linha do estoque

        for(int i=0; i<=quantidadeTipo-1; i++){
            for(int j=0; j<=quantidadeTamanho-1; j++){
                estoque[i][j] = scan.nextInt();
            }
        }


        // ler pedio a pedido
        int quantidadePedidos = scan.nextInt();
        int quantidadeVendidos = 0;

        for(int i=0; i<= quantidadePedidos - 1; i++){
            int linhaVendida = scan.nextInt(), colunaVendida = scan.nextInt();
            if(estoque[linhaVendida - 1][colunaVendida - 1] != 0){
                estoque[linhaVendida - 1][colunaVendida - 1] -= 1;
            }

        }

        System.out.println(quantidadeVendidos);


        }



        public static void imprimeVetor(int[][] estoque, int quantidadeTipo, int quantidadeTamanho){
            for(int i=0; i<=quantidadeTipo-1; i++){
                System.out.print('[');
                for(int j=0; j<=quantidadeTamanho-1; j++){
                    System.out.print(estoque[i][j] + ", ");
                }
                System.out.println(']');
            }
        }
}