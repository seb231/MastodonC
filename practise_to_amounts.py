#!/bin/python

import re
import fileinput

practise = "Z00000"
practise1 = "Z00001"
amount_prescribed = 0
total_prescribed = 0
output = open("practise_to_amounts.csv", "a")
month1 = 0

for f in fileinput.input():
	practise = f.split(",")[3]
	month = f.split(",")[0]
	amount_prescribed = int(f.split(",")[2])
	
	if practise == practise1:
		total_prescribed += amount_prescribed
		month1 = month
	else:
#		print practise1 + "," + str(month1) + "," + str(total_prescribed)
		output.write(practise + "," + str(month1) + "," + str(total_prescribed) + "\n")
		practise1 = practise
		month1 = month
		total_prescribed = amount_prescribed
	
