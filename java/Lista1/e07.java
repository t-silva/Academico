import java.util.Scanner;
class e07{
public static void main(String args[]){
	int maior,menor,soma=0,n=0,x=1;
	Scanner ler = new Scanner(System.in); //A declaração de objeto necessita ser declarada para alocar memória.
	x=ler.nextInt();
	//Preciso colocar um if (x>0), pois valores negativos não entram no laço, e ficamos com um n = 0
	//dando problema na compilação, por conta de uma divisão por 0 no final.
	maior = x; 
	menor = x;
	do{
		if (x>0){
			soma += x;
			n++;
			if (x>maior) maior = x;
			else if(x<menor) menor = x;
		}
		x = ler.nextInt();
	}while(x>0);
	System.out.println("O maior é: " +maior);
	System.out.println("O menor é: " +menor);
	System.out.println("Média: " + (soma/n));
	

}

}
