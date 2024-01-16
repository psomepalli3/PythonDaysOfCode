## Write a program to find the maximum and minimum values in a list.
def min_max(in_list):
  min_n = in_list[0]
  max_n = in_list[0]
  for n in in_list:
    if n < min_n:
      min_n = n
    if n > max_n:
      max_n = n
  return (min_n, max_n)
      
  
input_l = list(input("Enter space seperated list of numbers:").split(" "))
print("length of input",len(input_l))

print("using written function", min_max(input_l))
print("using built-in function",min(input_l),max(input_l))
