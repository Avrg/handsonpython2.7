#lambda and generators

def sum(num1,num2):
	return num1+num2

def cook(food, method):
	return method+' '+food
print ('Enter numbers to be added')
a=raw_input()
b=raw_input()
a=int(a)
b=int(b)

print (sum(a,b))

print ('Now lets cook!')
food=raw_input('what food? ')
method=raw_input("how will we cook it? ")
print cook(food,method)

#both functions only used once and both of them are simple statements. In comparison to js where you can have entire functions
#anonymous python supports only simple expressions so a more complex function might not work
#as we had to define 2 functions called sum and cook now we cannot use these names again even though we used this function only once
#python has a solution to this problem - lambda!

#same code but with lambda
print ('Enter 2 numbers to be added')
a=raw_input()
b=raw_input()
a=int(a)
b=int(b)

num_sum=lambda a,b: a+b
print (num_sum(a,b))

food=raw_input('what food? ')
method=raw_input("how will we cook it? ")
made_food=lambda food,method: food+' '+method
print ('Now lets cook! %s'%( made_food(food,method)))

#if it is done this way you are able to avoid wasting a name on a function which you will use only once
#so lambda works this way: lambda var: a simple expression
