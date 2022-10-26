from PIL import Image

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
