from PIL import Image
import cv2
import numpy as np
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

def histograma_equal(caminho_img):
  
  img = cv2.imread(caminho_img,0)
  img_h_equ = cv2.equalizeHist(img)
  img_final = np.hstack((img, img_h_equ))
  
  return img_final 
