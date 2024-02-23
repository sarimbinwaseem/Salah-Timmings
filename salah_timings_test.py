from Utils.salahtime import SalahTime
import datetime

st = SalahTime()

def test_num2month() -> None:
	month = st._number2month(2)
	assert month == "February"

def test_time2display() -> None:

	date = datetime.datetime(2024, 1, 1, 14, 25).time()
	res = st._time2display(date)
	print(res)

	assert type(res) is str
	assert res == "02:25 PM"

def test_getalltimes() -> None:
	res = st.get_all_times()
	assert type(res) is tuple

