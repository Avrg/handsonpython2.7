#this is an example of a generator. Is this a useful generator? Probably not.

def afib(number): #this is a generator creator so we have to use it to create an actual generator which we can use
	fib=[]
	for i in xrange (0,number): #saves a little bit of memory as only one number is gen at a time
		if i==0:
			fib1=1
			fib.append(fib1)
		elif i==1:
			fib2=2
			fib.append(fib2)
		else:
			fib.append(fib1+fib2)
			fib1=fib2
			fib2=fib[i]
	for each in fib:
		yield each

number=raw_input('How many fibonnacci numbers should be created? ')
number=int(number)
numfib=afib(number)
for member in numfib:
	print member
