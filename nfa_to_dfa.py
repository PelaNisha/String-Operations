# NFA of binary string with 2nd last bit is 1


accept_state = 'q2'
transition = {
	'q0':{'0':['q0','q1'],'1':['q1'] },
	'q1':{'0':['q2'],'1':['q2']},
	'q2':{'0':['q2'],'1':['q2'] }
	}


# User input
current_state = ['q0']
final_list = []
ini = []

initial_state=['q0']


def get_nfa_states(initial_state):
    start_state = initial_state
    final_list.append(start_state)
    for item in start_state:
        # print(item)
        state0 = transition[item]['0']
        ini.append(state0)
    for item in start_state:
        state1 = transition[item]['1']
        ini.append(state1)

        
    print(start_state,"(0)","->" ,state0, ", ",start_state,"(1)","->" ,state1)
    
    for i in ini:
        if i not in final_list:
            get_nfa_states(i)
    


get_nfa_states(initial_state)

# q0 (0) ->q0, q0 (1) -> q0q1
# q0q1 (0) -> q0q2, q0q1 (1) -> q0q1q2
# q0q2 (0) -> q0, q0q2 (1) -> q0q1
# q0q1q2 (0) -> q0q2, q0q1q2 (1) -> q0q1q2
