import sys
import threading
import time as timelib

from Utils.salahtime import SalahTime

print("Salah Timmings imported...")
stime = SalahTime()

thread = threading.Thread(target=stime.check_changes)
thread.start()


while True:

	current_time, next_namaz_time = stime.get_all_times()