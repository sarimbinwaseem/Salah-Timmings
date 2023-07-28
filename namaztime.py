import openpyxl
import time as timelib
import datetime
import shelve
# import sys


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

		# Index where the data is
		self.Fajir = 2
		self.Tulu = 3
		self.Zuhur = 5
		self.Asar = 6
		self.Maghrib = 7
		self.Isha = 8

		self.current_date = None
		self.current_time = None

		self._get_today_data()


	def _get_today_data(self) -> None:
		# May use shelve to store all timmings.
		self._get_current_date()
		# Opening sheet by Month
		with shelve.open(f"Times/July") as db:
			self.today_data = db[str(self.current_date.day)]

	def _get_current_time(self) -> datetime.time:
		# currentTime = datetime.datetime.today().time().strftime("%H:%M")
		current_time = datetime.datetime.today().time()
		self.current_time = current_time
		return current_time

	def _get_current_date(self) -> datetime.date:

		current_date = datetime.datetime.today().date()
		self.current_date = current_date
		return current_date

	def _get_namaz_time(self, waqt) -> datetime.time:
		return self.today_data[waqt]

	def _time2display(self, thetime: datetime.time) -> str:
		thetime = str(thetime)[:5]
		t = timelib.strptime(thetime, "%H:%M")
		display_time = timelib.strftime("%I:%M %p", t)
		return display_time

	def get_all_times(self) -> tuple:
		pass
		
n = NamazTime()
print(n._time2display(n._get_namaz_time(n.Isha)))


