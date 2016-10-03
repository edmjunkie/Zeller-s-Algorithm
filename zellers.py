# Name: Ibrahim Stamili
# Section: N/A
# Date: 29/9/2016
# zellers.py

import collections

print "********** Zeller's Algorithm **********"

def get_input():
	print '\nEnter any date: (e.g 22/10/1966)'
	day_ob = raw_input('day? ')
	#check if month is a number
	month_correct = False
	while not month_correct:
		month_ob = raw_input('month? ')
		month_correct = check_month(month_ob)
		
	year_ob = raw_input('year? ')
	 
	user_input = collections.namedtuple('user_input', 'day month year')
	this_user_input = user_input(day = day_ob, month = month_ob, year = year_ob)
	return this_user_input

def check_month(month):
	try:
		month = int(month)
		if month > 12:
			print 'error month must be 1-12'
			return False
		else:
			return True
	except ValueError:
		print 'error! enter month as a number'
		return False
		
def main():
	input = get_input()
	
	A = int(input.month)
	B = int(input.day)
	C = int(input.year[-2:]) #last two digits of year
	D = int(input.year[:2]) #first 2 digits of the year
	
	if A > 2: #march-dececmber
		A -= 2
	else:	#january and feb
		A += 10
		C -= 1 #use previous year
		
	W = (13 * A - 1) / 5
	X = C / 4
	Y = D / 4
	Z = W + X + Y + B + C - 2 * D
	R = Z % 7
	
	days = {
		0:'Sunday',
		1:'Monday',
		2:'Tuesday',
		3:'Wednesday',
		4:'Thursday',
		5:'Friday',
		6:'Saturday'
	}
	dob = input.day + '/' + input.month + '/' + input.year
	print '----------------'
	print 'Date entered:', dob
	print 'Day:', days[R]
		
	
	
main()