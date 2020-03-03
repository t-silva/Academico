import java.util.Scanner;
class e04{
	public static void main(String args[]){
	Scanner ler;
	ler = new Scanner(System.in);
	System.out.println("LADO A");
	double a = ler.nextDouble();
	System.out.println("LADO B");
	double b = ler.nextDouble();
	System.out.println("LADO C");
	double c = ler.nextDouble();
	if (a+b > c && a+c>b && b+c > a){
		if (a==b || b==c)
			System.out.println("Triangulo isosceles");
		else if(a==b || a==c | b==c)
			System.out.println("Triangulo equilatero");
		else
			System.out.println("Triangulo escaleno");
	}
	else
		System.out.println("Nao e triangulo");
	}
}
