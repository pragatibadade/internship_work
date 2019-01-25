def tokenize(abc):
	
		d={}
		result=(abc.rstrip()).split("\n")

		for line in result:
			
			i = line.split(':',2)
			
			d[i[0]]=i[-1].strip()
			if line == '':
				continue
		for k, v in d.items():
			print('{}:{}'.format(k, v))
