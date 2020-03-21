import time

from dataio import Audio
from dataio import Robot

stop = False


# Uma nova frase foi reconhecida
def speech_recognized(phrase):
    print(phrase)
    entry = phrase.lower()
    if entry == "isso é um assalto":
        Robot.hands_up()
        Audio.say("por favor não me machuque")
        return

    if entry == "de pé":
        Robot.view_top()
        return

    if entry == "desligar":
        stop = True
        return

    Audio.say("Não entendi o que você falou")


audioInputSensor = Audio.Input()
audioInputSensor.start(speech_recognized)

while not stop:
    time.sleep(1000)