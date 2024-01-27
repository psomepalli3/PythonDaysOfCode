## Write a function to count the number of vowels in a given string 
# Method 1: Using simple for loop
def cnt_vowels(inp_str):
  vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  cnt = 0
  for character in inp_str:
    cnt += sum(list(map(lambda vowel: vowel == character, vowels)))
  return(cnt)

# Method 2: Using lambda functions(map(), filter())
def cnt_vowels_map(inp_str):
  vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  cnt = 0
  cnt = sum(list(map(lambda character: len(filter(lambda vowel: vowel == character, vowels)), inp_str)))
  return(cnt)

# Method 3: Using filter function
def cnt_vowels_filter(inp_str):
    return len(list(filter(lambda x: x in "aeiouAEIOU", inp_str)))
  
# Method 4: Using list comprehension    
######## Found out to be the most efficient after profiled for time ######
####### import cProfile #############
####### cProfile.run('cnt_vowels_list(inp_str)')  ###########
def cnt_vowels_list(inp_str):
    return len([x for x in inp_str if x in "aeiouAEIOU"])


print('Enter a string')
inp_str = input()
print('Method 1: Using simple for loop')
print(cnt_vowels(inp_str))
print('Method 2: Using lambda functions(map(), filter())')
print(cnt_vowels_map(inp_str))
print('Method 3: Using filter function')
print(cnt_vowels_filter(inp_str))
print('Method 2: Using list comprehension')
print(cnt_vowels_list(inp_str))
