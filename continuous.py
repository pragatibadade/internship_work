import commands
from write_file import *

status, output=commands.getstatusoutput('sudo mozyutil continuous')
print "{}".format(output)
print ("Status is %s" %status)

if status == 0:
	d={}
	d['continuous']=output

	writeintofile("output1.txt",**d)
else:
	print "Failed to execute"
	exit()
