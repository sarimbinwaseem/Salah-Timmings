import sys
import threading
import time as timelib

from Utils.salahtime import SalahTime
from Utils.display import Display
from Utils.hardware import Hardware


LOOP = True
def display_loop(*args):
	### Getting data and displaying times.
	print(args)
#	while LOOP:
#		current_time, next_salah_time = stime.get_all_times()
		# display.create_image(draw, current_time, next_salah_time)

		# Display image.
		# display.display_image()
#		timelib.sleep(.4)

#		print(current_time, next_salah_time)
#		print("In the loop...")


def main():
	stime = SalahTime()
	display = Display()
	hard = Hardware(display_loop, stime, display)
	print("[+] Objects initialized...")

	display.begin_display()
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


	thread = threading.Thread(target=stime.check_changes)
	thread.start()
	print("[+] Check for time change started.")

	

		# except KeyboardInterrupt:
		# 	print("[-] Exiting...!")
		# 	display.clear()
		# 	stime.check_changes_flag = False
		# 	thread.join()
		# 	sys.exit()


if __name__ == "__main__":
	main()
