import java.util.Scanner;

public class Alfabeto {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		while(true) {
			int K = scan.nextInt(), N = scan.nextInt();
			
			if(K != 0 && N != 0) {
				String alfabeto = scan.next(), mensagem = scan.next();
				
				boolean saida = true;
				for(int j = 0; j<= mensagem.length() - 1; j++) {
					String letra = mensagem.substring(j, j + 1);
					
					if(!(alfabeto.indexOf(String.valueOf(letra)) >= 0)) {
						
						saida = false;
					} 
				}
				
				System.out.println(saida ? "Sim" : "Não");
			} else {
				break;
			}
			
			
			
		}
	}

}
