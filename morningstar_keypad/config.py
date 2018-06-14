from commands.pilight import use_pilight_url, turn_on, turn_off
from commands.system import execute
from executor import on_code

use_pilight_url('http://localhost:5001')

#
KEYPAD = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]

# Use BCM numbering
ROW_PINS = [4, 14, 15, 17]
COL_PINS = [18, 27, 22]

# You can define your desired commands here
# Always put code in following order:
# - Letter
# - Number
# - Symbol
# If you want to use keypads without letter column, prefix each code with 'A'
# eg. type A1* if you want to use code 1* on your keypad

COMMANDS = {
    on_code('A1*'): turn_on('BED-LIGHT-AMBIENT'),
    on_code('A1#'): turn_off('BED-LIGHT-AMBIENT'),
    on_code('A2*'): turn_on('BED-LIGHT-ACCENT'),
    on_code('A2#'): turn_off('BED-LIGHT-ACCENT'),
    on_code('A3*'): turn_on('LIVING-LIGHT-AMBIENT'),
    on_code('A3#'): turn_off('LIVING-LIGHT-AMBIENT'),

    on_code('B1*'): turn_on('LIVING-LIGHT-ACCENT'),
    on_code('B1#'): turn_off('LIVING-LIGHT-ACCENT'),

    on_code('D1*'): execute('/etc/init.d/pilight start'),
    on_code('D1#'): execute('/etc/init.d/pilight stop')
}
