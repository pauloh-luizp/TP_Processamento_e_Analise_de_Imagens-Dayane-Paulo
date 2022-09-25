def test(i, j, largura, altura):
  for i in range(largura):
    for j in range(altura):
      print("i: " + str(i))
      print("j: " + str(j))
      print("\n")

if __name__ == '__main__':
  i = 5
  j = 5
  largura = 12
  altura = 8
  
  largura = largura + i
  altura = altura + j

  test(i, j, largura, altura)



'''
###CORRELACAO_CRUZADA

  #mapa, largura, altura, media e desvio padrão da imagem A
  caminho_da_imagem_a = "/mnt/da/eng_computacao/processamento_de_imagens/TP/TP_PAI-Dayane-Paulo/image/9003175R.png"
  mapa_a = mapa_dos_pixels(caminho_da_imagem_a)
  largura_a, altura_a = obtendo_dimensoes(caminho_da_imagem_a)
  media_a = intensidade_media(largura_a, altura_a, mapa_a)
  dp_a = desvio_padrao(largura_a, altura_a, media_a, mapa_a)
  
  #mapa, largura, altura, media e desvio padrão da imagem B (Região buscada "_recorte")
  caminho_da_imagem_b = "/mnt/da/eng_computacao/processamento_de_imagens/TP/TP_PAI-Dayane-Paulo/image/9003175R_recorte.png"
  mapa_b = mapa_dos_pixels(caminho_da_imagem_b)  
  largura_b, altura_b = obtendo_dimensoes(caminho_da_imagem_b)
  media_b = intensidade_media(largura_b, altura_b, mapa_b)
  dp_b = desvio_padrao(largura_b, altura_b, media_a, mapa_b)

  ccn = normalized_cross_corr(mapa_a, media_a, largura_a, altura_a, dp_a, 
                              mapa_b, media_b, largura_b, altura_b, dp_b)

  print("\n")

  print("Largura_a: " + str(largura_a) + ", Altura_b: " + str(altura_a))
  print("Média_a: " + str(media_a))
  print("Desvio padrão_a: " + str(dp_a))

  sum_a = 0

  for i in range(largura_a):
    for j in range(altura_a):
      sum_a = sum_a + 1

  print("Tamanho_b: " + str(sum_a) + "\n")

  print("Largura_b: " + str(largura_b) + ", Altura_b: " + str(altura_b))
  print("Média_b: " + str(media_b))
  print("Desvio padrão_b: " + str(dp_b))

  sum_b = 0

  for i in range(largura_b):
    for j in range(altura_b):
      sum_b = sum_b + 1

  print("Tamanho_b: " + str(sum_b) + "\n")

  print("CCN: " + str(ccn))

'''