/*ILP506–Turma Manhã –Nome: Thiago da Silva   
 *
 * Funcionalidades extras:
 * 1. Tabela que se formata sozinha.
 * 	Métodos: 
 * 	a) digitos(int x): calcula  quantidade de dígitos necessários, de acordo com um número inteiro.
 * 	b) completa(int N, int M, char C): Calcula quantos caracteres (C), são necessários para um inteiro N para se adaptar a quantidade de caracteres de um número maior(M)
 */

import java.util.Random;
import java.util.Scanner;
public class Ex4{
	static Scanner ler = new Scanner(System.in);
	static int Min; 
	static int Max;
public static void main(String[] args){
	System.out.println("\n  +==================================+");
	System.out.println("  |   Iniciando gerador de codigos   |");
	System.out.println("  |           de 5 digitos           |");  
	lerMin();
	lerMax();
	System.out.print("  | . Numero de codigos a gerar: ");
	int N = ler.nextInt();
	System.out.println("  +==================================+");
	gera(Min,Max,N);
}
public static void lerMin(){
	Scanner ler = new Scanner(System.in);
	do{
		System.out.print("  +==================================+\n  | .Valor minimo para codigo: ");
		Min = ler.nextInt();
		if (Min<10000)     System.out.println("  | - ERRO: Valor abaixo de 5 digitos|");
		else if(Min>99998) System.out.println("  | - ERRO: Valor acima de 99998     |");//como maximo e 99999, valor maximo para min é 99998
	}while(Min<10000 || Min>99998);								//pois se forem iguais, o random da problema com nextInt(0). 
	}										
public static void lerMax(){
	Scanner ler = new Scanner(System.in);
	do{
		System.out.print("  +----------------------------------+\n  | .Valor maximo para codigo: ");
		Max = ler.nextInt();
		if (Max <= Min) System.out.println("  |  - ERRO: Valor máximo <= mínimo! |");
		else if(Max > 99999) System.out.println("  |    - ERRO: Excedeu 5 digitos     |");
	}while (Max<=Min || Max>99999 );
	System.out.println("  +==================================+");
	}
public static void gera(int a, int b, int x){
	int C[] = new int[x];
	int D[] = new int[x];
	Random gera = new Random();
	int intervalo = b - a;
	for (int i=0;i<x;i++){
		C[i] = a + gera.nextInt(intervalo+1);
		D[i] = mod7(C[i]);
	}
	exibe(C,D,x);
}
public static void exibe(int[] C,int[] D,int x){
	int dig = digitos(x);
	System.out.print("\n  +===");
		completa(1,dig,'=');
	System.out.println("+==========+===================+");
	System.out.print("  | N ");
		completa(1,dig,' ');
	System.out.println("|  Codigo  |  Dig. Verificador |");
	System.out.print("  +===");
                completa(1,dig,'=');
        System.out.println("+==========+===================+");
	for (int i=0;i<x;i++){
		System.out.print("  | "+(i+1)+" ");
		completa(i+1,dig,' ');
	       	System.out.print("|   "+ C[i] + "  ");
		System.out.println("|         "+ D[i] +"         |");
		System.out.print("  +---");
		completa(1,dig,'-');
		System.out.println( (i==(x-1))? "+------------------------------+\n":"+----------|-------------------+");
	}
}
public static void completa(int N, int M, char C){
	int i = 1;
	int aux = M - digitos (N);
	while ( i++ <= aux) System.out.print(C); 
}
public static int digitos(int x){
	int tam  = 0;
	int tmp = 1;
	while ( tmp <= x){
		tam++;
		tmp *= 10;
	}
	return tam;
}
public static int mod7(int x){
	int peso = 6, soma = 0;
	for (int i=0;i<5;i++){
		soma+=(x%10)*peso--;
		x/=10;
	}
	return soma%7;
}
}
