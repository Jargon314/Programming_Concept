############### Data Types	################

#strings and manipulation
string = 'The string'	#
index = string[0]
# integers  and manipulation
zero = 0
one  = 1
two  = 2 

result = 3*(3-4)/2
comp = -1.5

print('we accessed %s first char or first indice' % index )

####	Conditionals	########
if string == 'The string':
	print('the strings matched')
elif index == 'T':
	print("string was null finishing up")

else:
	print('strings didnt match defaulting')

if result != comp:
	print('result did not match')

######	Loops	#########

for i in range(10):
	print(i)

for i in string:
	print(i)



