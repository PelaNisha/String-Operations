# Construct a NFA over (a,b) that do not end with 'aa'

accept_states = ['q2']
transition = {
	'q_0':{'a':['q_0','q_1'],'b':'q_0' },
	'q_1':{'a':'q_2','b':'q_1' },
	'q_2':{'a':'q_2','b':'q_2' }
	}

# for input 
word = input("Enter the string: ")
list_word = list(word)
word_length = len(word)

def get_new_state(current_state,ch, index):
	li = []
	for states in current_state:
		new_state = transition[states][ch]
	print(new_state)
	li.append(new_state)
	func(new_state,index+1)


# Function for analize the string
def func(current_state, index):
	ch = list_word[index]
	print("for '", ch,"'")
	new_state = transition[current_state][ch]
	print("New state ", new_state)
	if len(new_state)!=3:
		for item in new_state:
			get_new_state(item, ch, index + 1)
	else:
		current_state = new_state
		print("new current state ", current_state)
	func(current_state, index+1)	



# check the intial length
if word_length>2:
# Function calling
	current_state = 'q_0'
	x = func(current_state, 0)
else:
	exit


# accepting cases
if x in accept_states:
	print("String is valid!")
else:
	print("String is invalid!")	

# eg baab- valid:
# for b
# q0 -> q0
# # for a
# q0 -> q0, q1
# # for a
# q0 -> q0,q1
# q1 -> q2
# # for b
# q0 -> q0
# q1 -> don't care
# q2 -> q2

