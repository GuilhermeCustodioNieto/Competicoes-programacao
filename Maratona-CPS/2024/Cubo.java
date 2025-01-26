import java.util.Scanner;

public class Cubo {
	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		
		int dimensao = 1;
		while(true) {
			dimensao = scan.nextInt();
			if(dimensao == 0) {
				break;
			}
			

			int total = (dimensao * dimensao * dimensao);
			
			System.out.println((int) Math.pow(dimensao - 2, 3));
			System.out.println((int) ((dimensao - 2) * (dimensao - 2)) * 6);
			System.out.println((int) (dimensao - 2) * 12);
			System.out.println(8);
		}
	}
}
