import random 
random.seed(123456789) #set a custom seed, by default current time is used as a seed.
# DO NOT USE THIS FOR security programs as random is not good enough
'''version 1-a is used as a hash value
	version 2 allows string, bit array to be used as it will be converted to int'''
variable=random.random() # any number from 0-1
x=random.randrange(4) #from 0-4  if you want to customise random.randrange(x,y,s) x-start y-stop, s-step
g=['a','b','c']
cho=random.sample(g,3) #cho will be a list with random 3 values from g 
lst=[1,2,'H','I']
ch=random.choice(str(lst)) #chooses 1 from string provided remember you can convert lst to str by str(list)
print variable,x,ch