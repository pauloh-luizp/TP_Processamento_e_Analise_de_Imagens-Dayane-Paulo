from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import math
import sys
import cv2
import os


#if __name__ == '__main__':

os.remove("result.txt")
with open('result.txt', 'w') as arquivo:

  x0=147
  y0=169

  for x in range(36):
    x_a = x0 + x
    for y in range(54):
      y_a = y0 + y
      print("mapa_a["+ str(x_a)+ "," + str(y_a) 
            + "] mapa_b[" + str(x) + "," + str(y) + "]", file=arquivo)
