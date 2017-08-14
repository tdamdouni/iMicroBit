icon = Image("55550:50050:50000:50090:55000")

def play():
	global score
	pip = None
	pip = random_pos()
	im = Image(5, 5)
	length = 3
	maxLength = 20
	positions = [ { 'x': 2, 'y': 5 } ] * maxLength
	headPointer = 2
	tailPointer = 0
	dx = 0
	dy = -1
	queue = []
	while True:
		nextPointer = (headPointer + 1) % maxLength
		# turn if need be
		if len(queue) > 0:
			button = queue[0]
			queue = queue[1:]
			if button == 'a':
				temp = dx
				dx = dy
				dy = -temp
			elif button == 'b':
				temp = dx
				dx = -dy
				dy = temp
		# advance one place
		positions[nextPointer] = { 'x': positions[headPointer]['x'] + dx, 'y': positions[headPointer]['y'] + dy }
		headPointer = nextPointer
		head = positions[headPointer]
		# die, eat a pip or advance the tail
		if head['x'] == pip['x'] and head['y'] == pip['y']:
			score = score + 1
			while is_lit(im, pip) > 0:
				pip = random_pos()
		else:
			unlight_pixel(im, positions[tailPointer])
			tailPointer = (tailPointer + 1) % maxLength
			if head['x'] < 0 or head['x'] > 4 or head['y'] < 0 or head['y'] > 4 or is_lit(im, head) == 5:
				break
		# update the screen
		light_pixel(im, head, 5)
		light_pixel(im, pip)
		display.show(im)
		button_sleep(400, False, queue)
