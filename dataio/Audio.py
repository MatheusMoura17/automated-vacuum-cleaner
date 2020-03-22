import unidecode

from pydub import AudioSegment
from pysndfx import AudioEffectsChain
import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound

if not os.path.exists("audios/recorded"):
    os.makedirs("audios/recorded")
if not os.path.exists("audios/auto"):
    os.makedirs("audios/auto")


class Input:
    # Callback para frase reconhecida
    callback = None

    # Algum texto foi reconhecido
    def _result(self, recognizer, audio):
        try:
            phrase = recognizer.recognize_google(audio, language="pt-BR")
            raw_phrase = phrase.replace(" ", "_").lower()
            raw_phrase = unidecode.unidecode(raw_phrase)

            # Salva o audio caso nao exista
            if not os.path.exists(f"audios/recorded/{raw_phrase}.wav"):
                with open(f'audios/recorded/{raw_phrase}.wav', "wb") as f:
                    f.write(audio.get_wav_data())
                    fx(f'audios/recorded/{raw_phrase}.wav', f'audios/recorded/{raw_phrase}__effect.wav')

            self.callback(phrase)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    # Inicia a escuta de audio
    def start(self, callback):
        self.callback = callback
        rec = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            rec.adjust_for_ambient_noise(source)
        rec.listen_in_background(mic, self._result, phrase_time_limit=3)
        print("AudioInput Start")


fx = (AudioEffectsChain()
      .tempo(factor=1.7)
      .speed(factor=0.7)
      .tremolo(freq=40, depth=80)
      .highshelf()
      .gain(db=10)
      )


def say(text):
    raw_text = text.replace(" ", "_").lower()
    raw_text = unidecode.unidecode(raw_text)

    # Se existir uma midia gravada por usuario, executamos
    if os.path.exists(f'audios/recorded/{raw_text}__effect.wav'):
        playsound(f'audios/recorded/{raw_text}__effect.wav')
        return

    # se não existir um arquivo gravado, iremos criar um novo
    if not os.path.exists(f'audios/auto/{raw_text}__effect.wav'):
        tts = gTTS(text, lang='pt-br', slow=False)

        tts.save(f'audios/auto/{raw_text}.mp3')
        wav = AudioSegment.from_mp3(f'audios/auto/{raw_text}.mp3')
        wav.export(f'audios/auto/{raw_text}.wav', format="wav")
        fx(f'audios/auto/{raw_text}.wav', f'audios/auto/{raw_text}__effect.wav')

    # Executa o arquivo
    playsound(f'audios/auto/{raw_text}__effect.wav')
