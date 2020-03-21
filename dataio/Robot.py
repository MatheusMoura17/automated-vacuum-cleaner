from pyfirmata import Arduino, util, SERVO

board = Arduino("COM4")
board.digital[3].mode = SERVO
board.digital[9].mode = SERVO

servo_right = board.get_pin('d:3:s')
servo_left = board.get_pin('d:9:s')

servo_left.write(90)
servo_right.write(90)


def hands_up():
    servo_left.write(0)
    servo_right.write(175)


def view_top():
    servo_left.write(175)
    servo_right.write(0)
