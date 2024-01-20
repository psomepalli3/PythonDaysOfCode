## Write a program to check if a number is even or odd

try:
  num = int(input('Enter an integer number:'))
  if num % 2 == 0:
    print(num, "is even!")
  else:
    print(num, "is odd!")
except ValueError:
  print('Invalid input!')
