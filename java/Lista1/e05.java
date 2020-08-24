import java.util.Scanner;
class e05{
	public static void main(String Args[]){
	Scanner ler;
	String resposta;
	ler = new Scanner(System.in);
	System.out.println("Nome fornecido:");
	String nome = ler.nextLine();
	System.out.println("Peso fornecido:");
	double peso = ler.nextDouble();
	if (peso < 65)
		resposta = "Pena";
	else if(peso >= 65 && peso < 72)
		resposta = "Leve";
	else if(peso >=72 && peso<79)
		resposta = "Ligeiro";
	else if(peso >= 79  && peso<86)
		resposta = "Meio Médio";
	else if(peso >= 86 && peso<93)
		resposta = "Médio";
	else if(peso >= 93 && peso<100)
		resposta = "Meio Pesado";
	else 
		resposta = "Pesado";

	System.out.println("O lutador "+nome+" pesa "+peso+"Kg e se enquadra na categoria "+resposta+"." );
	}
}
