
# Power is Knowledge

When I first lay my eyes on the miniscule BBC micro:bit my initial thought was...

_How can I power this without cramping its style?_

Having played around a bit with the Raspberry Pi, I had discovered the drawback of plugged in USB cables, and even pocket phone top-up chargers are quite heavy. Now I know that the Pi is a giant compared with the micro:bit, and bound to be more power-hungry, but just what does the dinky little micro:bit actually need?

With a bit of research, here's what I found out.


## Basics

### Electrical

First you need to know how much "electricity" to supply.

#### Voltage

The first measure of electricity is strength, or **Voltage**. 

The BBC documentation says 3V, or **3 Volts**, which is very handy as it means you just need two common AA or AAA batteries connected in series (in a line, one battery's **+** connected to the other battery's **-**). 

#### Current

The second is flow, or Current. 

Well, like humans, the energy a circuit uses depends on what it's doing. They more calculations a processor makes, the more lights it turns on, or the chattier it gets with the Bluetooth antenna, the more current it _draws_ (sucks) from its power source, and this is measured in Amperes, or for little circuits, milliAmps (mA). 

The short answer is that the micro:bit draws 2mA when just turned on, **6mA** when it's thinking hard, and just over **10mA** when all the **LED** lights are on. You could probably assume that if you were doing lots of calculations and using the display this might go up **14mA**. 

Of course all this is just the micro:bit, and if you attach more electronics to it, these will all draw more current. According to [micro:bit safety guide](https://microbit0.blob.core.windows.net/pub/jedfednb/Parent-and-Teacher-micro-bit-safety-guide.pdf) _"The maximum current safely supplied to an external circuit using the 3V pin on the edge connector is 100mA"_.

For more on how I found this out, as well as how to reduce it, see _Detailed Consumption_ below.

#### Supply

You can use this current to work out how long your stored electricity will last. 

Look on any rechargeable battery and you'll find a rating in mAh or **m**illi-**A**mp **h**ours. OK, this does assume it's a brand new battery, fully charged, and being used in perfect conditions, including temperature, but it gives you an idea. I have a couple of household "AAA" (mini-penlight) rechargeable batteries rated at 750mAh - ideally this would give me **1500mAh** to play with.

If my code did some fancy thinking, and used the lights quite a bit, let's say I average **7.5mA** of current draw. My calculation is that 1500mAh divided by 7.5mA gives **200h** of duration. Not bad, 200 hours is **more than a week** of continuous operation off a couple of tiny rechargeable cells, and not the fanciest ones either. Don't forget, though this is just an estimate, and the _Detailed consumption_ section below shows how the lower voltage of rechargeable batteries might bag you more time.


### Physical

There are lots of options for physically connecting power (see below), but the most logical, and stable, way would be to use the **Battery Socket**. This white plastic connector is soldered to the printed circuit board (PCB) and is one of the standard PCB connectors known as JST.

All the technical documents, and many product specification for power supplies, just refer to it as JST. Unfortunately, however, this just the name of a manufacturer who makes many different size and shape of connector. I did however manage to find two sources ([1](https://www.raspberrypi.org/forums/viewtopic.php?f=62&t=136251&p=908014) and [2](https://www.element14.com/community/thread/55711)) speculating on this, and the consensus seems to be that it is a **JST-PH** type connector.


#### Detailed consumption

The voltage and current figures above are approximate. More detailed information was a little bit harder to find. I started from the [Official micro:bit Hardware Description](https://www.microbit.co.uk/device) and the [originally released BBC specifications](http://www.bbc.co.uk/mediacentre/mediapacks/microbit/specs). They were not comprehensive, but fortunately I found useful responses from _the community_. This expression just means other people who are interested, either professionally or as amateurs, and are happy to share their knowledge and learning. 

First of all, supply voltages are not always totally reliable, so circuitry voltage is usually defined within an acceptable **range**. According to [https://www.element14.com/community/message/201992/l/re-bbc-microbit-battery-power#201992] the processor's manufacturer states a voltage range of 1.8V to 3.6V. Any more than that and you risk frying the chip, but of course as you get a lower voltage supply those LEDs are going to seem a little dimmer.

But how about current - that depends on the whole circuit, and what bits of it you are using. Fortunately the folk at Renewable Energy UK spend the time to experiment, and publish their results at [http://www.reuk.co.uk/wordpress/microbit-power-consumption/] with some interesting findings.

_(fill out later - include key finding that "lower voltage means much less consumption" and "recommending power limiting circuit between 2.2 and 3V" )_



## Options

Kitronik have a handy introduction to the various ways you can power your micro:bit [https://www.kitronik.co.uk/blog/powering-your-bbc-microbit/] and it's actually surprisingly flexible.

Probably the reason Kitronik published this is because they sell lots of bits for the micro:bit, like the great mini power supply below. However you'll find lots of outlets including UK local Maplin shops, Amazon, Pi suppliers like PiHut, or just use your search engine. Watch out, however, for delivery charges when your checking out prices - they can charge more on top than the cost of items you want to buy!


### USB micro-B cable

_NB: need to validate this section against the [micro:bit safety guide](https://microbit0.blob.core.windows.net/pub/jedfednb/Parent-and-Teacher-micro-bit-safety-guide.pdf)._

This is the way you will start out, and it's easy because you're almost sure to have a mobile charger around the house with this _thin D-shaped plug_, or a data transfer cable you plug into a computer. 

_NB: the following may be contrary to the safety advice - consider validating or removing_

If you want to un-tether yourself from the wall then you can try a pocket battery pack you might have for phone top-up charging. Some of these might not recognise the tiny amount of current the micro:bit draws, and shut off after a minute or two, but you might be lucky.


### AAA battery holder

This is the easiest and cheapest solution, but gives you reasonable longevity. If you choose one with a JST-PH connector, then you'll also get a discrete and reliable physical connection, even if you move your project around a lot.

Search for **AAA battery JST**. You're looking for a 2xAAA battery holder/cage/box, and an on-off switch might be handy. Although you'll probably get the right connector anyhow, you could maybe add the words **PH** or **micro bit** just to make sure the it's the right one. 


### MI:Power board

This has to be the ultimate solution for portability. Designed to fit soundly to the micro:bit, it just makes it a little thicker but no larger.

You can buy these direct from the maker, or from other outlets mentioned above.

Thanks to [Electronics Weekly](http://www.electronicsweekly.com/blogs/gadget-master/boards/kitronik-powers-bbc-microbit-with-coin-cell-battery-2016-05/) for leading me to this solution.

By the way, with typical CR2032 3V cells having a capacity of just over **200mAh**, and using a rough average from above of 8mA current draw with a reasonably active micro:bit, you are looking at an average of around **40 hours** of use before you need to replace the cell. Of course if your project is a little bit more idle and less flashy (using LEDs more conservatively) you might get over double that.

### LiPo cell pack

Please note that these cells often supply 3.7 Volts, above the recommended range. Therefore you should only use these cells (common in radio controlled equipment) if you also use a power-limiting circuit.


### Hack your own 3V cell power pack

If you follow anything in this next section it is at **your own responsibility**. Doing something wrong could **damage your micro:bit** and it might not work any more! Be prepared to accept these consequences, or just don't bother trying this yourself.

You don't need to buy much to make a discrete low power supply - you might have all you need lying around at home. If you have spare (or part used) batteries for common household items, like car remote fobs, mini remote controls, doorbell buttons or watches, you might well find they are 3V cells like the CR2032 above. Then all you need is a couple of short lengths of shielded electrical wire and some non-conductive tape.

Please note that if you are not careful, you might **risk damaging your micro:bit** by doing this, so any attempt must be at **your own responsibility**. If you're not sure ask someone who knows more about electronic circuits, or just choose one of the other options above.

Take two short lengths of fine plastic-coated electrical wire - if you can, choose black and red (or white) so you know which is positive/+/3V/red and which is negative/-/GND/black. Strip the ends bare, but make sure that the rest of the plastic coating stays intact - exposed wire risks making short circuits that are bad for your micro:bit's health. Loop the end of the black one through GND hole and twist it tight around the contact strip - beware to avoid contacting other surfaces, and if the twisted end is too long, snip it. 

Wait for the Red/3V connection until you are ready to power up. Remember as you go, the other exposed end of the Red cable should not touch the black wire or any part of your micro:bit. If you like cover it up with a little tape whilst you work.

You can tape the other end of the black, and one end of the red to the battery cell, making sure you follow the + and - signs on the battery cell. Electrical insulation tape 
would be ideal for this bit - it's somewhat sticky but you'll probably need to dispose of the battery once its exhausted anyhow. 

Tape each wire firmly to each side, making sure to avoid short circuits. That means the two wires mustn't touch at either end, and don't cross between the two different metal surfaces of the battery. If the exposed ends are long you could trim them or twist them round into a loop or spiral to avoid touching the other side of the battery. Press the tape firmly to ensure good contact, and consider wrapping it all around so that no metal surface of the battery is left exposed. 

Remember as you go, the other exposed end of the Red cable should not touch the black wire or any part of your micro:bit.

To keep the battery in place as you move around, you could tape it to the micro:bit. Paper-based Masking tape might be the best solution, as it is easy to remove and does not leave a sticky residue, but you MUST ensure that the surfaces of your battery cell are well covered, as masking tape alone is not a guarantee of electrical insulation. 

As I say, you **risk damaging your micro:bit** if you do not ensure safe connections and insulation. 


## More reading

* technical discussion about connectors and suitable power ranges for the micro:bit [https://www.element14.com/community/thread/55711/l/bbc-microbit-battery-power?displayFullThread=true]
* general stuff about powering small devices [https://learn.adafruit.com/battery-powering-wearable-electronics]


