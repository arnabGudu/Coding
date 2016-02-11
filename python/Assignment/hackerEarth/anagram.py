t = input()

for j in range(0, t):
	s1 = input()
	s2 = input()

	count = 0

	for i in s1:
		if (i in s2):
			count = count + 2
	
	print(len(s1) + len(s2) - count)

