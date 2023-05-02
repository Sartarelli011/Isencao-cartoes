from tkinter import *
from functions import start
#criando a janela com tkinter

janela = Tk()
janela.geometry("300x200")
janela.title("Isenção")

texto_orientacao = Label(janela, text="Isenção dos cartões de crédito.")
texto_orientacao.grid(column=1, row=1, padx=10, pady=10)

botao = Button(janela, text="Iniciar", command=start)
botao.grid(column=1, row=2, pady=10, padx=10)

janela.mainloop()
