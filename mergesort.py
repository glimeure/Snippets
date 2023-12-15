def mergesort(ls):
	n = len(ls)
	if n <= 1: return ls
	l_half = mergesort(ls[:n//2])
	r_half = mergesort(ls[n//2:])
	merger, l, r = [], 0, 0
	while l < len(l_half) and r < len(r_half):
		if l_half[l] < r_half[r]:
			merger.append(l_half[l])
			l += 1
		else:
			merger.append(r_half[r])
			r += 1
	return merger + l_half[l:] + r_half[r:]