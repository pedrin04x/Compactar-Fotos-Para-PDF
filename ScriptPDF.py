import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Check if ReportLab is installed
try:
    from reportlab import canvas
except ImportError:
    print('ReportLab module is not installed. Please install it and try again.')
    sys.exit()

def selecionar_diretorio():
    diretorio = input("Digite o caminho do diretório de imagens: ").strip()
    return diretorio

def compactar_fotos_para_pdf(diretorio_de_imagens, nome_arquivo_saida):
    imagens = [f for f in os.listdir(diretorio_de_imagens) if f.endswith(('.jpg', '.jpeg', '.png'))]

    if not imagens:
        print("Nenhuma imagem encontrada no diretório.")
        return

    # Obter o caminho completo para o arquivo de saída PDF no mesmo diretório das imagens
    pdf_path = os.path.join(diretorio_de_imagens, nome_arquivo_saida)

    # Tamanho da página PDF (usado como tamanho da imagem)
    tamanho_pagina = letter

    # Criar um arquivo PDF
    pdf = canvas.Canvas(pdf_path, pagesize=tamanho_pagina)

    for imagem_nome in imagens:
        imagem_path = os.path.join(diretorio_de_imagens, imagem_nome)

        # Adicionar a imagem à página PDF sem redimensionar
        pdf.drawImage(imagem_path, 0, 0, width=tamanho_pagina[0], height=tamanho_pagina[1])
        pdf.showPage()

    # Fechar o arquivo PDF
    pdf.save()

if __name__ == "__main__":
    diretorio_de_imagens = selecionar_diretorio()
    
    if not os.path.isdir(diretorio_de_imagens):
        print("Diretório inválido ou não encontrado.")
        exit()

    nome_arquivo_saida = "PFOT.pdf"

    compactar_fotos_para_pdf(diretorio_de_imagens, nome_arquivo_saida)

print("PDF criado com sucesso em:", os.path.join(diretorio_de_imagens, nome_arquivo_saida))
