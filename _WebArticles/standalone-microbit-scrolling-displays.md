# Standalone microbit scrolling displays

_Captured: 2017-11-27 at 18:04 from [www.suppertime.co.uk](http://www.suppertime.co.uk/blogmywiki/2017/11/microbit-scroller/)_

I wanted to make a scrolling display for my desk on parents' evening, and thought I might use a micro:bit. Then I thought 5 micro:bits might be even better. But how to get them scrolling one message across? I didn't want to use a computer to control them, I wanted them to be standalone, self-contained. And the radio abilities of the micro:bit mean that no wires should be needed.

So here's a very simple bit of Python that will turn any number of micro:bits into a rough and ready big scrolling display. There are two different programs, one for the transmitting micro:bit which goes on the right-hand end. Code your message into the Python script and flash it using the Mu editor. When all your other micro:bits are ready, press button A to begin.
    
    
    --------------------
    |RX4|RX3|RX2|RX1|TX|
    --------------------
    

The receiver code goes on all the other micro:bits numbered 1 upwards, lower numbers on the right. Change the number for each device. When powered up they stay blank until they receive the message from the transmitter.

Transmitter code - this goes on the micro:bit on the far right. Code your message in here:
    
    
    from microbit import *
    import radio
    
    message = 'Mr Booth - ICT'
    
    while True:
        if button_a.was_pressed():
            radio.on()
            radio.send(message)
            while True:
                display.scroll(message)
    

Here's the receiver code - change the rxnumber for the device number, numbering from 1 on the right, higher numbers as you go left:
    
    
    from microbit import *
    import radio
    radio.on()
    
    # set the receive device number here
    rxnumber = 1
    
    sleeptime = rxnumber * 750
    
    while True:
        incoming = radio.receive()
        if incoming:
            sleep(sleeptime)
            while True:
                display.scroll(incoming)
    

**UPDATE**

Unbeknown to me, Philip Meitiner of the micro:bit Educational Foundation has been working on pretty much exactly the same idea! Can't wait to see his code as I suspect his is a much more elegant solution:

> Found time to work on my [#microbit](https://twitter.com/hashtag/microbit?src=hash&ref_src=twsrc%5Etfw) RC matrix. Smooth scrolling was target for weekend - almost there! Lots of todos but a nice milestone :) [pic.twitter.com/ltxOTggHgg](https://t.co/ltxOTggHgg)
> 
> -- Philip Meitiner (@pragmaticPhil) [November 5, 2017](https://twitter.com/pragmaticPhil/status/927225892543385600?ref_src=twsrc%5Etfw)
