#Componentes do grupo:
# Dayane Gabriela Santos Cordeiro - 673915 - Engenharia de computação - PUC Minas Coração Eucarístico
# Paulo Henrique Luiz Pereira - 673667 - Engenharia de computação - PUC Minas Coração Eucarístico

#Imports necessários para a Interface Gráfica - Tkinter
import easygui

def selecionando_imagens(img):
  caminho = easygui.fileopenbox(title="Selecione a imagem " + str(img),
                                default="../TP_PAI-Dayane-Paulo/image/",
                                filetypes=["*.jpg","*.png"])
  return caminho