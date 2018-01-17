from microbit import *

grad1 = Image("13579:"
             "13579:"
             "13579:"
             "13579:"
             "13579")
             
grad2 = Image("35791:"
             "35791:"
             "35791:"
             "35791:"
             "35791")  
   
grad3 = Image("57913:"
             "57913:"
             "57913:"
             "57913:"
             "57913")
             
grad4 = Image("79135:"
             "79135:"
             "79135:"
             "79135:"
             "79135")   
             
grad5 = Image("91357:"
             "91357:"
             "91357:"
             "91357:"
             "91357") 
             
wave_A = [grad1, grad2, grad3, grad4, grad5]
wave_B = [grad5, grad4, grad3, grad2, grad1]

while True:
    if button_a.is_pressed():
            display.show(wave_A, delay=120)
    elif button_b.is_pressed():
            display.show(wave_B, delay=120)

