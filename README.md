# Redes-P2P_20222-Ex3.6
## Implementação do protótipo da aplicação da disciplina de Redes P2P

## CryptoForum sobre o Freechains

1. Qual é o objetivo da aplicação?

O objetivo da aplicação é desenvolver um mecanismo de busca por informações (palavras-chave) sobre um fórum publico cujo tema é oportunidades de investimentos (compra e venda) de criptomoedas. Por exemplo, se o usuário buscar por "Bitcoin" a aplicação deverá ser capaz de retornar as postagens que de alguma forma trouxeram informações de investimentos em bitcoins. Se o usuário buscar por um termo que não foi mencionado no fórum, o usuário deverá ser avisado sobre isso, ou seja, a aplicação deverá ser capaz de tratar os casos de busca por cadeia de strings que não se encontram no fórum. 

2. Que outras funcionalidades do Freechains a aplicação tira proveito? (Além do sistema de reputação.)

Além do sistema de reputação, a aplicação tira proveito principalmente da capacidade de o Freechains consensuar as postagens em um fórum público. Hoje em uma pesquisa na internet não foi possível encontrar um fórum público não permissionado em português sobre investimentos em critpoativos, todos eles como (br.investing.com ou https://br.advfn.com/forum são fóruns permissionados)

3. Rodando a aplicação:

Para executar a aplicação: primeiro, execute o código ./cryptoforum.sh para preencher o forum com postagens com indicações de compra ou de venda de cryptomoedas, além de outras informações sobre os ativos em si.

Após preencher o fórum com as postagens dos usuários, após isso rodar o arquivo (python3 cryptoforum.py) que tem como objetivo apresentar uma GUI (Graphical User Interface) feita através da biblioteca Tkinter do Python.

O que foi implementado

A aplicação rodará sobre o freechains, ou seja, ela usará o freechains como base e referência das informações (postagens). Para essa implementação, foi desenvolvido um script Python que instacia chamadas ao Freechains utilizando a biblioteca subprocess do Python. O objetivo da aplicação é permitir ao usuário do fórum CryptoForum do Freechains que consiga fazer busca por palavras-chaves sob a rede com o objetivo de encontrar algum indicativo de investimentos relevante para ajudar a investir em criptomoedas. A linguagem Python foi escolhida devido à sua versatilidade, disponibilidade de bibliotecas, mas principalmente por ser um pouco menos complexa de desenvolver como o JavaScript por exemplo.

O que não foi implementado

Uma interface gráfica onde o usuário conseguisse executar comandos do freechains via point-and-click como postar ou dar likes/dislikes. Devido ao prazo para cumprimento da tarefa, realmente só foi possível que eu conseguisse desenvolver uma GUI de busca no Freechains. Mas entendo que é plenamente possível continuar o desenvolvimento da aplicação visando implementar essas funcionalidades.

Ferramentas utilizadas
Shell script para rodar os comandos para simulação das postagens no Freechains, Python para a execução e implementação do protótipo do App e o próprio Freechains rodando por trás

Uma simulação foi desenvolvida para testar a aplicação
O ínicio da rede com 5 postagens, uma postagem vai ser descartada e o usuário leitor vai fazer uma busca pela rede por palavra chave
O Administrador vai validar as 5 postagens com o like, assim garantindo reps para os usuários
Um usuário sem reps tentará fazer uma postagem, mas não entrará na rede por conta do freechains
Cinco usuários vão postar informações importantes no repositório (Todas elas vão ser validadas pelo autor)
Um Disseminador tentará criar um conteúdo duplicado, porém os outros disseminadores/administradores irão impedir o conteúdo de aparecer no repositorio com os dislikes

O leitor fará uma busca no protótipo do app Python, por exemplo, pelas seguintes palavras: Bitcoin, Ethereum e Monero para obter os resultados

É importante frisar que o usuário do fórum não precisará estar 'logado', basta ter uma conexão com algum nó da rede.

Screenshots com funcionamento da aplicação estão disponíveis na raiz desse repositório
