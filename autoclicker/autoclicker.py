from pynput import keyboard, mouse
from pynput.mouse import Button, Controller

import time

"""
	Решил я значит поиграть в майнкрафт, ну а там гринд, как всегда, нужно куча копать, ломать.
	Ну и подумал я напишу как я скрипт, который упростит мне жизнь.
	Пожалуйста не баньте.
"""


def on_press(key) -> None:
	"""
	Проверяем нажатую клавишу
	"""

	if key == keyboard.Key.esc:
		global flag
		flag = False
	else:
		print(f"Нажата клавиша: {key}")

def run_script():
	"""
	Запускаем скрипт, надеемся не забанят
	"""

	#Run script
	global flag
	flag = True

	try:
		#Слушаем клавиатуруb
		keyboard_listener = keyboard.Listener(on_press=on_press)
		keyboard_listener.start()

		#Контроллеры мышки и клавиатуры
		kb_controller = Controller()
		mouse_controller = Controller()

		while flag:

			#Нажатие левой кнопки мыши
			mouse_controller.press(Button.left)

			time.sleep(2)

			#Отпускаем нажатие левой кнопки мыши
			mouse_controller.release(Button.left)

	except Exception:
		print("Программа окончила свою работу")

run_script()