import random
usr=''
while usr!='q':
	usr=raw_input('quit-q, see random number between 0-100 -r: ')
	if usr=='r':
		print random.randrange(100)
