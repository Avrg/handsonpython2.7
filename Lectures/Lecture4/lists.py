i=10
print('I=%d, This is your mark! %s') %(i,'Good job!') # change ? to an appropriate s,d or f
i=3/2
print i #both integers so give you a mistake answer 1
i=3.0/2
print ('i=%f and i=%d -2nd is wrong')%(i,i) #this shows difference between %f and %d
lst=[1,2,'Hi','I am a',"list"] #yes you can have many kinds of data stored!
print lst #prints entire list
print lst[0] #prints only first bit of the list, in our case 1. Programmers love 0 so they start numbering form 0 in lists.
print lst[2]

lst=[1,2]
lst.append(3) #add 3 to the list
lst[:0]=[0] # adds 0 before 1 in list
print (len(lst), lst[0:2]) #len() tells you the length of the list
print lst[2:4] #prints only 2-4 bits [:x] is from 0-x and [x:] is from x to the end
print lst[1:]
del lst #delete the list :'(
#print lst # will give you an error as lst was deleted a line above
