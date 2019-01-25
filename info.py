#!/usr/bin/python2.7
import subprocess
import commands
from scan2 import *
import sys
import re
from write_file import *

li=[]

for i in d.keys():
	li=list(d[i])

info_output=''
index=0

for item in li:
	
	actual_path="\'" + li[index].lstrip() + "\'"
	#actual_path="\'" + li[index] + "\'"
	print actual_path

	path= 'sudo mozyutil info --path' + ' '+ actual_path
	p=subprocess.Popen(path,shell=True,stderr=subprocess.PIPE)

	while True:
        	out=p.stderr.read(1)

        	if out=='' and p.poll() != None:
               		break

        	if out != '':
               		#global.info_output += sys.stdout.write(out).strip()
			sys.stdout.write(out).strip()
			info_output.append(out)

               		sys.stdout.flush()
	index=index+1

#info_result=re.sub(r'Not Found on server','',output)
#print info_result.rstrip()


write_string("output1.txt",info_output)
#with open("output1.txt",'a') as f:
#	f.write(info_output)
#	f.close()
