import java.util.Scanner;
import java.util.ArrayList;
class e09{
	public static void main(String args[]){
		Scanner ler = new Scanner(System.in);
		ArrayList<Integer> lista = new ArrayList<Integer>(); //dizemos que o objeto existe e colocamos na 
		int min,max,x,tot=0,n;				    //classe correta, alocando memória. Podemos fazer na mesma 
		System.out.print("Maior valor: ");		    //linha, ou em linhas separadas. 
		max = ler.nextInt();					
		System.out.print("Maior valor: ");
		min = ler.nextInt();
		if (max<min) {
			System.out.println("Atenção, " +max+ "<"+min+"\nInvertendo Valores...");
			int aux = max;
			max = min;
			min = aux;
		}
		System.out.println("Intervalo: ["+min+","+max+"].");
		do{
			x = ler.nextInt();
			if (x <= max && x >= min && x != 0){
				lista.add(x);
				tot +=x;
			}
			else if(x!=0) System.out.println("Valor fora do intervalo");
		}while(x!=0);
		System.out.println("Vetor = "+lista); //Uma opção é utilizar o lista.get (dentro de um for, para exibir um 
		System.out.println("Total = "+tot);     //item por vez
		System.out.println("Elementos contabilizados = "+lista.size());
	}
}

