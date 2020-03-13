1. Em um programa Java (na classe principal) crie dois atributos inteiros chamados Min e Max. Crie um método
para ler do teclado um valor para Min de modo que o mesmo seja no mínimo o valor 10000. Crie um método
para ler um valor para Max de modo que o mesmo seja obrigatoriamente maior que Min e menor ou igual
a 99999. Crie um método que identifique e exiba na tela todos os números primos existentes no intervalo
fechado [Min, Max].

2. Na classe principal de um programa Java, crie um método capaz de gerar um número aleatório (use a classe
Random) situado entre dois limites [Min, Max]. Esse número aleatório será usado como código de um
produto e precisará ter 5 dígitos. Mostre esse código na tela. Neste programa, use métodos semelhantes
aos desenvolvidos na questão 1 para fazer a leitura dos limites Min e Max.

3. Continuando o programa do item 2, crie um método capaz de calcular o dígito verificador do código de 5
dígitos gerado. A regra de cálculo desse dígito verificador tem o nome de módulo 7 e é descrita a seguir.
Exemplo: se o código for 21468, o dígito verificador será 3.
Em primeiro lugar deve-se tomar cada dígito individualmente e multiplicá-lo pelo peso apropriado. O peso
do dígito menos significativo é 6, o peso do segundo dígito menos significativo é 5 e assim por diante,
conforme mostrado na tabela. Os resultados das multiplicações devem ser somados e por fim calcula-se o
resto dessa soma por 7

4. No programa anterior crie um atributo inteiro N e faça sua leitura do teclado. Crie dois atributos do tipo
vetor de inteiros, ambos com N elementos, sendo um para códigos de produto e outro para os respectivos
dígitos verificadores. Use os métodos criados nas questões 2 e 3 para carregar esses dois vetores e exiba-os
na tela.
