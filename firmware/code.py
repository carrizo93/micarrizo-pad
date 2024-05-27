import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()
keyboard.modules = [encoder_handler]
keyboard.extensions.append(MediaKeys())

keyboard.col_pins = (board.D10, board.D11, board.D12, board.D13,)
keyboard.row_pins = (board.D7, board.D8, board.D9,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
encoder_handler.pins = ((board.D24, board.D25, board.D26,))

keyboard.keymap = [
    [ KC.F13, KC.F14, #row 0 top row
      KC.F15, KC.F15, KC.16,  #row 1 second row 
      KC.MPLY, KC.F17, KC.F18, KC.F19, #big switch #row 2 third row 
     ]
]

encoder_handler.map = [
    (KC.VOLU, KC.VOLD, KC.MPLY,)
]

if __name__ == '__main__':
    keyboard.go()