# Construct a NFA over (a,b) that has "aa" as a substring


accept_states = 'q2'
transition = {
	'q0':{'a':['q0','q1'],'b':['q0'] },
	'q1':{'a':['q2'],'b':["don't care"]},
	'q2':{'a':['q2'],'b':['q2'] }
	}


# for input 
word = input("Enter the string: ")
list_word = list(word)
word_length = len(word)
current_state = ['q0']


def func(current_state):
	if word_length>1:	
		for i in range(0,word_length):
			li = []
			ch = list_word[i]
			print("for ",list_word[i])
			for c in current_state:
				if c == "don't care":
					pass
				else:
					new_state = transition[c][ch]
					print(str(c)+" -> "+str(new_state))
					li.extend(new_state)
					print('states:', li)
			current_state = li
			print("-----------")
		return li	
			
	else:
		print("String size is less")
		quit()


x = func(current_state)
print("Final states ", x)


if accept_states in x:
	print("String is valid!")
else:
	print("String is invalid!")	
