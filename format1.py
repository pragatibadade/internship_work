import re
import tokenizer
from tokenizer import *

def formatResult(r,o):
	if r == "sudo mozyutil account --bytes":
		result=re.sub(r'Account Info','',o)
		result1=re.sub(r'------------','',result)
		tokenizer.tokenize(str(result1))	
