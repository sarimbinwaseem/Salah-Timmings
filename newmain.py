import sys
import threading
import time as timelib

from Utils.salahtime import SalahTime
from Utils.display import Display

def exiting(display, stime, thread):

	print("Exiting...!")
	display.clear()
	stime.check_changes_flag = False
	thread.join()
	sys.exit()

def main():
	stime = SalahTime()
	display = Display()

	thread = threading.Thread(target=stime.check_changes)
	thread.start()

	display.begin_display()
	display.set_image_support()
	image = display.create_blank_image()
	draw = display.get_draw(image)
	display.draw_rectangle(draw)
	try:
		display.display_image(image)
	except OSError:
		exiting(display, stime, thread)


	### Getting data and displaying times.
	while True:
		try:

			current_time, next_salah_time = stime.get_all_times()
			display.create_image(draw, current_time, next_salah_time)

			# Display image.
			display.display_image()
			timelib.sleep(.4)

		except KeyboardInterrupt:
			exiting(display, stime, thread)


if __name__ == "__main__":
	main()