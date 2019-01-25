import commands
import re
from write_file import *

status,output1=commands.getstatusoutput('sudo mozyutil deviceidentity')
#print output1

if status == 0:
	result=re.sub(r'Device Identity Information','',output1)
	result1=re.sub(r'-------------','',result)
	result2=result1.lstrip()

	d={}

	output=result2.split('\n')

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
