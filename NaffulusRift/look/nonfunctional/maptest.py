def arduino_map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

x1, x2, x3 = 0, -500, 500
x1_mapped = arduino_map(x1, -1024, 1024, -20, 20)
x2_mapped = arduino_map(x2, -1024, 1024, -20, 20)
x3_mapped = arduino_map(x3, -1024, 1024, -20, 20)
print(x1, x1_mapped, x2, x2_mapped, x3, x3_mapped)
