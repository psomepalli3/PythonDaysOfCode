# Write a program to find the sum of all elements in a list.
def add(l):
  s=0
  for n in l:
    s += n
  return(s)


new_list= [5, 4, -6, 7, 8, 0.33, 3]

#sum of the all the elements
print("sum of the all the elements using built in", sum(new_list))
print("sum of the all the elements using funcion", add(new_list))
