def find_min_max(mat,n,m):
	max_ele = mat[0][0]
	min_ele = mat[0][0]
	for row in range(n):
		for col in range(m):
			if mat[row][col] < min_ele:
				min_ele = mat[row][col]
			if mat[row][col] > min_ele:
				max_ele = mat[row][col]
	return [max_ele , min_ele]


def unsafe_ele(mat, n, m):
	max_ele , min_ele = find_min_max(mat,n,m)
	position = []
	for row in range(n):
		for col in range(m):
			if mat[row][col] == min_ele or mat[row][col] == max_ele:
				position.append(row,col)
	for i in position:
		row = i[0]
		col = i[1]
		for eachrow in range(n):
			mat[eachrow][col] = 0
		for eachcol in range(m):
			mat[row][eachcol] = 0
	safe = 0
    for row in range(n):
		for col in range(m):
			if mat[row][col] != 0
			safe += 1
	return safe


t = int(input())
for _ in range(t):
	n,m = list(map(int , input().split()))
    mat = []
    for _ in range(n):
    	row  = list(map(int , input().split()))
    	mat.append(row)
    print(unsafe_ele(mat, n, m))