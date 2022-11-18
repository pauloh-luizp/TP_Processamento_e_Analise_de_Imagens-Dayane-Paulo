from skimage.feature import graycomatrix, graycoprops
from pathlib import Path
import aumento_de_dados as ad
import pandas as pd 
import numpy as np
import cv2
import os


def pre_processamento():
  for i in range(0, 5):
    #configuramos o diretório base onde está as imagens das 5 classes
    diretorio_base = "../test"
    diretorio_class_raso = "../img_classf_raso"
    #a cada iteração do for muda-se a classe das imagens para serem feitas o aumento de dados
    diretorio_atual = diretorio_base + '/' + str(i) + '/'
    #obtem o caminho completo do diretório atual
    diretorio = os.path.abspath(diretorio_atual)
    #confirgura o novo diretório que será salva as imagens com o histograma equaliazado para o classificador raso
    novo_diretorio = os.path.join(diretorio_class_raso, str(i) + '/')
    if not os.path.exists(novo_diretorio):
      os.makedirs(novo_diretorio)
    for img in Path(diretorio).iterdir():
      if img.is_file():
        caminho_completo = diretorio + '/' + img.name
        ad.histograma_equal(caminho_completo,novo_diretorio)


def gray_l_co_o_matix():
  #propriedades que serão calculadas usando a matriz de co-ocorrencia de níveis de cinza
  propriedades = ['contrast', 'dissimilarity', 'homogeneity', 'energy', 'correlation', 'ASM']
  prop_imgs = []

  for i in range(0, 5):
    #configuramos o diretório base onde está as imagens das 5 classes
    diretorio_class_raso = "../img_classf_raso"
    #a cada iteração do for muda-se a classe das imagens para o calculo da matriz de co-ocorrencia de níveis de cinza
    diretorio_atual = diretorio_class_raso + '/' + str(i) + '/'
    #obtem o caminho completo do diretório atual
    diretorio = os.path.abspath(diretorio_atual)

    #percorre cada imagem do diretório e faz o caluclo da matriz, e da matriz tira cada uma das propriedades
    for img in Path(diretorio).iterdir():
      if img.is_file():
        imagem = cv2.imread(diretorio + '/' + img.name,0)
        prop_img = []
        #calcula a matriz de co-ocorrencia de niveis de cinza
        glcm = graycomatrix(imagem, distances = [5], angles = [0, np.pi/4, np.pi/2, 3*np.pi/4], 
                            levels = 256, symmetric = True, normed = True)
        #calcula todas as propiedades utilizando a matriz de co-ocorrencia de niveis de cinza
        glcm_props = [prop for propriedade in propriedades 
                            for prop in graycoprops(glcm, propriedade)[0]]
        for item in glcm_props:
          #coloca todos os valores das propriedades em uma lista
          prop_img.append(item)
        prop_img.append(img.name)
        prop_img.append(i)
        #coloca todos os valores das propriedades das imagens 
        #em uma lista que conterá a propriedade de todas as imagens do dataset
        prop_imgs.append(prop_img)

  return prop_imgs


if __name__=='__main__':
  #pre_processamento()
  carat = gray_l_co_o_matix()
  #print(carat)
  #print("espaco")
  #for i in range (0,4):
    #print(carat[i])
  
  propriedades = ['contrast', 'dissimilarity', 'homogeneity', 'energy', 'correlation', 'ASM']
  
  colunas = []
  anglulos = ['0', '45', '90','135']
  for name in propriedades :
      for ang in anglulos:
          colunas.append(name + "_" + ang)
          
  colunas.append("Nome_img")
  colunas.append("Classe")

  glcm_df = pd.DataFrame(carat, 
                        columns = colunas)

  glcm_df.head(15)

  print(glcm_df)