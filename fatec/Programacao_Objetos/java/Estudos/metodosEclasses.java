import java.util.Scanner; // Importando classe Scanner
public class metodosEclasses { //declarando Classe que iniciará a execução do programa;
	public static void main(String[] args){ // Criando método main(). Existente apenas na classe MetodosEclasses
	Scanner ler = new Scanner(System.in);  // Instanciando classe Scanner, alocando memória dentro de um objeto (ler);
	Retangulo r = new Retangulo();	      // Instanciando classe Retangulo, alocando memório dentro de um objeto (r);
	System.out.print("Digite o valor da base: ");
	r.setBase(ler.nextDouble()); //Utilizando atributo base no objeto r, já instanciado com a classe Retangulo;
	System.out.print("Digite o valor da altura: ");
	r.setAltura(ler.nextDouble()); //Utilizando atributo base no objeto r, já instanciado com a classe Retangulo;
	System.out.println("Area do Retangulo = " + r.calcArea()); 
	// O print da tela chama o método calcArea(), pertencente à classe Retaungulo. Que retornará o valor calculado.
	}
}
//public class Retangulo{ // Declarando classe Retangulo. 
//	private double base; // Atributos dessa classe incluirao base (double) e altura(double)
//	private double altura;
//	public double setBase(double valor){
//		base = valor;
//		return base;
//	}	
//	public double setAltura(double valor){
//		altura = valor;
//		return valor;
//	}
//	public double calcArea(){ //Método calcArea, vinculado a classe Retangulo, que retorna a conta necessária para o
//		return(base * altura); //cálculo da área.
//	}
//}
//
