import os

from pynput.keyboard import Key, Controller as KeyboardController
import pyperclip

class Keyboard:
    def copy_to_buffer(self, value: str):
        raise NotImplementedError

    def insert_buffer_value(self):
        raise NotImplementedError

    def copy_and_insert(self, value: str):
        raise NotImplementedError


class KeyboardSimulator(Keyboard):
    def __init__(self):
        self.cmd_key = Key.cmd if os.name == 'posix' else Key.ctrl
        self.keyboard = KeyboardController()

    def copy_to_buffer(self, value: str):
        pyperclip.copy(value)

    def insert_buffer_value(self):
        with self.keyboard.pressed(self.cmd_key):
            self.keyboard.tap('v')

    def copy_and_insert(self, value: str):
        self.copy_to_buffer(value)
        self.insert_buffer_value()
