#Componentes do grupo:
# Dayane Gabriela Santos Cordeiro - 673915 - Engenharia de computação - PUC Minas Coração Eucarístico
# Paulo Henrique Luiz Pereira - 673667 - Engenharia de computação - PUC Minas Coração Eucarístico

from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import math
import sys
import cv2

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

def desvio_padrao(largura, altura, media, mapa):

  somatorio = 0
  dp = 0

  for i in range(altura):
    for j in range(largura):
      somatorio = math.pow((mapa[i,j] - media), 2)

  dp = math.sqrt(somatorio)

  return(dp)

def valor_ccn(y0, x0, dp_a, dp_b, mapa_a, mapa_b,
              media_a, media_b, altura_b, largura_b):

  somatorio = 0
  ccn = 0

  for y in range(altura_b):
    for x in range(largura_b):
      somatorio += ((mapa_a[y0 + y,x0 + x] - media_a)*(mapa_b[y,x] - media_b))

  ccn = somatorio / (dp_a * dp_b)

  return(ccn)

def posicao_detectada(y0_a, x0_a, altura_b, largura_b, caminho_img_a, caminho_img_b):
  y = np.array(Image.open(caminho_img_b), dtype=np.uint8) 
  plt.imshow(y)
  x = np.array(Image.open(caminho_img_a), dtype=np.uint8)
  fig, ax = plt.subplots(1)
  ax.imshow(x)
  rect = patches.Rectangle((x0_a, y0_a), largura_b, altura_b,
                          linewidth=1, edgecolor='r', facecolor="none")
  ax.add_patch(rect)
  plt.show()

def calc_corr_cruz_ab(caminho_img_a, caminho_img_b):
  #mapa, altura, largura, média e desvio padrão da imagem A
  mapa_a = mapa_dos_pixels(caminho_img_a)
  altura_a, largura_a = obtendo_dimensoes(caminho_img_a)
  media_a = np.average(mapa_a)
  dp_a = np.std(mapa_a)
  
  #mapa, altura, largura, média e desvio padrão da imagem B (Região buscada "_recorte")
  mapa_b = mapa_dos_pixels(caminho_img_b)
  altura_b, largura_b = obtendo_dimensoes(caminho_img_b)
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
    ccn = valor_ccn(xy[0], xy[1], dp_a, dp_b, mapa_a, mapa_b,
                    media_a, media_b, altura_b, largura_b)
    if(ccn > ccn_max):
      ccn_max = ccn # valor máximo da correlação cruzada
      y0_ccn_max = xy[0] # Y da coordenada da imagem A
      x0_ccn_max = xy[1] # X da coordenada da imagem A

  print("CCN: " + str(ccn_max))
  print("x0_ccn_max: " + str(x0_ccn_max))
  print("y0_ccn_max: " + str(y0_ccn_max))
      
  posicao_detectada(y0_ccn_max, x0_ccn_max, altura_b, largura_b, caminho_img_a, caminho_img_b)