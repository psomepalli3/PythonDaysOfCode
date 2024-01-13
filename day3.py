## Write a function to count the number of vowels in a given string 
# Method 1: Using simple for loop
def cnt_vowels(inp_str):
  vowels = ['a', 'e', 'i', 'o', 'u']
  cnt = 0
  for character in inp_str:
    cnt += sum(list(map(lambda vowel: vowel == character, vowels)))
  return(cnt)

# Method 2: Using lambda functions(map(), filter())
def cnt_vowels1(inp_str):
  vowels = ['a', 'e', 'i', 'o', 'u']
  cnt = 0
  cnt = sum(list(map(lambda character: len(filter(lambda vowel: vowel == character, vowels)), inp_str)))
  return(cnt)



print('Enter a string')
inp_str = input()
print('Method 1: Using simple for loop')
print(cnt_vowels1(inp_str))
print('Method 2: Using lambda functions(map(), filter())')
print(cnt_vowels1(inp_str))
