# Take a Grammar of your choice and 
# implement parse tree for the string produced by the grammar.


di = {
	'S':'sAB',
	'A':'a',
	'B':'b'
}

fi = []
li = []
for i in di.keys():
	li.append(i)

# The input string is “sab”
str ='sab'
def parse_string(s, initial_string):
	st = ''
	p = di[s]
	i_string = initial_string
	print(s, " -> ", p)
	for i in p:
		if i not in li:
			fi.append(i)
			st = st+i
			# print('string update',st)
			# print("S ",s)
			# print("ST ", st)
			i_string = i_string.replace(s,st,1)
			print("updated string ",i_string)
		else:
			st = st+i
			# print(st)
			parse_string(i,i_string)
	return fi
			

start = "S"
initial_string = 'sAB'
x = parse_string(start,initial_string)
final_string = ""

for i in x:
	final_string = final_string+i
print(final_string)
