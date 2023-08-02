import sys
import time as timelib
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
	"""
	def __init__(self):
		super(SalahTime, self).__init__()

		# Indexes where the data is
		self._FAJIR = 2
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

	def check_changes(self):
		"""Check for month and date changes"""

		self._get_current_date()

		if self._backup_date != self.date:
			self._get_today_data()
			self._backup_date = self.date

		if self._backup_month != self.month:
			self._get_today_data()
			self._backup_month = self.month

	def _get_today_data(self) -> None:
		# Call it with threading to check month change.

		# month = self.current_date.strftime("%B")
		
		# Opening current month data and today's timmings.
		with shelve.open(f"Times/{self.month}") as db:
			self._today_data = db[str(self.current_date.day)]

	def _get_current_time(self) -> datetime.time:

		current_time = datetime.datetime.today().time()
		self.current_time = current_time
		return current_time

	def _get_current_date(self) -> datetime.date:

		current_date = datetime.datetime.today().date()
		self.current_date = current_date
		return current_date

	def _get_salah_time(self) -> datetime.time:

		salah_times = (
		self._today_data[self._FAJIR],
		self._today_data[self._TULU],
		self._today_data[self._ZUHUR],
		self._today_data[self._ASAR],
		self._today_data[self._MAGHRIB],
		self._today_data[self._ISHA]
			)

		salah_time = None
		for n_time in salah_times:
			if n_time > self.current_time:
				salah_time = n_time
				break
		
		if salah_time is None:
			with shelve.open(f"Times/{self.month}") as db:
				next_day_data = db[str(self.current_date.day + 1)]

			salah_time = next_day_data[self._FAJIR]

		return salah_time

	# def _get_salah_time(self, waqt) -> datetime.time:
	# 	return self._today_data[waqt]

	def _time2display(self, the_time: datetime.time) -> str:
		the_time = str(the_time)[:5]
		t = timelib.strptime(the_time, "%H:%M")
		display_time = timelib.strftime("%I:%M %p", t)
		return display_time

	def get_all_times(self) -> tuple:
		
		self._get_current_time()
		current_salah_time = self._get_salah_time()
		current_salah_time = self._time2display(current_salah_time)
		current_time = self._time2display(self.current_time)
		return (current_time, current_salah_time)

if __name__ == "__main__":
	n = SalahTime()
	thread = threading.Thread(target = n.check_changes)
	thread.start()

	while True:
		try:
			e = n.get_all_times()
			print(e, end = "\r")
			timelib.sleep(.3)
		except KeyboardInterrupt:
			sys.exit()
