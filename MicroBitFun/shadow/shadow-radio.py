from microbit import *  
import radio

def get_accelerometer():
    return (accelerometer.get_x(), accelerometer.get_y())

def chunks(l, n):
    n = max(1, n)
    return [l[i:i + n] for i in range(0, len(l), n)]

def limit(value):
    if value > 9:
        return 9
    
    if value < 0:
        return 0
    
    return value
    

class Matrix(object):
    SIZE_X = 5
    SIZE_Y = 5

    def __init__(self, start_x, start_y):
        self.matrix = [
            0 for x in range(self.SIZE_X * self.SIZE_Y)
        ]
        
        self.last_pos = (start_x, start_y)
   
    def get(self, pos):
        x = pos[0]
        y = pos[1]
        return self.matrix[y*self.SIZE_X + x]
    
    def set(self, pos, value):
        x = pos[0]
        y = pos[1]

        self.matrix[y*self.SIZE_X + x] = limit(value)
        
    def bytes(self):
        return bytes(self.matrix)
        
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
        
    def show(self, guest_matrix):
        result_matrix = [limit(m + g) for m, g in zip(self.matrix, guest_matrix)]
        
        matrix_str = ":".join([
            "".join([str(cell) for cell in row]) 
            for row in chunks(result_matrix, self.SIZE_X)
        ])
        
        display.show(Image(matrix_str))

    def show_direct(self, guest_matrix):
        result_matrix = [limit(m + g) for m, g in zip(self.matrix, guest_matrix)]

        for x in range(self.SIZE_X):
            for y in range(self.SIZE_Y):
                p = display.get_pixel(x, y)
                rmp = result_matrix[y*self.SIZE_X + x]
                if p != rmp:
                    display.set_pixel(x, y, rmp)

matrix = Matrix(2, 2)
empty_matrix = Matrix(2, 2)
guest_matrix = empty_matrix.bytes()

radio.on()
radio.config(channel=42, queue=10, length=32, data_rate=radio.RATE_2MBIT)

failed_count = 0

while True:
    for num in range(2):            
        if num == 0:
            matrix.fading()

        new_pos = get_accelerometer()
        matrix.set_position(new_pos)
            
        radio.send_bytes(matrix.bytes())
        message = radio.receive_bytes()
        if message and len(message) == 25:
            failed_count = 0
            guest_matrix = message
        else:
            failed_count += 1
            if failed_count == 50:
                guest_matrix = empty_matrix.bytes()

        matrix.show_direct(guest_matrix)
