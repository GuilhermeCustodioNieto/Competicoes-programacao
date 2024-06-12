import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class toupeiras {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        List<List<Integer>> grafo = new ArrayList<>();


        // Entrada de dados
        // 1. quantidade de salões e tuneis
        // 2. Lê T linhas, representando túneis, qeu recebe X e Y, que indicam os túneis conectados
        // 3. Quantidade de sugestões de passeio
        // 4. Lê cada sugestão de passeio, onde o primeiro número representa a quantidade de tuneis, e os valores a seguir (na mesma linha) são os túneis em sequência de passeio


        //passo 1
        int quantidadeSaloes = scan.nextInt();
        int quantidadeTuneis = scan.nextInt();



        for (int i = 0; i < quantidadeSaloes; i++) {
            grafo.add(new ArrayList<>());
            grafo.getLast().add(i+1);
        }

        //passo 2
        for (int i = 0; i < quantidadeTuneis; i++) {
            addAresta(grafo, scan.nextInt(), scan.nextInt());
        }

        //passo 3
        int contadorFinal = 0;

        List<List<Integer>> matriz = new ArrayList<>();

        int quantidadeCaminhosPossiveis = scan.nextInt();
        for (int i=0; i<quantidadeCaminhosPossiveis; i++){
            matriz.add(new ArrayList<>());
            int quantidadeCamaras = scan.nextInt()  ;
            for (int j = 0; j < quantidadeCamaras ; j++) {
                matriz.getLast().add(scan.nextInt());
            }

        }

        for (int i=0; i<matriz.size(); i++) {
            List<Integer> linha = matriz.get(i);
            boolean caminhoBom = true;
            for (int j = 0; j < linha.size(); j++) {



                    for (int x =0; x<grafo.size(); x++){
                        if(grafo.get(x).getFirst() == linha.get(j)){
                            if(!grafo.get(x).contains(linha.get(j)  - 1)){
                                caminhoBom = false;
                                System.out.println("Não é mais correto");
                            }
                        }
                    }





            }
            if(caminhoBom){
                contadorFinal++;
            }

        }


        System.out.println(contadorFinal);


    }

    public static void addAresta(List<List<Integer>> grafo, int v1, int v2){
        for (int i =0; i<grafo.size(); i++){
            if(grafo.get(i).getFirst() == v1){
                grafo.get(i).add(v2);
            }
        }

        for (int i =0; i<grafo.size(); i++){
            if(grafo.get(i).getFirst() == v2){
                grafo.get(i).add(v1);
            }
        }

    }

    public static void printGrafo(List<List<Integer>> grafo) {
        for (int i = 0; i < grafo.size(); i++) {
            System.out.print("Vértice " + i + ":");
            for (int j : grafo.get(i)) {
                System.out.print(" -> " + j);
            }
            System.out.println();
        }
    }
}
