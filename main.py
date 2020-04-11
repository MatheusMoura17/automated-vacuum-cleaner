import time

from dataio import Audio
from dataio import Robot

stop = False

def move():
    Robot.hands_middle()
    Robot.motor_foward()
    time.sleep(5)
    Robot.motor_idle()
    Robot.motor_left()
    time.sleep(0.2)
    Robot.motor_idle()
    Robot.hands_up()
    Robot.motor_foward()
    time.sleep(0.2)
    Robot.motor_idle()
    Robot.motor_foward()
    time.sleep(5)
    Robot.motor_idle()

move()

# Uma nova frase foi reconhecida
def speech_recognized(phrase):
    print(phrase)
    entry = phrase.lower()
    if entry == "levante as mãos":
        Robot.hands_up()
        Audio.say("por favor não me machuque")
        return

    if entry == "ande para frente":
        Robot.motor_foward()
        return

    Audio.say("Não entendi o que você falou")


# audioInputSensor = Audio.Input()
# audioInputSensor.start(speech_recognized)

# Audio.say("Sistema iniciado")

# while not stop:
 #   time.sleep(1000)
