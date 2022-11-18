from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from tkinter import *
import cv2 
import os
import re
from skimage.feature import graycomatrix, graycoprops
import pandas as pd 

d = 'teste'
diretorio_base = "../test"+ d

print(diretorio_base)


'''
# import necessary packages

from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import  train_test_split
from sklearn.metrics import classification_report
import os
import glob
import cv2
import numpy as np

def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles

imagePaths = getListOfFiles("../img_classf_raso") ## Folder structure: datasets --> sub-folders with labels name
#print(imagePaths)

data = []
lables = []
c = 0 ## to see the progress
for image in imagePaths:

    lable = os.path.split(os.path.split(image)[0])[1]
    lables.append(lable)

    img = cv2.imread(image)
    img = cv2.resize(img, (32, 32), interpolation = cv2.INTER_AREA)
    data.append(img)
    #c=c+1
    #print(c)

#print(lables)

# encode the labels as integer
data = np.array(data)
lables = np.array(lables)

le = LabelEncoder()
lables = le.fit_transform(lables)

myset = set(lables)
print(myset)

dataset_size = data.shape[0]
data = data.reshape(dataset_size,-1)

f = open('saidas.txt','w')

print(data[0], file=f)
print(lables, file=f)

print(data.shape)
print(lables.shape)
print(dataset_size)

(trainX, testX, trainY, testY ) = train_test_split(data, lables, test_size= 0.25, random_state=42)

model = KNeighborsClassifier(n_neighbors=3, n_jobs=-1)
model.fit(trainX, trainY)

print(classification_report(testY, model.predict(testX), target_names=le.classes_))
'''

'''
from pathlib import Path
diretorio = "../KneeXrayData/ClsKLData/kneeKL224/auto_test/0/"
#diretorio = "/image"
for child in Path(diretorio).iterdir():
  if child.is_file():
      print(child)

caminho_img = '../KneeXrayData/ClsKLData/kneeKL224/auto_test/0/9656070_2.png'

nome_img = caminho_img[caminho_img.rfind('/') + 1 : caminho_img.rfind('.')]
print(nome_img)
formato_img = caminho_img[caminho_img.rfind('.') : len(caminho_img)]
print(formato_img)
img = nome_img + '_esp_horz' + formato_img
print(caminho_img)
'''

'''
#https://github.com/alfianhid/Feature-Extraction-Gray-Level-Co-occurrence-Matrix-GLCM-with-Python/blob/master/Feature_Extraction_Gray_Level_Co_occurrence_Matrix_(GLCM)_with_Python.ipynb
def normalize_label(str_):
    str_ = str_.replace(" ", "")
    str_ = str_.translate(str_.maketrans("","", "()"))
    str_ = str_.split("_")
    return ''.join(str_[:2])

def normalize_desc(folder, sub_folder):
    text = folder + " - " + sub_folder 
    text = re.sub(r'\d+', '', text)
    text = text.replace(".", "")
    text = text.strip()
    return text

def print_progress(val, val_len, folder, sub_folder, filename, bar_size=10):
    progr = "#"*round((val)*bar_size/val_len) + " "*round((val_len - (val))*bar_size/val_len)
    if val == 0:
        print("", end = "\n")
    else:
        print("[%s] folder : %s/%s/ ----> file : %s" % (progr, folder, sub_folder, filename), end="\r")

# ----------------- calculate greycomatrix() & greycoprops() for angle 0, 45, 90, 135 ----------------------------------
def calc_glcm_all_agls(img, label, props, dists=[5], agls=[0, np.pi/4, np.pi/2, 3*np.pi/4], lvl=256, sym=True, norm=True):
    
    glcm = graycomatrix(img, 
                        distances=dists, 
                        angles=agls, 
                        levels=lvl,
                        symmetric=sym, 
                        normed=norm)
    feature = []
    glcm_props = [propery for name in props for propery in graycoprops(glcm, name)[0]]
    for item in glcm_props:
            #print("item" + str(item))
            feature.append(item)

    #print("label" + label)
    feature.append(label) 
    
    print(feature)

    return feature
def carrega_diretorios():
  dataset_dir = "../testes1/" 

  imgs = [] #list image matrix 
  labels = []
  descs = []
  for folder in os.listdir(dataset_dir):
      for sub_folder in os.listdir(os.path.join(dataset_dir, folder)):
          sub_folder_files = os.listdir(os.path.join(dataset_dir, folder, sub_folder))
          len_sub_folder = len(sub_folder_files) - 1
          for i, filename in enumerate(sub_folder_files):
              print(filename)
              img = cv2.imread(os.path.join(dataset_dir, folder, sub_folder, filename))
              
              gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
              
              h, w = gray.shape
              ymin, ymax, xmin, xmax = h//3, h*2//3, w//3, w*2//3
              crop = gray[ymin:ymax, xmin:xmax]
              
              resize = cv2.resize(crop, (0,0), fx=0.5, fy=0.5)
              
              imgs.append(resize)
              labels.append(normalize_label(os.path.splitext(filename)[0]))
              descs.append(normalize_desc(folder, sub_folder))
              
              print_progress(i, len_sub_folder, folder, sub_folder, filename)

  # ----------------- call calc_glcm_all_agls() for all properties ----------------------------------
  properties = ['dissimilarity', 'correlation', 'homogeneity', 'contrast', 'ASM', 'energy']

  print(imgs)
  print(labels)

  glcm_all_agls = []
  for img, label in zip(imgs, labels): 
      #print(img)
      #print("label " + label)
      glcm_all_agls.append(
              calc_glcm_all_agls(img, 
                                  label, 
                                  props=properties)
                              )
  
  columns = []
  angles = ['0', '45', '90','135']
  for name in properties :
      for ang in angles:
          columns.append(name + "_" + ang)

  columns.append("label")

  return glcm_all_agls, columns
          
  
def panda(glcm_all_agls, columns):
  glcm_df = pd.DataFrame(glcm_all_agls, 
                        columns = columns)

  glcm_df.head(5)


if __name__=='__main__':
  glcm_all_agls, columns = carrega_diretorios()
  panda(glcm_all_agls, columns)
'''

'''
https://sourceexample.com/article/en/cad76b26f0627fb94e787be4439f1e05/
# Define the maximum number of gray levels
gray_level = 64

def maxGrayLevel(img, altura, largura):
  
  max_gray_level=0
  print("The height and width of the image are: height,width", altura, largura)
  for y in range(altura):
    for x in range(largura):
      if img[y][x] > max_gray_level:
        max_gray_level = img[y][x]
        print("max_gray_level:",max_gray_level)
  
  return max_gray_level+1

def getGlcm(input, d_x, d_y, altura, largura):
  
  srcdata = input.copy()
  
  ret=[[0.0 for i in range(gray_level)] 
        for j in range(gray_level)]
  
  max_gray_level = maxGrayLevel(input, altura, largura)
  # If the number of gray levels is greater than gray_level, the gray level of the image is reduced to gray_level, reduce the size of the gray-level co-occurrence matrix
  if max_gray_level > gray_level:
    for j in range(altura):
      for i in range(largura):
        srcdata[j][i]= srcdata[j][i]*gray_level / max_gray_level

  for j in range(altura-d_y):
    for i in range(largura-d_x):
      rows = srcdata[j][i]
      cols = srcdata[j + d_y][i+d_x]
      ret[rows][cols]+=1.0
      for i in range(gray_level):
        for j in range(gray_level):
          ret[i][j]/=float(altura*largura)
  
  return ret

def feature_computer(p):
  # con:Contrast reflects the sharpness of the image and the depth of the grooves of the texture. The sharper the texture, the greater the contrast, the greater the contrast.
  # eng:Entropy,ENT) measures the randomness of the amount of information contained in the image and expresses the complexity of the image. When all the values in the co-occurrence matrix are equal or the pixel values show the greatest randomness, the entropy is the largest.
  # agm:Angle second-order moment (energy), a measure of the uniformity of image gray distribution and texture thickness. When the image texture is uniform and regular, the energy value is large; on the contrary, the element values of the gray-level co-occurrence matrix are similar, and the energy value is small.
  # idm:The inverse difference matrix is also called the inverse variance, which reflects the clarity and regularity of the texture. The texture is clear, regular, easy to describe, and has a larger value.
  Con=0.0
  Eng=0.0
  Asm=0.0
  Idm=0.0
  for i in range(gray_level):
    for j in range(gray_level):
      Con+=(i-j)*(i-j)*p[i][j]
      Asm+=p[i][j]*p[i][j]
      Idm+=p[i][j]/(1+(i-j)*(i-j))
      if p[i][j]>0.0:
        Eng+=p[i][j]*math.log(p[i][j])
  
  return Asm,Con,-Eng,Idm

def test(image_name):
  img = cv2.imread(image_name) 
  try:
    img_shape=img.shape
  except:
    print('imread error')
    return

  altura = img.shape[0]
  largura = img.shape[1]
  
  # If you use &#39;/&#39;Will report TypeError: integer argument expected, got float
  # In fact, the main error is because of cv2.The parameter in resize is required to be an integer
  img=cv2.resize(img,(img_shape[1]//2,img_shape[0]//2),interpolation=cv2.INTER_CUBIC)

  img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  glcm_0 = getGlcm(img_gray,1,0, altura, largura)
  # glcm_1=getGlcm(src_gray,0,1)
  # glcm_2=getGlcm(src_gray,1,1)
  # glcm_3=getGlcm(src_gray,-1,1)print(glcm_0)

  asm,con,eng,idm = feature_computer(glcm_0)
  
  return[asm,con,eng,idm]

if __name__=='__main__':
   
  result = test("image/image_sample.jpg")
  print(result)
'''