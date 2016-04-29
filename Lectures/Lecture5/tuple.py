t={4,5,6}
#tuple cannot be changed, but lists can
lst=list(t)
for i in range(3):
	lst.append(i+1)
t=tuple(lst)
print t