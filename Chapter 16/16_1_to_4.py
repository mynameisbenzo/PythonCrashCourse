'''
	16-1:
		Goal:
			Do what was done with data from Sitka and
			Death Valley for San Francisco data
	16-2:
		Goal:
			Make a direct comparison between Sitka and
			Death Valley
	16-3:
		Goal:
			Visualize the rainfall on a location of my
			choice.  First, for a month and then for
			the entire year.
	16-4:
		Goal:
			Extra visualizations for the fun of it.
			
	Approach:
		All problem solutions will be contained in this
		file, so it may be rather long.  
		
		Problem 1, I believe, should be very straight-
		forward.  The methods already done are there for
		me to implement, so it's a matter of repeating or
		reusing previous code.
		
		UPDATE: Problem 1 will be skipped until I find a
		service that provides csv files.  
		
		Problem 2 shouldn't be too difficult either.  In
		the previous example, to note different data being
		mapped the colors of the data were different colors.
		An issue brought up in the book is that determining
		the Y-values on the plot will be something to consider.
		I believe finding the lowest and highest overal temp-
		eratures from either dataset would be the resolution.
		
		Problem 3 allows me to ditch high/low temperatures in 
		favor of a new parameter to visualize: rainfall.  The
		obvious go to here would be Seattle in my opinion.
		
		Problem 4 Free reign on visualization.  My choice is 
		Seattle rainfall vs the rainfall of somewhere really
		dry.  I'll have to look that up.
		
		NOTE: it seems that wunderground has moved away from
		providing csv/comma-delimited files at the bottom of
		each query so I will be working with the csv's provided
		by the crash course.
'''
import csv
from datetime import datetime

from matplotlib import pyplot as plt
from matplotlib import patches as mPatch

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
			dates_2.append(current_date_2)
			highs_2.append(high_2)
			lows_2.append(low_2)
		
	# plot data
	fig = plt.figure(dpi=128, figsize=(10,6))
	
	# legend
	red_patch = mPatch.Patch(color='red', label='Sitka Highs')
	blue_patch = mPatch.Patch(color='blue', label='Sitka Lows')
	yellow_patch = mPatch.Patch(color='yellow', label='Death Valley Highs')
	green_patch = mPatch.Patch(color='green', label='Death Valley Lows')
	plt.legend(handles=[red_patch, blue_patch, yellow_patch, green_patch])
	
	plt.plot(dates, highs, c='red', alpha=0.5)
	plt.plot(dates, lows, c='blue', alpha=0.5)
	plt.plot(dates_2, highs_2, c='yellow', alpha=0.5)
	plt.plot(dates_2, lows_2, c='green', alpha=0.5)
	plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
	plt.fill_between(dates_2, highs_2, lows_2, facecolor='green', alpha=0.1)
	
	# format plot
	plt.title("Daily high and low temperatures - 2014\n" + 
		"Death Valley, CA", fontsize=20)
	plt.xlabel('', fontsize=16)
	fig.autofmt_xdate()
	plt.ylabel("Temperature (F)", fontsize=16)
	plt.tick_params(axis='both', which='major', labelsize=16)
	
	plt.show()