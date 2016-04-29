#import functions first
#gLobal variables next
happy=False
food='YUMMY'
#functions next
def smile(kind): #takes in a string
	'''documentation goes here'''
	''' draws a smile and rates happyness of the user'''
	#initialize variables here!
	happyness_factor=0 #0-10 10 is max :)
	global happy
	#code here
	if kind=="happy":
		print (':)')
		happyness_factor=10
		happy=True
	elif kind=='sad':
		print(':(')
		happyness_factor=3
		happy=False
	elif kind=='crying':
		print(': (') 
		happyness_factor=0
		happy=False
	#smile(kind) # function recursion. Can be helpful if function is to be called multiple times. In this case it would lead to infinite loop
	return happyness_factor #return value is an integer as no values returned are floats or another type!

#have an empty line as that helps to see where next function starts
def hap():
	#functions can be also called in functions. Function being called in function has to be already initialized
	'''just calls smile cuz that function is that good'''
	j=smile(food) # as function returns something it has to be stored. This will not change anything as food is an exception.
	'''be aware that if you would call function now with a non exceptionit could change global variable if kind would be different
	 from user input. This would
	matter only if this function is called before we are done working with usr input'''
	
#main code
hap()
usr=raw_input('are you happy,sad or crying? ')
#returns_integer=smile(usr) #function call and stores return in return_integer. This will lead 2 smiles in a row :)
#j=smile('sad') #will alter global happy variable
print ('Your happyness factor is %i') % smile(usr) #function call can be substituted by returns_integer
hap() #wont alter our answer to usr
j=smile('food') # you can also give just string

