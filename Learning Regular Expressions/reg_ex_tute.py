import re

'''
	without regex, determine if value is phone number
'''
def is_phone_number(text):
	if len(text) != 12:
		return False
	for i in range(0,3):
		if not text[i].isdecimal():
			return False
	if text[3] != '-':
		return False
	for i in range(4,7):
		if not text[i].isdecimal():
			return False
	if text[7] != '-':
		return False
	for i in range(8-12):
		if not text[i].isdecimal():
			return False
	return True
	
print(is_phone_number('513-512-1234'))
print(is_phone_number('123@123-1234'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
	chunk = message[i:i+12]
	if is_phone_number(chunk):
		print('Phone number found: ' + chunk)
		
print('Done')

phone_num_regex = re.compile(r"\d{3}-\d{3}-\d{4}")
mo = phone_num_regex.search("my number is 123-123-1234")
print("Phone number found: " + mo.group())
