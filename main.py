#Componentes do grupo:
# Dayane Gabriela Santos Cordeiro - XXXXXX - Engenharia de computação - PUC Minas Coração Eucarístico
# Paulo Henrique Luiz Pereira - 673667 - Engenharia de computação - PUC Minas Coração Eucarístico

import sys
import selecionando_imagem
import recorte_imagem
import correlacao_cruzada

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
'''
    #mapa, largura, altura, média e desvio padrão da imagem A
    caminho_da_imagem_a = caminho_completo_img_sel
    mapa_a = correlacao_cruzada.mapa_dos_pixels(caminho_da_imagem_a)
    largura_a, altura_a = correlacao_cruzada.obtendo_dimensoes(caminho_da_imagem_a)
    media_a = correlacao_cruzada.intensidade_media(largura_a, altura_a, mapa_a)
    dp_a = correlacao_cruzada.desvio_padrao(largura_a, altura_a, media_a, mapa_a)

    #mapa, largura, altura, média e desvio padrão da imagem B (Região buscada "_recorte")
    caminho_da_imagem_b = caminho_compelto_img_recortada
    mapa_b = correlacao_cruzada.mapa_dos_pixels(caminho_da_imagem_b)  
    largura_b, altura_b = correlacao_cruzada.obtendo_dimensoes(caminho_da_imagem_b)
    media_b = correlacao_cruzada.intensidade_media(largura_b, altura_b, mapa_b)
    dp_b = correlacao_cruzada.desvio_padrao(largura_b, altura_b, media_a, mapa_b)

    #CCN máximo, x0 e y0 da imagem A onde ocorre o valor máximo de CCN
    #sys.float_info.min
    ccn_max = sys.float_info.min
    x0_ccn_max = 0
    y0_ccn_max = 0

    #Iteração para obter x0 e y0 da imagem A onde ocorre o valor máxmo de CCN
    for x0_a in range(largura_b):
        for y0_a in range(altura_b):
            if((x0_a + largura_b <= largura_a) and (y0_a + altura_b <= altura_a)):
                ccn = correlacao_cruzada.normalized_cross_corr(mapa_a, mapa_b, media_a, media_b, dp_a, dp_b,
                                                                largura_b, altura_b, x0_a, y0_a)
                if(ccn >= ccn_max):
                    ccn_max = ccn
                    x0_ccn_max = x0_a
                    y0_ccn_max = y0_a


    print("CCN: " + str(ccn_max))
    print("x0_ccn_max: " + str(x0_ccn_max))
    print("y0_ccn_max: " + str(y0_ccn_max))

    correlacao_cruzada.posicao_detectada(x0_ccn_max, y0_ccn_max, largura_b, altura_b, caminho_da_imagem_a)
'''