mem = {}

def A(m, n):
	if (m,n) in mem:
		return mem[(m,n)]
	if m == 0:
		mem[(m,n)] = n + 1
	elif m > 0 and n == 0:
		mem[(m,n)] = A(m-1, 1)
	else:
		mem[(m,n)] = A(m-1, A(m,n-1))
	return mem[(m,n)]

print A(5,5)
