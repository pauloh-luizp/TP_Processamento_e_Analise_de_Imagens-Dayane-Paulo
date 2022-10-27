from PIL import Image
import correlacao_cruzada as cc

def espelhamento_horz(caminho_completo_img):
  img = Image.open(caminho_completo_img)
  horizontal_img = img.transpose(method=Image.FLIP_LEFT_RIGHT)

  #Configurando novo nome do arquivo da imagem espelhada horizontalmente
  if (caminho_completo_img[: len(caminho_completo_img) - 4] == "peg"):
    caminho_img_horz = caminho_completo_img[: len(caminho_completo_img) - 5]
    formato_img_horz = caminho_completo_img[len(caminho_completo_img) - 5 :]
    caminho_img_esp_horz = caminho_img_horz + '_esp_horz' + formato_img_horz
  else:
    caminho_img_horz = caminho_completo_img[: len(caminho_completo_img) - 4]
    formato_img_horz = caminho_completo_img[len(caminho_completo_img) - 4 :]
    caminho_img_esp_horz = caminho_img_horz + '_esp_horz' + formato_img_horz

  #Salvando a imagem invertida horizontalmente
  horizontal_img.save(caminho_img_esp_horz)

  return caminho_img_esp_horz

def histograma_prob(caminho_img):
  
  mapa = cc.mapa_dos_pixels(caminho_img)
  altura, largura = cc.obtendo_dimensoes(caminho_img)
  
  qtd_pixels = altura * largura
  intensidades = []
  histo_prob = []

  for i in range(0, 256):
    intensidades.append(0)
    histo_prob.append(0)

  for y in range(altura):
    for x in range(largura):
      intensidades[mapa[y,x]] += 1
      print(mapa[y,x])

  for i in range(0, 256):
    histo_prob[i] = intensidades[i]/qtd_pixels

  return histo_prob 

  #https://medium.com/data-hackers/equaliza%C3%A7%C3%A3o-de-histograma-em-python-378830368d60