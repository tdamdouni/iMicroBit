import microbit

def number_to_row_col(number):
    number=number-1
    x=(number % 5)
    y=int(number / 5)
    return(x,y)

a_was_pressed = False
b_was_pressed = False
number=0

while True:
    if microbit.button_a.is_pressed() and a_was_pressed==False:
        a_was_pressed=True
        number+=1
        
        x=number_to_row_col(number)[0]
        y=number_to_row_col(number)[1]
        microbit.display.clear()
        microbit.display.set_pixel(x,y,9)

    if microbit.button_a.is_pressed() == False:
        a_was_pressed=False
    
    if microbit.button_b.is_pressed() and b_was_pressed==False:
        b_was_pressed=True
        number+=-1
        
        x=number_to_row_col(number)[0]
        y=number_to_row_col(number)[1]
        microbit.display.clear()
        microbit.display.set_pixel(x,y,9)

    if microbit.button_b.is_pressed() == False:
        b_was_pressed=False
