import time
import random

import math
import pyautogui
from pytweening import easeInOutQuad


pyautogui.FAILSAFE = False


class Mouse:
    def move(self, end):
        raise NotImplementedError

    def move_and_click(self, end):
        raise NotImplementedError

    def move_and_click_inside_rectangle(self, x, y, width, height):
        raise NotImplementedError


class MouseSimulate(Mouse):
    """Укажи, что благодаря target_width можно менять скорость мышки
        Добавь при иницилизации класса размер адресной панели браузера
    """
    def move(self, end, target_width=300):
        duration = self._calculate_duration(end, target_width)
        pyautogui.moveTo(
            end,
            duration=duration,
            tween=easeInOutQuad
        )

    def move_and_click(self, end):
        self.move(end)
        time.sleep(0.5)
        pyautogui.click()

    def move_and_click_inside_rectangle(self, x, y, width, height):
        target_x, target_y = self._get_inside_point(x, y, width, height)
        self.move_and_click((target_x, target_y))

    def _calculate_duration(self, end, target_width):
        start = pyautogui.position()
        distance = math.hypot(end[0] - start[0], end[1] - start[1])

        # Параметры a и b для формулы Фиттса, установлены эмпирически
        a = random.uniform(0.1, 0.15)
        b = random.uniform(0.1, 0.15)

        # Расчет времени перемещения по закону Фиттса
        return a + b * math.log2((distance / target_width) + 1)

    def _get_inside_point(self, x, y, width, height):
        center_x, center_y = x + width / 2, y + height / 2

        target_x = int(random.gauss(center_x, width / 8))
        target_y = int(random.gauss(center_y, height / 8))

        target_x = max(min(target_x, x + width), x) + 1
        target_y = max(min(target_y, y + height), y) + 114

        return (target_x, target_y)
