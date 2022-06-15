# NFA of binary string with 2nd last bit is 1


accept_state = 'q2'
transition = {
	'q0':{'0':['q0','q1'],'1':['q1'] },
	'q1':{'0':['q2'],'1':['q2']},
	'q2':{'0':['q2'],'1':['q2'] }
	}


# User input
word = input("Enter the string: ")
word_list = list(word)
word_length = len(word)
current_state = ['q0']


def get_nfa_states():
    li =[]
    di ={}
    li1 = []
    li2 = []
    li3 = []
    for i in transition.keys():
        
        print(i,"(0)","->" ,transition[i]['0'], ", ",i,"(1)","->" ,transition[i]['1'])

        li1.append(i)
        li2.append(transition[i]['0'])
        li3.append(transition[i]['1'])
    
    # if di[transition[i]['0']] or di[transition[i]['1']] not in li:
    #     li.append(di[transition[i]['0']])
    # print(li)


def get_dfa_states():
    pass

# # Returns the final states of the nfa
# def get_final_states(current_state):
# 	if word_length>1:	
# 		# For each charater of the given word
# 		for i in range(0,word_length):
# 			li = []
# 			ch = word_list[i]
# 			print("for ",word_list[i]) # Each character

# 			# For every state in the current_state find their next_state
# 			for c in current_state: 
# 				if c == "don't care":
# 					pass
# 				else:
# 					print(type(c))
# 					new_state = transition[c][ch]
# 					print(type(new_state))
# 					print(c+" -> "+str(new_state))
# 					li.extend(new_state)
# 					print('states:', li)
# 			current_state = li
# 			print("-----------")
# 		return li	
			
# 	else:
# 		print("String size is less")
# 		quit()


# x = get_final_states(current_state)
# print("Final states ", x)


# # If the accept_state if present in the final_states
# if accept_state in x:
# 	print("String is valid!")
# else:
# 	print("String is invalid!")	

get_nfa_states()

# q0 (0) ->q0, q0 (1) -> q0q1
# q0q1 (0) -> q0q2, q0q1 (1) -> q0q1q2
# q0q2 (0) -> q0, q0q2 (1) -> q0q1
# q0q1q2 (0) -> q0q2, q0q1q2 (1) -> q0q1q2
