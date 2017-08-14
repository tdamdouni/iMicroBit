# A-Shaky-Start-Talk-Timer

This is a BBC micro:bit count down talk timer to tell you how much time you have left to complete your talk. 

**You start the timer** by **shaking** the micro:bit. It gives you a visual indication as to the time left to give your talk. It starts counting down when you stop shaking it. Initially it lights all LEDs, and as time passes it progressively switches then off. When your time is up it displays a clock animation :-)  

**To abandon a count down**, press button A when it is timing a talk.

**To set the duration** of the talk press button A.
  * You **increment the talk length** in 1 min steps by pressing button B; and 
  * You **decrement the talk length** in 1 min steps by pressing button A. 
  * To **exit** this mode, press Button A for more than 2 seconds. It will then tell you the length of the talk, with 1 LED being lit per minute of the talk.

**When waiting to be shaken** it will tell you the length of the talk by lighting 1 LED per minute of the talk.

**Broadcasting to other microbits** - If you have other micro:bits with the "A-Shaky-Start-Talk-Timer" program it broadcasts a start message plus talk duration, which causes them to count down in the same way too - cool eh!

This is written in MicroPython.

**Debug mode** - If you press button B for more than 2 seconds whilst not counting down, this sets the timer into debug mode which sets the talk duration to 15 seconds. This will display as a single dimly lit LED. To exit debug mode, use button A to set a new talk duration.

**The radio message** being sent has the format "asstt COMMAND PAYLOAD" and is sent as a string. For the COMMAND start, the PAYLOAD is the talk length/25 (milliseconds) i.e. the delay to switch off each LED. The other COMMAND is stop and it has no PAYLOAD.

**A little trivia** - The first submit was made from a Chromebook on a train journey between Cromford to Nottingham when approaching Derby. Just after Derby I saw Britain’s rarest train, the “Flying Banana” aka the [New Measurement Train](https://en.wikipedia.org/wiki/New_Measurement_Train). Improvements to this help were subsquently made just after leaving Paddington having seen InterCity 125 engine 43003 (still looking out for 43002 which has the BR livery).
