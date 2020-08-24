/*ILP506–Turma Manhã –Nome: Thiago da Silva   
 *
*/

import java.util.Scanner;
public class Ex01{
	public static void main(String[] args){ 
		int Menor = min();
		int Maior = max(Menor);
		prim(Menor,Maior);
	}
	public static int min(){ // se removo o 'static', o método min não pode ser refenciado do main (static);
		Scanner ler = new Scanner(System.in);
		int Min; 
		do{
			System.out.print("Digite o valor minimo: ");
			Min = ler.nextInt();
			if ( Min < 10000 ) 
				System.out.println( "Valor deve ser pelo menos 10000" );
			if ( Min > 99998 ) 
				System.out.println( "\n! ! ! ERRO: Valor mínimo muito alto. Escolha entre 10000 e 99998 ! ! !\n" ); //Como valor máximo é 99999, há a necessidade de estabalecer um teto;
		} while( Min < 10000 || Min > 99998);
		return Min;
	}
	public static int max(int compara){
		int Max;
		Scanner ler = new Scanner(System.in);
		do{
			System.out.print("Digite o valor maximo: ");
			Max = ler.nextInt();
			if ( Max < compara ) System.out.println("\n! ! ! ERRO: Valor maximo menor que o minimo:\n\n  Max("+Max+") < Min("+compara+") \n");
		}while(Max < compara || Max > 99999);
		return Max;
	}
	public static void prim(int menor, int maior){
		int count = 0;
		for (int i= menor; i <= maior; i++){
			boolean p = true;
			int div = 2;
			while (div<i && p) if (i%div++==0) p=false;
			if (p) {
				System.out.println("Número "+i+" e primo");
				count++;
			}
		} 
		System.out.println("\n Foram encontrados "+count+" números primos.");
	}
}
