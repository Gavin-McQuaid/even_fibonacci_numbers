term_1 = 1
term_2 = 2
total = 0
while term_2 < 4000000:
	
	tmp = term_2
	term_2 = term_1 + term_2
	term_1 = tmp
	
	if term_1 % 2 == 0:
		total += term_1
print total
