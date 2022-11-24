# Redes-P2P_20222-Ex3.6

## Implementação do protótipo da aplicação da disciplina de Redes P2P - Exercício 3.6

## App de Busca num fórum simulado com informações e dicas de compra/venda de criptomoedas - CryptoForum

### 1. Qual é o objetivo da aplicação?

O objetivo da aplicação é desenvolver um mecanismo de busca por informações (palavras-chave) sobre um fórum publico cujo tema é oportunidades de investimentos (compra e venda) de criptomoedas. Por exemplo, se o usuário buscar por "Bitcoin" a aplicação deverá ser capaz de retornar as postagens que de alguma forma trouxeram informações de investimentos em bitcoins. Se o usuário buscar por um termo que não foi mencionado no fórum, o usuário deverá ser avisado sobre isso, ou seja, a aplicação deverá ser capaz de tratar os casos de busca por cadeia de strings que não se encontram no fórum. 

### 2. Que outras funcionalidades do Freechains a aplicação tira proveito? (Além do sistema de reputação.)

Além do sistema de reputação, a aplicação tira proveito principalmente da capacidade de o Freechains consensuar as postagens em um fórum público. Hoje em uma pesquisa na internet não foi possível encontrar um fórum público não permissionado em português sobre investimentos em critpoativos, a maioria deles como por exemplo (https://br.investing.com ou https://br.advfn.com/forum) são fóruns permissionados.

### 3. Rodando a aplicação:

Primeiramente, é importante destacar que uma simulação foi desenvolvida para testar utilização da aplicação. O ínicio da rede com 5 postagens, uma postagem vai ser descartada e o usuário leitor vai fazer uma busca pela rede por palavra chave. O Administrador vai validar as 5 postagens com o like, assim garantindo reps para os usuários. Um usuário sem reps tentará fazer uma postagem, mas não entrará na rede por conta do freechains. Cinco usuários vão postar informações importantes no repositório (Todas elas vão ser validadas pelo autor). Um Disseminador tentará criar um conteúdo duplicado, porém os outros disseminadores/administradores irão impedir o conteúdo de aparecer no repositorio com os dislikes.

Para executar a aplicação: primeiro, execute o código ./cryptoforum.sh para preencher o fórum com postagens com indicações de compra ou de venda de criptomoedas, além de outras informações sobre os criptoativos em si.

Após preencher o fórum com as postagens dos usuários com o script cryptoforum.sh, executar o arquivo python cryptoforum.py que tem como objetivo gerar uma GUI (Graphical User Interface) feita através da biblioteca Tkinter do Python.

### b. Descreva exatamente o que foi implementado

A aplicação rodará sobre o Freechains, ou seja, ela usará o Freechains como base e referência das informações (postagens) utilizando seu mecanismo de consenso. Para essa implementação, foi desenvolvido um script Python que instacia chamadas ao Freechains utilizando a biblioteca subprocess do Python. Foi desenvolvido um mecanismo de busca por palavras chave em uma cadeia de postagens do Freechains, ou seja, a aplicação é capaz de analisar post por post se determinada cadeia de string pertence às postagens, retornando não só a cadeia de strings em si, mas todo o contexto em que ela se insere. Também foi implementado o tratamento do retorno no caso de a cadeia de strings não pertecer ao conjunto de postagens. O objetivo da aplicação é permitir que o usuário do fórum do Freechains CryptoForum consiga fazer busca por palavras-chaves sob a rede com o objetivo de encontrar algum indicativo de investimentos relevante para ajudar a investir em criptomoedas. A linguagem Python foi escolhida devido à sua versatilidade, disponibilidade de bibliotecas, mas principalmente por ser um pouco menos complexa de se desenvolver que por exemplo C++ ou JavaScript.

### c. Descreva exatamente o que *não* foi implementado

Uma interface gráfica onde o usuário conseguisse executar comandos do freechains via point-and-click como postar ou dar likes/dislikes. Devido ao prazo para cumprimento da tarefa, realmente só foi possível que eu conseguisse desenvolver uma GUI de busca no Freechains. Mas entendo ser plenamente plausível continuar o desenvolvimento da aplicação visando implementar tais funcionalidades.

### d. Enumere as ferramentas utilizadas para a implementação

Shell script para rodar os comandos para simulação das postagens no Freechains, Python para a execução e implementação do protótipo do App e uma instância do Freechains rodando em um Terminal.

### Como utilizar a aplicação?

### a. Inclua um manual de utilização da aplicação

O usuário poderá efetuar buscas utilizando o App. Primeiro ele deve digitar o termo procurado no item Procurar no CryptoForum, em seguida, após a digitação ele deverá clicar no Botão Buscar. Se o termo buscado estiver contido em alguma postagem no fórum, essa postagem será exibida para o usuário. Caso não esteja presente, o usuário será avisado sobre isso. Por fim, o usuário poderá utilizar o botão "Limpar" para limpar a tela para uma nova pesquisa. No exemplo para essa questão, simulamos buscas pelas seguintes palavras-chave: Bitcoin, Ethereum e Monero para obter os resultados correspondentes caso haja ou se não, avisar ao usuário de que não há o termo buscado.

(*) É importante frisar que o usuário do fórum não precisará estar 'logado', basta ter uma conexão com algum nó da rede.

(**) Screenshots com funcionamento da aplicação estão disponíveis na raiz desse repositório
