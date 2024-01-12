## Create a program to calculate the area of a circle given its radius.

from math import pi

def area(r):
  return(pi* r**2)

print('Enter the radius of circle:')
r = float(input())
print('area of the circle:', area(r))
