from pydub import AudioSegment
from pydub.effects import speedup
from gtts import gTTS
import pygame
import os


def text_to_speech_speed(string, lang='tr', speed_factor=1.5, delay: float = 1):
    tts = gTTS(string, lang=lang)
    tts.save('output.mp3')

    sound = AudioSegment.from_file('output.mp3')
    speedup_sound = speedup(sound, playback_speed=speed_factor)
    speedup_sound.export('speed_up.mp3', format='mp3')

    pygame.init()
    pygame.mixer.init()

    final = pygame.mixer.Sound('speed_up.mp3')
    final.play()

    while pygame.mixer.get_busy():
        pygame.time.delay(int(delay * 1000))

    os.remove('speed_up.mp3')
    os.remove('output.mp3')


if __name__ == '__main__':
    text = 'Hangi güncellemeyi talep ediyorsunuz?'

    # text_to_speech_speed('merhaba', speed_factor=1.3, delay=0.01)
    text_to_speech_speed(text, speed_factor=1.3)
