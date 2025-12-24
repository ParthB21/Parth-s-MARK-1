import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

from kmk.modules.encoder import EncoderHandler
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306


keyboard = KMKKeyboard()

PINS = [
    board.D1,
    board.D2,
    board.D3,
    board.D4,
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

encoder = EncoderHandler()
keyboard.modules.append(encoder)

encoder.pins = (
    (board.A0, board.A1),
)

encoder.map = [
    (
        (KC.VOLD, KC.VOLU),
    ),
]

oled = Display(
    display=SSD1306(
        i2c=keyboard.i2c,
        device_address=0x3C,
    ),
    entries=[
        TextEntry(text="Hackpad", x=0, y=0),
        TextEntry(text="Layer 0", x=0, y=16),
    ],
)

keyboard.extensions.append(oled)

keyboard.keymap = [
    [
        KC.A,
        KC.B,
        KC.C,
        KC.D,
    ]
]

if __name__ == "__main__":
    keyboard.go()
