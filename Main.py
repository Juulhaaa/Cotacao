import requests
from tkinter import *
def pegar_cotacao():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    rqs = requisicao.json()
    a = rqs['USDBRL']['bid']
    e = rqs['EURBRL']['bid']
    b = rqs['BTCBRL']['bid']

    texto = f'''
        DOLAR:{a}
        EURO:{e}
        BTC:{b}'''
    
    #print(texto)

    texto_resposta["text"] = texto
    
    def limpar():
        texto_resposta["text"] = " "

janela = Tk()
janela.geometry("200x200")
janela.title("cotação atual de moedas")
texto = Label(janela,text ="clique no no botão para exibir as cotações de moedas")
texto.grid (column = 0,row = 0, padx = 10, pady = 10)

botao = Button(janela,text="Buscar cotações", command = pegar_cotacao)
botao.grid(column = 0, row = 1, padx = 10, pady = 10)

janela.mainloop()


