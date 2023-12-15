def insertionsort(ls):
	for r in range(1, len(ls)):
		l, temp = r, ls[r]
		while l > 0 and temp < ls[l-1]:
			ls[l] = ls[l-1]
			l -= 1
		ls[l] = temp
	return ls
