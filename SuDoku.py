import numpy as np


board = np.array([[7, 5, 1,  8, 4, 3,  9, 2, 6],
[8, 9, 3,  6, 2, 5,  1, 7, 4], 
[6, 4, 2,  1, 7, 9,  5, 8, 3],
[4, 2, 5,  3, 1, 6,  7, 9, 8],
[1, 7, 6,  9, 8, 2,  3, 4, 5],
[9, 3, 8,  7, 5, 4,  6, 1, 2],
[3, 6, 4,  2, 9, 7,  8, 5, 1],
[2, 8, 9,  5, 3, 1,  4, 6, 7],
[5, 1, 7,  4, 6, 8,  2, 3, 9]])

def validate(board):
	assert np.shape(board)==(9,9)

	def check(segment):
		segment = segment.reshape(-1)
		assert all(segment) in [1,2,3,4,5,6,7,8,9]
		if np.unique(segment).shape == segment.shape:
			return 1
		else:
			return 0
	for i in range(9):
		if not check(board[i, :]):
			raise ValueError('Row ' +str(i+1) +' is invalid in.')
	for i in range(9):
		if not check(board[:, i]):
			raise ValueError('Col ' + str(i+1) +' is invalid.')
	for a in [0,3,6]:
		for b in [0,3,6]:
			if not check(board[a:a+3, b:b+3]):
				raise ValueError('Box segment '+\
					str(a)+':'+str(a+3)+';'+str(b)+':'+str(b+3)+' is invalid')
	else:
		return 1



try:
	validate(board)
except AssertionError as e:
	print("Invalid entry on board")
else:
	print("Given board is valid")

