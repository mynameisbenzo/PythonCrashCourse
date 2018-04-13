import csv

filename = 'sitka_weather_07-2014.csv'

# get high temperatures from file
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	highs = []
	for row in reader:
		highs.append(row)
		
	print(highs)