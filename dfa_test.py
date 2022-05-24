# Construct a DFA over (a,b) that do not end with 'ba'

accept_states = ['q0','q1']
transition = {
	'q0':{'a':'q0','b':'q1' },
	'q1':{'a':'q2','b':'q1' },
	'q2':{'a':'q0','b':'q1' }
	}


def split(word):
	li = []
	for char in word:
		li.append(char)
	return li	


word = input("Enter the string: ")
list_word = split(word)
index = len(word)


# Function for analize the string
def func():
	if index>1:
		current_state = 'q0'
		for i in range(0,index):
			new_state = transition[current_state][list_word[i]]
			print(current_state+" -> "+new_state)
			current_state = new_state
		return current_state	
			
	else:
		return "string size is less"


# Function calling
x = func()

if x in accept_states:
	print("String is valid!")
else:
	print("String is invalid!")	
