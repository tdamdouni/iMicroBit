from microbit import *  
import radio

def get_accelerometer():
    return (accelerometer.get_x(), accelerometer.get_y())

class Matrix(object):
    SIZE_X = 5
    SIZE_Y = 5
    
    def __init__(self, start_x, start_y):
        self.matrix = [
            [0 for x in range(self.SIZE_X)] 
            for y in range(self.SIZE_Y)
        ]
        
        self.last_pos = (start_x, start_y)
   
    def get(self, pos):
        x = pos[0]
        y = pos[1]
        return self.matrix[y][x]
    
    def set(self, pos, value):
        x = pos[0]
        y = pos[1]

        if value > 9:
            value = 9
        elif value < 0:
            value = 0
        self.matrix[y][x] = value
        
    def fading(self):
        for x in range(self.SIZE_X):
            for y in range(self.SIZE_Y):
                pos = (x, y)
                self.set(pos, self.get(pos) - 1)

    def _round_index(self, raw_value, last_index):
        index = int(round((raw_value / 100) + 2, 0))
        return min(max(index, max(last_index - 1, 0)), min(last_index + 1, 4))

    def validate_position(self, position):
        return tuple(
            self._round_index(new_value, last_value)
            for new_value, last_value in zip(position, self.last_pos)
        )
        
    def set_position(self, position):
        pos = self.validate_position(position)
        self.last_pos = pos
        
        self.set(pos, 9)
        
    def show(self):
        matrix_str = ":".join([
            "".join([str(cell) for cell in row]) 
            for row in self.matrix
        ])
        
        display.show(Image(matrix_str))

matrix = Matrix(2, 2)

while True:
    for num in range(2):
        if num == 0:
            matrix.fading()

        new_pos = get_accelerometer()
        matrix.set_position(new_pos)

        matrix.show()
        