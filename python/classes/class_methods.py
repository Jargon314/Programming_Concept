

class builtin_funcs:

	def __init__(self, x, y):
		self.x, self.y = x, y

	def __repr__(self):	#used compute more accurate and official string/math
		return 'Point(x=%s, y=%s)' %(self.x, self.y)


	def __str__(self):	#mostly for the user end to handle strings
		return 'Point(x=%s and y=%s)' %(self.x, self.y)


	def __format__(self, format_spec):
		format_spec = 'this string has been formatted'
		return 'point is equal to {format_spec}'
	

P = builtin_funcs(1,2)
print(P)
string= 'thisis a string'
