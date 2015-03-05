#!/bin/python

import re
import fileinput

month = 0
amount = 0
No_Methylphenidate = 0
No_Atomoxetine = 0
No_Dexamfetamine = 0
No_Methylamfetamine = 0
No_Lisdexamfetamine = 0
No_Hyroxyamfetamine = 0
output = open("drugs.month", "a")
output2 = open("per.month", "a")

# need to change input filename to include all data

for f in fileinput.input():
	if re.search("0404000M0", f):
		month = f.split(",")[9]
		BNF = f.split(",")[3]
		drug = BNF[0:9]
		amount = f.split(",")[5]
		practise = f.split(",")[2]
		net_cost = f.split(",")[6]
		act_cost = f.split(",")[7]
		No_Methylphenidate += int(amount)
		output.write(month + "," + drug + "," + amount + "," + practise + "," + net_cost + "," + act_cost + "\n")
	elif re.search("0404000S0", f):
		month = f.split(",")[9]
		BNF = f.split(",")[3]
		drug = BNF[0:9]
		amount = f.split(",")[5]
		practise = f.split(",")[2]
		net_cost = f.split(",")[6]
		act_cost = f.split(",")[7]
		No_Atomoxetine += int(amount)
		output.write(month + "," + drug + "," + amount + "," + practise + "," + net_cost + "," + act_cost + "\n")
	elif re.search("0404000L0", f):
		month = f.split(",")[9]
		BNF = f.split(",")[3]
		drug = BNF[0:9]
		amount = f.split(",")[5]
		practise = f.split(",")[2]
		net_cost = f.split(",")[6]
		act_cost = f.split(",")[7]
		No_Dexamfetamine += int(amount)
		output.write(month + "," + drug + "," + amount + "," + practise + "," + net_cost + "," + act_cost + "\n")
	elif re.search("0404000N0", f):
		month = f.split(",")[9]
		BNF = f.split(",")[3]
		drug = BNF[0:9]
		amount = f.split(",")[5]
		practise = f.split(",")[2]
		net_cost = f.split(",")[6]
		act_cost = f.split(",")[7]
		No_Methylamfetamine += int(amount)
		output.write(month + "," + drug + "," + amount + "," + practise + "," + net_cost + "," + act_cost + "\n")
	elif re.search("0404000U0", f):
		month = f.split(",")[9]
		BNF = f.split(",")[3]
		drug = BNF[0:9]
		amount = f.split(",")[5]
		practise = f.split(",")[2]
		net_cost = f.split(",")[6]
		act_cost = f.split(",")[7]
		No_Lisdexamfetamine += int(amount)
		output.write(month + "," + drug + "," + amount + "," + practise + "," + net_cost + "," + act_cost + "\n")
	elif re.search("1105000G0", f):
		month = f.split(",")[9]
		BNF = f.split(",")[3]
		drug = BNF[0:9]
		amount = f.split(",")[5]
		practise = f.split(",")[2]
		net_cost = f.split(",")[6]
		act_cost = f.split(",")[7]
		No_Hyroxyamfetamine += int(amount)
		output.write(month + "," + drug + "," + amount + "," + practise + "," + net_cost + "," + act_cost + "\n")
Total = No_Methylphenidate + No_Atomoxetine + No_Dexamfetamine + No_Methylamfetamine + No_Lisdexamfetamine + No_Hyroxyamfetamine

output2.write(month + "," + str(No_Methylphenidate) + "," + str(No_Atomoxetine) + "," + str(No_Dexamfetamine) + "," + str(No_Methylamfetamine) + "," + str(No_Lisdexamfetamine) + "," + str(No_Hyroxyamfetamine) + "," + str(Total) + "\n")
