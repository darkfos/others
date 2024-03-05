from pynput import keyboard, mouse
from pynput.mouse import Button, Controller

import time


class AutoClicker:

	"""
		Решил я значит поиграть в майнкрафт, ну а там гринд, как всегда, нужно куча копать, ломать.
		Ну и подумал я напишу как я скрипт, который упростит мне жизнь.
		Пожалуйста не баньте.
	"""

	def __init__(self):
		self.flag = True

	def on_press(self, key) -> None:
		"""
		Проверяем нажатую клавишу
		"""

		if key == keyboard.Key.esc:
			self.flag = False
		else:
			print(f"Нажата клавиша: {key}")

	def run_script(self, ):
		"""
		Запускаем скрипт, надеемся не забанят
		"""

		try:
			#Слушаем клавиатуруb
			keyboard_listener = keyboard.Listener(on_press=self.on_press)
			keyboard_listener.start()

			#Контроллеры мышки и клавиатуры
			kb_controller = Controller()
			mouse_controller = Controller()

			while self.flag:

				#Нажатие левой кнопки мыши
				mouse_controller.press(Button.left)

				time.sleep(2)

				#Отпускаем нажатие левой кнопки мыши
				mouse_controller.release(Button.left)
			else:
				print("Программа окончила свою работу")

		except Exception:
			print("Программа окончила свою работу")


#Экземпляр авто кликера
auto_click = AutoClicker()
auto_click.run_script()