/*ILP506–Turma Manhã –Nome: Thiago da Silva   
 *
 * Funcionalidades extras:
 * 1. Tabela simples de formatação de saída
 */

import java.util.Random;
import java.util.Scanner;
public class Ex03{
	static int Min; 
	static int Max;
public static void main(String[] args){
	lerMin();
	lerMax();
	gera(Min,Max);
	System.out.print("=============== FIM ===============\n");
}
public static void lerMin(){
	Scanner ler = new Scanner(System.in);
	do{
		System.out.print("==================================\n . Valor minimo para codigo: ");
		Min = ler.nextInt();
		if (Min<10000) System.out.println("\n!!! Valor abaixo de 5 digitos...\n");
		if (Min > 99998) System.out.println("\n!!! Valor mínimo deve ser abaixo de 99999..\n");
	}while(Min<10000 || Min > 99998);
	}
public static void lerMax(){
	Scanner ler2 = new Scanner(System.in);
	do{
		System.out.print("----------------------------------\n . Valor maximo para codigo: ");
		Max = ler2.nextInt();
		if (Max <= Min) System.out.println("\n  !!! Valor máximo <= mínimo !!! \n");
		else if(Max > 99999) System.out.println("\n!!! Só podemos gerar até 5 dígitos\n");
	}while (Max<=Min || Max>99999 );
	System.out.print("==================================\n");
	ler2.close();
	}
public static void gera(int a, int b){
	Random gera = new Random();
	System.out.println("\n    Gerando...");
	int intervalo = b - a;
	int cod = a + gera.nextInt(intervalo + 1);
	System.out.println("\n         +===============+\n         |               |");
	System.out.println("         | Codigo: "+ cod+ " |");
	System.out.println("         |               |\n         +===============+");
	mod7(cod);
	}
public static void mod7(int x){
	int peso = 6, soma = 0;
	for (int i=0;i<5;i++){
		soma+=(x%10)*peso--;
		x/=10;
	}
	System.out.println("       Digito verificador: "+soma%7+"\n");
}
}
