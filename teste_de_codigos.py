import os

os.remove("result.txt")

def varrer(x0, y0, largura_b, altura_b):
  print("\nPara: (" + str(x0) + "," + str(y0) + ")", file=arquivo)
  for x in range(x0, x0 + largura_b):
    for y in range(y0, y0 + altura_b):
      print("x_a, y_a = (" + str(x) + "," + str(y) + ")", file=arquivo)

x0 = 2
y0 = 0
largura_a = 10
altura_a = 10
largura_b = 5
altura_b = 5

coordenadas_a = []

for i in range(largura_a-largura_b+1):
  for j in range(altura_a-altura_b+1):
    coordenadas_a.append((i, j))

with open('result.txt', 'a') as arquivo:
  #print(str(coordenadas_a) + "\n", file=arquivo)

  for xy in coordenadas_a:
    varrer(xy[0], xy[1], largura_b, altura_b)




def test(x0_a, y0_a, largura_b, altura_b):

  with open('result.txt', 'a') as arquivo:
    print("\nFor de fora: x_b, y_b = (" + str(x0_a) + "," + str(y0_a) + ")", file=arquivo)
    for x in range(x0_a, x0_a + largura_b):
      for y in range(y0_a, y0_a + altura_b):
        print("x_a, y_a = (" + str(x) + "," + str(y) + ")", file=arquivo)

if __name__ == '__main__':
  largura_a = 10
  altura_a = 10
  largura_b = 5
  altura_b = 5
  x = 0
  y = 0

  

  #os.remove("result.txt")

  #Calculando a diferença das dimensões da imagem A coparada com a B
  dif_lar = largura_a - largura_b
  dif_alt = altura_a - altura_b
  
  chamadas = 0


  for i in range(largura_b):
    x = x + 1
    test(1,1,largura_b, altura_b)
    '''
    for j in range(altura_b):
      y = y + 1
      #if((x0_a + largura_b <= largura_a) and (y0_a + altura_b <= altura_a)):
      chamadas = chamadas + 1
      test(i, j, largura_b, altura_b)
    '''

  print(x)
  print(y)
  print(chamadas)


'''
###CORRELACAO_CRUZADA

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
  #sys.float_info.min
  ccn_max = -1000000
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

  posicao_detectada(x0_ccn_max, y0_ccn_max, largura_b, altura_b, caminho_da_imagem_a)

'''