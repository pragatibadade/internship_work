import commands
from write_file import *

status,output=commands.getstatusoutput('sudo mozyutil pwd')

if status == 0:
	d={}

	d['working_directory']=output

	writeintofile("output1.txt",**d)

else:
	print "Failed to execute"
	exit()
