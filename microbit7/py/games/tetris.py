icon = Image("00050:00550:30000:55909:50933")

def play():
	global score
	im = Image(5, 5)
	block = None

	def crash():
		for pos in block:
			yp = y + pos['y']
			xp = x + pos['x']
			if yp >= 5 or xp < 0 or xp >= 5 or (yp >= 0 and im.get_pixel(xp, yp) > 0):
				return True
		return False

	def draw(col = None):
		if col == None:
			col = color
		for pos in block:
			yp = y + pos['y']
			xp = x + pos['x']
			if yp >= 0 and yp < 5 and xp >= 0 and xp < 5:
				im.set_pixel(xp, yp, col)
	def hide():
		draw(0)

	game_over = False
	while not game_over:
		block_id = random.randint(0, 7)
		if block_id == 0:
			block = [ { 'x': 0, 'y': 0 } ]
			rotate = False
			color = 9
		elif block_id <= 2:
			block = [ { 'x': 0, 'y': 0 }, { 'x': 0, 'y': 1 } ]
			rotate = True
			color = 7
		elif block_id <= 6:
			block = [ { 'x': 0, 'y': 0 }, { 'x': 0, 'y': 1 }, { 'x': 1, 'y': 0 } ]
			rotate = True
			color = 5
		else:
			block = [ { 'x': 0, 'y': 0 }, { 'x': 0, 'y': 1 }, { 'x': 1, 'y': 0 }, { 'x': 1, 'y': 1 } ]
			rotate = False
			color = 3
		x = 2
		y = -2
		while not game_over:
			for n in range(0, 30):
				display.show(im)
				queue = button_sleep(10, True)
				if len(queue) > 0:
					hide()
					for press in queue:
						if press == 'a':
							x -= 1
							if crash():
								x += 1
						elif press == 'b':
							x += 1
							if crash():
								x -= 1
						elif press == 'ab' and rotate:
							# 00 -> 01, 10 -> 00, 11 -> 10, 01 -> 11
							for pos in block:
								temp = pos['x']
								pos['x'] = pos['y']
								pos['y'] = 1 - temp
							if crash():
								for pos in block:
									temp = pos['x']
									pos['x'] = 1 - pos['y']
									pos['y'] = temp
					draw()
			hide()
			y += 1
			if crash():
				y -= 1
				for pos in block:
					if y + pos['y'] < 0:
						game_over = True
						break
				else:
					draw()
					row = 4
					while row >= 0:
						clear = True
						for col in range(0, 5):
							if im.get_pixel(col, row) == 0:
								clear = False
						if clear:
							for x in range(0, 5):
								for y in range(row, 0, -1):
									im.set_pixel(x, y, im.get_pixel(x, y - 1))
								im.set_pixel(x, 0, 0)
							score += 1
						else:
							row -= 1
					break
			else:
				draw()
			display.show(im)
