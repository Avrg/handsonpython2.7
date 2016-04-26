#all logic operators which were mentioned
#Includes also boolean variables!

i=bool(raw_input('i=')) #remember input is string so we need to convert to bool
j=bool(raw_input('j='))

if i==True & j!=True: #and operator. both have to be true for condition to be met
	print('i is not j')
if i==True | j==True: #or operator. one has to be true or both has to be true
	print ('one or both are true')
if i==False ^ j==False: #xor. Only one can be true for condition to be met
	print('Only one is false')
# signs can be substituted with and,or,xor
