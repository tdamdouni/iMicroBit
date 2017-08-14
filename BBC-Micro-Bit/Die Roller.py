from microbit import *
import random


dienum6 = ["1", "2", "3", "4", "5", "6",]
dienum10 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]
dienum20 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
            "13", "14", "15", "16", "17", "18", "19", "20",]
            
die61 = Image("00000:00000:00900:00000:00000")
die62 = Image("90000:00000:00000:00000:00009")
die63 = Image("90000:00000:00900:00000:00009")
die64 = Image("90009:00000:00000:00000:90009")
die65 = Image("90009:00000:00900:00000:90009")
die66 = Image("90009:00000:90009:00000:90009")
die6nums = [die61, die62, die63, die64, die65, die66,]
display.show(Image.ARROW_W)
sleep(200)
display.scroll("d6")
display.show(Image.ARROW_W)
sleep(200)
display.scroll("d6")
sleep(1000)
display.show(Image.ARROW_E)
sleep(200)
display.scroll("d10")
display.show(Image.ARROW_E)
display.scroll("d10")
sleep(1000)
display.show(Image.ARROW_W)
sleep(200)
display.show(Image.ARROW_E)
sleep(200)
display.scroll("d20")
display.show(Image.ARROW_W)
sleep(200)
display.show(Image.ARROW_E)
sleep(200)
display.scroll("d20")
sleep(1000)

while True:
    sleep(2000)
    x = button_a.get_presses()
    y = button_b.get_presses()
    if x==1 and y==1:
        outnumber3 = random.choice(dienum20)
        display.scroll("d20")
        display.show(outnumber3, delay=700)
    elif x==1:
        outnumber = random.choice(die6nums)
        display.scroll("d6")
        display.show(outnumber)
    elif y==1:
        outnumber2 = random.choice(dienum10)
        display.scroll("d10")
        display.show(outnumber2, delay=700)
        
