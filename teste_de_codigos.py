from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from tkinter import *
import GUI

root = Tk()

caminho = "////999"

ci = GUI.Caminho_img()

ci.set_caminho_img_a(caminho)

caminho2 = ci.get_caminho_img_a()
print(caminho2)


root.mainloop()

