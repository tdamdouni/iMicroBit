from microbit import *

# Gets direction of accelerometer and convert into url 
# which is sent via serial port to a PC proxy
# The PC performs a wget and confirms response

# time to wait betweeen samples - in ms
delay = 500
# translate to left sharp, left gentle, no change, right gentle anything > right sharp
x_positions = [-500, -200, 200, 500]
# y has more positions to allow finer control, but only displayed as 5 steps on led display
# translates to 10 forward, 8 , 6 , 4, stop, 4, 6, 8, 10 reverse
y_positions = [-500, -400, -300, -200, 200, 300, 400, 500]

# Array of speed to send
speed_percent = [0, 40, 60, 80, 100]

# Read from accelerometer and convert into a direction
# returns x (-2 to 2) y (-4 to 4)
def get_direction():
    x, y, z = accelerometer.get_values()
    # send to serial port
    # print ("Values are x: " + str(x) + " y: " + str(y) + " z: " + str(z))

    # convert x into -2 to +2
    # First set to the top end of the range (if other conditions not met)
    x_val = 2
    for i in range (0, 4) :
        if (x < x_positions[i]):
            x_val = i - 2
            break
    y_val = 4
    for i in range (0, 8) :
        if (y < y_positions[i]):
            y_val = i - 4
            break
    # convert y into + for forward and - for backwards
    y_val = y_val * -1
    
    return (x_val, y_val)
    

# shows status as a dot on the microbit display
def show_status(x, y):
    # show x and y on LED display
    # set all to 0
    display.clear()
    display.set_pixel(x+2, int(y* -0.5)+2, 9)
    

# Convert speed y value to % speed, direction
# if forward 1 then increase to 20 (or maintain speed), forward 2 = +10 (to 100)
def speed_change(y) :
    # stop
    if (y == 0) :
        return (0, 0)
    #reverse 
    if (y < 0) :
        direction = -1
        # make speed positive
        y = y * -1
    else :
        direction = 1
    
    # convert speed to %
    speed = speed_percent[y]
    
    return (speed, direction)
    
    
def motor_change (x, direction) :
    if (direction == 0) :
        return (0, 0)
    # when 0 then both forward or reverse
    if (x ==0) :
        # forward (1)
        if (direction > 0): return (1, 1)
        # reverse (2)
        else: return (2, 2) 
    # when +2 or -2 then that side goes reverse and opposite side goes forward
    # when +1 or -1 then that side stop and opposite side goes forward
    if (x == 2) :
        if (direction > 0): return (2, 1) 
        else: return (1, 2)
    if (x == 1) :
        if (direction > 0): return (0, 1)
        else: return (0, 2)
    if (x == -1) :
        if (direction > 0): return (1, 0)
        else: return (2, 0) 
    if (x == -2) :
        if (direction > 0): return (1, 2) 
        else: return (2, 1)
    # catch anything else and return stop
    return (0, 0)

def send_speed (speed):
    print ("/control?cmd=speed&set="+str(speed))


def send_motor (m1, m2):
    print ("/control?cmd=motor&m1="+str(m1)+"&m2="+str(m2))


    
def run():
    # Speed is % of max power start speed at 0
    speed = 0
    # direction = -1 for reverse, 1 for forward or 0 for stop
    direction = 0
    # motor values
    m1 = 0
    m2 = 0
    # send initial state
    while True:
        # Store old values - only send msg if changed
        old_speed = speed
        old_direction = direction
        old_m1 = m1
        old_m2 = m2
        x, y = get_direction()
        show_status (x, y)
        # print ("X " + str (x) + " , Y " + str(y))
        speed, direction = speed_change(y)
        m1, m2 = motor_change (x, direction)
        
        # if changed then send cmd
        if (speed != old_speed) : send_speed (speed)
        if (m1 != old_m1 or m2 != old_m2) : send_motor (m1, m2) 
        
        sleep (delay)
    
run()