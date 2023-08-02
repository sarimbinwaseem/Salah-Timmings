import sys
import time as timelib
import datetime
import shelve
import threading



class NamazTime:
	"""
	This class will get namaz time from XLSX file and
	pass it to the display module.

	two main returns:
	current time to display
	Namaz time to display.
	"""
	def __init__(self):
		super(NamazTime, self).__init__()

		# Indexes where the data is
		self._FAJIR = 2
		self._TULU = 3
		self._ZUHUR = 5
		self._ASAR = 6
		self._MAGHRIB = 7
		self._ISHA = 8

		self.current_date = self._get_current_date()
		self.current_time = self._get_current_time()
		self.today_data = None
		self.month = self.backup_month = self.current_date.strftime("%B")
		self.date = self.backup_date = self.current_date.strftime("%d")

		self._get_today_data()

	def check_changes(self):
		"""Check for month and date changes"""

		self._get_current_date()

		if self.backup_date != self.date:
			self._get_today_data()
			self.backup_date = self.date

		if self.backup_month != self.month:
			self._get_today_data()
			self.backup_month = self.month

	def _get_today_data(self) -> None:
		# Call it with threading to check month change.

		# month = self.current_date.strftime("%B")
		
		# Opening current month data and today's timmings.
		with shelve.open(f"Times/{self.month}") as db:
			self.today_data = db[str(self.current_date.day)]

	def _get_current_time(self) -> datetime.time:

		current_time = datetime.datetime.today().time()
		self.current_time = current_time
		return current_time

	def _get_current_date(self) -> datetime.date:

		current_date = datetime.datetime.today().date()
		self.current_date = current_date
		return current_date

	def _get_namaz_time(self) -> datetime.time:

		namaz_times = (
		self.today_data[self._FAJIR],
		self.today_data[self._TULU],
		self.today_data[self._ZUHUR],
		self.today_data[self._ASAR],
		self.today_data[self._MAGHRIB],
		self.today_data[self._ISHA]
			)

		namaz_time = None
		for n_time in namaz_times:
			if n_time > self.current_time:
				namaz_time = n_time
				break
		
		if namaz_time is None:
			with shelve.open(f"Times/{self.month}") as db:
				next_day_data = db[str(self.current_date.day + 1)]

			namaz_time = next_day_data[self._FAJIR]

		return namaz_time

	# def _get_namaz_time(self, waqt) -> datetime.time:
	# 	return self.today_data[waqt]

	def _time2display(self, theTime: datetime.time) -> str:
		theTime = str(theTime)[:5]
		t = timelib.strptime(theTime, "%H:%M")
		display_time = timelib.strftime("%I:%M %p", t)
		return display_time

	def get_all_times(self) -> tuple:
		
		self._get_current_time()
		current_namaz_time = self._get_namaz_time()
		current_namaz_time = self._time2display(current_namaz_time)
		current_time = self._time2display(self.current_time)
		return (current_time, current_namaz_time)

if __name__ == "__main__":
	n = NamazTime()
	thread = threading.Thread(target = n.check_changes)
	thread.start()

	while True:
		try:
			e = n.get_all_times()
			print(e, end = "\r")
			timelib.sleep(.3)
		except KeyboardInterrupt:
			sys.exit()
