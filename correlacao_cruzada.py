from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import math
import sys
import os

def mapa_dos_pixels(caminho_da_imagem):
  #Importando a imagem
  imagem_completa = Image.open(caminho_da_imagem)

  #Obtendo o mapa de pixels
  mapa_de_pixels = imagem_completa.load()

  return mapa_de_pixels

def obtendo_dimensoes(caminho_da_imagem):
  #Importando a imagem
  imagem_completa = Image.open(caminho_da_imagem)

  #Obtendo a largura e altura da imagem
  largura, altura = imagem_completa.size

  return(largura, altura)

def intensidade_media(largura, altura, mapa):

  n = largura*altura
  somatorio = 0
  media = 0

  for i in range(largura):
    for j in range(altura):
      somatorio = somatorio + mapa[i,j]

  media = somatorio/n

  return(media)

def desvio_padrao(largura, altura, media_a, mapa):

  somatorio = 0
  dp = 0

  for i in range(largura):
    for j in range(altura):
      somatorio = math.pow((mapa[i,j] - media_a), 2)

  dp = math.sqrt(somatorio)

  return(dp)

def normalized_cross_corr(mapa_a, media_a, somatorio_b, dp_a, dp_b,
                          largura_b, altura_b, x0_a, y0_a):

  somatorio_a = 0
  ccn = 0

  for x_a in range(x0_a + largura_b):
    for y_a in range(y0_a + altura_b):
      somatorio_a = somatorio_a + ((mapa_a[x_a,y_a] - media_a))
      #somatorio = (somatorio + ((mapa_a[x_a,y_a] - media_a)*(mapa_b[i,j] - media_b)))
      #print("x_a, y_a = (" + str(x_a) + "," + str(y_a) + ")", file=arquivo)
      #print("x_b, y_b = (" + str(i) + "," + str(j) + ")\n", file=arquivo)
      #somatorio = (somatorio + ((mapa_a[x_a,y_a])*(mapa_b[i,j])))

  ccn = ((somatorio_a * somatorio_b) / (dp_a * dp_b))

  return(ccn)

def somatoriob__mb(largura_b, altura_b, mapa_b, media_b):
  somatorio = 0
  
  for i in range(largura_b):
    for j in range(altura_b):
      somatorio = somatorio + (mapa_b[i,j] - media_b)

  return(somatorio)

def posicao_detectada(x0_a, y0_a, largura_b, altura_b, caminho_da_imagem_a):
  x = np.array(Image.open(caminho_da_imagem_a), dtype=np.uint8) 
  plt.imshow(x)
  fig, ax = plt.subplots(1)
  ax.imshow(x)
  rect = patches.Rectangle((x0_a, y0_a - altura_b), largura_b, altura_b,
                            linewidth=1, edgecolor='r', facecolor="none")
  ax.add_patch(rect)
  plt.show()


if __name__ == "__main__":
  
  #mapa, largura, altura, média e desvio padrão da imagem A
  caminho_da_imagem_a = "/mnt/da/eng_computacao/processamento_de_imagens/TP/TP_PAI-Dayane-Paulo/image/9018291R.png"
  mapa_a = mapa_dos_pixels(caminho_da_imagem_a)
  largura_a, altura_a = obtendo_dimensoes(caminho_da_imagem_a)
  media_a = intensidade_media(largura_a, altura_a, mapa_a)
  dp_a = desvio_padrao(largura_a, altura_a, media_a, mapa_a)
  
  #mapa, largura, altura, média e desvio padrão da imagem B (Região buscada "_recorte")
  caminho_da_imagem_b = "/mnt/da/eng_computacao/processamento_de_imagens/TP/TP_PAI-Dayane-Paulo/image/9018291R_recorte.png"
  mapa_b = mapa_dos_pixels(caminho_da_imagem_b) 
  largura_b, altura_b = obtendo_dimensoes(caminho_da_imagem_b)
  media_b = intensidade_media(largura_b, altura_b, mapa_b)
  dp_b = desvio_padrao(largura_b, altura_b, media_a, mapa_b)

  #CCN máximo, x0 e y0 da imagem A onde ocorre o valor máximo de CCN
  #sys.float_info.min
  ccn_max = sys.float_info.min
  x0_ccn_max = 0
  y0_ccn_max = 0

  #Calculando a diferença das dimensões da imagem A coparada com a B
  dif_lar = largura_a - largura_b
  dif_alt = altura_a - altura_b

  #Iteração para obter x0 e y0 da imagem A onde ocorre o valor máxmo de CCN

  somatorio_b = somatoriob__mb(largura_b, altura_b, mapa_b, media_b)

  for x0_a in range(dif_lar+1):
    for y0_a in range(dif_alt+1):
      #if((x0_a + dif_lar <= largura_a) and (y0_a + dif_alt <= altura_a)):
      ccn = normalized_cross_corr(mapa_a, media_a, somatorio_b, dp_a, dp_b,
                                  largura_b, altura_b, x0_a, y0_a)
      #print("\n\nx0_a, y0_a = (" + str(x0_a) + "," + str(y0_a) + ")" +
      #      "\nCCN: " + str(ccn))
      if(ccn > ccn_max):
        ccn_max = ccn
        x0_ccn_max = x0_a
        y0_ccn_max = y0_a
  
  print("\n")

  print("Largura_a: " + str(largura_a) + ", Altura_b: " + str(altura_a))
  print("Média_a: " + str(media_a))
  print("Desvio padrão_a: " + str(dp_a))

  sum_a = 0

  for i in range(largura_a):
    for j in range(altura_a):
      sum_a = sum_a + 1

  print("Tamanho_a: " + str(sum_a) + "\n")

  print("Largura_b: " + str(largura_b) + ", Altura_b: " + str(altura_b))
  print("Média_b: " + str(media_b))
  print("Desvio padrão_b: " + str(dp_b))

  sum_b = 0

  for i in range(largura_b):
    for j in range(altura_b):
      sum_b = sum_b + 1

  print("Tamanho_b: " + str(sum_b) + "\n")

  print("CCN: " + str(ccn_max))
  print("x0_ccn_max: " + str(x0_ccn_max))
  print("y0_ccn_max: " + str(y0_ccn_max))

  print("\n")

  posicao_detectada(x0_ccn_max, y0_ccn_max, largura_b, altura_b, caminho_da_imagem_a)