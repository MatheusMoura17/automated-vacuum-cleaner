import tempfile

from pydub import AudioSegment
from pysndfx import AudioEffectsChain
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound


class Input:
    # Callback para frase reconhecida
    callback = None

    rec = sr.Recognizer()

    # Algum texto foi reconhecido
    def _result(self, recognizer, audio):
        try:
            phrase = recognizer.recognize_google(audio, language='pt-BR')
            self.callback(phrase)
        except():
            print("Frase não reconhecida")

    # Inicia a escuta de audio
    def start(self, callback):
        with sr.Microphone() as mic:
            self.callback = callback

            self.rec.listen_in_background(mic, self._result)
            print("AudioInputSensor iniciado")


fx = (AudioEffectsChain()
      .tempo(factor=1.7)
      .speed(factor=0.7)
      .tremolo(freq=40, depth=80)
      .highshelf()
      .gain(db=10)
      )


def say(text):
    tts = gTTS(text, lang='pt-br', slow=False)
    with tempfile.TemporaryDirectory() as temp:
        # Salva a fala normal
        tts.save(f'{temp}/audio.mp3')

        # Converte em wav
        wav = AudioSegment.from_mp3(f'{temp}/audio.mp3')
        wav.export(f'{temp}/audio.wav', format="wav")

        # Aplica os efeitos
        fx(f'{temp}/audio.wav', f'{temp}/audio_with_effects.wav')
        playsound(f'{temp}/audio_with_effects.wav')
