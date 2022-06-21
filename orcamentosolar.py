from cgitb import text
from msilib.schema import RadioButton
from tkinter import CENTER, Button, Entry, Grid, Image, IntVar, Label, Tk, Toplevel
from turtle import bgcolor
from numpy import place

import math


master = Tk()
master.geometry('650x650')
master.title("ORÇAMENTOS SISTEMA SOLAR")


#FUNÇÃO PRINCIPAL DO CODIGO CONTENDO AS OPERAÇÕES#
def return_entry():
    """PEGA O CONTEUDO DO TEXTO"""
    nome = entry.get()
    
    consumo = float(entry1.get())

    valor = consumo/30.4

    psistema = (valor/0.76)/4.78

    janeiro = psistema*6.43*30.4*0.76
    fevereiro = psistema*5.91*30.4*0.76
    marco = psistema*5.35*30.4*0.76
    abril = psistema*4.19*30.4*0.76
    maio = psistema*3.27*30.4*0.76
    junho = psistema*2.79*30.4*0.76
    julho = psistema*3.02*30.4*0.76
    agosto = psistema*3.98*30.4*0.76
    setembro = psistema*4.28*30.4*0.76
    outubro = psistema*5.29*30.4*0.76
    novembro = psistema*6.17*30.4*0.76
    dezembro = psistema*6.63*30.4*0.76
    
    geracao_media = float(janeiro+fevereiro+marco+abril+maio+junho+julho+agosto+setembro+outubro+novembro+dezembro)/12
    
    quant_placas = float(psistema*1000)/450
    
    area_sistema = float(quant_placas*2.158)
    
    lb_nome = Label(master, text=f'CLIENTE: {nome}').grid(row=4,column=10)
    
    lb_soma = Label(master, text=f'{round(valor, 2)} Consumo diario(kWh/mês)'
                   , font=50).grid(row=5, column=10)
    lb_sistema = Label(
        master, text=f'{round(psistema, 2)} Potência do sistema/calculada(kWp)', bg='red', font=50).grid(row=6, column=10)
    lb_janeiro = Label(
        master, text=f'{math.ceil(janeiro)} kWh/mês-Geração mês de janeiro',  font=50).grid(row=7, column=10)
    lb_fevereiro = Label(
        master, text=f'{math.ceil(fevereiro)} kWh/mês-Geração mês de Fevereiro',  font=50).grid(row=8, column=10)
    lb_marco = Label(
        master, text=f'{math.ceil(marco)} kWh/mês-Geração mês de Março', font=50).grid(row=9, column=10)
    lb_abril = Label(
        master, text=f'{math.ceil(abril)} kWh/mês-Geração mês de Abril',font=50).grid(row=10, column=10)
    lb_maio = Label(
        master, text=f'{math.ceil(maio)} kWh/mês-Geração mês de Maio', font=50).grid(row=11, column=10)
    lb_junho = Label(
        master, text=f'{math.ceil(junho)} kWh/mês-Geração mês de Junho',  font=50).grid(row=12, column=10)
    lb_julho = Label(
        master, text=f'{math.ceil(julho)} kWh/mês-Geração mês de Julho',  font=50).grid(row=13, column=10)
    lb_agosto = Label(
        master, text=f'{math.ceil(agosto)} kWh/mês-Geração mês de Agosto',  font=50).grid(row=14, column=10)
    lb_setembro = Label(
        master, text=f'{math.ceil(setembro)} kWh/mês-Geração mês de Setembro', font=50).grid(row=15, column=10)
    lb_outubro = Label(
        master, text=f'{math.ceil(outubro)} kWh/mês-Geração mês de Outubro', font=50).grid(row=16, column=10)
    lb_novembro = Label(
        master, text=f'{math.ceil(novembro)} kWh/mês-Geração mês de Novembro', font=50).grid(row=17, column=10)
    lb_dezembro = Label(
        master, text=f'{math.ceil(dezembro)} kWh/mês-Geração mês de Dezembro',  font=50).grid(row=18, column=10)
    
    lb_geracao_media = Label(master , text=f'{round(geracao_media , 2)} Geração Média', font=50).grid(row=19,column=10)
    
    lb_quant_placas = Label(master , text=f'{round(quant_placas)} Paineis Solares de 450W', font=50).grid(row=20,column=10)
    
    lb_area_sistema = Label(master, text=f'{round(area_sistema)} m²',font=50).grid(row=21,column=10)
    
    

def painel460w():
    nome = entry.get()
    consumo = float(entry1.get())
    valor = consumo/30.4

    psistema = (valor/0.76)/4.78

    janeiro = psistema*6.43*30.4*0.76
    fevereiro = psistema*5.91*30.4*0.76
    marco = psistema*5.35*30.4*0.76
    abril = psistema*4.19*30.4*0.76
    maio = psistema*3.27*30.4*0.76
    junho = psistema*2.79*30.4*0.76
    julho = psistema*3.02*30.4*0.76
    agosto = psistema*3.98*30.4*0.76
    setembro = psistema*4.28*30.4*0.76
    outubro = psistema*5.29*30.4*0.76
    novembro = psistema*6.17*30.4*0.76
    dezembro = psistema*6.63*30.4*0.76
    
    geracao_media = float(janeiro+fevereiro+marco+abril+maio+junho+julho+agosto+setembro+outubro+novembro+dezembro)/12
    
    quant_placas = float(psistema*1000)/460
    
    area_sistema = float(quant_placas*2.158)
    lb_nome = Label(master, text=f'CLIENTE: {nome}').grid(row=4,column=10)
    lb_soma = Label(master, text=f'{round(valor, 2)} Consumo diario(kWh/mês)'
                    , font=50).grid(row=5, column=10)
    lb_sistema = Label(
        master, text=f'{round(psistema, 2)} Potência do sistema/calculada(kWp)', bg='red', font=50).grid(row=6, column=10)
    lb_janeiro = Label(
        master, text=f'{math.ceil(janeiro)} kWh/mês-Geração mês de janeiro',  font=50).grid(row=7, column=10)
    lb_fevereiro = Label(
        master, text=f'{math.ceil(fevereiro)} kWh/mês-Geração mês de Fevereiro',  font=50).grid(row=8, column=10)
    lb_marco = Label(
        master, text=f'{math.ceil(marco)} kWh/mês-Geração mês de Março', font=50).grid(row=9, column=10)
    lb_abril = Label(
        master, text=f'{math.ceil(abril)} kWh/mês-Geração mês de Abril',font=50).grid(row=10, column=10)
    lb_maio = Label(
        master, text=f'{math.ceil(maio)} kWh/mês-Geração mês de Maio', font=50).grid(row=11, column=10)
    lb_junho = Label(
        master, text=f'{math.ceil(junho)} kWh/mês-Geração mês de Junho',  font=50).grid(row=12, column=10)
    lb_julho = Label(
        master, text=f'{math.ceil(julho)} kWh/mês-Geração mês de Julho',  font=50).grid(row=13, column=10)
    lb_agosto = Label(
        master, text=f'{math.ceil(agosto)} kWh/mês-Geração mês de Agosto',  font=50).grid(row=14, column=10)
    lb_setembro = Label(
        master, text=f'{math.ceil(setembro)} kWh/mês-Geração mês de Setembro', font=50).grid(row=15, column=10)
    lb_outubro = Label(
        master, text=f'{math.ceil(outubro)} kWh/mês-Geração mês de Outubro', font=50).grid(row=16, column=10)
    lb_novembro = Label(
        master, text=f'{math.ceil(novembro)} kWh/mês-Geração mês de Novembro', font=50).grid(row=17, column=10)
    lb_dezembro = Label(
        master, text=f'{math.ceil(dezembro)} kWh/mês-Geração mês de Dezembro',  font=50).grid(row=18, column=10)
    
    lb_geracao_media = Label(master , text=f'{round(geracao_media , 2)} Geração Média', font=50).grid(row=19,column=10)
    
    lb_quant_placas = Label(master , text=f'{round(quant_placas)} Paineis Solares de 460W', font=50).grid(row=20,column=10)
    
    lb_area_sistema = Label(master, text=f'{round(area_sistema)} m²',font=50).grid(row=21,column=10)

def painel545w():
    nome = entry.get()
    consumo = float(entry1.get())
    valor = consumo/30.4

    psistema = (valor/0.76)/4.78

    janeiro = psistema*6.43*30.4*0.76
    fevereiro = psistema*5.91*30.4*0.76
    marco = psistema*5.35*30.4*0.76
    abril = psistema*4.19*30.4*0.76
    maio = psistema*3.27*30.4*0.76
    junho = psistema*2.79*30.4*0.76
    julho = psistema*3.02*30.4*0.76
    agosto = psistema*3.98*30.4*0.76
    setembro = psistema*4.28*30.4*0.76
    outubro = psistema*5.29*30.4*0.76
    novembro = psistema*6.17*30.4*0.76
    dezembro = psistema*6.63*30.4*0.76
    
    geracao_media = float(janeiro+fevereiro+marco+abril+maio+junho+julho+agosto+setembro+outubro+novembro+dezembro)/12
    
    quant_placas = float(psistema*1000)/545
    
    area_sistema = float(quant_placas*2.5)
    lb_nome = Label(master, text=f'CLIENTE: {nome}').grid(row=4,column=10)
    lb_soma = Label(master, text=f'{round(valor, 2)} Consumo diario(kWh/mês)',
                     font=50).grid(row=5, column=10)
    lb_sistema = Label(
        master, text=f'{round(psistema, 2)} Potência do sistema/calculada(kWp)', bg='red', font=50).grid(row=6, column=10)
    lb_janeiro = Label(
        master, text=f'{math.ceil(janeiro)} kWh/mês-Geração mês de janeiro',  font=50).grid(row=7, column=10)
    lb_fevereiro = Label(
        master, text=f'{math.ceil(fevereiro)} kWh/mês-Geração mês de Fevereiro',  font=50).grid(row=8, column=10)
    lb_marco = Label(
        master, text=f'{math.ceil(marco)} kWh/mês-Geração mês de Março', font=50).grid(row=9, column=10)
    lb_abril = Label(
        master, text=f'{math.ceil(abril)} kWh/mês-Geração mês de Abril',font=50).grid(row=10, column=10)
    lb_maio = Label(
        master, text=f'{math.ceil(maio)} kWh/mês-Geração mês de Maio', font=50).grid(row=11, column=10)
    lb_junho = Label(
        master, text=f'{math.ceil(junho)} kWh/mês-Geração mês de Junho',  font=50).grid(row=12, column=10)
    lb_julho = Label(
        master, text=f'{math.ceil(julho)} kWh/mês-Geração mês de Julho',  font=50).grid(row=13, column=10)
    lb_agosto = Label(
        master, text=f'{math.ceil(agosto)} kWh/mês-Geração mês de Agosto',  font=50).grid(row=14, column=10)
    lb_setembro = Label(
        master, text=f'{math.ceil(setembro)} kWh/mês-Geração mês de Setembro', font=50).grid(row=15, column=10)
    lb_outubro = Label(
        master, text=f'{math.ceil(outubro)} kWh/mês-Geração mês de Outubro', font=50).grid(row=16, column=10)
    lb_novembro = Label(
        master, text=f'{math.ceil(novembro)} kWh/mês-Geração mês de Novembro', font=50).grid(row=17, column=10)
    lb_dezembro = Label(
        master, text=f'{math.ceil(dezembro)} kWh/mês-Geração mês de Dezembro',  font=50).grid(row=18, column=10)
    
    lb_geracao_media = Label(master , text=f'{round(geracao_media , 2)} Geração Média', font=50).grid(row=19,column=10)
    
    lb_quant_placas = Label(master , text=f'{round(quant_placas)} Paineis Solares de 545W', font=50).grid(row=20,column=10)
    
    lb_area_sistema = Label(master, text=f'{round(area_sistema)} m²',font=50).grid(row=21,column=10)

def painel550w():
    nome = entry.get()
    consumo = float(entry1.get())
    valor = consumo/30.4

    psistema = (valor/0.76)/4.78

    janeiro = psistema*6.43*30.4*0.76
    fevereiro = psistema*5.91*30.4*0.76
    marco = psistema*5.35*30.4*0.76
    abril = psistema*4.19*30.4*0.76
    maio = psistema*3.27*30.4*0.76
    junho = psistema*2.79*30.4*0.76
    julho = psistema*3.02*30.4*0.76
    agosto = psistema*3.98*30.4*0.76
    setembro = psistema*4.28*30.4*0.76
    outubro = psistema*5.29*30.4*0.76
    novembro = psistema*6.17*30.4*0.76
    dezembro = psistema*6.63*30.4*0.76
    
    geracao_media = float(janeiro+fevereiro+marco+abril+maio+junho+julho+agosto+setembro+outubro+novembro+dezembro)/12
    
    quant_placas = float(psistema*1000)/550
    
    area_sistema = float(quant_placas*2.5)
    lb_nome = Label(master, text=f'CLIENTE: {nome}').grid(row=4,column=10)
    lb_soma = Label(master, text=f'{round(valor, 2)} Consumo diario(kWh/mês)',
                   font=50).grid(row=5, column=10)
    lb_sistema = Label(
        master, text=f'{round(psistema, 2)} Potência do sistema/calculada(kWp)', bg='red', font=50).grid(row=6, column=10)
    lb_janeiro = Label(
        master, text=f'{math.ceil(janeiro)} kWh/mês-Geração mês de janeiro',  font=50).grid(row=7, column=10)
    lb_fevereiro = Label(
        master, text=f'{math.ceil(fevereiro)} kWh/mês-Geração mês de Fevereiro',  font=50).grid(row=8, column=10)
    lb_marco = Label(
        master, text=f'{math.ceil(marco)} kWh/mês-Geração mês de Março', font=50).grid(row=9, column=10)
    lb_abril = Label(
        master, text=f'{math.ceil(abril)} kWh/mês-Geração mês de Abril',font=50).grid(row=10, column=10)
    lb_maio = Label(
        master, text=f'{math.ceil(maio)} kWh/mês-Geração mês de Maio', font=50).grid(row=11, column=10)
    lb_junho = Label(
        master, text=f'{math.ceil(junho)} kWh/mês-Geração mês de Junho',  font=50).grid(row=12, column=10)
    lb_julho = Label(
        master, text=f'{math.ceil(julho)} kWh/mês-Geração mês de Julho',  font=50).grid(row=13, column=10)
    lb_agosto = Label(
        master, text=f'{math.ceil(agosto)} kWh/mês-Geração mês de Agosto',  font=50).grid(row=14, column=10)
    lb_setembro = Label(
        master, text=f'{math.ceil(setembro)} kWh/mês-Geração mês de Setembro', font=50).grid(row=15, column=10)
    lb_outubro = Label(
        master, text=f'{math.ceil(outubro)} kWh/mês-Geração mês de Outubro', font=50).grid(row=16, column=10)
    lb_novembro = Label(
        master, text=f'{math.ceil(novembro)} kWh/mês-Geração mês de Novembro', font=50).grid(row=17, column=10)
    lb_dezembro = Label(
        master, text=f'{math.ceil(dezembro)} kWh/mês-Geração mês de Dezembro',  font=50).grid(row=18, column=10)
    
    lb_geracao_media = Label(master , text=f'{round(geracao_media , 2)} Geração Média',bg='red' ,font=50).grid(row=19,column=10)
    
    lb_quant_placas = Label(master , text=f'{round(quant_placas)} Paineis Solares de 550W',bg='red' ,font=50).grid(row=20,column=10)
    
    lb_area_sistema = Label(master, text=f'{round(area_sistema)} m²',bg='red' ,font=50).grid(row=21,column=10)

def abrir_janela():
    janela2 = Toplevel()
    janela2.title("INFORMAÇOES")
    botao_voltar = Button(janela2, text="FECHAR JANELA2" , command= janela2.destroy)
    botao_voltar.grid(column=11,row=30)

#LINHAS DOS DADOS DE ENTRADA DOS CLIENTES#




Label(master, text="Consumo Médio(kWh/mês):",
      font='Arial').grid(row=0, column=2)
Label(master, text='Nome do Cliente:', font='Arial').grid(row=2, column=2)
btn = Button(master, text='Painel de 450 W', font='Arial', bg="blue", command=return_entry).grid(row=7, column=2)

painel = Button(master, text='Painel de 460 W' , font='Arial', bg ='blue', command=painel460w).grid(row=8,column=2)

painell = Button(master, text='Painel de 545 W' , font='Arial', bg ='blue', command=painel545w).grid(row=9,column=2)

painelll = Button(master,text='Painel de 550 W' , font='Arial', bg ='blue', command=painel550w).grid(row=10,column=2)

botao_janela = Button(master , text='ABRIR NOVA JANELA AQUI' , command=abrir_janela).grid(row=22,column=11)


#ENTRADAS DE DADOS DOS CLIENTES#
entry = Entry(master, text='Nome do Cliente')
entry.grid(row=2, column=5)

entry1 = Entry(master, text='CONSUMO')
entry1.grid(row=0, column=5)


entry.bind('<Return>', return_entry)
entry1.bind('<Return>', return_entry)


master.mainloop()
