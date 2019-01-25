import commands
import re
from write_file import *

status,output=commands.getstatusoutput('sudo mozyutil ls')

if status == 0:
	d={}

	d['ls_dir']=output

	writeintofile("output1.txt",**d)

else:
	print "Failed to execute"
	exit()
