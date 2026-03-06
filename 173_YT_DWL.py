import streamlit as st
from yt_dlp import YoutubeDL
import os

st.title("YouTube Video Downloader")
st.markdown("Insira o link do vídeo do YouTube, escolha a pasta de destino e clique no botão para fazer o download.")
url = st.text_input("Insira o link do vídeo do YouTube:")

diretorio='~/downloads'


if st.button("Download"):
            # Opções para o yt-dlp
            ydl_opts = {
                'format': 'best',
                'outtmpl': os.path.join(diretorio, '%(title)s.%(ext)s'),
            }
            # Realizar o download
            with YoutubeDL(ydl_opts) as ydl:
                st.info("Iniciando o download...")
                ydl.download([url])
                st.success(f"Download concluído! O vídeo foi salvo em: {diretorio}")

