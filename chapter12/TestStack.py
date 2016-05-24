from Stack import Stack
Stack=Stack()
for i in range(10):
	Stack.push(i)
while  not Stack.isEmpty():
	# pass
	print (Stack.pop(),end=', ')