#! /usr/bin/env  python
import commands
import tokenizer
from tokenizer import *
from format1 import *

def execute(cmd):
	status,output=commands.getstatusoutput(cmd)	
	
	formatResult(cmd,output)
	
	if status == 0:
		print "Executed successfully"
	else:
		print "Oopss...Failed to execute"
		exit()
