from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import math
import sys
import cv2
import os

def mapa_dos_pixels(caminho_da_imagem):

  #Obtendo o mapa de pixels
  mapa_de_pixels = cv2.imread(caminho_da_imagem,0)

  return mapa_de_pixels

def obtendo_dimensoes(caminho_da_imagem):
  #Importando a imagem
  imagem_completa = cv2.imread(caminho_da_imagem,0)

  #Obtendo a largura e altura da imagem
  altura = imagem_completa.shape[0]
  largura = imagem_completa.shape[1]

  return(altura, largura)

def intensidade_media(altura, largura, mapa):

  n = largura*altura
  somatorio = 0
  media = 0

  for i in range(0, altura):
    for j in range(0, largura):
      somatorio = somatorio + mapa[i,j]

  media = somatorio/n

  return(media)

def desvio_padrao(mapa):

  dp = np.std(mapa)

  return(dp)

def corr_cruz(x0, y0, dp_a, dp_b, mapa_a, mapa_b,
              altura_b, largura_b):

  somatorio = 0
  ccn = 0

  for x in range(altura_b):
    x_a = x0 + x
    for y in range(largura_b):
      y_a = y0 + y
      somatorio = somatorio + ((mapa_a[x_a,y_a] - media_a)*(mapa_b[x,y] - media_b))

  ccn = somatorio / (dp_a * dp_b)

  return(ccn)

'''
def corr_cruz(x0, y0, dp_a, dp_b, mapa_a, somatorio_b,
              altura_b, largura_b):

  somatorio_a = 0
  ccn = 0

  for x in range(x0, x0 + altura_b):
    for y in range(y0, y0 + largura_b):
      somatorio_a = somatorio_a + ((mapa_a[x,y] - media_a))

  ccn = ((somatorio_a * somatorio_b) / (dp_a * dp_b))

  return(ccn)
'''

def somatoriob__mb(altura_b, largura_b, mapa_b, media_b):
  somatorio = 0
  
  for i in range(0, altura_b):
    for j in range(0, largura_b):
      somatorio = somatorio + (mapa_b[i,j] - media_b)

  return(somatorio)

def posicao_detectada(x0_a, y0_a, altura_b, largura_b, caminho_da_imagem_a):
  x = np.array(Image.open(caminho_da_imagem_a), dtype=np.uint8) 
  plt.imshow(x)
  fig, ax = plt.subplots(1)
  ax.imshow(x)
  rect = patches.Rectangle((x0_a, y0_a - altura_b), altura_b, largura_b,
                            linewidth=1, edgecolor='r', facecolor="none")
  ax.add_patch(rect)
  plt.show()


if __name__ == "__main__":
  
  os.remove("result.txt")
  
  with open('result.txt', 'w') as arquivo:

    #mapa, altura, largura, média e desvio padrão da imagem A
    #caminho_da_imagem_a = "/mnt/da/eng_computacao/processamento_de_imagens/TP/TP_PAI-Dayane-Paulo/image/9018291R.png"
    caminho_da_imagem_a = "/home/mostarda/Documentos/Eng_computacao/proc_imagens/TP_PAI-Dayane-Paulo/image/9018291R.png"
    mapa_a = mapa_dos_pixels(caminho_da_imagem_a)
    altura_a, largura_a = obtendo_dimensoes(caminho_da_imagem_a)
    media_a = intensidade_media(altura_a, largura_a, mapa_a)
    dp_a = desvio_padrao(mapa_a)
    
    #mapa, altura, largura, média e desvio padrão da imagem B (Região buscada "_recorte")
    #caminho_da_imagem_b = "/mnt/da/eng_computacao/processamento_de_imagens/TP/TP_PAI-Dayane-Paulo/image/9018291R_recorte.png"
    caminho_da_imagem_b = "/home/mostarda/Documentos/Eng_computacao/proc_imagens/TP_PAI-Dayane-Paulo/image/9018291R_recorte.png"
    mapa_b = mapa_dos_pixels(caminho_da_imagem_b)
    altura_b, largura_b = obtendo_dimensoes(caminho_da_imagem_b)
    media_b = intensidade_media(altura_b, largura_b, mapa_b)
    dp_b = desvio_padrao(mapa_b)

    print("Largura_a: " + str(largura_a) + ", Altura_a: " + str(altura_a))
    print("Largura_b: " + str(largura_b) + ", Altura_b: " + str(altura_b))

    print("Mapa de A:", file=arquivo)
    for i in range(altura_a):
      for j in range(largura_a):
        print(mapa_a[i,j], file=arquivo)

    print("Mapa de B:", file=arquivo)
    for i in range(altura_b):
      for j in range(largura_b):
        print(mapa_b[i,j], file=arquivo)

    #Variáveis para armazenar o
    #CCN máximo, x0 e y0 da imagem A onde ocorre o valor máximo de CCN
    #sys.float_info.min
    ccn_max = sys.float_info.min
    x0_ccn_max = 0
    y0_ccn_max = 0

    #Calculando a diferença das dimensões da imagem A coparada com a B
    dif_alt = altura_a - altura_b
    dif_lar = largura_a - largura_b    

    #Calcula o somatorio de B para ser utilizado pela função de correlação cruzada
    somatorio_b = somatoriob__mb(altura_b, largura_b, mapa_b, media_b)

    #Gera uma lista de tuplas com as coordenadas possíveis de se encontrar 
    #a imagem B em A
    coordenadas_a = []

    for i in range(dif_alt+1):
      for j in range(dif_lar+1):
        coordenadas_a.append((i, j))
    
    #Iteração para obter x0 e y0 da imagem A onde ocorre o valor máxmo de CCN
    for xy in coordenadas_a:
      #print("x: " + str(xy[0]) + " , y: " + str(xy[1]), file=arquivo)
      ccn = corr_cruz(xy[0], xy[1], dp_a, dp_b, mapa_a, mapa_b,
                      altura_b, largura_b)
      #print("CCN: " + str(ccn), file=arquivo)
      if(ccn > ccn_max):
        ccn_max = ccn # valor máximo da correlação cruzada
        x0_ccn_max = xy[0] # X da coordenada da imagem A
        y0_ccn_max = xy[1] # Y da coordenada da imagem A

    print("\n")

    print("Altura_a: " + str(altura_a) + ", Largura_a: " + str(largura_a))
    print("Média_a: " + str(media_a))
    print("Desvio padrão_a: " + str(dp_a))

    sum_a = 0

    for i in range(altura_a):
      for j in range(largura_a):
        sum_a = sum_a + 1

    print("Tamanho_a: " + str(sum_a) + "\n")

    print("Altura_b: " + str(altura_b) + ", Largura_b: " + str(largura_b))
    print("Média_b: " + str(media_b))
    print("Desvio padrão_b: " + str(dp_b))

    sum_b = 0

    for i in range(0, largura_b):
      for i in range(0, altura_b):
        sum_b = sum_b + 1

    print("Tamanho_b: " + str(sum_b) + "\n")

    print("CCN: " + str(ccn_max))
    print("x0_ccn_max: " + str(x0_ccn_max))
    print("y0_ccn_max: " + str(y0_ccn_max))

    print("\n")

    posicao_detectada(x0_ccn_max, y0_ccn_max, altura_b, largura_b, caminho_da_imagem_a)
    