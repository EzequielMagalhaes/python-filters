from PIL import Image, ImageFilter, ImageEnhance

## FILTRO DE BLUR ##
def aplicar_filtro_blur(caminho_imagem, caminho_saida):
    # Abre a imagem
    imagem = Image.open("kny_image.png")
    imagem.show()

    # Aplica o filtro de suavização (blur)
    imagem_suavizada = imagem.filter(ImageFilter.BLUR)

    # Salva a imagem suavizada
    imagem_suavizada.save("imagem_blur.png")

    print("Filtro de suavização aplicado com sucesso!")
    imagem_suavizada.show()

# Caminhos dos arquivos de entrada e saída
caminho_imagem_entrada = "kny_image.png"
caminho_imagem_saida = "imagem_blur.png"

# Chama a função para aplicar o filtro de suavização
aplicar_filtro_blur(caminho_imagem_entrada, caminho_imagem_saida)
#=============================================================================================================

## FILTRO DE REALCE ##
def aplicar_filtro_realce(caminho_imagem, caminho_saida):
    # Abre a imagem
    imagem = Image.open("kny_image.png")

    # Aplica o filtro de realce (sharpen)
    imagem_realcada = imagem.filter(ImageFilter.SHARPEN)

    # Salva a imagem realçada
    imagem_realcada.save("imagem_realce.jpg")

    print("Filtro de realce aplicado com sucesso!")
    imagem_realcada.show()

# Caminhos dos arquivos de entrada e saída
caminho_imagem_entrada = "kny_image.png"
caminho_imagem_saida = "imagem_realce.jpg"

# Chama a função para aplicar o filtro de realce
aplicar_filtro_realce(caminho_imagem_entrada, caminho_imagem_saida)
#=============================================================================================================

## FILTRO DE DETECÇÃO DE BORDAS ##
def aplicar_filtro_detecao_bordas(caminho_imagem, caminho_saida):
    # Abre a imagem
    imagem = Image.open("kny_image.png")

    # Aplica o filtro de detecção de bordas
    imagem_bordas = imagem.filter(ImageFilter.FIND_EDGES)

    # Salva a imagem com as bordas detectadas
    imagem_bordas.save("imagem_bordas.jpg")

    print("Filtro de detecção de bordas aplicado com sucesso!")
    imagem_bordas.show()

# Caminhos dos arquivos de entrada e saída
caminho_imagem_entrada = "kny_image.png"
caminho_imagem_saida = "imagem_bordas.jpg"

# Chama a função para aplicar o filtro de detecção de bordas
aplicar_filtro_detecao_bordas(caminho_imagem_entrada, caminho_imagem_saida)
#=============================================================================================================

## FILTRO ENCHANCE ##
def aplicar_filtro_realce_cor(caminho_imagem, caminho_saida, fator_contraste=1.2, fator_saturacao=1.2):
    # Abre a imagem
    imagem = Image.open("kny_image.png")

    # Aplica o realce de cor
    aprimoramento = ImageEnhance.Contrast(imagem)
    imagem_aprimorada = aprimoramento.enhance(fator_contraste)

    aprimoramento = ImageEnhance.Color(imagem_aprimorada)
    imagem_final = aprimoramento.enhance(fator_saturacao)

    # Salva a imagem com o realce de cor
    imagem_final.save("imagem_enchanced.jpg")

    print("Filtro de realce de cor aplicado com sucesso!")
    imagem_final.show()

# Caminhos dos arquivos de entrada e saída
caminho_imagem_entrada = "kny_image.png"
caminho_imagem_saida = "imagem_enchanced.jpg"

# Chama a função para aplicar o filtro de realce de cor
aplicar_filtro_realce_cor(caminho_imagem_entrada, caminho_imagem_saida)