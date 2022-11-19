from skimage.feature import graycomatrix, graycoprops
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
from pathlib import Path
import aumento_de_dados as ad
import pandas as pd 
import numpy as np
import cv2
import os


def pre_processamento(tipo_classf, tipo_dataset):
  
  if(tipo_classf == 2):
    classf = '_binaria'
  elif(tipo_classf == 5):
    classf = '_5_classes_KL'
  
  for i in range(0, tipo_classf):
    #configuramos o diretório base onde está as imagens das 5 classes
    diretorio_base = "../classf" + classf + '/' + tipo_dataset
    diretorio_class_raso = "../img_classf_raso" + classf + '/' + tipo_dataset
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


def gray_l_co_o_matix(tipo_classf, tipo_dataset, propriedades):
  #lista contendo os valores das propriedades que serão 
  #calculadas usando a matriz de co-ocorrencia de níveis de cinza
  prop_imgs = []

  if(tipo_classf == 2):
    classf = '_binaria'
  elif(tipo_classf == 5):
    classf = '_5_classes_KL'

  for i in range(0, tipo_classf):
    #configuramos o diretório base onde está as imagens das 5 classes
    diretorio_class_raso = "../img_classf_raso" + classf + '/' + tipo_dataset
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
        #prop_img.append(img.name)
        prop_img.append(i)
        #coloca todos os valores das propriedades das imagens 
        #em uma lista que conterá a propriedade de todas as imagens do dataset
        prop_imgs.append(prop_img)

  return prop_imgs


def exibir_propriedades(glcm, propriedades):
  colunas = []
  anglulos = ['0', '45', '90','135']
  for name in propriedades :
      for ang in anglulos:
          colunas.append(name + "_" + ang)
          
  #colunas.append("Nome_img")
  colunas.append("Classe")

  glcm_df = pd.DataFrame(glcm, columns = colunas)

  glcm_df.head(15)

  print(glcm_df)


#temos que remodelar os dados para se adequar ao classificador
def remodelando_dados(glcm):
  dados = []
  classes_dados = []

  dados = [item[:24] for item in glcm]

  for i in range (0, len(glcm)):
    classes_dados.append(glcm[i][24])

  dados = np.array(dados)
  classes_dados = np.array(classes_dados)
  dados_qtd = dados.shape[0]
  dados = dados.reshape(dados_qtd, -1)

  return (dados, classes_dados)

def classf_raso(tipo_classf):
  
  f = open('saidas.txt','w')
  
  train = []
  test = []
  val =[]
  classes_train = []
  classes_test = []
  classes_val = []
  
  propriedades = ['contrast', 'dissimilarity', 'homogeneity', 'energy', 'correlation', 'ASM']
  
  tipo_dataset = 'train'
  #pre_processamento(tipo_classf, tipo_dataset)
  glcm_train = gray_l_co_o_matix(tipo_classf, tipo_dataset, propriedades)
  train, classes_train = remodelando_dados(glcm_train)

  tipo_dataset = 'test'
  #pre_processamento(tipo_classf, tipo_dataset)
  glcm_test = gray_l_co_o_matix(tipo_classf, tipo_dataset, propriedades)
  test, classes_test = remodelando_dados(glcm_test)

  tipo_dataset = 'val'
  #pre_processamento(tipo_classf, tipo_dataset)
  glcm_val = gray_l_co_o_matix(tipo_classf, tipo_dataset, propriedades)
  val, classes_val = remodelando_dados(glcm_val)

  le = LabelEncoder()
  classes = le.fit_transform(classes_test)

  #print(classes_train, file=f)
  #print(train, file=f)

  knn_model = KNeighborsClassifier(n_neighbors=3, n_jobs=-1)
  knn_model.fit(train, classes_train)
  
  print('\n')
  print(classification_report(classes_test, knn_model.predict(test), zero_division=0))


if __name__=='__main__':
  tipo_classf = 5
  classf_raso(tipo_classf)
  