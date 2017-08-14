icon = Image("0000:09000:009900:09900:0000")

def play():
	# inititalise
	board = []
	for x in range(0, 5):
		board[x] = []
		for y in range(0, 5):
			board[x][y] = False
	# run
	im = Image(5, 5)
	first = True
	while True:
		# display
		for x in range(0, 5):
			for y in range(0, 5):
				if board[x][y]:
					im.set_pixel(x, y, 9)
				else
					im.set_pixel(x, y, 0)
		display.show(im)
		# wait for go
		if first:
			while first:
				for press in button_sleep(50, True):
					if press == 'a'
						first = False
		# quit
		for press in button_sleep(400, True):
			if press == 'ab':
				return
		# iterate
		newBoard = []
		for x in range(0, 5):
			newBoard[x] = []
			for y in range(0, 5):
				nCount = 0
				for dx in range(-1, 2):
					if board[x + dx]:
						for dy in range(-1, 2):
							if (x != 0 or y != 0) and board[y + dy]:
								nCount += 1
				if board[x][y]:
					newBoard[x][y] = (nCount < 2 or nCount > 3)
				else:
					newBoard[x][y] = nCount != 3
		board = newBoard