import commands
import re
from write_file import *

status,output=commands.getstatusoutput('sudo mozyutil listbackupdirs')
print("Status is %s:" % status)
if status == 0:
	d={}
	result=re.sub(r'Note: You can now export the listed backupdirs above into a JSON file and use it as a backup set with more configurable features. See "backupset" command for more details.','',output)

	result1=result.strip()

	d['directories']=result1

	writeintofile("output1.txt",**d)

else:
	print "Failed to execute"
	exit()
