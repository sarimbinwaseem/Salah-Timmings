"""Salah Timmings module"""

import sys
from time import strftime, strptime, sleep
import datetime
import shelve
import threading


class SalahTime:
	"""
	This class will get salah time from pickled XLSX file and
	pass it to the display module.

	two main returns:
	current time to display
	Salah time to display.

	Usage:
	stime = SalahTime()
	stime.get_all_times()
	"""

	def __init__(self, send_conn):
		super().__init__()
		
		self.send_conn = send_conn
		self.check_changes_flag = True
		self.check_change_of_salah_flag = True
		# Indexes where the data is
		self._FAJAR = 2
		self._TULU = 3
		self._ZUHUR = 5
		self._ASAR = 6
		self._MAGHRIB = 7
		self._ISHA = 8

		self.current_date = self._get_current_date()
		self.current_time = self._get_current_time()
		self._today_data = None
		self.month = self._backup_month = self.current_date.strftime("%B")
		self.date = self._backup_date = self.current_date.strftime("%d")

		self._get_today_data()

		self.curr_salah_time = self.curr_salah_time_backup = self._get_salah_time()

	def check_change_of_salah(self):
		"""Checks for Salah TIme change."""
		while self.check_change_of_salah_flag:
			curr_salah_time = self._get_salah_time()
			if curr_salah_time != self.curr_salah_time_backup:
				self.send_conn.send(3)
				sleep(65)


	def check_changes(self):
		"""Check for month and date changes"""
		try:
			while self.check_changes_flag:
				self._get_current_date()

				if self._backup_date != self.date:
					self._get_today_data()
					self._backup_date = self.date

				if self._backup_month != self.month:
					self._get_today_data()
					self._backup_month = self.month

				sleep(1)
		except KeyboardInterrupt:
			self.check_changes_flag = False

	def _get_today_data(self) -> None:

		FLAG = True
		# Opening current month data and today's timmings.
		try:
			with shelve.open(f"Times/{self.month}") as db:
				self._today_data = db[str(self.current_date.day)]
		except FileNotFoundError:
			print(f"[-] Times/{self.month} not found!")
			while FLAG:
				print(f"[!] Trying again to open Times/{self.month}.")
				try:
					with shelve.open(f"Times/{self.month}") as db:
						self._today_data = db[str(self.current_date.day)]
				except FileNotFoundError:
					sleep(0.4)
				else:
					FLAG = False

	def _get_current_time(self) -> datetime.time:

		"""returning and saving current time.
		Should not be called separetely"""

		current_time = datetime.datetime.today().time()
		self.current_time = current_time
		return current_time

	def _get_current_date(self) -> datetime.date:
		# current_date = datetime.datetime(2023, 9, 30)

		current_date = datetime.datetime.today().date()
		self.current_date = current_date
		return current_date

	def _number2month(self, number):
		month = datetime.datetime(2023, number, 3).strftime("%B")
		return month

	def _get_salah_time(self) -> datetime.time:
		salah_times = (
			self._today_data[self._FAJAR],
			self._today_data[self._TULU],
			self._today_data[self._ZUHUR],
			self._today_data[self._ASAR],
			self._today_data[self._MAGHRIB],
			self._today_data[self._ISHA],
		)

		salah_time = None
		for n_time in salah_times:
			if n_time > self.current_time:
				salah_time = n_time
				break

		if salah_time is None:
			try:
				with shelve.open(f"Times/{self.month}") as db:
					next_day_data = db[str(self.current_date.day + 1)]

				salah_time = next_day_data[self._FAJAR]

			except KeyError:  # Possible month change.
				current_month_number = self.current_date.strftime("%m").replace("0", "")
				next_month_name = self._number2month(int(current_month_number) + 1)

				with shelve.open(f"Times/{next_month_name}") as db:
					next_day_data = db[str(1)]

				salah_time = next_day_data[self._FAJAR]

		return salah_time

	# def _get_salah_time(self, waqt) -> datetime.time:
	# 	return self._today_data[waqt]

	def _time2display(self, the_time: datetime.time) -> str:
		the_time = str(the_time)[:5]
		t = strptime(the_time, "%H:%M")
		display_time = strftime("%I:%M %p", t)
		return display_time

	def get_all_times(self) -> tuple:
		"""Return current_time and current salah's ending time."""

		self._get_current_time()
		current_salah_time = self._get_salah_time()
		current_salah_time = self._time2display(current_salah_time)
		current_time = self._time2display(self.current_time)
		return (current_time, current_salah_time)


if __name__ == "__main__":
	stime = SalahTime()
	thread = threading.Thread(target=stime.check_changes)
	thread.start()

	while True:
		try:
			e = stime.get_all_times()
			print(e, end="\r")
			sleep(0.3)
		except KeyboardInterrupt:
			# Stopping thread
			stime.check_changes_flag = False
			sys.exit()
