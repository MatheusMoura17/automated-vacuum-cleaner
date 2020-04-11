import unidecode

import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound

if not os.path.exists('audios/auto'):
    os.makedirs('audios/auto')


class Input:
    # Callback para frase reconhecida
    callback = None

    # Algum texto foi reconhecido
    def _result(self, recognizer, audio):
        try:
            phrase = recognizer.recognize_google(audio, language='pt-BR')
            self.callback(phrase)
        except sr.UnknownValueError:
            print('Google Speech Recognition could not understand audio')
        except sr.RequestError as e:
            print('Could not request results from Google Speech Recognition service; {0}'.format(e))

    # Inicia a escuta de audio
    def start(self, callback):
        self.callback = callback
        rec = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            rec.adjust_for_ambient_noise(source)
        rec.listen_in_background(mic, self._result, phrase_time_limit=3)
        print('AudioInput Start')


def say(text):
    raw_text = text.replace(' ', '_').lower()
    raw_text = unidecode.unidecode(raw_text)

    # se não existir um arquivo gravado, iremos criar um novo
    if not os.path.exists(f'audios/auto/{raw_text}.mp3'):
        tts = gTTS(text, lang='pt-br', slow=False)

        tts.save(f'audios/auto/{raw_text}.mp3')

    # Executa o arquivo
    playsound(f'audios/auto/{raw_text}.mp3')
