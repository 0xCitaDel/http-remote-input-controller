from services.mouse_service import Mouse, MouseSimulate
from services.keyboard_service import Keyboard, KeyboardSimulator


class KeyboardMouseEmulator:
    def __init__(self, mouse: Mouse, keyboard: Keyboard):
        self.mouse = mouse
        self.keyboard = keyboard

    def simulate_mouse_movement(self, end):
        self.mouse.move(end)

    def simulate_mouse_move_and_click(self, x, y, width, height):
        self.mouse.move_and_click_inside_rectangle(x, y, width, height)

    def simulate_move_click_paste(self, x, y, width, height, value):
        self.simulate_mouse_move_and_click(x, y, width, height)
        self.keyboard.copy_and_insert(value)


mouse = MouseSimulate()
keyboard = KeyboardSimulator()


emu = KeyboardMouseEmulator(mouse, keyboard)

