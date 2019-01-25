#!/usr/bin/python2.7

#import the required modules
import commands
import re
from write_file import *

#call the method to execute the specified command and retrive output
status,output=commands.getstatusoutput('sudo mozyutil account --bytes')
print('status is %s' %status)

#removing the unrequired text
result=re.sub(r'Account Info','',output)
result1=re.sub(r'------------','',result)

#define dictionary to store the result
d={}

#removing white spaces
result2=result1.lstrip()

#tokenize the string with \n
lines=result2.split('\n')
print type(lines)

#travers the result
for line in lines:
	#tokenize the line in result
	item=line.split(':',2)

	#if line contains space 
	if item[-1]=='':
		item[-1].strip()
		item[-1]= ''

	#store the result into the dictionary
	d[item[0]]=item[-1].strip()

	#even if the line is empty keep continuing
	if line==' ':
		continue
	
for k, v in d.items():
    print('{}: {}'.format(k, v))

writeintofile("output1.txt",**d)

