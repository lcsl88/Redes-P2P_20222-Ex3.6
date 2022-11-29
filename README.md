# Redes-P2P_20222-Ex3.6

## Implementação do protótipo da aplicação da disciplina de Redes P2P - Exercício 3.6

## Fórum simulado com informações e dicas de compra/venda de criptomoedas - CryptoForum

### 1. Qual é o objetivo da aplicação?

O objetivo da aplicação é desenvolver um protótipo que utilize o sistema de reputação do Freechains com um sistema de reputação das postagens e um mecanismo de consenso. Para isso foi simulado um fórum público P2P (o CryptoForum) cujo tema é oportunidades de investimentos (compra e venda) de criptomoedas. Além disso também foi desenvolvido um mecanismo de busca por informações (palavras-chave) sobre esse fórum publico, além do desenvolvimento também da possibilidade de o usuário postar novos conteúdos e dar likes ou dislikes em postagens buscadas. Por exemplo, se o usuário buscar por "Bitcoin" a aplicação deverá ser capaz de retornar as postagens que de alguma forma trouxeram informações de investimentos em bitcoins. Ou se o usuário buscar por um termo que não foi mencionado no fórum, ele deverá ser avisado sobre isso, ou seja, a aplicação deverá ser capaz de tratar os casos de busca por cadeia de strings que não se encontram no fórum. Por fim, se o usuário postar um conteúdo novo, a aplicação também será capaz de recuperar esse conteúdo depois de ser feita uma busca por ele. Os usuários também poderão interagir com likes ou dislikes ao conteúdo postado e buscado, representando a utilização do mecanismo de reputação do Freechains pela aplicação.

### 2. Que outras funcionalidades do Freechains a aplicação tira proveito? (Além do sistema de reputação.)

Além do sistema de reputação, a aplicação tira proveito principalmente da capacidade de o Freechains consensuar as postagens em um fórum público, bem como a capacidade do Freechains coibir abusos. Hoje em uma pesquisa na internet não foi possível encontrar um fórum público não permissionado em português sobre investimentos em critpoativos, a maioria deles como por exemplo (https://br.investing.com ou https://br.advfn.com/forum) são fóruns permissionados. A aplcação também tira proveito das opções de postagem de novos conteúdos pelo usuário.

### 3. Rodando a aplicação:

Para executar a aplicação: primeiro, execute o código ./cryptoforum.sh para preencher o fórum com postagens iniciais com indicações de compra ou de venda de criptomoedas, além de outras informações sobre os criptoativos em si.

Após preencher o fórum com as postagens dos usuários com o script cryptoforum.sh, executar o arquivo python cryptoforum.py que tem como objetivo gerar uma GUI (Graphical User Interface) feita através da biblioteca Tkinter do Python. Nessa GUI é possível buscar conteúdo, postar conteúdo, limpar o conteúdo da pesquisa ou da busca e dar likes ou dislikes nos conteúdos. Em todos os casos a aplicação é capaz de avisar se houve êxito ou não na ação.

### b. Descreva exatamente o que foi implementado

A aplicação rodará sobre o Freechains, ou seja, ela usará o Freechains como base e referência das informações (postagens) utilizando seu mecanismo de consenso. Para essa implementação, foi desenvolvido um script Python que instacia chamadas ao Freechains utilizando a biblioteca subprocess do Python (Popen). Foi desenvolvido um mecanismo de busca por palavras chave em uma cadeia de postagens do Freechains, ou seja, a aplicação é capaz de analisar post por post se determinada cadeia de string pertence às postagens, retornando não só a cadeia de strings em si, mas todo o contexto em que ela se insere. Também foi implementado o tratamento do retorno no caso de a cadeia de strings não pertecer ao conjunto de postagens. Foi desenvolvido também a capacidade de o usuário efetuar novas postagens, bem como dar likes ou dislikes nos conteúdos buscados. Os objetivos da aplicação é permitir que o usuário do fórum do Freechains (CryptoForum) consiga fazer busca por palavras-chaves sob a rede com o objetivo de encontrar algum indicativo de investimentos relevante para ajudar a investir em criptomoedas, além de fazer novas postagens e dar likes ou dislikes em postagens buscadas. A linguagem Python foi escolhida devido à sua versatilidade, disponibilidade de bibliotecas, mas principalmente por ser um pouco menos complexa de se desenvolver que por exemplo C++ ou JavaScript.

### c. Descreva exatamente o que *não* foi implementado

Uma interface gráfica onde o usuário conseguisse assinar as postagens com suas chaves públicas (as chaves utilizadas ficaram internalizadas nos scripts - Python e Shell)

### d. Enumere as ferramentas utilizadas para a implementação

Primeiramente, é importante destacar que uma simulação foi desenvolvida para testar utilização da aplicação. O ínicio da rede com 5 postagens, uma postagem vai ser descartada e o usuário leitor vai fazer uma busca pela rede por palavra chave. O Administrador vai validar as 5 postagens com o like, assim garantindo reps para os usuários. Um usuário sem reps tentará fazer uma postagem, mas não entrará na rede por conta do freechains. Cinco usuários vão postar informações importantes no repositório (Todas elas vão ser validadas pelo autor). Um Disseminador tentará criar um conteúdo duplicado, porém os outros disseminadores/administradores irão impedir o conteúdo de aparecer no repositorio com os dislikes. As ferramentas utilizadas para a implementação foram Shell script para rodar os comandos para simulação das postagens no Freechains, Python para a execução e implementação do protótipo do App e uma instância do Freechains rodando em um Terminal.

### Como utilizar a aplicação?

### a. Inclua um manual de utilização da aplicação

MANUAL: O usuário poderá efetuar buscas utilizando o App. Primeiro ele deve digitar o termo procurado no item Procurar no CryptoForum, em seguida, após a digitação ele deverá clicar no Botão Buscar. Se o termo buscado estiver contido em alguma postagem no fórum, essa postagem será exibida para o usuário. Caso não esteja presente, o usuário será avisado sobre isso. Por fim, o usuário poderá utilizar o botão "Limpar" para limpar a tela para uma nova pesquisa. No exemplo para essa questão, simulamos buscas pelas seguintes palavras-chave: Bitcoin, Ethereum e Monero para obter os resultados correspondentes caso haja ou se não, avisar ao usuário de que não há o termo buscado. O usuário também poderá efetuar postagens de novos conteúdos na rede. Depois de efetuada uma busca por conteúdo, o usuário poderá dar like ou dislike nesse conteúdo buscado.

(*) É importante frisar que o usuário do fórum não precisará estar 'logado', basta ter uma conexão com algum nó da rede.

(**) Screenshots com funcionamento da aplicação estão disponíveis na raiz desse repositório
