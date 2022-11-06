from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from tkinter import *

'''
from pathlib import Path
diretorio = "../KneeXrayData/ClsKLData/kneeKL224/auto_test/0/"
#diretorio = "/image"
for child in Path(diretorio).iterdir():
  if child.is_file():
      print(child)
'''

caminho_img = '../KneeXrayData/ClsKLData/kneeKL224/auto_test/0/9656070_2.png'

nome_img = caminho_img[caminho_img.rfind('/') + 1 : caminho_img.rfind('.')]
print(nome_img)
formato_img = caminho_img[caminho_img.rfind('.') : len(caminho_img)]
print(formato_img)
img = nome_img + '_esp_horz' + formato_img
print(caminho_img)
