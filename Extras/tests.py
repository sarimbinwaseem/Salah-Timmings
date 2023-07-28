# import datetime

# currentDate = datetime.datetime.today().date()

# print(type(currentDate.month))

import shelve
import openpyxl

months = ["January", "February", "March", "April", "May", "June",
			"July", "August", "September", "October","November", 
			"December"]
month = "July"
# for month in months:

# 	workbook = openpyxl.load_workbook(f'../XLSX/{month}.xlsx')
# 	sheet = workbook.active

# 	date = 1
# 	with shelve.open(f"../Times/{month}") as db:
		
# 		for row in sheet.iter_rows(values_only = True):
# 			db[str(date)] = row
# 			date += 1

with shelve.open(f"../Times/{month}") as db:
		
		# for row in sheet.iter_rows(values_only = True):
		# 	db[str(date)] = row
		# 	date += 1

		f = db["6"]

print(len(f))

import datetime

print(datetime.datetime.today().date().day)