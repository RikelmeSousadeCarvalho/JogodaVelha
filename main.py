import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk 
import tkinter as tk
import random
from tkinter import messagebox


def futebol():
    janela.destroy()
    futebol = tk.Toplevel()
    global times 
    times =["PALMEIRAS", "FLAMENGO", "SAOPAULO", "INTERNACIONAL", "GRÊMIO", "CRUZEIRO", "CORINTHIANS", "MANAUS", "BOTAFOGO", "BARCELONA", "LIVERPOOL", "CRB", "GALATASARAY", "VITORIA", "VASCO", "SANTOS", "GOIAS", "FORTALEZA", "PSG", "SEVILLA", "JUVENTUS", "NAPOLI", "FIORENTINA"]
    global time_escolhido 
    time_escolhido = random.choice(times)
    global erros 
    erros = 3
    global tamanho_time 
    tamanho_time = len(time_escolhido)
    global letrasCertas 
    letrasCertas = []
    global letrasErradas 
    letrasErradas = []
    global jogarNovamente 
    jogarNovamente = True
    global vit 
    vit = "n"

    global letrasPalavra 
    letrasPalavra = list('_' * tamanho_time)  # Inicializa com '_' para representar letras ocultas
    #funções
    def acrescentarLetra():
        global erros
        global letrasCertas
        global letrasErradas
        global letrasPalavra
        
        t = tamanho_time
        e = valorEntrada.get().upper()
        
        # Verificação se a letra já foi utilizada
        if e in letrasCertas or e in letrasErradas:
            messagebox.showwarning(title="ATENÇÃO!", message="A letra {} já foi utilizada! Tente outra letra".format(e))
        else:
            if e in time_escolhido:
                letrasCertas.append(e)
                lbresrod.config(text="A letra {} está na palavra".format(e))
                valorEntrada.set("")
                
                # Atualiza a exibição da palavra revelada
                for i, letra in enumerate(time_escolhido):
                    if letra == e:
                        letrasPalavra[i] = e
                lbintro2.config(text="Palavra: {}".format(' '.join(letrasPalavra)))
                
            else:
                letrasErradas.append(e)
                erros -= 1
                lbresrod.config(text="Você errou a letra!\nTente novamente.\n")
                valorEntrada.set("")
        
        lbletra_e.config(text="Letras erradas: {}".format(', '.join(letrasErradas)))
        lberros.config(text="Quantidade de erros: {}".format(erros))
        verificarVitoria()

    def verificarVitoria():
        global vit
        global letrasCertas
        global erros
        
        if len(letrasCertas) == len(set(time_escolhido)):
            messagebox.showinfo(title="Parabéns!", message="Você venceu!")
            vit="s"
            redefinir()
        elif erros <= 0:
            messagebox.showerror(title="Não foi desta vez!", message="Você perdeu! O time era o {}".format(time_escolhido))
            redefinir()

    def redefinir():
        global letrasErradas
        global jogarNovamente
        global erros
        global letrasCertas
        global vit
        global letrasPalavra
        global time_escolhido
        
        jogarNovamente = True
        erros = 3
        letrasCertas = [] 
        letrasErradas = []
        lbletra_e.config(text="Letras erradas: {}".format(', '.join(letrasErradas)))
        vit = "n"
        lbresrod.config(text=" ")
        lberros.config(text="Quantidade de erros: {}".format(erros))
        time_escolhido = random.choice(times)
        letrasPalavra = list('_' * len(time_escolhido))
        lbintro2.config(text="Palavra: {}".format(' '.join(letrasPalavra)))

    futebol.resizable(False, False)
    icone = "D:/Cursos/Jornada_do_Dev/python/aulas/jogodaforca/icon.ico"
    futebol.title("Jogo da Forca")
    icone = "D:/Cursos/Jornada_do_Dev/python/aulas/jogodaforca/icon.ico"
    futebol.iconbitmap(icone)
    futebol.geometry("900x700")
    futebol.configure(background="#2c6b21")

    #Titulo da janela

    titulo = Label(futebol, text="Times de futebol", foreground="#fff", background="#2c6b21", font=("Roboto", 30))
    titulo.pack(ipady=20)

    #quadro1 - parte a esquerda da janela

    quadro1 = Frame(futebol, background="#2c6b21", relief="solid", borderwidth=2)
    quadro1.place(x = 15, y = 150, width = 500, height = 500)

    lbintro1 = Label(quadro1, text="Bem-vindo/a ao jogo da forca(categoria times de futebol)!\n Digite letras até completar a palavra, mas lembrando:\n você tem apenas 6 chances!", fg="#fff", background="#2c6b21", font=("Roboto", 14))
    lbintro1.pack(pady=20)

    lbintro2 = Label(quadro1, text="Palavra: {}".format(' '.join(letrasPalavra)), fg="#fff", background="#2c6b21", font=("Roboto", 16))
    lbintro2.pack()


    lbentry = Label(quadro1, text="Digite aqui a letra: ", fg="#fff", background="#2c6b21", font=("Roboto", 16))
    lbentry.pack(pady = 30)

    valorEntrada = StringVar()
    entrada = Entry(quadro1, width = 15, background="#fff", font=("Roboto", 16), relief="flat",textvariable=valorEntrada)
    entrada.pack(pady=20)

    bnt_entrada = Button(quadro1, text="Enviar letra", font=("Roboto", 16), relief="flat", fg="#fff", background="#000", command=acrescentarLetra)
    bnt_entrada.pack()

    #quadro2 - parte a direita da janela

    quadro2 = Frame(futebol, background="#2c6b21", relief="solid", borderwidth=2)
    quadro2.place(x = 530, y = 150, width = 350, height = 500)

    lbresrodt = Label(quadro2, text="Resultado da rodada:", fg="#fff", background="#2c6b21", font=("Roboto", 20)) #label pra mostrar o titulo resultado da rodada
    lbresrodt.pack(anchor="nw", pady=20, padx=35)

    lbresrod = Label(quadro2, text="", fg="#fff", background="#2c6b21", font=("Roboto", 12)) #label pra mostrar o resultado da rodada
    lbresrod.pack(anchor="center", pady=40)

    lbletra_e = Label(quadro2, text="Letras erradas: {}".format(', '.join(letrasErradas)), fg="#fff", background="#2c6b21", font=("Roboto", 16)) #label pra mostrar as letras erradas
    lbletra_e.pack(anchor="nw", pady=20, padx=10)

    lberros = Label(quadro2, text="Quantidade de erros: {}".format(erros), fg="#fff", background="#2c6b21", font=("Roboto", 16)) #label pra mostrar os erros
    lberros.pack(anchor="nw", pady=20, padx=10)


        


def Sobre():
    janela.destroy()
    sobre = tk.Toplevel() #abre o tkinter
    sobre.resizable(False, False) #impossibilita que o usuário mude o formato da janela
    icone = "D:/Cursos/Jornada_do_Dev/python/aulas/jogodaforca/icon.ico"#endereço do ícone
    sobre.iconbitmap(icone)#icone
    sobre.title("Sobre o jogo")
    sobre.geometry("900x700")
    sobre.configure(background="#69d2ff")

    #Título
    h1 = Label(sobre,text="Sobre o jogo", font=("Montserrat",36), background="#69d2ff")
    h1.pack(pady=20)

    #Parágrafos
    p1 = Label(sobre,text="Espero que tenham desfrutado deste simples jogo!", font=("Montserrat", 16), background="#69d2ff")
    p1.pack(pady=20)

    #foto
    image = Image.open("D:/Cursos/Jornada_do_Dev/python/aulas/jogodaforca/icon.ico")
    photo = ImageTk.PhotoImage(image)
    img = Label(sobre, image=photo)
    img.pack(pady=50)

    p2 = Label(sobre,text="Esse jogo foi desenvolvido por Rikelme Sousa de Carvalho", font=("Montserrat",16), background="#69d2ff")
    p2.pack(side="bottom", pady=30)



janela = Tk()
os.system('cls')
janela.resizable(False, False)
icone = "D:/Cursos/Jornada_do_Dev/python/aulas/jogodaforca/icon.ico"
janela.title("Jogo da Forca")
icone = "D:/Cursos/Jornada_do_Dev/python/aulas/jogodaforca/icon.ico"
janela.iconbitmap(icone)
janela.geometry("900x700")
janela.configure(background="#2c6b21")

titulo = Label(janela, text="Jogo da forca", foreground="#fff", background="#2c6b21", font=("Roboto", 32))
titulo.pack(ipady=40)

main = Frame(janela, background="#2c6b21")
main.pack(fill=X, expand= True, ipady=60)

btn_jogar = Button(main, text="Jogar", command=futebol, width=15, height=3, font=("Roboto", 16), relief="solid", borderwidth=3, background="#2c6b21", fg="#fff")
btn_jogar.pack(pady=60)

btn_sobre = Button(main, text="Sobre", command=Sobre, width=15, height=3, font=("Roboto", 16), relief="solid", borderwidth=3, background="#2c6b21", fg="#fff")
btn_sobre.pack()

image = Image.open("D:/Cursos/Jornada_do_Dev/python/aulas/jogodaforca/icon.ico")
photo = ImageTk.PhotoImage(image)
img = Label(main, image=photo)
img.pack(pady=50)

janela.mainloop()