from tkinter import *
import subprocess

root = Tk()
root.title('CryptoForum - Freechains')
root.geometry("1000x1000")

############################
resultados = {}
############################

# Clear
def clear():
	my_entry.delete(0, END)
	my_text.delete(0.0, END)
	############################
	resultados = {}
	############################

# Search
def search():
	busca = my_entry.get()
	# Clear screen
	clear()

	# Define os comandos a executar

	c1 = "freechains chain '#repository' consensus"
	c2 = "freechains chain '#repository' get payload {0}"

	# Executa os comandos para obtencao dos blocos e salva stdout em out

	p1 = subprocess.Popen(c1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p1.communicate()

	# Trata a saida fazendo cast para string e removendo quebras de linha desnecessarias

	utf = out.decode('utf-8')	
	utf = utf.strip()

	# Carrega os blocos separadamente no array arrblock

	arrblock = utf.split(' ')

	# Inicializa a resposta

	nao_encontrado = "Termo '{0}' nao encontrado!".format(busca)
	encontrado = "Encontrado(s) o(s) seguinte(s) resultado(s) na busca no CryptoForum:\n"
	bfind = False

	# Para cada bloco, procura o valor passado como argumento

	for block in arrblock:
		p1 = subprocess.Popen(c2.format(block), shell=True,	stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		out, err = p1.communicate()
		utf = out.decode('utf-8')
		utf = utf.strip()
		if utf.find(busca) > -1:
			bfind = True
			encontrado = encontrado + "\n" + utf + "\n"
			############################
			resultados[block] = utf
			############################

	if bfind:
		my_text.insert(0.0, encontrado)
	else:
		my_text.insert(0.0, nao_encontrado)

#def join():

#    j1 = "freechains chains join '#repository' 32B0CCE2868C450622FE08E73CF16133EE04BF63A480F75946F8461B0F5DDE40"

#    p2 = subprocess.Popen(j1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#    out, err = p2.communicate()

def post():

    postar = my_entry.get()
    # Clear screen
    clear()

    po1 = "freechains chain '#repository' post inline '{0}' --sign=77172726A1B20A63F749B3187F020C443D9341F1CE922751857D672F99202382E308A88847A990D2996F32256C3B9EF0331A11E297327D506955B5DCD9BF5B13"
    p3 = subprocess.Popen(po1.format(postar), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    my_text.insert(0.0, "Termo(s) postado(s)!")

def like():

	# Define o comando a executar

	l1 = "freechains chain '#repository' like $POSTDISSEMINATOR'{0}' --sign=BD52C3810352019D542891CF46EF0B26DCA8B0C901B367AE16B5E34B6ABFA1B832B0CCE2868C450622FE08E73CF16133EE04BF63A480F75946F8461B0F5DDE40"
	p4 = subprocess.Popen(l1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p4.communicate()
	clear()
	my_text.insert(0.0, "Postagem curtida! +1 rep")

def dislike():

	d1 = "freechains chain '#repository' dislike $POSTDISSEMINATOR5 --sign=BD52C3810352019D542891CF46EF0B26DCA8B0C901B367AE16B5E34B6ABFA1B832B0CCE2868C450622FE08E73CF16133EE04BF63A480F75946F8461B0F5DDE40"
	p5 = subprocess.Popen(d1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p5.communicate()
	clear()
	my_text.insert(0.0, "Postagem descurtida! -1 rep")

my_label_frame = LabelFrame(root, text="Postar ou Procurar no CryptoForum")
my_label_frame.pack(pady=20)

# Create entry box for Post / Search
my_entry = Entry(my_label_frame, font=("Helvetica", 18), width=47)
my_entry.pack(pady=20, padx=20)

# create text box frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# Create Vertical Scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Create Horizontal Scrollbar
hor_scroll = Scrollbar(my_frame, orient='horizontal')
hor_scroll.pack(side=BOTTOM, fill=X)

# Create Text Box
my_text = Text(my_frame, yscrollcommand=text_scroll.set, wrap="word", xscrollcommand=hor_scroll.set)
my_text.pack()

# Configure Scrollbars
text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)

# Button Frame
button_frame = Frame(root)
button_frame.pack(pady=10)

# Buttons
search_button = Button(button_frame, text="Buscar", font=("Helvetica", 32), fg="#3a3a3a", command=search)
search_button.grid(row=0, column=0, padx=20)

post_button = Button(button_frame, text="Postar", font=("Helvetica", 32), fg="#3a3a3a", command=post)
post_button.grid(row=0, column=1, padx=20)

clear_button = Button(button_frame, text="Limpar", font=("Helvetica", 32), fg="#3a3a3a", command=clear)
clear_button.grid(row=0, column=2, padx=20)

like_button = Button(button_frame, text="Like", font=("Helvetica", 32), fg="#3a3a3a", command=like)
like_button.grid(row=0, column=3, padx=20)

dislike_button = Button(button_frame, text="Dislike", font=("Helvetica", 32), fg="#3a3a3a", command=dislike)
dislike_button.grid(row=0, column=4, padx=20)

root.mainloop()
