from gtts import gTTS
import pygame
from io import BytesIO


def play_tts(string):
    tts = gTTS(text=string, lang='tr', slow=False)
    audio_stream = BytesIO()
    tts.write_to_fp(audio_stream)
    audio_stream.seek(0)

    pygame.mixer.init()
    pygame.mixer.music.load(audio_stream)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue


if __name__ == '__main__':
    text = 'Merhaba, bu metin yapay zeka ile yapıldı'
    big_text = 'hangi güncellemeyi talep ediyorsunuz?'

    play_tts(big_text)
