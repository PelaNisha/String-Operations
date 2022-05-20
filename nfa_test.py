# NFA over {0, 1} that accepts substring 0110 or 1001

def split(word):
	li = []
	for char in word:
		li.append(char)
	return li	

word = input("Enter the string: ")
list_word = split(word)
index = len(word)


def get_ans():
	if index>=4:
		for i in range(0,index-3):
			if list_word[i] == '0':
				if list_word[i+1] == '1':
					if list_word[i+2] == '1':
						if list_word[i+3] == '0':
							return "accepted"
						else:
							pass
					else:
						pass
				else:
					pass 
			elif list_word[i] == '1':
				if list_word[i+1] == '0':
					if list_word[i+2] == '0':
						if list_word[i+3] == '1':
							return "accepted"							
						else:
							pass
					else:
						pass
				else:
					pass 
			else:
				pass     
					
	else:
		print("Rejected!")             

a = get_ans()
if a == 'accepted':
	print(a)
else:
	print('rejected')	