import cv2
import numpy as np
import pyautogui
from mss import mss

# Захват экрана
def capture_screen(region=None):
    with mss() as sct:
        monitor = sct.monitors[1] if region is None else region
        screenshot = sct.grab(monitor)
        img = np.array(screenshot)
        return cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

# Пример области для захвата (координаты необходимо настроить под ваш экран)
region = {"top": 100, "left": 100, "width": 800, "height": 600}

# Функция для распознавания карт
def recognize_cards(img):
    # Здесь нужно использовать обученную модель или алгоритм для распознавания карт
    # Например, использовать каскады Хаара или обученную модель машинного обучения
    # В данном примере используется простой подход сопоставления шаблонов
    card_templates = load_card_templates()  # Функция загрузки шаблонов карт
    recognized_cards = []

    for template, card_name in card_templates:
        result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        threshold = 0.8
        if max_val >= threshold:
            recognized_cards.append((card_name, max_loc))

    return recognized_cards

# Функция загрузки шаблонов карт (пример)
def load_card_templates():
    # Здесь нужно загрузить изображения шаблонов карт и вернуть их в виде списка
    # Например:
    card_templates = [
        (cv2.imread('card_vision/2h.png', 0), '2h'),
        (cv2.imread('card_vision/3d.png', 0), '3d'),
        # Добавьте остальные шаблоны карт
    ]
    return card_templates

# Захват изображения экрана
img = capture_screen(region)

# Преобразование изображения в серый масштаб
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Распознавание карт
recognized_cards = recognize_cards(gray_img)

# Вывод распознанных карт и их местоположений
for card_name, loc in recognized_cards:
    print(f"Recognized card: {card_name} at location: {loc}")


