import numpy as np

board = np.array([[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,8,2,5,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]])



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
			raise ValueError('Row ' +str(i+1) +' is invalid.')
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

