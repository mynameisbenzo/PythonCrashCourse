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

# creating groups with parentheses in a regex
group_phone_regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = group_phone_regex.search("my number is 123-123-1234.  My fax is 123-123-1233")
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())
print(mo.groups())
area_code, main_num = mo.groups()
print(area_code)
print(main_num)

hero_regex = re.compile(r"Batman|Tina Fey")
mo1 = hero_regex.search("Batman and Tina Fey.")
print(mo1.group())

mo2 = hero_regex.search("Tina Fey and Batman.")
print(mo2.group())

# | is a pipe which allows regex to take the pattern outside and match it
# with any item inside the parentheses separated by the |
bat_regex = re.compile(r"Bat(mobile|man|copter|bat)")
mo3 = bat_regex.search("Batmobile lost a wheel. Batbat.")
print(mo3.group())
print(mo3.group(1))

# using a question mark can make a piece of the regex optional
bat_regex_1 = re.compile(r"Bat(wo)?man")
mo4 = bat_regex_1.search("Batman is a bat and a man.")
print(mo4.group())

mo5 = bat_regex_1.search("Batwoman is basically Batman but a woman.")
print(mo5.group())

optional_phone = re.compile(r"(\d{3}-)?\d{3}-\d{4}")
mo6 = optional_phone.search("my full number is 123-123-1234")
print(mo6.group())

mo7 = optional_phone.search("here's the number without the area code 123-1234")
print(mo7.group())

# using * to match the repeating occurence of a pattern within a pattern
# or no occurence of the pattern! almost missed that.
banana_search = re.compile(r'ba(na)*')
mo8 = banana_search.search("I think it's spelled: banananananana")
print(mo8.group())

mo9 = banana_search.search("No... it's banana")
print(mo9.group())

mo10 = banana_search.search("I think it's ba.")
print(mo10.group())

# using + to match would find the pattern in a parentheses at least once
eric_bana_search = re.compile(r"Ba(na)+")
mo11 = eric_bana_search.search("Hi, I'm Eric Bana.")
print(mo11.group())

mo12 = eric_bana_search.search("No, you're a Banana.")
print(mo12.group())