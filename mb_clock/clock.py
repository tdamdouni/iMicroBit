from microbit import *
import radio

radio.config(group=7)
TICK_RATE = 1000
HOURS, MINS, SECS = 'h','m','s'

def read_config():
    global config
    if pin0.read_digital() == 1:
        config = HOURS
    elif pin1.read_digital() == 1:
        config = MINS
    else:
        config = SECS

FONT = ( # WhaleySans font, 2x5 digits only
("99","99","99","99","99"),
("09","09","09","09","09"),
("99","09","99","90","99"),
("99","09","99","09","99"),
("90","90","99","09","09"),
("99","90","99","09","99"),
("99","90","99","99","99"),
("99","09","09","09","09"),
("99","99","00","99","99"),
("99","99","99","09","99")
)

def img(n):
    lg = FONT[int(n/10)]
    rg = FONT[int(n%10)]
    c = ""
    for r in range(5):
        c += lg[r] + "0" + rg[r]
        if r != 4:
            c += ':'
    return Image(c)

def set_clock(t):
    global hours, mins, secs
    #hh:mm:ss\n
    try:
        t2 = t.strip()
        hours, mins, secs = t2.split(':')
        hours = int(hours)
        mins = int(mins)
        secs = int(secs)
    except:
        print("Invalid time set:%s" % str(t))
    
def tick():
    global hours, mins, secs
    secs += 1
    if secs >= 60:
        secs = 0
        mins += 1
        if mins >= 60:
            mins = 0
            hours += 1
            if hours >= 24:
                hours = 0
    
def refresh_display():
    if config == HOURS:
        display.show(img(hours))
    elif config == MINS:
        display.show(img(mins))
    elif config == SECS:
        display.show(img(secs))
    
def check_time_usb():
    t = uart.readline()
    if t is not None:
        set_clock(t)
        radio.send(t)
        
def check_time_radio():
    try:
        t = radio.receive()
        if t is not None:
            set_clock(t)
    except:
        # reset radio on error
        print("radio reset")
        radio.off()
        radio.on()
        
def pass_on_time():
    t = "%02d:%02d:%02d" % (hours, mins, secs)
    radio.send(t)

def check_update():
    global next_tick
    now = running_time()
    if now >= next_tick:
        tick()
        if config==SECS:
            pass_on_time()
        next_tick = now + TICK_RATE
        refresh_display()

def run():
    read_config()
    while True:
        check_time_usb()
        check_time_radio()
        check_update()
 
run()
