from random import randrange

from pyfirmata2 import Arduino
import time

board = Arduino("/dev/ttyUSB0 ")

in1 = board.get_pin('d:10:o')
in2 = board.get_pin('d:9:o')
in3 = board.get_pin('d:8:o')
in4 = board.get_pin('d:7:o')
supersonic_echo = board.get_pin('d:6:i')
supersonic_trigger = board.get_pin('d:5:o')
servo_right = board.get_pin('d:4:s')
servo_left = board.get_pin('d:3:s')


def move_foward():
    in2.write(True)
    in3.write(True)

def move_back():
    in1.write(True)
    in4.write(True)

def turn_left():
    in1.write(True)
    in3.write(True)

def turn_right():
    in2.write(True)
    in4.write(True)

def get_distance():
    supersonic_trigger.write(True)
    board.pass_time(0.00015)
    supersonic_trigger.write(False)

    # Envia um ping para detectar distancia
    pulse_start = time.time()
    pulse_end = 0

    while not supersonic_echo.read():
        pulse_start = time.time()

    while supersonic_echo.read():
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance + 1.15, 2)

    return distance

def hands_middle():
    servo_left.write(90)
    servo_right.write(90)

def hands_up():
    servo_left.write(0)
    servo_right.write(175)


def hands_bottom():
    servo_left.write(175)
    servo_right.write(0)

def move():
    hands_middle()

    for a in range(10):
        for i in range(90):
            servo_right.write(90 - i)
            servo_left.write(90 + i)
            time.sleep(0.02)
        time.sleep(0.5)
        # for i in range(90):
        #     servo_right.write(90-i)
        #     servo_left.write(175-i)
        #     time.sleep(0.01)
        # for i in range(90):
        #     servo_right.write(0+i)
        #     servo_left.write(90+i)
        #     time.sleep(0.01)
    hands_middle()


def down():
    servo_left.write(175)


def up():
    servo_left.write(70)
