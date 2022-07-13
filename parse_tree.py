# Take a Grammar of your choice and 
# implement parse tree for the string produced by the grammar.


# Production Function
di = {
	'S':['AB'],
	'A':['c','aA'],
	'B':['d', 'bB']
}


fi = []
str ='acbd'
length_of_string = len(str)


# Parse Function
def parse_string(c):
	s = 'S'
	initial = str[c]
	p = di[s][0]
	for i in p:
		for j in di[i]:
			if initial in j:
				print(i , '->', j, " String : ", str[0:c+1])
				fi.append(j)
				if c != len(str)-1:
					c = c +1
					parse_string(c)
				else:
					pass
	return "Done!"	


start = "S"
count = 0
x = parse_string(count)
print(x)
