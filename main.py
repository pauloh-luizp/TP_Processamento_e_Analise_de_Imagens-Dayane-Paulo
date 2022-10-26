#Componentes do grupo:
# Dayane Gabriela Santos Cordeiro - 673915 - Engenharia de computação - PUC Minas Coração Eucarístico
# Paulo Henrique Luiz Pereira - 673667 - Engenharia de computação - PUC Minas Coração Eucarístico

import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt
from tkinter import *
import aumento_de_dados
import selecionando_imagem
import recorte_imagem
import correlacao_cruzada as cc

caminho_img_a = ""
caminho_img_b = ""
caminho_completo_img_b = ""

def sel_img_a():
  global caminho_img_a
  #Abrindo o explorador de arquivos e selecionando a imagem A
  caminho_img_a = selecionando_imagem.selecionando_imagens("A")

def sel_img_b():
  global caminho_completo_img_b
  #Abrindo o explorador de arquivos e selecionando a imagem B
  caminho_completo_img_b = selecionando_imagem.selecionando_imagens("B")

def recorte():
  global caminho_img_b
  #chama a função de recortar a imagem
  caminho_img_b = recorte_imagem.recortar_img(caminho_completo_img_b)

def corr_cruz_ab():
  cc.calc_corr_cruz_ab(caminho_img_a, caminho_img_b)

def espelhamento():
  img_a_horz = aumento_de_dados.espelhamento_horz(caminho_img_a)
  img_b_horz = aumento_de_dados.espelhamento_horz(caminho_completo_img_b)
  img_a = cv2.imread(img_a_horz,0)
  img_b = cv2.imread(img_b_horz,0)
  cv2.imshow('Img A espelhada H', img_a)
  cv2.imshow('Img b espelhada H', img_b)

def interface():                                                                                               
  window = Tk()
    
  window.title('Diagnóstico de Osteoartrite Femorotibial através de imagens de raio X') 
    
  window.geometry("200x300") 
    
  window.config(background = "white") 
        
  button_explore_img_a = Button(window,  
                                text = "Selecionar a imagem A", 
                                command = sel_img_a)

  button_explore_img_b = Button(window,
                                text = "Selecionar a imagem B", 
                                command = sel_img_b)  
    
  button_recorte_img_b = Button(window,
                                text = "Recortar a imagem B", 
                                command = recorte)

  button_corr_a_b = Button(window,
                           text = "Corr Cruz A e B",
                           command = corr_cruz_ab)

  button_esp_horz = Button(window, 
                           text = "Espelhamento A e B",
                           command = espelhamento)
    
  button_explore_img_a.grid(column = 0, row = 1) 
  button_explore_img_b.grid(column = 0, row = 2) 
  button_recorte_img_b.grid(column = 0, row = 3)
  button_esp_horz.grid(column= 0, row = 4)
  button_corr_a_b.grid(column= 0, row = 5)
    
  window.mainloop()


if __name__ == '__main__':
  interface()