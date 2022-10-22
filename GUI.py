from tkinter import *
from tkinter import filedialog 
import selecionando_imagem
import recorte_imagem

class Caminho_img:
    def __init__(self, img_a = "", img_b = ""):
        self.img_a = img_a
        self.img_b = img_b
    
    def set_caminho_img_a(self, img_a):
        self.img_a = img_a

    def set_caminho_img_b(self, img_b):
        self.img_b = img_b

    def get_caminho_img_a(self):
        return self.img_a

    def get_caminho_img_b(self):
        return self.img_b
   
def sel_img_a(): 
  Caminho_img.set_caminho_img_b(selecionando_imagem.selecionando_imagens())

def sel_img_b(): 
  Caminho_img.set_caminho_img_b(selecionando_imagem.selecionando_imagens())

def recorte():
    #Configurando o recorte da imagem
    caminho_img_b = Caminho_img.get_caminho_img_b
    screen, px = recorte_imagem.setup(caminho_img_b)
    left, upper, right, lower = recorte_imagem.mainLoop(screen, px)

    #Garante que a imagem de saida tenha altura e largura positivas
    if right < left:
        left, right = right, left
    if lower < upper:
        lower, upper = upper, lower

    #Recortando a imagem
    im = recorte_imagem.Image.open(caminho_img_b)
    im = im.crop(( left, upper, right, lower))
    recorte_imagem.pygame.display.quit()

    #Salvando a imagem recortada
    im.save(caminho_img_b)

def interface():                                                                                               
  window = Tk() 
    
  window.title('Diagnóstico de Osteoartrite Femorotibial através de imagens de raio X') 
    
  window.geometry("200x200") 
    
  window.config(background = "white") 
        
  button_explore = Button(window,  
                          text = "selecionar a imagem A", 
                          command = sel_img_a)

  button_explore = Button(window,
                          text = "selecionar a imagem B", 
                          command = sel_img_b)  
    
  button_exit = Button(window,
                      text = "Recortar a imagem B", 
                      command = recorte)  
    
  button_explore.grid(column = 0, row = 2) 
    
  button_exit.grid(column = 0,row = 3) 
    
  window.mainloop() 