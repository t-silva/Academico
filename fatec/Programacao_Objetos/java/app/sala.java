import java.util.Scanner;
import java.util.Random;
import java.util.ArrayList;
class sala{
	static boolean status = true;
	static ArrayList<String> TAREFAS = new ArrayList<String>();
	public static void main(String args[]){
		Scanner ler =  new Scanner(System.in);
		char tipo;
		int R=0;
		System.out.println("Deseja iniciar com um banco pré-definido? (s/n)");
		tipo = ler.next().charAt(0);
		if (tipo == 's') {
			TAREFAS.add("Lavar Louça");
			TAREFAS.add("Secar/Guardar Louça");
			TAREFAS.add("Limpar Fogão");
			TAREFAS.add("Limpar Pia");
			TAREFAS.add("Limpar Chão");
		}
		while ( status ){

			System.out.println("================================================================================");
			System.out.println("1 - Adicionar Tarefa | 2 - Realizar Limpeza | 3 - Alerta do que falta | 0 - Sair");
			System.out.println("================================================================================");
			R = ler.nextInt();
			checarR(R);
		}
		System.out.println("Saiu R:"+R);
	}
	public static void checarR(int a){
		if ( a < 0 || a > 3) System.out.println("Valor incorreto");
		else if ( a == 0) status = false;
		else if ( a == 1 ){ 
			System.out.println("Respondeu 1");
			gerenciarAfazeres();
		}
		else if ( a == 2 ) 
			if (TAREFAS.isEmpty()) System.out.println("Não há tarefas cadastradas"); 
			else realizarTarefa();
	}
	public static void gerenciarAfazeres(){
		Scanner ler =  new Scanner(System.in);
		boolean check = true;
		int resp;
		System.out.println("Entrando no sistema");
	       while (check){	
			System.out.println("================================================================================");
			System.out.println("1 - Adicionar Item | 2 - Listar Itens | 0 - Sair");
			System.out.println("================================================================================");
			resp = ler.nextInt();
			if ( resp  == 1 ) {
				System.out.print("Item a cadastrar: ");
				TAREFAS.add(ler.next());
			}
			else if (resp == 2 ) System.out.println(TAREFAS);
			else if (resp == 0 ) check = false;

	       }
	
	
	
	}
	public static void realizarTarefa(){
		Scanner ler = new Scanner(System.in);
		System.out.println("Qual tarefa deseja executar?");
		for (int i = 0 ; i < TAREFAS.size(); i++ ){
			System.out.println(i+"-"+TAREFAS.get(i));
		}


    		}

}


