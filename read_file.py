import os
import sys

#size=os.path.getsize("output1.txt")
d={}

f=open("output1.txt",'r')

#size=os.path.getsize("output1.txt")
#print size

#read_bytes=0

for line in f:
	#read_bytes += sys.getsizeof(line)

	item=line.split(':',2)
	d[item[0]]=item[-1]

	if line == '':
		continue
f.close()

#print read_bytes

for i in d.keys():

	print i + ':' + d[i]
