import java.util.Scanner;
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
			int countn=0,countp=0;
			float A[] = new float[N];
			float NEG[] = new float[N];
			float POS[] = new float[N];
				for (int i=0;i<N;i++){
					System.out.print(i+1+"º número: ");
					A[i] = ler.nextFloat();
					if(A[i]<0) 
						NEG[countn++] = A[i];
					else 
						POS[countp++] = A[i];
				}
			int tam=A.length;
			System.out.println("-----------------------------\nO vetor A[] possui "
									+A.length+" elementos");
				System.out.println("Vetor POS[]: "+(countp)+" elementos.");
			for(int i=0;i<countp;i++) System.out.println((i+1)+"º:"+POS[i]);
			System.out.println("Vetor NEG[]: "+(countn)+" elementos.");
			for(int i=0;i<countn;i++) System.out.println((i+1)+"º:"+NEG[i]);
		
		}
	ler.close();
	}
}
