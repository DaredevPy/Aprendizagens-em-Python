import streamlit as st
import qrcode
from PIL import Image # Lib de manipulação de imagens
import io # lib para manipulação de bytes
st.title('Gerador de QR Code')
url = st.text_input("Cole sua Url aqui", placeholder= 'https://www.exemplo.com',)
if url:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L, # Tratamento de erros
        box_size=10,
        border=4,
    )
    qr.add_data(url)  # Adiciona a URL ao QR Code
    qr.make(fit=True) # Ajusta o tamanho do QR Code
    img = qr.make_image(fill_color="black", back_color="white") # Definindo as cores do QR Code
    pil_img = img.get_image() # Convertendo para imagem PIL
    st.image(pil_img, caption='QR Code gerado', use_container_width=True) # Exibindo o QR Code na tela
    # Armazenando a imagem na memória para download
    buf = io.BytesIO()              # Criando um buffer de bytes
    pil_img.save(buf, format='PNG') # Salvando a imagem no buffer com o formato PNG
    byte_im = buf.getvalue()        # Obtendo os bytes da imagem
    # Definindo o botão de download
    st.download_button(
        label = 'Baixar QR Code', # Label do botão
        data = byte_im,           # Dados da imagem em bytes
        file_name = 'qrcode.png', # Nome do arquivo para download
        mime = 'image/png',       # Tipo MIME da imagem
        )