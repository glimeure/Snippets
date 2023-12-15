def bubblesort(ls):
	paused, flag = False, len(ls)-2
	while not paused:
		paused = True
		for i in range(0, flag+1):
			if ls[i] > ls[i+1]:
				ls[i], ls[i+1] = ls[i+1], ls[i]
				paused, flag = False, i-1
	return ls