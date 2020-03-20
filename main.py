from pyfirmata import Arduino, util, SERVO
import time
import math

board = Arduino("COM4")

board.digital[3].mode = SERVO

servo_pin = board.get_pin('d:3:s')

servo_pin.write(170)
time.sleep(1000)
exit()