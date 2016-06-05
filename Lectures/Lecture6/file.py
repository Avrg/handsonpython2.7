file=open('filename.txt','r+') # Py expects us to work with file so we need to save it in a way 
#similar to  a variable. Let's imagine that it does exist and contain something random with at 
#least 2 lines.
#Few cool things you can do with a file
line=file.readlines() #save lines in line
# line.strip is a useful function as it removes new lines and can make line variable into one line
filestr=''.join(line) #make it a string
#let's make a twin file:
extension='.txt'
file2=open('twin'+'.txt','w')
file2.write(filestr)
#NOW IMPORTANT STEP we need to close them to avoid wasting resources
file.close()
file2.close()
#now let's work on file2 a bit more and use a more tricky method but it will remove such hussle 
#with closing files
with open('twin.txt','r+') as f:
    first10=f.read(10) #only reads first 10 characters and saves as str
    full_str=f.read() #reads entire file and saves as 1 string
    print ('This is first 10 characters: %s, this is the entire file: %s'%(first10,full_str))
#file is closed automatically
