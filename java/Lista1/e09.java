import java.util.Scanner;
import java.util.ArrayList;
class e09{
	public static void main(String args[]){
		Scanner ler = new Scanner(System.in);
		ArrayList<Integer> lista = new ArrayList<Integer>();
		int min,max,x,tot=0,n;
		System.out.print("Maior valor: ");
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
		System.out.println("Vetor = "+lista);
		System.out.println("Total = "+tot);
		System.out.println("Elementos contabilizados = "+lista.size());
	}
}
/*O problema desse exercício é o tamanho do vetor. Usando vetores, eu posso estourar o limite e, em java
 não é possível realocar mais memória para o vetor, sendo necessário utilizar outro vetor e jogar o conteúdo do 
primeiro fora.*/
