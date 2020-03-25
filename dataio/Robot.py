from pyfirmata import Arduino, util, SERVO
import time

board = Arduino("COM4")
board.digital[3].mode = SERVO
board.digital[9].mode = SERVO

servo_right = board.get_pin('d:3:s')
servo_left = board.get_pin('d:9:s')


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
