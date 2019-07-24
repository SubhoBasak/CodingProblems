import random

def rand5():
	return random.randint(1, 5)

def rand7():
	while True:
		num = 5*(rand5()-1)+rand5()
		if num < 22:
			return num%7+1
