
import java.util.Scanner;
public class Adicao {
    public static void main(String args[]){
        Scanner input = new Scanner(System.in);
        int num1;
        int num2;
        System.out.print("Digite o primeiro numero: ");
        num1 = input.nextInt();
        System.out.print("Digite o primeiro numero: ");
        num2 = input.nextInt();
        System.out.print("Soma: ");
        System.out.printf("%d\n", num1+num2);
    }    
}