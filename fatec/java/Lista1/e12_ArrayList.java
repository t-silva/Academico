import java.util.Scanner;
import java.util.Random;
import java.util.ArrayList;
class e12_ArrayList{
	public static void main(String args[]){
		Scanner ler =  new Scanner(System.in);
		int N=0;
		while(N<=0 || N>50){
			System.out.print("Quantos elementos no vetor (Entre 1 e 50): ");
			N = ler.nextInt();

		}
		ArrayList<Integer> R = new ArrayList<Integer>();
		Random gera = new Random();
		for (int i=0;i<N;i++){
			R.add(-10+gera.nextInt(20));
		}
		System.out.println("Vetor: " +R);
		int x;
		while(1==1){
			System.out.print("\nDigite um valor para eliminar: ");
			x = ler.nextInt();
			Boolean resp = R.contains(x);
			while (R.contains(x)) R.remove(Integer.valueOf(x));
			System.out.println("Vetor: " +R);
		}
	}
}
