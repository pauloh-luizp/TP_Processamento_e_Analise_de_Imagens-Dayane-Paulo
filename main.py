#Componentes do grupo:
# Dayane Gabriela Santos Cordeiro - 673915 - Engenharia de computação - PUC Minas Coração Eucarístico
# Paulo Henrique Luiz Pereira - 673667 - Engenharia de computação - PUC Minas Coração Eucarístico

import sys
import numpy as np
from tkinter import *
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

def corr_cruz_ab():
    global caminho_img_a
    global caminho_img_b
    #mapa, altura, largura, média e desvio padrão da imagem A
    mapa_a = cc.mapa_dos_pixels(caminho_img_a)
    altura_a, largura_a = cc.obtendo_dimensoes(caminho_img_a)
    media_a = np.average(mapa_a)
    dp_a = np.std(mapa_a)
    
    #mapa, altura, largura, média e desvio padrão da imagem B (Região buscada "_recorte")
    mapa_b = cc.mapa_dos_pixels(caminho_img_b)
    altura_b, largura_b = cc.obtendo_dimensoes(caminho_img_b)
    media_b = np.average(mapa_b)
    dp_b = np.std(mapa_b)

    #Variáveis para armazenar o
    #CCN máximo, x0 e y0 da imagem A onde ocorre o valor máximo de CCN
    ccn_max = sys.float_info.min
    x0_ccn_max = 0
    y0_ccn_max = 0

    #Calculando a diferença das dimensões da imagem A coparada com a B
    dif_alt = altura_a - altura_b
    dif_lar = largura_a - largura_b    

    #Gera uma lista de tuplas com as coordenadas possíveis de se encontrar a
    #imagem B em A
    coordenadas_a = []

    for i in range(dif_alt+1):
      for j in range(dif_lar+1):
        coordenadas_a.append((i, j))
    
    #Iteração para obter x0 e y0 da imagem A onde ocorre o valor máxmo de CCN
    for xy in coordenadas_a:
      ccn = cc.corr_cruz(xy[0], xy[1], dp_a, dp_b, mapa_a, mapa_b,
                        media_a, media_b, altura_b, largura_b)
      if(ccn > ccn_max):
        ccn_max = ccn # valor máximo da correlação cruzada
        y0_ccn_max = xy[0] # Y da coordenada da imagem A
        x0_ccn_max = xy[1] # X da coordenada da imagem A

    print("CCN: " + str(ccn_max))
    print("x0_ccn_max: " + str(x0_ccn_max))
    print("y0_ccn_max: " + str(y0_ccn_max))
        
    cc.posicao_detectada(y0_ccn_max, x0_ccn_max, altura_b, largura_b, caminho_img_a, caminho_img_b)

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
                           text = "Corr_Cruz_AB",
                           command = corr_cruz_ab) 
    
  button_explore_img_a.grid(column = 0, row = 1) 
  button_explore_img_b.grid(column = 0, row = 2) 
  button_recorte_img_b.grid(column = 0, row = 3)
  button_corr_a_b.grid(column=0, row = 4)
    
  window.mainloop()


if __name__ == '__main__':
  interface()
