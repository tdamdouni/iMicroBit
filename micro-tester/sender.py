from microbit import *
import radio

broadcastPower=""

def selectBroadcastPower():
 display.clear()
 i=0
 print(i)
 while True:
  display.show(str(i), wait=False)
  if button_b.was_pressed():
   return i
  if button_a.was_pressed():
   i=i+1
   if i > 7: i=0
   display.clear()
   print(i)

def startBroadcasting(broadcastPower):
 display.clear()
 radio.on()
 radio.config(power=broadcastPower,length=32)
 i=0
 print(i)
 display.show(str(i),delay=200,clear=True,wait=False)
 radio.send(str(i))
 while True:
  sleep(75) #Debounce
  if button_a.was_pressed():
   i-=1
   print(i)
   display.show(str(i),delay=200,clear=True,wait=False)
   radio.send(str(i))
  if button_b.was_pressed():
   i+=1
   print(i)
   display.show(str(i),delay=200,clear=True,wait=False)
   radio.send(str(i))

message="I am a sender. Select my broadcast power using button a then press button b to continu"
print(message)
display.scroll(message,delay=100,wait=False)
while True:
 while broadcastPower == "":
  if button_a.was_pressed():
   broadcastPower=selectBroadcastPower()
 startBroadcasting(broadcastPower)
