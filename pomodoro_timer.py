from microbit import *

counter_set = 0
display.show(str(counter_set))

while True:

    #When button a gets presses the counter will increase
    if button_a.get_presses():
        counter_set += 1
        display.show(str(counter_set))  
        
    #When button b gets presses the timer will start with counter set above
    elif button_b.get_presses():
        for counts in range(counter_set):
            counter_set -= 1
            sleep(60000) #sleep is in milliseconds so I have to enter 60000 for one minute
            display.show(str(counter_set))
        if counter_set == 0:
            display.scroll('Have a break')
            
    #if nothing happens, display counter
    else:
        display.show(str(counter_set))   
