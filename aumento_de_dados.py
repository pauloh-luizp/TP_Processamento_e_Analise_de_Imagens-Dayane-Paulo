from pathlib import Path
import cv2
import os

def espelhamento_horz(caminho_img, novo_caminho):
  #Lendo a imagem e espelhando horizontalmente
  img = cv2.imread(caminho_img)
  horizontal_img = cv2.flip(img,1)
  
  #Configurando novo nome do arquivo da imagem espelhada horizontalmente
  nome_img = caminho_img[caminho_img.rfind('/') + 1 : caminho_img.rfind('.')]
  formato_img = caminho_img[caminho_img.rfind('.') : len(caminho_img)]
  caminho_img_horz = novo_caminho + nome_img + '_esp_horz' + formato_img

  #Salvando a imagem invertida horizontalmente
  cv2.imwrite(caminho_img_horz , horizontal_img)

def histograma_equal(caminho_img, novo_caminho):
  #Lendo a imagem e realizando a equalização do histograma 
  img = cv2.imread(caminho_img,0)
  img_h_equ = cv2.equalizeHist(img)

  #Configurando novo nome do arquivo da imagem com o histograma equalizado
  nome_img = caminho_img[caminho_img.rfind('/') + 1 : caminho_img.rfind('.')]
  formato_img = caminho_img[caminho_img.rfind('.') : len(caminho_img)]
  caminho_h_equ = novo_caminho + nome_img + '_h_equ' + formato_img

  #Salvando a imagem com o histograma equalizado
  cv2.imwrite(caminho_h_equ , img_h_equ)

def aumentoDados():
  for i in range(0, 5):
    #Configuramos o diretório base onde está as imagens das 5 classes
    diretorio_base = "../test"
    #A cada iteração do for muda-se a classe das imagens para serem feitas o aumento de dados
    diretorio_atual = diretorio_base + '/' + str(i) + '/'
    #obtem o caminho completo do diretório atual
    diretorio = os.path.abspath(diretorio_atual)
    
    #Para cada imagem na pasta será feito a equalizacao do histograma e o espelhamento horizontal
    for img in Path(diretorio).iterdir():
      if img.is_file():
        caminho_completo = diretorio + '/' + img.name
        espelhamento_horz(caminho_completo,diretorio_atual)
        histograma_equal(caminho_completo,diretorio_atual)