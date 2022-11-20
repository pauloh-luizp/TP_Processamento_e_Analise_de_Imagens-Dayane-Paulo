from PIL import ImageTk, Image
import tkinter as tk
import random
from tkinter import messagebox
import selecionando_imagem
import recorte_imagem
import correlacao_cruzada as cc
import classificador_raso
import CNN_Resnet50_custon
#/mnt/da/eng_computacao/processamento_de_imagens/TP/TP_PAI-Dayane-Paulo/image/escolha_img_a.png
caminho_img_a = "../TP_PAI-Dayane-Paulo/image/escolha_img_a.png"
caminho_img_b = "../TP_PAI-Dayane-Paulo/image/escolha_img_b.png"
caminho_completo_img_b = "../TP_PAI-Dayane-Paulo//image/recorte_img_b.png"


class Interface:
  def __init__(self, master):
    self.interTela1 = master
    
    #Config da janela
    self.interTela1.title("Diagnóstico de Osteoartrite Femorotibial através de imagens de raio X")
    self.interTela1.geometry('940x560')

    #Widgets da janela

    #Widget da exibicao dos resultados
    self.img_a = ImageTk.PhotoImage(Image.open(caminho_img_a))
    self.exibe_img_a = tk.Label(self.interTela1, image=self.img_a)
    self.exibe_img_a.grid(row=0, column=0, columnspan=5)
    self.lbl_img_a = tk.Label(self.interTela1, text="Imagem A")
    self.lbl_img_a.grid(row=1, column=0, columnspan=5)

    self.resultado = tk.Text(self.interTela1, width=60, height=20)
    self.resultado.grid(row=0, column=6, columnspan=5)
    self.lbl_img_b = tk.Label(self.interTela1, text="Resultado")
    self.lbl_img_b.grid(row=1, column=6, columnspan=5)
    
    self.img_b = ImageTk.PhotoImage(Image.open(caminho_img_b))
    self.exibe_img_b = tk.Label(self.interTela1, image=self.img_b)
    self.exibe_img_b.grid(row=0, column=13, columnspan=5)
    self.lbl_img_b = tk.Label(self.interTela1, text="Imagem B")
    self.lbl_img_b.grid(row=1, column=13, columnspan=5)
    
    self.r_img_b = ImageTk.PhotoImage(Image.open(caminho_completo_img_b))
    self.exibe_r_img_b = tk.Label(self.interTela1, image=self.r_img_b)
    self.exibe_r_img_b.grid(row=2, column=6, columnspan=5)
    self.lbl_recorte_img_b = tk.Label(self.interTela1, text="Imagem B recortada")
    self.lbl_recorte_img_b.grid(row=3, column=6, columnspan=5)

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
    self.barra_menu.add_command(label="Sobre")

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
    #chama a função de recortar a imagem
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
    tf = open('saidas.txt', 'r')
    saida = tf.read()
    self.resultado.insert(tk.END, saida)
    tf.close()

  

def interface():
  #Gera a interface
  janelaRaiz = tk.Tk()

  Interface(janelaRaiz)

  janelaRaiz.mainloop()

'''
def sel_img_a():
  global caminho_completo_img_a
  #Abrindo o explorador de arquivos e selecionando a imagem A
  caminho_completo_img_a = selecionando_imagem.selecionando_imagens("A")


def sel_img_b():
  global caminho_completo_img_b
  #Abrindo o explorador de arquivos e selecionando a imagem B
  caminho_completo_img_b = selecionando_imagem.selecionando_imagens("B")

def recorte():
  #Configurando o recorte da imagem e o novo nome do arquivo
  caminho_img_sel = caminho_completo_img_b[: len(caminho_completo_img_b) - 4]
  formato_img_sel = caminho_completo_img_b[len(caminho_completo_img_b) - 4 : ]
  caminho_img_b = caminho_img_sel + '_recorte' + formato_img_sel
  screen, px = recorte_imagem.setup(caminho_completo_img_b)
  left, upper, right, lower = recorte_imagem.mainLoop(screen, px)

  #Garante que a imagem de saida tenha altura e largura positivas
  if right < left:
    left, right = right, left
  if lower < upper:
    lower, upper = upper, lower

  #Recortando a imagem
  im = recorte_imagem.Image.open(caminho_completo_img_b)
  im = im.crop(( left, upper, right, lower))
  recorte_imagem.pygame.display.quit()

  #Salvando a imagem recortada
  im.save(caminho_img_b)

def interface():                                                                                               
  window = tk.Tk() 
    
  window.title('Diagnóstico de Osteoartrite Femorotibial através de imagens de raio X') 
    
  window.geometry("200x200") 
    
  window.config(background = "white") 
        
  button_explore_img_a = tk.Button(window,  
                          text = "Selecionar a imagem A",
                          compound= "center", 
                          command = sel_img_a)

  button_explore_img_b = tk.Button(window,
                          text = "Selecionar a imagem B",
                          compound= "center",
                          command = sel_img_b)  
    
  button_recorte_img_b = tk.Button(window,
                          text = "Recortar a imagem B",
                          compound= "center",
                          command = recorte)
    
  button_explore_img_a.grid(column = 0, row = 1) 
  
  button_explore_img_b.grid(column = 0, row = 2) 
    
  button_recorte_img_b.grid(column = 0,row = 3) 
    
  window.mainloop()
'''

