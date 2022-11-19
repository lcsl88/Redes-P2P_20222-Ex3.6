from tkinter import *
import subprocess

root = Tk()
root.title('CryptoForum - Freechains')
root.geometry("700x675")

# Clear
def clear():
	my_entry.delete(0, END)
	my_text.delete(0.0, END)

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

	if bfind:
		my_text.insert(0.0, encontrado)
	else:
		my_text.insert(0.0, nao_encontrado)

my_label_frame = LabelFrame(root, text="Procurar no CryptoForum")
my_label_frame.pack(pady=20)

# Create entry box
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

clear_button = Button(button_frame, text="Limpar", font=("Helvetica", 32), fg="#3a3a3a", command=clear)
clear_button.grid(row=0, column=1)


root.mainloop()
