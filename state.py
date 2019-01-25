#! /usr/bin/python2.7

import commands
import re
from write_file import *

status, output1=commands.getstatusoutput('sudo mozyutil state --engine --snapshot --appstate --summary --bytes')

if output1 == "UNINITIALIZED":
	print "Software is disconnected from the Mozy cloud and not attempting to connect."
elif output1 == "CONNECTING":
	print "Software is attempting to connect to the Mozy cloud."
elif output1 == "AUTHENTICATED":
	print "Software is connected to the Mozy cloud and your account is authenticated."
else:
	print "nothing"



print("Status is %s" %status)
if status == 0:
	result=re.sub(r'General Info','',output1)
	result1=re.sub(r'-------------','',result)
	result2=re.sub(r'Manual Backup Mode','',result1)
	result3=result2.lstrip()

	d={}

	output=result3.split('\n')

	for line in output:
		item=line.split(':',2)
		if item[-1]=='':
			item[-1].strip()
			item[-1]=''
		d[item[0]]=item[-1].strip()
		if line=='':
			continue

	for k, v in d.items():
    		print('{}: {}'.format(k, v))

	writeintofile("output1.txt",**d)

else:
	print "Failed to execute"
	exit()
