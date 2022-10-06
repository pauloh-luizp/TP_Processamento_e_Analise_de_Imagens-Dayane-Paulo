from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os
import GUI

caminho = "////999"

ci = GUI.Caminho_img()

ci.set_caminho_img_a(caminho)

caminho2 = ci.get_caminho_img_a()
print(caminho2)


