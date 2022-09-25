from PIL import Image

def obtendo_dimensoes(caminho_da_imagem):
  #Importando a imagem
  imagem_completa = Image.open(caminho_da_imagem)

  #Obtendo o mapa de pixels
  mapa_de_pixels = imagem_completa.load()

  #Obtendo a largura e altura da imagem
  largura, altura = imagem_completa.size

  return(largura, altura)

  for i in range(largura):
    for j in range(altura):
      print(mapa_de_pixels[i,j])

if __name__ == '__main__':
  caminho_da_imagem = "/mnt/da/eng_computacao/processamento_de_imagens/TP/TP_PAI-Dayane-Paulo/image/9003175R_recorte.png"
  obtendo_dimensoes(caminho_da_imagem)

