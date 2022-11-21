#Componentes do grupo:
# Dayane Gabriela Santos Cordeiro - 673915 - Engenharia de computação - PUC Minas Coração Eucarístico
# Paulo Henrique Luiz Pereira - 673667 - Engenharia de computação - PUC Minas Coração Eucarístico

from PIL import ImageTk, Image
import tkinter as tk
from tkinter import messagebox
import selecionando_imagem
import recorte_imagem
import correlacao_cruzada as cc
import classificador_raso
import CNN_Resnet50_custon


caminho_img_a = "../TP_PAI-Dayane-Paulo/image/escolha_img_a.png"
caminho_img_b = "../TP_PAI-Dayane-Paulo/image/escolha_img_b.png"
caminho_completo_img_b = "../TP_PAI-Dayane-Paulo//image/recorte_img_b.png"


class Interface:
  def __init__(self, master):
    self.interTela1 = master
    
    #Config da janela
    self.interTela1.title("Diagnóstico de Osteoartrite Femorotibial através de imagens de raio X")
    self.interTela1.geometry('910x560')

    #Widgets da janela
    #Widget da imagem A
    self.img_a = ImageTk.PhotoImage(Image.open(caminho_img_a))
    self.exibe_img_a = tk.Label(self.interTela1, image=self.img_a)
    self.exibe_img_a.grid(row=0, column=0, columnspan=5)
    self.lbl_img_a = tk.Label(self.interTela1, text="Imagem A")
    self.lbl_img_a.grid(row=1, column=0, columnspan=5)

    #Widget do resultado
    self.resultado = tk.Text(self.interTela1, width=60, height=20)
    self.resultado.grid(row=0, column=6, columnspan=5)
    self.lbl_resultado = tk.Label(self.interTela1, text="Resultado")
    self.lbl_resultado.grid(row=1, column=6, columnspan=5)
    
    #Widget da imagem B
    self.img_b = ImageTk.PhotoImage(Image.open(caminho_img_b))
    self.exibe_img_b = tk.Label(self.interTela1, image=self.img_b)
    self.exibe_img_b.grid(row=0, column=13, columnspan=5)
    self.lbl_img_b = tk.Label(self.interTela1, text="Imagem B")
    self.lbl_img_b.grid(row=1, column=13, columnspan=5)

    self.lbl = tk.Label(self.interTela1)
    self.lbl.grid(row=2, column=0, columnspan=15)
    
    #Widget da imagem B recortada
    self.r_img_b = ImageTk.PhotoImage(Image.open(caminho_completo_img_b))
    self.exibe_r_img_b = tk.Label(self.interTela1, image=self.r_img_b)
    self.exibe_r_img_b.grid(row=3, column=6, columnspan=5)
    self.lbl_recorte_img_b = tk.Label(self.interTela1, text="Imagem B recortada")
    self.lbl_recorte_img_b.grid(row=4, column=6, columnspan=5)

    #Config da barra de menu
    self.barra_menu = tk.Menu(self.interTela1)
    self.interTela1.config(menu = self.barra_menu)

    #SubMenu de Arquivo, Classf raso e CNN
    self.arquivo = tk.Menu(self.barra_menu, tearoff=0)
    self.classf_raso = tk.Menu(self.barra_menu, tearoff=0)
    self.cnn = tk.Menu(self.barra_menu, tearoff=0)

    #Opções do SubMenu de Arquivo
    self.arquivo.add_command(label="Abrir img A", command=self.sel_img_a)
    self.arquivo.add_command(label="Abrir img B", command=self.sel_img_b)
    self.arquivo.add_separator()
    self.arquivo.add_command(label="Recortar img B", command=self.recorte)

    #Opções do SubMenu de Classf raso
    self.classf_raso.add_command(label="Binária", command=self.classf_raso_bin)
    self.classf_raso.add_command(label="5 classes KL", command=self.classf_raso_5classesKL)

    #Opções do SubMenu de CNN
    self.cnn.add_command(label="Binária", command=self.cnn_bin)
    self.cnn.add_command(label="5 classes KL", command=self.cnn_5classesKL)

    #Botões do Menu
    self.barra_menu.add_cascade(label="Arquivo", menu=self.arquivo)
    self.barra_menu.add_command(label="Corr cruz A&B", command=self.corr_cruz_ab)
    self.barra_menu.add_cascade(label="Classf raso", menu=self.classf_raso)
    self.barra_menu.add_cascade(label="CNN", menu=self.cnn)
    self.barra_menu.add_command(label="Exibir último resultado", command=self.exibir_resultados)
    self.barra_menu.add_command(label="Sobre", command=self.sobre)

  def sel_img_a(self):
    global caminho_img_a
    #Abrindo o explorador de arquivos e selecionando a imagem A
    caminho_img_a = selecionando_imagem.selecionando_imagens("A")
    self.img_a = ImageTk.PhotoImage(Image.open(caminho_img_a))
    self.exibe_img_a.configure(image=self.img_a)

  def sel_img_b(self):
    global caminho_completo_img_b
    #Abrindo o explorador de arquivos e selecionando a imagem B
    caminho_completo_img_b = selecionando_imagem.selecionando_imagens("B")
    self.img_b = ImageTk.PhotoImage(Image.open(caminho_completo_img_b))
    self.exibe_img_b.configure(image=self.img_b)

  def recorte(self):
    global caminho_img_b
    caminho_img_b = recorte_imagem.recortar_img(caminho_completo_img_b)
    self.r_img_b = ImageTk.PhotoImage(Image.open(caminho_img_b))
    self.exibe_r_img_b.configure(image=self.r_img_b)

  def corr_cruz_ab(self):
    cc.calc_corr_cruz_ab(caminho_img_a, caminho_img_b)
    self.exibir_resultados()

  def classf_raso_bin(self):
    tipo_classf=2
    classificador_raso.classf_raso(tipo_classf)
    self.exibir_resultados()

  def classf_raso_5classesKL(self):
    tipo_classf=5
    classificador_raso.classf_raso(tipo_classf)
    self.exibir_resultados()
  
  def cnn_bin(self):
    CNN_Resnet50_custon.resnet50_Binaria()
    self.exibir_resultados()

  def cnn_5classesKL(self):
    CNN_Resnet50_custon.resnet50_5classesKL()
    self.exibir_resultados()
  
  def exibir_resultados(self):
    #Limpa a caixa de texto com os resultados
    self.resultado.delete("1.0",tk.END)
    
    #Abre o arquivo com os resultados e exibe na caixa e fecha o arquivo
    f = open('saidas.txt', 'r')
    saida = f.read()
    self.resultado.insert(tk.END, saida)
    f.close()

  def sobre(self):
    self.sobre = messagebox.showinfo(
        "Sobre","Trabalho desenvolvido para a disciplina de "
                "Processamento e Análise de Imagens\n"      
                "\nEngenharia de Computacão\nPUC Minas Coração Eucarístico"
                "\n2° semestre de 2022\n8° período\n"
                "\nAutores:"
                "\nDayane Gabriela\nSantos Cordeiro - 673915"
                "\nPaulo Henrique\nLuiz Pereia - 673667")
  

def interface():
  #Gera a interface
  janelaRaiz = tk.Tk()

  #Passa a instância de Tk
  Interface(janelaRaiz)
  
  #Faz a janela ficar aberta 
  #esperando a interação com o usuário
  janelaRaiz.mainloop()