#Imports necessários para a Interface Gráfica - Tkinter
import easygui

def selecionando_imagens():
  caminho = easygui.fileopenbox(default="../TP_PAI-Dayane-Paulo/image/")
  return caminho
  