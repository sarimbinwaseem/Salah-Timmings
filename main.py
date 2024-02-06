"""Main entry of the system"""

import sys
import threading
import time as timelib

from Utils.salahtime import SalahTime
from Utils.display import Display
from Utils.hardware import Hardware


def display_loop(*args):
	"""display loop to show time on the screen"""
	### Getting data and displaying times.
	stime = args[1]
	display = args[2]
	for _ in range(13):
		current_time, next_salah_time = stime.get_all_times()
		# display.create_image(draw, current_time, next_salah_time)

		# Display image.
		# display.display_image()
		timelib.sleep(0.4)

		print(current_time, next_salah_time)

	display.clear()


def main():
	"""Main entry of the system"""
	try:
		stime = SalahTime()
		display = Display()
		# hard will be used later
		hard = Hardware(display_loop, stime, display)
		print("[+] Objects initialized...")

		res = display.begin_display()
		if res == -1:
			print("[-] Display module may not be connected.")
		display.set_image_support()
		image = display.create_blank_image()
		draw = display.get_draw(image)
		display.draw_rectangle(draw)
		try:
			display.display_image(image)
		except OSError:
			print("[-] Display module may not be connected.")
			# print("[-] Exiting...!")
			# sys.exit()

		thread = threading.Thread(target=stime.check_changes, daemon=True)
		thread.start()
		print("[+] Check for the time change has been started.")

	except KeyboardInterrupt:
		print("[-] Exiting...!")
		# display.clear()
		stime.check_changes_flag = False
		thread.join()
		sys.exit()


if __name__ == "__main__":
	main()
