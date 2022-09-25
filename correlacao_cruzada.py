from PIL import Image
import math
import sys

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

def normalized_cross_corr(mapa_a, mapa_b, media_a, media_b, dp_a, dp_b,
                          largura_b, altura_b, x0_a, y0_a):

  somatorio = 0
  ccn = 0

  for i in range(largura_b):
    x_a = x0_a + i
    for j in range(altura_b):
      y_a = y0_a + j
      somatorio = somatorio + ((mapa_a[x_a,y_a] - media_a)*(mapa_b[i,j] - media_b))

  ccn = somatorio / (dp_a * dp_b)

  return(ccn)

if __name__ == '__main__':
  #mapa, largura, altura, média e desvio padrão da imagem A
  caminho_da_imagem_a = "/mnt/da/eng_computacao/processamento_de_imagens/TP/TP_PAI-Dayane-Paulo/image/9003175R.png"
  mapa_a = mapa_dos_pixels(caminho_da_imagem_a)
  largura_a, altura_a = obtendo_dimensoes(caminho_da_imagem_a)
  media_a = intensidade_media(largura_a, altura_a, mapa_a)
  dp_a = desvio_padrao(largura_a, altura_a, media_a, mapa_a)
  
  #mapa, largura, altura, média e desvio padrão da imagem B (Região buscada "_recorte")
  caminho_da_imagem_b = "/mnt/da/eng_computacao/processamento_de_imagens/TP/TP_PAI-Dayane-Paulo/image/9003175R_recorte.png"
  mapa_b = mapa_dos_pixels(caminho_da_imagem_b)  
  largura_b, altura_b = obtendo_dimensoes(caminho_da_imagem_b)
  media_b = intensidade_media(largura_b, altura_b, mapa_b)
  dp_b = desvio_padrao(largura_b, altura_b, media_a, mapa_b)

  #Calculando a diferença das dimensões da imagem A coparada com a B
  dif_lar = largura_a - largura_b
  dif_alt = altura_a - altura_b

  #CCN máximo, x0 e y0 da imagem A onde ocorre o valor máximo de CCN
  ccn_max = sys.float_info.min
  x0_ccn_max = 0
  y0_ccn_max = 0

  #Iteração para obter x0 e y0 da imagem A onde ocorre o valor máxmo de CCN
  for x0_a in range(largura_b):
    for y0_a in range(altura_b):
      if((x0_a + dif_lar <= largura_a) and (y0_a + dif_alt <= altura_a)):
        ccn = normalized_cross_corr(mapa_a, mapa_b, media_a, media_b, dp_a, dp_b,
                                    largura_b, altura_b, x0_a, y0_a)
        if(ccn >= ccn_max):
          ccn_max = ccn
          x0_ccn_max = x0_a
          y0_ccn_max = y0_a

  print("\n")

  print("Largura-" + str(dif_lar))
  print("Altura-" + str(dif_alt))

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