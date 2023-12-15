# def pi(n): return (n - 1) // 2
def LCI(n): return (n * 2) + 1
def RCI(n): return (n * 2) + 2
def MCI(ls, i, n): return LCI(i) if RCI(i) > n-1 or ls[LCI(i)] > ls[RCI(i)] else RCI(i)

def heapify(ls, s, n):
	paused, i = False, s
	while not paused and LCI(i) <= n-1:
		paused, mci = True, MCI(ls, i, n)
		if ls[mci] > ls[i]:
			ls[mci], ls[i] = ls[i], ls[mci]
			paused = False
		i = mci

def heapsort(ls):
	n = len(ls)
	for s in range(n // 2 - 1, -1, -1): heapify(ls, s, n)
	while n > 0:
		ls[0], ls[n-1] = ls[n-1], ls[0]
		n -= 1
		heapify(ls, 0, n)
	return ls