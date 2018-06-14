from config import COMMANDS, KEYPAD, ROW_PINS, COL_PINS
from executor import Executor, Address
from pad4pi import rpi_gpio
import time

if __name__ == '__main__':
    executor = Executor(COMMANDS)
    factory = rpi_gpio.KeypadFactory()
    keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

    group = 'A'
    code = '0'

    def execute(key):
        global group
        global code

        if key in 'ABCD':
            group = key
        if key in '0123456789':
            code = key
        if key in '*#':
            executor.execute(Address(group=group, code=code, action=key))


    keypad.registerKeyPressHandler(execute)



while True:
    print("Waiting for input...")
    time.sleep(1)

