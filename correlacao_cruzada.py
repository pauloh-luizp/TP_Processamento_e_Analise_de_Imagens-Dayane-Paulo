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

def desvio_padrao(largura, altura, media, mapa):

  somatorio = 0
  dp = 0

  for i in range(altura):
    for j in range(largura):
      somatorio = math.pow((mapa[i,j] - media), 2)

  dp = math.sqrt(somatorio)

  return(dp)

def corr_cruz(y0, x0, dp_a, dp_b, mapa_a, mapa_b,
              media_a, media_b, altura_b, largura_b):

  somatorio = 0
  ccn = 0

  for y in range(altura_b):
    for x in range(largura_b):
      somatorio = somatorio + ((mapa_a[y0 + y,x0 + x] - media_a)*(mapa_b[y,x] - media_b))

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