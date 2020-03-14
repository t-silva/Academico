import java.util.Random;
import java.util.Scanner;
public class e04{
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
		else if(Min>99998) System.out.println("  | - ERRO: Valor acima de 99998     |");//como maximo e 99999, valor maximo para
	}while(Min<10000 || Min>99998);								//min é 99998 pois se forem iguais, o
	}											//random da problema com nextInt(0).	
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
	Random gera = new Random();
	int C[] = new int[x];
	int D[] = new int[x];
	System.out.println("\n  +==================================+");
	System.out.println("  |    Codigo    |  Dig. Verificador |");
	System.out.println("  +==================================+");
	for (int i=0;i<x;i++){
		//int cod = 21468; //descomentar aqui para usar valores do exemplo 3.
		int cod = a + gera.nextInt(b - a);
		C[i] = cod;
		D[i] = mod7(cod);
		System.out.print("  |     "+ C[i] + "    ");
		System.out.println("|         "+ D[i] +"         |"+(i+1));
		System.out.println("  +--------------|-------------------+");
	}
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
