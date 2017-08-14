from microbit import accelerometer as acc, sleep

tx = 10
ty = 10
tz = 40
x = y = z = 0

while True:
    nx, ny, nz = acc.get_values()

    if abs(nx - x) >= tx or abs(ny - y) >= ty or abs(nz - z) >= tz:
        x, y, z = nx, ny, nz
        print(x, y, z)

    sleep(50)
