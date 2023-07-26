import openpyxl
import time as timelib
import datetime
import sys


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
		self.Fajir = "C"
		self.Tulu = "D"
		self.Zuhur = "F"
		self.Asar = "G"
		self.Maghrib = "H"
		self.Isha = "I"

		self.sheet = None
		self._open_sheet()

		self.current_date = None
		self.current_time = None

	def _open_sheet(self) -> None:
		# Opening sheet by Month
		workbook = openpyxl.load_workbook(f'../XLSX/July.xlsx')
		self.sheet = workbook.active # Activating sheet

	def get_current_time(self) -> datetime.time:
		# currentTime = datetime.datetime.today().time().strftime("%H:%M")
		current_time = datetime.datetime.today().time()
		self.current_time = current_time
		return current_time

	def get_current_date(self) -> datetime.date:

		current_date = datetime.datetime.today().date()
		self.current_date
		return current_date

	def get_namaz_time(self, waqt, date) -> datetime.time:
		return self.sheet[f'{waqt}{date}'].value

	def time2display(self, thetime: datetime.time) -> str:
		thetime = str(thetime)[:5]
		t = timelib.strptime(thetime, "%H:%M")
		display_time = timelib.strftime("%I:%M %p", t)
		return display_time
		
n = NamazTime()
print(n.time2display(n.get_namaz_time()))


