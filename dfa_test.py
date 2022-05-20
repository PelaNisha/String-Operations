# Construct a DFA over (a,b) that do not end with 'ba'

def split(word):
	li = []
	for char in word:
		li.append(char)
	return li	

word = input("Enter the string: ")
list_word = split(word)
index = len(word)
if list_word[index-2]== 'b' and list_word[index-1]=='a':
	print("String not accepted!")
else:
	print("Accepted!")	
