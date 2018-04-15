import csv
from datetime import datetime

from matplotlib import pyplot as plt

# filename = 'sitka_weather_07-2014.csv'
filename_1 = 'sitka_weather_2014.csv'
filename_2 = 'death_valley_2014.csv'

# get dates, high, and low temperatures from file
with open(filename_1) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	dates, highs, lows = [], [], []
	for row in reader:
		try:
			current_date = datetime.strptime(row[0], "%Y-%m-%d")	
			low = int(row[3])
			high = int(row[1])
		except ValueError:
			print(current_date, 'missing data')
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)
		
with open(filename_2) as f_2:
	reader_2 = csv.reader(f_2)
	header_row_2 = next(reader_2)
	
	dates_2, highs_2, lows_2 = [], [], []
	for row_2 in reader_2:
		try:
			current_date_2 = datetime.strptime(row_2[0], "%Y-%m-%d")	
			low_2 = int(row_2[3])
			high_2 = int(row_2[1])
		except ValueError:
			print(current_date_2, 'missing data')
		else:
			dates.append(current_date_2)
			highs.append(high_2)
			lows.append(low_2)
		
	# plot data
	fig = plt.figure(dpi=128, figsize=(10,6))
	plt.plot(dates, highs, c='red', alpha=0.5)
	plt.plot(dates, lows, c='blue', alpha=0.5)
	plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
	
	# format plot
	plt.title("Daily high and low temperatures - 2014\n" + 
		"Death Valley, CA", fontsize=20)
	plt.xlabel('', fontsize=16)
	fig.autofmt_xdate()
	plt.ylabel("Temperature (F)", fontsize=16)
	plt.tick_params(axis='both', which='major', labelsize=16)
	
	plt.show()