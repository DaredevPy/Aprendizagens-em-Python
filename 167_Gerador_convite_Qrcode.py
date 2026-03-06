
# Importar bibliotecas necesarias
import qrcode
from reportlab.pdfgen import canvas         # Utilizando uma parte da biblioteca ReportLab para gerar PDFs
from reportlab.lib.pagesizes import letter  # Parte da lib que define o tamanho da página

# Dados do convite
link = "https://www.exemplo.com/convite"  # Link do convite

# Gerar QR Code para o convite
qr = qrcode.QRCode(
    version=1, # Tamanho do QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L, # Serve para definir o nível de correção de erros
    box_size=10,                                       # Tamanho de cada caixa do QR Code
    border=4,                                          # Tamanho da borda do QR Code
)
qr.add_data(link)  # Adiciona o link ao QR Code
qr.make(fit=True)  # Ajusta o QR Code para caber no tamanho definido
img_qr = qr.make_image(fill_color="black", back_color="white")  # Cria a imagem do QR Code

# Salvar o Qrcode como imagen
img_qr.save("qr_code_.png")  # Salva o QR Code como uma imagem PNG

# Criar o arquivo PDF
c = canvas.Canvas("convite.pdf", pagesize=letter)  # Cria um canvas para o PDF com tamanho carta
width, height = letter  # Obtém as dimensões da página
c.drawImage("tema.png",0,0,width=width, height=height) # Adiciona uma imagem de fundo ao PDF

# Adicionar o Qrcode no PDF
qr_code_size = 100  # Define o tamanho do QR Code no PDF
qr_x_position = (width - qr_code_size) / 2  # Centraliza o QR Code na página
qr_y_position = height - qr_code_size  / 2 -250 # Centraliza o QR Code na parte superior da página
c.drawImage("qr_code_.png", qr_x_position, qr_y_position, width=qr_code_size, height=qr_code_size)  # Adiciona o QR Code ao PDF

# Salvar o PDF
c.save()