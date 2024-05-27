import tkinter as tk
from tkinter import messagebox as mb
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import StringVar
from tkinter import messagebox
import sqlite3

#começar com tela com um botão e um entry (nome)- v1
#adicionar mais duas entrys (cpf e estado) e suas labels - v2
#mudar o fundo para uma imagem mais bonita, adicionar readme.txt explicando como usar - v3
#adicionar clicar no botão salva os 3 dados em um sqlite - v4
#Criar uma branch em que le um config.txt com uma lista de 5 estados possiveis separados por pular linha - x1
#Mudar o separador para ; e adicionar mais 5 estados - x2
#Voltar para main, criar outra branch e criar um dropdown com 3 opções (clt, mei, socio) - y1
#Voltar para main, Corrigir o bug da função de cpf - v5
#Merge de x com v - v6
#Adicionar verificação de CPF e de estado, com base na função cpf e na lista de estados .txt antes de adicionar no sqlite v7

#Cria conexção
connection = sqlite3.connect("teste.db")

#Cria o cursos e cria a tabela
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Tabela1 (nome TEXT, cpf TEXT, estado TEXT)")

#Ler config
config = open('config.txt', 'r')
config_read = config.read()
config_final = config_read.split(';')


def VerificarCPF(CPF):
    #CPF deve ser na forma "123.456.789-10"
    print(CPF)
    validado = True
    if len(CPF)!=14:
        return False
    CPF = CPF.split("-")[0]
    for trecho in CPF.split("."):
        if len(trecho)!=3:
                validado = False
    return validado

def Verificar_Estado(estado):
    print(estado)
    if estado in config_final:
        return True
    else:
        return False

def inserevalores(Valor1, Valor2, Valor3):
    #Insere linha na tabela
 if VerificarCPF(Valor2) and Verificar_Estado(Valor3):
        cursor.execute(f"INSERT INTO Tabela1 VALUES ('{Valor1}', '{Valor2}', '{Valor3}')")
        messagebox.showinfo('Aviso!', 'Adicionado com sucesso!')
        print('adicionado')
    else:
        messagebox.showinfo('Erro!', 'Não adicionado. Informações Incorretas.')
        print('Error.')

def pegavalores():
    #Pega valores da tabela
    rows = cursor.execute("SELECT * FROM Tabela1").fetchall()
    print(rows)

def funcExemplo():
    print("Exemplo de funcao")

def Main():
    root = tk.Tk()
    root.title("Trabalho RAD")
    root.geometry('714x260')
    root.resizable(False, False)
    bi = PhotoImage(file=r"C:\Users\Usuário\Desktop\TrabRad\bg.png")
    bi_l = tk.Label(root, image=bi)
    bi_l.place(x=0, y=0, relwidth=1, relheight=1)

    label = tk.Label(root, text="Nome")
    label.pack()

    textoEntrada = tk.StringVar()
    e1 = tk.Entry(root)
    e1.bind('<Key>', lambda x:textoEntrada.set(e1.get()+x.char))
    e1.pack()

    l2 = tk.Label(root, text='CPF')
    l2.pack()

    e2 = tk.Entry(root)
    e2.pack()

    l3 = tk.Label(root, text="Estado")
    l3.pack()

    e3 = tk.Entry(root)
    e3.pack()
    print(config_final)

    l4 = tk.Label(root, text='Função')
    l4.pack()


    variable = StringVar(root)
    variable.set('CLT')
    d1 = tk.OptionMenu(root, variable, 'CLT','MEI', 'Sócio')
    d1.pack()
    
    test2 = tk.Button(root, text="Salvar")
    test2['command'] = lambda:inserevalores(Valor1=e1.get(), Valor2=e2.get(), Valor3=e3.get())  #alterar para chamar outra função
    test2.pack()

    root.iconify() #Minimiza a tela
    root.update()
    root.deiconify() #Maximiza a tela
    root.mainloop()  #loop principal, impede o código de seguir e permite capturar inputs
