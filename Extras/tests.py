# import datetime

# currentDate = datetime.datetime.today().date()

# print(type(currentDate.month))

import openpyxl
import shelve

month = "April"

with shelve.open(f"../Times/{month}") as db:
		
		# for row in sheet.iter_rows(values_only = True):
		# 	db[str(date)] = row
		# 	date += 1

		f = db["6"]

print(len(f))

import datetime

print(datetime.datetime.today().date().day)