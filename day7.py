## Write a program to check if a number is positive, negative, or zero.
in_num = float(input("Enter a number"))

## Method 1
if in_num > 0.0:
  print("Number is positive!")
elif in_num < 0.0:
  print("Number is negative!")
else:
  print("Number is Zero!")
  
