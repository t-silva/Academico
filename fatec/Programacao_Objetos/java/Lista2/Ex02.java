/*ILP506–Turma Manhã –Nome: Thiago da Silva   
 * Atenções: 1) intervalos considerado pela classe random;
 *           2) Necessidade de conseguir fechar o Scanner em cada método;
 */

import java.util.Random;
import java.util.Scanner;
public class Ex02{
	static int Min; 
	static int Max;
public static void main(String[] args){
	lerMin();
	lerMax();
	gera(Min,Max);
}
public static void lerMin(){
	Scanner ler = new Scanner(System.in);
	do{
		System.out.print("===================================\n . Valor minimo para codigo: ");
		Min = ler.nextInt();
		if (Min<10000) System.out.println("\n ! ! ! Valor abaixo de 5 digitos...\n");
		if (Min > 99998 ) System.out.println("\n ! ! ! Valor mínimo inválido para o intervalo \n Solução: Tente um valor abaixo de 99999"); 
	}while(Min<10000 || Min > 99998);
//	ler.close(); //!nao consigo fechar objeto aqui, o .close provavelmente fecha o objeto, e o System.in.
	}
public static void lerMax(){
	Scanner lerMax = new Scanner(System.in);
	do{
		System.out.print("-----------------------------------\n . Valor maximo para codigo: ");
		Max = lerMax.nextInt();
		if (Max < Min) System.out.println("\n!!! Valor máximo < mínimo !!! \n");
		else if(Max > 99999) System.out.println("!!! Só podemos gerar até 5 dígitos");
	}while (Max<Min || Max>99999 );
	System.out.print("===================================\n");
	lerMax.close();
}
public static void gera(int a, int b){
	Random gera = new Random();
	System.out.println("\nGerando...");
	int intervalo = b - a;
	int cod = a + gera.nextInt( intervalo + 1 ); /*Soma-se um para poder manter o intervalo fechado no máximo.
						       Ex. gera.nextInt(1) - só retorna 1 valor possível: 0;
						           gera.nextInt(2) - retorna 0 e 1;
						       */
	System.out.println("\n   +===============+\n   |               |");
	System.out.println("   | Codigo: "+ cod+ " |");
	System.out.println("   |               |\n   +===============+\n");
}
}
