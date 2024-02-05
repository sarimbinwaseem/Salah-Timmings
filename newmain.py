import sys
import threading
import time as timelib

from Utils.salahtime import SalahTime
from Utils.display import Display


def main():
	stime = SalahTime()
	display = Display()

	display.begin_display()
	display.set_image_support()
	image = display.create_blank_image()
	draw = display.get_draw(image)
	display.draw_rectangle(draw)
	display.display_image(image)

	thread = threading.Thread(target=stime.check_changes)
	thread.start()

	### Getting data and displaying times.
	while True:
		try:

			current_time, next_salah_time = stime.get_all_times()
			display.create_image(draw, current_time, next_salah_time)

			# Display image.
			display.display_image()
			timelib.sleep(.4)

		except KeyboardInterrupt:
			print("Keyboard Interrupt... Exiting")
			display.clear()
			stime.check_changes_flag = False
			thread.join()
			sys.exit()


if __name__ == "__main__":
	main()