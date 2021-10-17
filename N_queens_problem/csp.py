
def check(board, row, col,n):
    	#no need considering right side
	# Check this row on left side
	for i in range(col):
		if board[row][i] == 1:
			return False

	# Check upper diagonal on left side
	for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
		if board[i][j] == 1:
			return False

	# Check lower diagonal on left side
	for i, j in zip(range(row, n, 1), range(col, -1, -1)):
		if board[i][j] == 1:
			return False

	return True

def backtracking(board, col,n):
	if col >= n:
		return True

	# Consider this column and try placing
	# this queen in all rows one by one
	for i in range(n):

		if check(board, i, col,n):
			# Place this queen in board[i][col]
			board[i][col] = 1

			# recur to place rest of the queens
			if backtracking(board, col + 1,n) == True:
				return True

			board[i][col] = 0

	return False

def csp(n):
	outfile_name="./AI/"+str(n)+"_csp_output.txt"
	outfile=open(outfile_name,"w")
	board = [[0 for i in range(n)] for j in range(n)]
	if backtracking(board, 0,n) == False:
		outfile.write ("No solution")
	else:  		
		for i in range(n):
			for j in range(n):
				if board[j][i]==1:
					outfile.write(str(j+1)+" ")
					break


