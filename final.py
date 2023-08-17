from pydub import AudioSegment
from pydub.effects import speedup
from gtts import gTTS
import pygame
import os


def text_to_speech(string, lang='tr', is_speed=False, speed_factor=1.5, delay=1.0):
    try:
        tts = gTTS(string, lang=lang)
        tts.save('output.mp3')

        sound = AudioSegment.from_file('output.mp3')
        if is_speed:
            new_sound = speedup(sound, playback_speed=speed_factor)
        else:
            new_sound = sound

        new_sound.export('final.mp3', format='mp3')

        pygame.init()
        pygame.mixer.init()

        final = pygame.mixer.Sound('final.mp3')
        final.play()

        while pygame.mixer.get_busy():
            pygame.time.delay(int(delay * 1000))

        os.remove('output.mp3')
        os.remove('final.mp3')
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    text = 'Hangi güncellemeyi talep ediyorsunuz?'

    text_to_speech('merhaba', delay=0)
    text_to_speech(text, is_speed=True, speed_factor=1.3)
