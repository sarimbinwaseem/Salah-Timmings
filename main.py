"""
This project is made by Sarim Bin Waseem
github.com/sarimbinwaseem

What is this?
A program to show "current time" and "current salah's ending time"
on a SSD1306 display when a physical button attached to
raspberry pi is pressed.

Next:
1. To add a buzzer sound when the time ends.
2. Implement "signal" to exit gracefully.

It also has a systemd service file so this program can start
at the boot of the system.

sudo cp salah_timings.service /etc/systemd/system/
sudo systemctl enable salah_timings.service
"""

import sys
from multiprocessing import Pipe
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
		display.draw_rectangle()
		display.draw_time_image(current_time, next_salah_time)

		# Display image.
		display.display_image()
		timelib.sleep(0.4)

		print(current_time, next_salah_time)

	display.clear()


def main():
	"""Main entry of the system"""
	try:
		# Making Pipe to communicate.
		recv_conn, send_conn = Pipe()

		stime = SalahTime(send_conn)
		display = Display()
		res = display.begin_display()
		if res == -1:
			print("[-] Display module may not be connected.")
			print("[-] Exiting...!")
			sys.exit(1)

		display.set_image_support()
		display.create_image("Images/image.png")
		display.display_image()
		timelib.sleep(3)

		display.create_blank_image()
		display.create_draw()
		display.draw_rectangle()
		display.clear()

		# hard will be used later
		hard = Hardware(display_loop, stime, display)
		print("[+] Objects initialized...")

		# Program is in loop and stuck because of this thread.
		# Ending this thread will exit the program. (May not be now)
		thread = threading.Thread(target=stime.check_changes)
		thread.start()
		print("[+] Check for the time change has been started.")

		while True:
			if recv_conn.recv() == 1:
				hard.buzz(1)
			elif recv_conn.recv() == 3:
				hard.buzz(3)

			timelib.sleep(.9)

	except KeyboardInterrupt:
		print("[-] Exiting...!")
		# display.clear()
		stime.check_date_changes_flag = False
		thread.join()
		sys.exit()


if __name__ == "__main__":
	main()
