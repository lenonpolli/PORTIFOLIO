from cgitb import text
from doctest import master
from tkinter import *
import sqlite3

master = Tk()
master.geometry("500x500")
master.title('GRAEFF ENGENHARIA - SISTEMA')
master.configure(background='gray40')


def return_entry():
    
    
    #COLETA DOS DADOS#
    nome = entry.get()
    potencia = campo_potencia.get()
    email = campo_potencia.get()
    placas = campo_placas.get()
    inversor = campo_inversor.get()
    endereco = campo_endereco.get()
    
    
    #BANCO DE DADOS#
    banco = sqlite3.connect('DADOS_empresa.db') # CRIA UM ARQUIVO SQL
    cursor = banco.cursor()
    #cursor.execute("CREATE TABLE CLIENTES(nome text,potencia text,email text,placas integer,inversor text,endereco text)")
    cursor.execute("INSERT INTO CLIENTES VALUES('"+nome+"',"+str(potencia)+",'"+email+"',"+str(placas)+",'"+inversor+"','"+endereco+"')") # SQL ARMAZENA O TEXTO
    
    

    print(nome)
    banco.commit() # FIM BANCO DE DADOS#



#NOME CLIENTE#
entry = Entry(master, text='CLIENTE')
entry.grid(row=1,column=5)
Label(master , text='NOME DO CLIENTE' , bg='red').grid(row=1,column=0)

#CAMPO POTENCIA#
campo_potencia = Entry(master,text= 'POTENCIA')
campo_potencia.grid(row=3,column=5)
Label(master , text='POTENCIA', bg='red').grid(row=3,column=0)

#CAMPO EMAIL#
campo_email  = Entry(master,text = 'EMAIL')
campo_email.grid(row=5,column=5)
Label(master , text='EMAIL',bg='red').grid(row=5,column=0)

#CAMPO QUANTIDADE DE PLACAS#
campo_placas = Entry(master, text = 'PLACAS')
campo_placas.grid(row=7,column=5)
Label(master , text='QUANTIDADE DE PLACAS',bg='red').grid(row=7,column=0)

#CAMPO INVERSOR INSTALADO#
campo_inversor = Entry(master,text='INVERSOR')
campo_inversor.grid(row=9,column=5)
Label(master , text='INVERSOR',bg='red').grid(row=9,column=0)

#CAMPO ENDEREÇO#
campo_endereco = Entry(master,text = 'ENDEREÇO')
campo_endereco.grid(row=11,column=5)
Label(master , text='ENDEREÇO',bg='red').grid(row=11,column=0)


#BOTAO#
botao_cadastrar = Button(master, text='CADASTRAR', command=return_entry).grid(row=15,column=5)




master.mainloop()
