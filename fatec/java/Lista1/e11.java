import java.util.Scanner;
import java.util.Random;
class e10{
	public static void main(String args[]){
		Scanner ler;
		ler = new Scanner(System.in);
		System.out.print("Numero de entradas: ");
		int N = ler.nextInt();
		if (N<0 || N>50){
			System.out.println("Valor deve estar entre 0 e 50!");
			//break;
		}
		else{
			Random gera = new Random();
				int R[]=new int[N];
				System.out.print("R = [");
			for (int i=0;i<N;i++){
				R[i] = -3000 + gera.nextInt(6000);
				System.out.print(i<N-1? R[i]+",":R[i]+"]");
			}
			int x=1;
			while(x!=0){
				System.out.print("\nDigite um valor para buscar no vetor: ");
				x = ler.nextInt();
				int prim=0;
				for (int i=0;i<N;i++){
					if ( x == R[i] ) {
						System.out.print(prim++==0? "Encontrado na(s) posição(ões): "+i : ","+i);
					}
				}
				System.out.println();
			}
			
		
		}
	ler.close();
	}
}
