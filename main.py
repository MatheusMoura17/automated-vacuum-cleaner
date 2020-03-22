import time

from dataio import Audio
#from dataio import Robot

stop = False

#Robot.move()

# Uma nova frase foi reconhecida
def speech_recognized(phrase):
    print(phrase)
    entry = phrase.lower()
    if entry == "levante as mãos":
        #Robot.hands_up()
        Audio.say("por favor não me machuque")
        return

    if entry == "ande para frente":
        #Robot.move()
        return

    if entry == "de pé":
        #Robot.hands_bottom()
        return

    Audio.say("Não entendi o que você falou")


audioInputSensor = Audio.Input()
audioInputSensor.start(speech_recognized)

Audio.say("Sistema iniciado")

while not stop:
    time.sleep(1000)
