import java.util.Scanner;
class e08{
public static void main(String args[]){
	Scanner ler = new Scanner(System.in);
	int tot=0,n=0,x;
	System.out.print("Maior valor: ");
	int maior = ler.nextInt();
	System.out.print("Menor valor: ");
	int menor = ler.nextInt();
	if (maior<menor) {
		System.out.println("ATENÇÃO!"+maior+"<"+menor+".\nInvertendo valores: ");
		int aux = maior;
		maior = menor;
		menor = aux;
	}
	System.out.println("Intervalo: ["+menor+","+maior+"]");
	do{
		x= ler.nextInt();
		//if (x>=menor && x<=maior && x!=0){ //aqui não contaria o 0 se estivesse no intervalo
		if (x>=menor && x<=maior && x!=0){
			tot+=x;
			n++;
		}
		else if (x!=0) System.out.println("Valor fora do intervalor ["+menor+","+maior+"]");

	}while(x!=0);
	System.out.println("Total: " +tot+ "\nNumero de entradas: "+n);

	}
}
