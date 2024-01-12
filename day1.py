## Create a program that swaps the values of two variables
# Method 1 : Using tuple unpacking
var1 = 'string 1'
var2 = 'string 2'
print("Method 1 : Using tuple unpacking")
print("Var1: , var2: ", var1, var2)
var2, var1 = var1, var2
print("Var1: , var2: ", var1, var2)

# method 2: Using functions
def swap(var1, var2):
	return(var2, var1)

var1 = 'string 1'
var2 = 'string 2'
print("Method 2 : Using function call")
print("Var1: , var2: ", var1, var2)
swap(var1, var2)
print("Var1: , var2: ", var1, var2)
  
