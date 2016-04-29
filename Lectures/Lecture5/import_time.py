import time
import datetime
f=datetime.datetime.now() #storing current time data in f
msec=f.microsecond
sec=f.second
mins=f.minute
hour=f.hour
day=f.day
month=f.month
year=f.year
print msec,sec,mins,hour,day,month, year
'''now you know how to get all this data. Can be handy
next step. How to make a clock which would figure out how long it takes to do something'''
usr=raw_input('You are going to be timed! Pess enter and then Write something!')
start=time.time() #storing current time
usr2=raw_input('')
end=time.time() #end time
usrtime=end-start #dif between end and start is the time taken
''' This is handy if you want to time something'''
print('processing function sleep next 5 seconds')
time.sleep(5) #stops program from continuing for the next 5 sec
print 'this took you: %f' %usrtime #recall why %f