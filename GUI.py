from tkinter import *
from tkinter import filedialog 
import selecionando_imagem
import recorte_imagem

caminho_completo_img_a = ""
caminho_completo_img_b = ""
   
def sel_img_a():
    global caminho_completo_img_a
    #Abrindo o explorador de arquivos e selecionando a imagem A
    caminho_completo_img_a = selecionando_imagem.selecionando_imagens("A")

def sel_img_b():
    global caminho_completo_img_b
    #Abrindo o explorador de arquivos e selecionando a imagem B
    caminho_completo_img_b = selecionando_imagem.selecionando_imagens("B")

def recorte():
    #Configurando o recorte da imagem e o novo nome do arquivo
    caminho_img_sel = caminho_completo_img_b[: len(caminho_completo_img_b) - 4]
    formato_img_sel = caminho_completo_img_b[len(caminho_completo_img_b) - 4 : ]
    caminho_img_b = caminho_img_sel + '_recorte' + formato_img_sel
    screen, px = recorte_imagem.setup(caminho_completo_img_b)
    left, upper, right, lower = recorte_imagem.mainLoop(screen, px)

    #Garante que a imagem de saida tenha altura e largura positivas
    if right < left:
        left, right = right, left
    if lower < upper:
        lower, upper = upper, lower

    #Recortando a imagem
    im = recorte_imagem.Image.open(caminho_completo_img_b)
    im = im.crop(( left, upper, right, lower))
    recorte_imagem.pygame.display.quit()

    #Salvando a imagem recortada
    im.save(caminho_img_b)

def interface():                                                                                               
  window = Tk() 
    
  window.title('Diagnóstico de Osteoartrite Femorotibial através de imagens de raio X') 
    
  window.geometry("200x200") 
    
  window.config(background = "white") 
        
  button_explore_img_a = Button(window,  
                            text = "Selecionar a imagem A", 
                            command = sel_img_a)

  button_explore_img_b = Button(window,
                            text = "Selecionar a imagem B", 
                            command = sel_img_b)  
    
  button_recorte_img_b = Button(window,
                            text = "Recortar a imagem B", 
                            command = recorte)  
    
  button_explore_img_a.grid(column = 0, row = 1) 
  
  button_explore_img_b.grid(column = 0, row = 2) 
    
  button_recorte_img_b.grid(column = 0,row = 3) 
    
  window.mainloop()


interface()