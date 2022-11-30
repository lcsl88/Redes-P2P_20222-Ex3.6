# Redes-P2P_20222-Ex3.6

## Implementação do protótipo da aplicação da disciplina de Redes P2P - Exercício 3.6

## Wiki com informações e dicas de compra/venda de criptomoedas e informações sobre criptoativos em geral - CryptoWiki

### 1. Qual é o objetivo da aplicação?

O objetivo da aplicação é desenvolver um protótipo que utilize o sistema de reputação do Freechains com o mecanismo de consenso e um sistema de reputação das postagens. Para isso foi desenvolvida uma Wiki pública em rede P2P (o CryptoWiki) cujo tema é oportunidades de investimentos (compra e venda) de criptomoedas e informações técnicas gerais sobre criptoativos. Além disso também foi desenvolvido um mecanismo de busca por informações (palavras-chave) sobre essa Wiki, além do desenvolvimento também da possibilidade de o usuário postar novos conteúdos na Wiki e dar likes ou dislikes em postagens buscadas e selecionadas. Por exemplo, se o usuário buscar por "Bitcoin" na CryptoWiki a aplicação deverá ser capaz de retornar as postagens que de alguma forma trouxeram informações de investimentos em bitcoins. Ou se o usuário buscar por um termo que não foi mencionado na Wiki, ele deverá ser avisado sobre isso, ou seja, a aplicação deverá ser capaz de tratar os casos de busca por cadeia de strings que não se encontram na Wiki. Por fim, se o usuário postar um conteúdo novo, a aplicação também é capaz de inserir esse conteúdo à cadeia e depois também é capaz de recuperar esse conteúdo caso seja feita uma busca por ele. Os usuários também poderão interagir com likes ou dislikes ao conteúdo postado e buscado na Wiki, representando a utilização do mecanismo de reputação do Freechains pela aplicação. Os botões de like e dislike permanecem inativos até que o usuário selecione uma postagem para curtir ou descurtir, portanto não é possível promover ação dos botões de like e dislike aleatoriamente.

### 2. Que outras funcionalidades do Freechains a aplicação tira proveito? (Além do sistema de reputação.)

Além do sistema de reputação, a aplicação tira proveito principalmente da capacidade de o Freechains consensuar as postagens, bem como a capacidade do Freechains coibir abusos. Hoje em uma pesquisa na internet não foi possível encontrar uma Wiki pública não permissionado em português sobre investimentos em critpoativos. A aplcação também tira proveito das opções de postagem de novos conteúdos pelo usuário, bem como permite que o usuário dê like ou dislikes somente nas postagens selecionadas pelo usuário.

### 3. Rodando a aplicação:

Para executar a aplicação: primeiro, execute o código ./simul.sh para preencher a Wiki com postagens iniciais com indicações de compra ou de venda de criptomoedas, além de outras informações técnicas sobre os criptoativos em si.

Após preencher a Wiki com as postagens dos usuários com o script cryptowiki.sh, executar o arquivo python cryptowiki.py que tem como objetivo gerar uma GUI (Graphical User Interface) feita através da biblioteca Tkinter do Python. Nessa GUI é possível buscar conteúdo, postar conteúdo, limpar o conteúdo da pesquisa ou da busca e dar likes ou dislikes nos conteúdos da Wiki. Em todos os casos a aplicação é capaz de avisar se houve êxito ou não na ação.

### b. Descreva exatamente o que foi implementado

A aplicação rodará sobre o Freechains, ou seja, ela usará o Freechains como base e referência das informações (postagens) utilizando seu mecanismo de consenso. Para essa implementação, foi desenvolvido um script Python que instacia chamadas ao Freechains utilizando a biblioteca subprocess do Python (Popen). Foi desenvolvido um mecanismo de busca por palavras chave em uma cadeia de postagens do Freechains, ou seja, a aplicação é capaz de analisar post por post se determinada cadeia de string pertence às postagens, retornando não só a cadeia de strings em si, mas todo o contexto em que ela se insere. Também foi implementado o tratamento do retorno no caso de a cadeia de strings não pertecer ao conjunto de postagens. Foi desenvolvido também a capacidade de o usuário efetuar novas postagens, bem como dar likes ou dislikes nos conteúdos buscados. Os objetivos da aplicação é permitir que o usuário da Wiki do Freechains (CryptoWiki) consiga fazer busca por palavras-chaves sob a rede com o objetivo de encontrar algum indicativo de investimentos relevante para ajudar a investir em criptomoedas, além de fazer novas postagens e dar likes ou dislikes em postagens buscadas. A linguagem Python foi escolhida devido à sua versatilidade, disponibilidade de bibliotecas, mas principalmente por ser um pouco menos complexa de se desenvolver que por exemplo C++ ou JavaScript.

### c. Descreva exatamente o que *não* foi implementado

Uma interface gráfica onde o usuário conseguisse assinar as postagens com suas chaves públicas (as chaves utilizadas ficaram internalizadas nos scripts - Python e Shell)

### d. Enumere as ferramentas utilizadas para a implementação

Primeiramente, é importante destacar que uma simulação foi desenvolvida para testar utilização da aplicação. O ínicio da rede com 5 postagens, uma postagem vai ser descartada e o usuário leitor vai fazer uma busca pela rede por palavra chave. O Administrador vai validar as 5 postagens com o like, assim garantindo reps para os usuários. Um usuário sem reps tentará fazer uma postagem, mas não entrará na rede por conta do freechains. Cinco usuários vão postar informações importantes no repositório (Todas elas vão ser validadas pelo autor). Um Disseminador tentará criar um conteúdo duplicado, porém os outros disseminadores/administradores irão impedir o conteúdo de aparecer no repositorio com os dislikes. As ferramentas utilizadas para a implementação foram Shell script para rodar os comandos para simulação das postagens no Freechains, Python para a execução e implementação do protótipo do App e uma instância do Freechains rodando em um Terminal.

### Como utilizar a aplicação?

### a. Inclua um manual de utilização da aplicação

MANUAL: O usuário poderá efetuar buscas utilizando o App. Primeiro ele deve digitar o termo procurado no item Procurar na CryptoWiki, em seguida, após a digitação ele deverá clicar no Botão Buscar. Se o termo buscado estiver contido em alguma postagem na Wiki, essa postagem será exibida para o usuário. Caso não esteja presente, o usuário será avisado sobre isso. Por fim, o usuário poderá utilizar o botão "Limpar" para limpar a tela para uma nova pesquisa. No exemplo para essa questão, simulamos buscas pelas seguintes palavras-chave na Wiki: Bitcoin, Ethereum e Monero para obter os resultados correspondentes caso haja ou se não, avisar ao usuário de que não há o termo buscado. O usuário também poderá efetuar postagens de novos conteúdos na Wiki. Depois de efetuada uma busca por conteúdo, o usuário poderá dar like ou dislike nesse conteúdo buscado somente após ser selecionado pelo usuário.

(*) É importante frisar que o usuário da Wiki não precisará estar 'logado', basta ter uma conexão com algum nó da rede, denotando o caráter permissionless da rede.

(**) Screenshots (de 1 a 10) com funcionamento da aplicação estão disponíveis na raiz desse repositório
