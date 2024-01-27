## Write a program to remove duplicates from a list.

in_list = [10, 3, 4, 6, 4, 17, 10, -10, 15, 3, 6]

def rem_duplicate(in_list):
	new_list = []
	for n in in_list:
  	if n not in new_list:
    	new_list.append(n)
	return(new_list)

print(rem_duplicate(in_list))
