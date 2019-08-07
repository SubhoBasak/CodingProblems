# Solution part

def find_two_prime_num(n):
	op_lst = []
	for i in range(2, int(n/2)+1):
		if is_prime(i):
			if is_prime(n-i):
				op_lst.append([i, n-i])
	return op_lst

def is_prime(n):
	if n == 2:
		return True
	for i in range(2, n):
		if n%i == 0:
			return False
	return True

# Testing part

tmp_lst = find_two_prime_num(12)
print('for 12:')
for i in tmp_lst:
	print(i)

print('\nfor 100:')
tmp_lst = find_two_prime_num(100)
for i in tmp_lst:
	print(i)

print('\nfor 40:')
tmp_lst = find_two_prime_num(40)
for i in tmp_lst:
	print(i)

print('\nfor 4:')
tmp_lst = find_two_prime_num(4)
for i in tmp_lst:
	print(i)
