from gtts import gTTS
import os
import tempfile
import pygame

def speak_with_gtts(text):
    """Versão usando Google TTS (requer internet)"""
    if text:
        try:
            # Criar arquivo temporário
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp:
                temp_filename = tmp.name
            
            # Gerar áudio
            tts = gTTS(text=text, lang='pt')
            tts.save(temp_filename)
            
            # Reproduzir
            pygame.mixer.init()
            pygame.mixer.music.load(temp_filename)
            pygame.mixer.music.play()
            
            # Esperar terminar
            while pygame.mixer.music.get_busy():
                continue
            
            # Limpar
            pygame.mixer.quit()
            os.unlink(temp_filename)
            
        except Exception as e:
            print(f"Erro: {e}")

# Para usar:
speak_with_gtts("O Mateus é um baita de um viado !!!")