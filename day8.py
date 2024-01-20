## Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it.

def cnt_upper_lower(in_str):
  if (len(in_str) == 0):
    print("Error, string length is zero")
    return(0,0)
  cnt_u = 0
  cnt_l = 0
  for c in in_str:
    if c.isalpha():
      if c.isupper():
        cnt_u +=1
      elif c.islower():
        cnt_l +=1
  return(cnt_l, cnt_u)

      
in_str = input('Enter an input string')
cnt_l, cnt_u = cnt_upper_lower(in_str)
print("No.of lower case letters:", cnt_l, "No.of upper case letters", cnt_u)
    
  
