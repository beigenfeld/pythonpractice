for x in range(1,101):
	if x%3 == 0 and x%5==0:
		number = "fizzbuzz"
	elif x%5 == 0:
		number = "buzz"
	elif x%3 == 0:
		number = "fizz"
	else:
		number = x
	print(number)
	