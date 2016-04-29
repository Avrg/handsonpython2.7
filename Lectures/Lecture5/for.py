code='code'
lst=['']
anotherlst=['']
for i in range(0,10,1): #0-starting value, 10 stop, 1 step. if starts at 0 and step is one only stop value has to be present
    print code
for i in xrange(0,10,1):
    print code
for i in range(20): # can be used to work with 2 or more lists or similar variables. 
 lst.append(i)
 anotherlst.append(i)
print i
for i in lst: #best for working with one list only
    print i

#a fancy way for previous example
print ('GENERATOR')
print ([i for i in lst]) # list comprehension. Prints i for each member of the lst as it is run through the loop
''' same as
for i in lst:
	print i
'''
print lst