def writeintofile(filename,**data):
	with open(filename,'a')as f:
		for key,value in data.items():
			f.write("%s : %s\n" %(key,value))


def write_string(filename,string):
	with open(filename,'a') as f:
		f.write(string)	
