#Componentes do grupo:
# Dayane Gabriela Santos Cordeiro - XXXXXX - Engenharia de computação - PUC Minas Coração Eucarístico
# Paulo Henrique Luiz Pereira - 673667 - Engenharia de computação - PUC Minas Coração Eucarístico

import selecionando_imagem
import recorte_imagem

if __name__ == '__main__':
    #Abrindo o explorador de arquivos, selecionando a imagem e definindo o nome do novo arquivo
    caminho_completo_img_sel = selecionando_imagem.selecionando_imagens()
    caminho_img_sel = caminho_completo_img_sel[: len(caminho_completo_img_sel) - 4]
    formato_img_sel = caminho_completo_img_sel[len(caminho_completo_img_sel) - 4 : ]
    caminho_compelto_img_recortada = caminho_img_sel + '_recorte' + formato_img_sel

    #Configurando o recorte da imagem
    screen, px = recorte_imagem.setup(caminho_completo_img_sel)
    left, upper, right, lower = recorte_imagem.mainLoop(screen, px)

    #Garante que a imagem de saida tenha altura e largura positivas
    if right < left:
        left, right = right, left
    if lower < upper:
        lower, upper = upper, lower
    
    #Recortando a imagem
    im = recorte_imagem.Image.open(caminho_completo_img_sel)
    im = im.crop(( left, upper, right, lower))
    recorte_imagem.pygame.display.quit()

    #Salvando a imagem recortada
    im.save(caminho_compelto_img_recortada)
