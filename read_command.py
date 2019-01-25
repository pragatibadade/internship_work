#! /usr/bin/env python
import execute_command
from execute_command import *

with open("commands.txt",'r')as f:
	for line in f:
		execute_command.execute(line.strip())
