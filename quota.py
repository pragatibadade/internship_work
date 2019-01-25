#!/usr/bin/python2.7

import commands
import re
from write_file import *

status,output=commands.getstatusoutput('sudo mozyutil quota')

if status == 0:
	d={}

	lines=output.split('\n')

	for line in lines:
	
        	item=line.split(':',2)
        #print item

        	if item[-1]=='':
                	item[-1].strip()
                	item[-1]= ''
        	d[item[0]]=item[-1].strip()

        	if line==' ':
                	continue

	for k, v in d.items():
    		print('{}: {}'.format(k, v))
	writeintofile("output1.txt",**d)

else:
	print "Failed to execute"
	exit()
