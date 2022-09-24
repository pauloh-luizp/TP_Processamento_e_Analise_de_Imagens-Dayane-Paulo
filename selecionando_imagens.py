
#Imports necessários para a Interface Gráfica - Tkinter
from tkinter import *
from tkinter import filedialog

'''
Abrindo os arquivos pelo explorador de arquivos
e selecionando a parte da imagem a ser utilizada
'''

def browseFiles(): 
    filename = filedialog.askopenfilename(initialdir = "../", 
                                          title = "Escolha uma imagem", 
                                          filetypes = (("Imagens png", 
                                                        "*.png*"), 
                                                       ("Imagens jpg", 
                                                        "*.jpg*"))) 


