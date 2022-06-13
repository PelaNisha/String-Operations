# Construct a NFA over (a,b) that accepts string having "aa" as a substring


accept_state = 'q2'
transition = {
	'q0':{'a':['q0','q1'],'b':['q0'] },
	'q1':{'a':['q2'],'b':["don't care"]},
	'q2':{'a':['q2'],'b':['q2'] }
	}


# User input
word = input("Enter the string: ")
word_list = list(word)
word_length = len(word)
current_state = ['q0']


# Returns the final states of the nfa
def get_final_states(current_state):
	if word_length>1:	
		# For each charater of the given word
		for i in range(0,word_length):
			li = []
			ch = word_list[i]
			print("for ",word_list[i]) # Each character

			# For every state in the current_state find their next_state
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


x = get_final_states(current_state)
print("Final states ", x)


# If the accept_state if present in the final_states
if accept_state in x:
	print("String is valid!")
else:
	print("String is invalid!")	
