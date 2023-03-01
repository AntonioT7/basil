#
# ------------------------------------------------------------
# Copyright (c) All rights reserved
# SiLab, Institute of Physics, University of Bonn
# ------------------------------------------------------------
#

''' This script shows how to use a Motor Stage
'''


from basil.dut import Dut
import numpy as np
import time


def move_source(target, std_position):
    dut["MotorStage"].set_position(target)
    current_position = dut["MotorStage"].get_position()
    time.sleep(1)
    while (np.abs(current_position - target) > std_position):
        current_position = dut["MotorStage"].get_position()
        time.sleep(1)
    print(f"Start scanning!, current position = {current_position}")
    return dut["MotorStage"].get_position()

if __name__ == '__main__':

    dut = Dut('mercury_pyserial.yaml')
    dut.init()

    move_source(-700000, 50)
    #print(dut["MotorStage"].get_position())


"""if (value>5) or (value<0):
            print("Value must be defined between 0 and 4")
        else:
            value = -700000 + value*175000
            print(value)"""


