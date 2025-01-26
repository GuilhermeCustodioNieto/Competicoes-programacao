import java.util.Scanner;

public class Danca {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		int n, m, p;
		while ((n = scan.nextInt()) != 0) {
			m = scan.nextInt();
			p = scan.nextInt();

			int[][] pistaDanca = new int[n][m];

			int total = (n * m);

			int contadorTemp = 0;
			for (int l = 0; l <= n - 1; l++) {

				for (int c = 0; c <= m - 1; c++) {
					contadorTemp++;
					pistaDanca[l][c] = contadorTemp;
				}
			}

			
			for (int i = 0; i <= p - 1; i++) {

				String comando = scan.next();

				int a = scan.nextInt();
				int b = scan.nextInt();

				if (comando.equalsIgnoreCase("0") && a == 0 && b == 0) {
					break;
				}

				if (comando.equalsIgnoreCase("c")) {
					for (int linha = 0; linha <= n - 1; linha++) {
						int temp = pistaDanca[linha][a - 1];

						pistaDanca[linha][a - 1] = pistaDanca[linha][b - 1];

						pistaDanca[linha][b - 1] = temp;

					}
				} else if (comando.equalsIgnoreCase("l")) {
					for (int coluna = 0; coluna <= m - 1; coluna++) {
						int temp = pistaDanca[a - 1][coluna];
						pistaDanca[a - 1][coluna] = pistaDanca[b - 1][coluna];

						pistaDanca[b - 1][coluna] = temp;

					}
				}

			}
			for (int l = 0; l <= n - 1; l++) {
				for (int c = 0; c <= m - 1; c++) {
					System.out.print(pistaDanca[l][c] + " ");
				}
				System.out.println();
			}

		}

	}

	public static int[] encontraPosicao(int[][] pistaDanca, int busca) {
		int[] saida = new int[2];
		for (int l = 0; l <= pistaDanca.length - 1; l++) {
			for (int c = 0; c <= pistaDanca[l].length - 1; c++) {
				if (pistaDanca[l][c] == busca) {

					saida[0] = l;
					saida[1] = c;
					return saida;
				}
			}

		}
		return saida;
	}

}
