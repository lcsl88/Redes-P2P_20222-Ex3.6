from tkinter import *
import subprocess
import math

root = Tk()
root.title('CryptoForum - Freechains')
root.geometry("1000x1000")

# Globais

resultados = {}
dict_likes = {}
id_selecionado_like_dislike = ''
usuarios = {}


# Carrega usuarios

usuarios['administrator'] = {}
usuarios['administrator']['pubkey'] = '32B0CCE2868C450622FE08E73CF16133EE04BF63A480F75946F8461B0F5DDE40'
usuarios['administrator']['prvkey'] = 'BD52C3810352019D542891CF46EF0B26DCA8B0C901B367AE16B5E34B6ABFA1B832B0CCE2868C450622FE08E73CF16133EE04BF63A480F75946F8461B0F5DDE40'

usuarios['disseminator01'] = {}
usuarios['disseminator01']['pubkey'] = 'E308A88847A990D2996F32256C3B9EF0331A11E297327D506955B5DCD9BF5B13'
usuarios['disseminator01']['prvkey'] = '77172726A1B20A63F749B3187F020C443D9341F1CE922751857D672F99202382E308A88847A990D2996F32256C3B9EF0331A11E297327D506955B5DCD9BF5B13'

usuarios['disseminator02'] = {}
usuarios['disseminator02']['pubkey'] = '8D600F743F57EDE23EBA0E0BC80569EB00F100276844C306C00671B164C4A80A'
usuarios['disseminator02']['prvkey'] = '8555BE0DD829BC1C7D16FC5EF9D53C9DEC71E570A6D8AF5795711095C423239D8D600F743F57EDE23EBA0E0BC80569EB00F100276844C306C00671B164C4A80A'

usuarios['disseminator03'] = {}
usuarios['disseminator03']['pubkey'] = 'BC609D95042D28B1E26F45F860520AC22E67414F086E2357A38E938DAA99B373'
usuarios['disseminator03']['prvkey'] = '4181F0A39AD309FB79E431FB8AA3A1E8D57D162D66F30EBD2D86801BF78D8CECBC609D95042D28B1E26F45F860520AC22E67414F086E2357A38E938DAA99B373'

usuarios['disseminator04'] = {}
usuarios['disseminator04']['pubkey'] = 'B7D8C108E7DA3579436C23A825E59F6AB74DF5A67EF19F38523748E49486283D'
usuarios['disseminator04']['prvkey'] = '35465DD6C622834ACF7383117759771E29D6E60F52093F4B656E2339EE7C5B65B7D8C108E7DA3579436C23A825E59F6AB74DF5A67EF19F38523748E49486283D'

usuarios['disseminator05'] = {}
usuarios['disseminator05']['pubkey'] = '394506F4A6B276221E67090B3D7F4E7677BF2127445B48F38CF846D2C110EB16'
usuarios['disseminator05']['prvkey'] = 'A12C40852DF49C5F9E548F028AFF9593CE929A760663BD14ED1D09D060D103B1394506F4A6B276221E67090B3D7F4E7677BF2127445B48F38CF846D2C110EB16'

usuarios['disseminatorinvalid'] = {}
usuarios['disseminatorinvalid']['pubkey'] = 'A1357A53BF18A0295D57B8672944A139FDA75668A58FCC33766E99454203F3EE'
usuarios['disseminatorinvalid']['prvkey'] = '10F506BBEB35EF76EBE14CD2ABCD4CF0FAB481B43A46F66CDFE52C550C7C049BA1357A53BF18A0295D57B8672944A139FDA75668A58FCC33766E99454203F3EE'

# Clear
def clear():
	my_entry.delete(0, END)
	my_text.delete(0.0, END)
	resultados = {}
	like_button["state"] = "disabled"
	dislike_button["state"] = "disabled"

# Search
def search():
	busca = my_entry.get()

	# Evita a busca com valor vazio

	if re.match('^\s*$', busca):
        	return

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
	
	indice = 3

	for block in arrblock:
		p1 = subprocess.Popen(c2.format(block), shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		out, err = p1.communicate()
		utf = out.decode('utf-8')
		utf = utf.strip()
		if utf.find(busca) > -1:
			# Define os comandos a executar

			c1 = "freechains chain '#repository' reps '{0}'"

			# Executa os comandos para obtencao dos blocos e salva stdout em out

			p1 = subprocess.Popen(c1.format(block), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			out, err = p1.communicate()

			reputacao = out.decode('utf-8')
			reputacao = reputacao.strip()

			# Trata a saida fazendo cast para string e removendo quebras de linha desnecessarias
			
			bfind = True
			if not block in dict_likes:
				dict_likes[block] = 0
			encontrado = encontrado + "\n" + utf + "[" + reputacao + " rep]" + "\n"
			resultados[indice] = {}
			resultados[indice]['texto'] = utf
			resultados[indice]['id'] = block
			indice = indice + 2

	if bfind:
		my_text.insert(0.0, encontrado)
	else:
		my_text.insert(0.0, nao_encontrado)


# Show
def show():
	# busca = my_entry.get()

	# Evita a busca com valor vazio

	# if re.match('^\s*$', busca):
        #	return

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

	nao_encontrado = "Termo nao encontrado!"
	encontrado = "Posts existentes no CryptoForum:\n"
	bfind = False

	# Para cada bloco, procura o valor passado como argumento
	
	indice = 3

	for block in arrblock:
		p1 = subprocess.Popen(c2.format(block), shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		out, err = p1.communicate()
		utf = out.decode('utf-8')
		utf = utf.strip()
		#if 1 == 1:
		if not re.match('^\s*$', utf):
		#if utf.find(busca) > -1:
			# Define os comandos a executar

			c1 = "freechains chain '#repository' reps '{0}'"

			# Executa os comandos para obtencao dos blocos e salva stdout em out

			p1 = subprocess.Popen(c1.format(block), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			out, err = p1.communicate()

			reputacao = out.decode('utf-8')
			reputacao = reputacao.strip()

			bfind = True
			if not block in dict_likes:
				dict_likes[block] = 0
			encontrado = encontrado + "\n" + utf + "[" + reputacao + " rep]" + "\n"
			resultados[indice] = {}
			resultados[indice]['texto'] = utf
			resultados[indice]['id'] = block
			indice = indice + 2

	if bfind:
		my_text.insert(0.0, encontrado)
	else:
		my_text.insert(0.0, nao_encontrado)


def post():
	postar = my_entry.get()

	# Evita a busca com valor vazio

	if re.match('^\s*$', postar):
		my_text.insert(0.0, "Post vazio!")
		return

	usuario = Lb1.get(Lb1.curselection())
	clear()

	l1 = "freechains chain '#repository' post inline '{0}' --sign={1}"
	
	p3 = subprocess.Popen(l1.format(postar, usuarios[usuario]['prvkey']), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p3.communicate()

	msg_ret = out.decode('utf-8')
	msg_ret = msg_ret.strip()
	
	msg = "Termos(s) postado(s)!\n\n{0}"
	
	my_text.insert(0.0, msg.format(msg_ret))
    
def like():
	global id_selecionado_like_dislike

	usuario = Lb1.get(Lb1.curselection())

	l1 = "freechains chain '#repository' like '{0}' --sign={1}"
	p4 = subprocess.Popen(l1.format(id_selecionado_like_dislike, usuarios[usuario]['prvkey']), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p4.communicate()
	
	msg_ret = out.decode('utf-8')
	msg_ret = msg_ret.strip()

	msg = "Operação de like realizada.\n\n{0}"

	clear()
	
	my_text.insert(0.0, msg.format(msg_ret))


def dislike():
	global id_selecionado_like_dislike

	usuario = Lb1.get(Lb1.curselection())
	
	d1 = "freechains chain '#repository' dislike '{0}' --sign={1}"
	p5 = subprocess.Popen(d1.format(id_selecionado_like_dislike, usuarios[usuario]['prvkey']), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p5.communicate()

	msg_ret = out.decode('utf-8')
	msg_ret = msg_ret.strip()

	msg = "Operação de dislike realizada.\n\n{0}"

	clear()

	my_text.insert(0.0, msg.format(msg_ret))

def rep_user():
	usuario = Lb1.get(Lb1.curselection())
	
	d1 = "freechains chain '#repository' reps '{0}'"
	p5 = subprocess.Popen(d1.format(usuarios[usuario]['pubkey']), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p5.communicate()

	msg_ret = out.decode('utf-8')
	msg_ret = msg_ret.strip()

	msg = "A reputacao do usuário '{0}' é '{1}'"

	clear()

	my_text.insert(0.0, msg.format(usuario, msg_ret))



def _on_click(event):
        global id_selecionado_like_dislike

        my_text.tag_remove("highlight", "1.0", "end")
        linha_clicada = math.trunc(float(my_text.index("@%d,%d" % (event.x, event.y))))
        start_idx = "{0}.0".format(linha_clicada)
        end_idx = "{0}.end".format(linha_clicada)
        if linha_clicada in resultados:
                my_text.tag_add("highlight", start_idx, end_idx)
                like_button["state"] = "normal"
                dislike_button["state"] = "normal"
                id_selecionado_like_dislike = resultados[linha_clicada]['id']

my_label_frame = LabelFrame(root, text="Postar ou Procurar no CryptoForum")
my_label_frame.pack(pady=20)

# Create entry box for Post / Search
my_entry = Entry(my_label_frame, font=("Helvetica", 14), width=47)
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

# Configura comportamento
my_text.bind("<ButtonRelease-1>", _on_click)
my_text.tag_configure("highlight", background="green", foreground="black")

# Configure Scrollbars
text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)

# Button Frame
button_frame = Frame(root)
button_frame.pack(pady=10)

# Buttons
search_button = Button(button_frame, text="Buscar", font=("Helvetica", 14), fg="#3a3a3a", command=search)
search_button.grid(row=0, column=0, padx=20)

post_button = Button(button_frame, text="Postar", font=("Helvetica", 14), fg="#3a3a3a", command=post)
post_button.grid(row=0, column=1, padx=20)

clear_button = Button(button_frame, text="Limpar", font=("Helvetica", 14), fg="#3a3a3a", command=clear)
clear_button.grid(row=0, column=2, padx=20)

like_button = Button(button_frame, text="Like", font=("Helvetica", 14), fg="#3a3a3a", command=like)
like_button.grid(row=0, column=3, padx=20)
like_button["state"] = "disabled"

dislike_button = Button(button_frame, text="Dislike", font=("Helvetica", 14), fg="#3a3a3a", command=dislike)
dislike_button.grid(row=0, column=4, padx=20)
dislike_button["state"] = "disabled"

show_button = Button(button_frame, text="Mostrar", font=("Helvetica", 14), fg="#3a3a3a", command=show)
show_button.grid(row=0, column=5, padx=20)

reput_button = Button(button_frame, text="Rep. Usuario", font=("Helvetica", 14), fg="#3a3a3a", command=rep_user)
reput_button.grid(row=0, column=6, padx=20)

Lb1 = Listbox(root)

Lb1.insert(1, "administrator")
Lb1.insert(2, "disseminator01")
Lb1.insert(3, "disseminator02")
Lb1.insert(4, "disseminator03")
Lb1.insert(5, "disseminator04")
Lb1.insert(6, "disseminator05")
Lb1.insert(7, "disseminatorinvalid")

Lb1.pack()

Lb1.selection_set(0)

root.mainloop()
