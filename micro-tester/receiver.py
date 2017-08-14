from microbit import *
import radio

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

def startListening(broadcastPower):
 radio.on()
 radio.config(power=broadcastPower,length=32)
 while True:
  received=radio.receive()
  if received != None: #Make sure we've received something
   print(received)
   display.show(str(received),delay=200,clear=True,wait=False)


message="I am a receiver. 		Select my broadcast power using button a then press button b to continu"
print(message)
display.scroll(message,delay=100,wait=False)
while True:
 if button_a.was_pressed():
  broadcastPower=selectBroadcastPower()
  break

startListening(broadcastPower)
