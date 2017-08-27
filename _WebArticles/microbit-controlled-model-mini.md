# Microbit controlled model mini

_Captured: 2017-08-15 at 19:32 from [kershaw-kids.blogspot.de](http://kershaw-kids.blogspot.de/2017/02/microbit-controlled-model-mini.html?m=1)_

I recently found this RC model mini in a charity shop for a bargain price of 50p. There was no remote controller but the model itself had the all important motors (1 for steering the front wheels and 1 for driving the rear wheels).

![](https://4.bp.blogspot.com/-LoChRRz9hTI/WKd1Qf7yPzI/AAAAAAAAJpw/ai9ITQnBDn0z9dl0KN_4M4p0YP17-slKACLcB/s280/DSC_1948.JPG)

![](https://1.bp.blogspot.com/-pPoGFRWq-2o/WKd4i9u0PZI/AAAAAAAAJqQ/NNJsCUg0hHM7oKuiBh5kyF6HRfl0e2e_wCLcB/s200/DSC_2105.JPG)

I had previously hacked a smaller RC car for use with an Arduino, but this time wanted to try out the BBC micro:bit. As it was half term, I roped my son into helping me, especially with some of the fiddly connections and soldering (my eyesight not really being up for the job).

First, he took it apart being careful to reserve screws and take photos as he went along. Once inside, we then identified all the important electrical connections we needed and removed the existing circuit board leaving as much of the wiring as we could.

![](https://4.bp.blogspot.com/-DKqEGhUtnx8/WKd2XYu7YiI/AAAAAAAAJp4/YLhR6Q6ixnwlyX9nfRE-1rwXSKNIysv-gCLcB/s280/DSC_1953.JPG)

Next began the gradual process of reworking and testing the model.

Our plan was to use the existing battery box to power the motors, but for the Micro:Bit to control them via an [L298N H-bridge motor driver](https://www.amazon.co.uk/Controller-Module-Bridge-Stepper-Arduino/dp/B00HNHUYSG/ref=cm_cr_arp_d_product_sims?ie=UTF8) (which we already had). The Micro:Bit would have its own power supply (2 AAA batteries).

![](https://1.bp.blogspot.com/-hx4K680YIOk/WKg_WRtqoKI/AAAAAAAAJss/1bezloYKksspHLX6Mtsz3W7r4xs_AqzDQCLcB/s280/final%2Bcircuit.jpg)

> _Plan of the final circuit_

##  The motor power supply

The battery box (accessible from underneath) was a little corroded in places and the on/off switch was stuck in the on position. We cleaned everything up, but decided to ditch the switch and remove the existing wiring. The good news was that the battery compartment was for six AA batteries which meant there would be plenty of power for use with the H-bridge.

We tested the end to end connection with a volt meter and soldered on two good lengths of wire - black for -ve and red for +ve.

![](https://3.bp.blogspot.com/-RL_8lLLdyvc/WKgiZHjZ57I/AAAAAAAAJsU/0Rf9qRte644SV-HCpJIa_5HLsEQzX4VYACLcB/s280/battery%2Bbox.jpg)

> _Locating good points to solder on the +ve and -ve wires_

##  The motor connections

For each motor, we identified the two wires required to activate them. We then gave them a quick test by temporarily connecting them in turn to the battery box. All was fine.

As usual in toys of this sort each motor had a capacitor (or two) connected in parallel; we left these in place. The wires looked long enough to use directly so we just used some solder to tin them ready for connection to the H-bridge.

![](https://3.bp.blogspot.com/-X5H8LV-1nTk/WKd2xF96boI/AAAAAAAAJp8/OaePd5MOpMU2qTF9lECxfJ6fRWCC6FAGgCLcB/s280/DSC_1960.JPG)

> _Locating the two wires connected to the rear wheels_

##  Wiring up and testing the H-bridge

The four motor wires and the two wires from the battery compartment were connected to the H-bridge as follows:

![](https://1.bp.blogspot.com/-Pu5qmIEgeOY/WKhBjaNuDdI/AAAAAAAAJs8/y4Qzc1mb49Q_PYZpGWNH3zUhq-i88NnjACLcB/s280/motor%2Bcircuit.jpg)

The positions marked 1,2,3 and 4 are the signal pins to which the Micro:Bit would be later connected. However, rather than bring the Micro:Bit into the mix at this stage I got my son to simulate its action by a second circuit driven by 2 AA batteries, connected as follows.

![](https://3.bp.blogspot.com/-5r408Sf1dQ4/WKhEcXpft2I/AAAAAAAAJtc/ksiLI9jTs7gxm3bvYAlmooj9sZirtOM_gCEw/s320/microbit%2Bcircuit.jpg)

He used an old Snap Circuits battery box for this and just moved the +ve connection to each of the signal pins in turn.

Note that the two circuits have the GND connection in common.

Once this had been tested we put the mini away and concentrated on the Micro:Bit side of things.

##  Accessing and programming the GPIO pins of the Micro:Bit

We were going to need four of the Micro:Bit pins for our project which meant purchasing an edge connector board. We opted for this one from [Kitronik](https://www.kitronik.co.uk/)

![](https://www.kitronik.co.uk/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/5/6/5601b_large_edge_connector_breakout_board.jpg)

> _Edge Connector Breakout Board_

There are lots of options for programming the Micro:Bit. I opted for the [Microsoft PXT](https://www.pxt.io/) using the block editor as this seemed to fit our purposes best. I aimed for us to control our car from an Android phone over bluetooth and [this project](https://www.kitronik.co.uk/blog/part-6-coding-with-the-pxt-editor) provided clear instructions and a ready made app.

##  A simple LED circuit

![](https://4.bp.blogspot.com/-E2k_ImaiNMw/WKhf8AdPJ2I/AAAAAAAAJt4/Ed5wzEz_R08SN_T5Beek0w4jtwtsjdB7gCLcB/s280/blink.PNG)

As my son was new to the Micro:Bit and its programming environment I got him to connect up a simple LED circuit and make sure he understood the build and download process. When this code is loaded the LED lights if Button A is pressed and goes off when it is released.

![](https://4.bp.blogspot.com/-md6uaJMM6gk/WKhiUu37L8I/AAAAAAAAJuI/-XmLalToaAIDuBxO6JDpRr0ptRbfzcvsgCLcB/s280/blink%2Bcode.PNG)

Once this was working via a button press I got him to move on to getting it to work remotely via a smartphone using bluetooth.

##  Controlling the LED from the Android App

We downloaded the [Android App](https://play.google.com/store/apps/details?id=com.bittysoftware.bittygamectrlr&hl=en_GB) which we planned to use to control our car. Full information on how to write code for the Micro:Bit which responds to events from this app can be found at the [Kitronk Blog](https://www.kitronik.co.uk/blog/part-6-coding-with-the-pxt-editor). (We used Bitty Software's dedicated Bitty Game Controller App rather than the general Microbit Blue App, but the principles and event numbers are the same.)

![](https://1.bp.blogspot.com/-AHTa8clXTZE/WKhl4NDagiI/AAAAAAAAJuc/f4zMHGRlDF8ikY2gG2oIWbuMNHaKYGQnACLcB/s280/dpad_Ink_LI.jpg)

> _Bitty Game Controller's DPad with event names marked_

Following the instructions, it was very simple to put together the code necessary to connect to the Micro:Bit and to remotely activate the LED by pressing button 1 on the DPad:

![](https://1.bp.blogspot.com/-EOqoE9-iN_Q/WKhuAXLH6II/AAAAAAAAJu0/8we-cAcdFEItx4_B3W61vrwDg9kjP7M9QCLcB/s280/bluetooth%2Bconnect.PNG)

> _This code provides visual confirmation of our connect / disconnect status_

![](https://1.bp.blogspot.com/-RYYwWojYXG0/WKhuCKMJpkI/AAAAAAAAJu4/uhaNKRwAnrEntrheKWaPxAPyUM80V5njACLcB/s280/bluetooth%2Bevents.PNG)

> _This code handles the events sent when button 1 is pressed on the DPad_

After testing the connection to the Android App my son then extended the circuit to include four LEDs and added the rest of the code. We could now operate four LEDs via the forward/reverse and left/right buttons on the Android App.

The only complication was having to re-pair the Android device with the Micro:Bit every time we had downloaded new code over the USB connection. You do get used to doing this, but at first it was frustrating.

##  Attaching the Micro:bit to the mini's motors via the H-Bridge

After testing the code with the LEDs we were ready to attach the Micro:bit to the motors.

We attached the jumper wires from the Micro:bit pins to the H-Bridge pins. We tested each connection via the app as we went along to make sure each game control button activated the correct motor and direction. No adjustment was required to the code at this stage.

![](https://1.bp.blogspot.com/-aMbtBkBfpf8/WKgWJqcepLI/AAAAAAAAJrk/d3HDwgEt1Z8F9ybQUer_mKotCeuAnIUVACLcB/s280/DSC_2097.JPG)

> _Connecting the microbit to the H-bridge and testing_

The Micro:bit was then connected to a battery box and we were ready to put everything back together.

##  Putting things together

This was probably the most difficult part of the project as my son was insistent that none of our mods should be visible once the car body was back in place. For me, the important constraints were no risk of short circuits and the ability to easily disconnect both power supplies.

![](https://3.bp.blogspot.com/-Fk4XTD4sSuw/WKd6FOmPP_I/AAAAAAAAJqc/FzvO1T2NEiEUwYHWzk1LQSiUkrKd4xnAwCLcB/s280/DSC_2096.JPG)

> _H-Bridge connected and secured in position_

After some carefully placed velcro, bluetack, foam sheets and sticky pads we managed to squeeze everything in, replace the body and screw it back into position.

![](https://1.bp.blogspot.com/-IgpDfiwzWB0/WKgXCHgsbPI/AAAAAAAAJr0/y4ocIrQcEGMBtNc3_GKUOGvGcLByc0CKQCEw/s280/DSC_2099.JPG)

> _Microbit secured_

![](https://4.bp.blogspot.com/-EmOgCNkQNBU/WKgXCFeWv-I/AAAAAAAAJrw/JDZnCMmxPgI8gwBlcd51LfPTl1qlMytTwCEw/s280/DSC_2098.JPG)

> _Battery compartment attached to the top for easy access_

The very top part was just slotted in and allowed easy access to the inside.

![](https://2.bp.blogspot.com/-cOWKQOClPGo/WKgXzPsKUoI/AAAAAAAAJr8/KUqXD5M0rxkjjDUhlfrt9LBwIBC3y-XmwCLcB/s280/DSC_2100.JPG)

> _Closing the hatch_

Ready for the test drive!

##  The Test Drive

The power to the motor driver is cut by detaching a connector. The power to the microbit is cut by a switch on its battery compartment. Both of these have easy access. What doesn't have such easy access is the ability to pair the microbit. Fortunately, once your code is loaded and you have already paired with a device it is not something you have to do again as the Android device will remember. But changing to a different Android device will probably require unscrewing a few things.

Still, not a bad half term project.
