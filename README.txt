COMPONENTE WEB

Antes de usar, alterar no ficheiro auxfunctions.py
-Mudar o username, password e tlmorigem do serviço lusosms
-Mudar o FROM para enviar emails

Este programa tem duas fases. A primeira faz o sorteio e a segunda 
encarrega-se de entregar o conteúdo do sorteio.

Instruções

0. Criar o ficheiro nome.txt com os nomes necessários. Comentar os que não entram com '#'
1. Correr o programa "shuffle.py" que cria um ficheiro "shuffled_data.txt"
2. Mudar o nome do ficheiro para "deliver.txt" e mudar permissões para escrita por terceiros
3. Correr via browser o "deliver.py"


COMPONENT STANDALONE

Have an account in www.lusosms.com or changed the code to handle another site

./standalone.py Usage:
create a file named nomes.csv with names and phone numbers separated by a comma. 
The first line should be "nomes,telemovel".
change: LUSOSMS_USER, LUSOSMS_PASS, LUSOSMS_NUMBER

./standalone_single.py Usage:
change SINGLE, SHUFFLED_FILE and Lusosms credentials (LUSOSMS_USER, LUSOSMS_PASS, LUSOSMS_NUMBER)
