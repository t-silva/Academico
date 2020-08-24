import java.util.Scanner;
import java.util.Random;
import java.util.ArrayList;   
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
			Random gera = new Random(); //crio o objeto gera, e aloco memória para ele;
				ArrayList<Integer> R = new ArrayList<Integer>();
			for (int i=0;i<N;i++){
				R.add(gera.nextInt(50));
			}
         System.out.print(R);
		   int x;
		   while(1==1){
		      System.out.print("\nDigite um valor para buscar no vetor: ");
			   x = ler.nextInt(); //nextInt é método do objeto ler
			   if (R.contains(x)) {
                  for(int j = 0;j<R.size();j++){
                     if (x==R.get(j)) {System.out.println(x+" esta nas posicoes: "+j);}
                  }
			   }
            else System.out.println("Não presente");
		   }
	   }
      System.out.println();
   }
}
