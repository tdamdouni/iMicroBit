# Weekend Halloween Project: Illuminated Candy Bucket Featuring BBC Microbit

_Captured: 2017-10-28 at 12:42 from [www.element14.com](https://www.element14.com/community/community/stem-academy/microbit/blog/2017/10/02/weekend-halloween-project-illuminated-candy-bucket-featuring-bbc-microbit)_

![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-464797/1473-900/IMG_2103.jpg)

Many of you who have been following me over the years knows that Halloween is my favorite holiday of the year, and that I always build a project or two for Element14. This year I decided to mix things up a little bit and build two separate projects. For this first project I wanted to do something simple that a family could sit down and put together over the course of a weekend. As you can imagine, that presented a challenge in that this project had to be quick and simple, yet challenging enough to help teach all parties involved a thing or two about embedded electronics.

I came up with a few ideas, and after talking it over with the team here at Element14, it was decided that I would build an illuminated candy bucket that parents could build with their children within a Saturday, or Sunday if needed. So you know what that means right? NeoPixels! Yes, for the third year in a row, I am incorporating my favorite lighting components into a halloween project. Now that I had a concept, I needed to figure out which child-friendly development board I would use to breath life into the NeoPixels. The Arduino Uno was my obvious first choice, but then I realized that this was the perfect opportunity to build something with the BBC Micro:bit. (If you would like to learn more about the Micro:bit, click here.) With the plan coming together I put in a request for the hardware, and a few days later I had a few Micro:bit's on my doorstep, and I was able to begin work on the project.

## The Parts

Before I get started with the tutorial let's take a moment to look at the hardware, software, and tools that we will need to complete this project. Items that can be purchased at Element14 / Newark.com have been linked to for your convenience.

### **Hardware**

### Software

### Tools

      * E6000 Hobby Glue (_Sourced Locally. It is important to use this brand or a generic equivalent for a good bond._)
      * 80-grit Sandpaper (_Sourced Locally_)
      * Velcro Dots (_Sourced Locally_)

## Building The Hardware

![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462780/1350-900/IMG_2011.jpg)

To get started we need to cut the NeoPixel strip into smaller pieces so that they will better conform to the candy buckets concave inner surface. I chose four strips that were six pixels long each, but after building the project, I feel like five strips of five pixels each would have provided a more circular pattern inside the candy bucket. In the end I will leave this decision up to you, but remember that if you do five strips of five pixels each, you will need to cut an extra piece of connecting wire to accommodate the extra strip.

![Neopixel Strips](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462782/1350-900/IMG_2087.jpg)

Some people like to use razor blades, or x-acto knives to cut these strips, but I find it much easier, and a lot quicker to just use a pair of scissors. Cutting thin soft copper with a good pair of scissors will do no damage to the scissors, and you will thank yourself with the time you save if you have to cut a bunch of these. If you have not worked with NeoPixels before, you can cut the strip at each of the exposed copper pads like in the image above. Simply cut along the black line, or in the middle of the pads. The idea is to leave enough room on both sides of the new strip to solder wires too.

![Cut Neopixel Strips, Wire, and Flush Cutters](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462783/1344-899/IMG_2016.jpg)

With the strips cut, I measured the circumference of the inside top of the bucket. This was a bit complicated as the buckets surface is a compound curve, and I did not know what would be the best location for the leds to be placed. After a few different measurements I settled on 19-inches. 25-inches would give me a complete wrap, but I was unsure at how much bend I would have once the new LED strip has been assembled, so I felt that 19-inches would be enough to give me good light coverage inside of the bucket, while not risking any overlap of LEDs. With this little issue solved, I cut three pieces of three-conductor ribbon cable one-inch long and stripped back the ends. When soldered together, this would give me a total length of about 19-inches.

![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462784/1350-900/IMG_2023.jpg)

![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462785/381-254/IMG_2019.jpg)

![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462786/381-254/IMG_2025.jpg)

Something I always like to promote in my projects that involve soldering is the use of flux. Many of the issues that beginner solderers find himself experiencing can be solved with this magical mystery fluid… Ok so, I know that it's not a magical mystery fluid, and is just a mild acid that cleans the oxide from the metals to be joined, which results in the solder flowing between, and bonding to the metals easier. I just like to think of it as black magic because it works so well. I like to use what is known as a flux pen. It works just like a permanent marker, with the user simply brushing on the flux. I also urge you to purchase quality solder from brands such as [Kester](https://www.element14.com/community/view-product.jspa?fsku=NULL&nsku=98H3732&COM=noscript), [Multicore](https://www.element14.com/community/view-product.jspa?fsku=9887148&nsku=93K2261&COM=noscript), and [Duratool](https://www.element14.com/community/view-product.jspa?fsku=2527484&nsku=20M4919&COM=noscript) (not lead free).

I also want to point out that you absolutely must use lead-free solder on this project as there is a possibility for your child's candy could come in contact with it during their trick-o-treating adventures. I used leaded solder because this candy bucket will not be used by anyone. I built it for the purpose of creating this tutorial.

![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462787/1350-900/IMG_2027.jpg)

I like to solder LED strips on a flat surface rather than in a helping hands device as it is easier to keep everything aligned properly using this method. Blue painters tape works wonders in ensuring that everything is flat and held firmly into place. It also helps (slightly) with preventing my project mat from burning from the heat. Remember to dab the copper pads with a generous amount of flux, as they have a thick oxidization layer on them from being exposed since being manufactured. Note that when soldering the strips together, you have to make sure that you solder the Data In (DI) pad to the Data Out (DO) pad. If you reverse this and solder two of the same pads together, the strips will not work.

![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462788/1350-900/IMG_2031.jpg)

Typically you do not want a balled profile of solder when creating a solder joint, but when soldering LED strips, it is almost impossible to avoid due to their oblong shape. It kind of forces the solder into a ball shape, even if the minimal amount of solder is used. As long as the joints are shiny and there is no sign of a pad lifting or anything, they will be perfectly fine for our purpose. Again, make sure that you solder the Data In (DI) pad to the Data Out (DO) pad.

![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462789/IMG_2032.jpg)

Well there we have it. The "lighting fixture" for our project is complete. At this point we need to add a wire to connect the strip to the BBC Micro:bit.

![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462790/1350-900/IMG_2033.jpg)

I used three 10-inch long lengths of red, black, and yellow solid core hookup wire that I twisted together using a cordless drill. The picture above is actually stranded hookup wire, and I realized my mistake shortly after taking this photo. You will see why it is important to use solid core wire in just a bit.

![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462791/1350-900/IMG_2037.jpg)

Using the same masking tape method as earlier I soldered the hookup wire to the NeoPixel strip making sure that the yellow wire was soldered to the Data In (DI) pad. When soldering thicker wire to these type of LED strips, it is easy to create a solder bridge, so be careful and don't be afraid to use a solder sucker or braid to remove excessive solder if needed.

![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462792/1354-900/IMG_2039.jpg)

Now we need to add a small amount of strain relief to this new connection. To do this I broke out my "_handy dandy box-o-heat-shrink"_ (I trademarked that name by the way). Heat shrink is something I find to be invaluable as a maker, and I use it on everything from wiring projects, to para-cord ends. You do not need a collection this big, but keeping [a small assortment](https://www.element14.com/community/view-product.jspa?fsku=NULL&nsku=32M2893&COM=noscript) on hand is a good idea if you like to tinker.

![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462793/537-358/IMG_2043.jpg)

![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462794/538-358/IMG_2045.jpg)

When building LED strips, I like to add a piece of heat shrink to the end to provide strain relief, and to protect the solder joints. To do this, I find a piece of heat-shrink that barely fits over the LED strip, and then will bend the wire in the direction I need right after I shrink the heat shrink tubing. Once cooled, this provides a decent strain relief, with minimal effort.

![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462795/1350-900/IMG_2047.jpg)

With the NeoPixel strips soldered together, we can begin attaching them to the BBC Micro:bit, and there is several methods on how to do this. The easiest is to twist a stripped section of the hookup wire through the four pin holes on the Micro:bit. The next easiest is to use alligator clips, but that method should be used for prototyping and lab use only. A permanent attachment method would be to solder the wires directly to the pin pads, but this ruins the edge connector functionality that makes the Micro:bit unique. Instead, I chose to use this nifty quick connect adapter I found on Thingiverse.com.

![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462796/2017-09-27-02_20_21-Start.jpg)

It's amazing how easy it is to develop and share ideas, designs, and almost anything else with anyone on the planet. After agonizing over how to connect the LED strips to the Micro:bit and still maintain the lowest profile possible, I stumbled across the [Micro:Bit Edge Connector by MiniSumo](https://www.element14.com/community/external-link.jspa?url=https%3A%2F%2Fwww.thingiverse.com%2Fthing%3A1719849) on Thingiverse.com. I understand that not everyone will have [a 3D printer](https://www.element14.com/community/view-product.jspa?fsku=2448730&nsku=82X7299&COM=noscript), but I do, and I wanted to try this out. If you do not have a printer, you could use any of the methods I mentioned above, and things would still work just fine.

![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462797/1350-900/IMG_2048.jpg)

I printed the connector at a layer height of 100 microns, with an average speed of 40mm/sec to get the best quality possible. Unfortunately, the current printer I have set up is a cheap I3 I built from a kit for a review I am writing for another website. This means that the print was a little sloppy because of the very low quality linear bearings, and just overall sloppy tolerances of all of the parts. If I would have used my Lulzbot Taz 4, or Prusa Research Prusa I3 MK2s, the print would have been much better, and I would have not had to drill out the holes. In the end, it worked well after a little cleanup of the locking button that fits through the Pin 2 hole on the Micro:bit.

Follow this schematic when wiring up your [NeoPixels](https://www.element14.com/community/view-product.jspa?fsku=&nsku=26Y8461&COM=noscript) to the Micro:bit. Most short runs of NeoPixels will work with 3V logic just fine, and in this case, it worked out perfect for us.

![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462798/2017-09-27+00_53_58-Start.png)

    * **NeoPixel**_Data In (DO) Pin_to_Pin 0 on_**Micro:bit**
    * **NeoPixel**_5V Pin_to 3V _Pin on_**Micro:bit**
    * **NeoPixel**_GND Pin_to_GND Pin on_**Micro:bit **
![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462799/1350-900/IMG_2049.jpg)

The way this connector works is that the solid core wires are stripped back about two inches, and each is fed into the big holes on the bottom of the connector. Having the stripped portions of these wires as straight as possible is a big help here.

![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462800/1350-900/IMG_2051.jpg)

Feeding the wires in from the top and looping them back up through the second hole locks them into place, and the stripped portion of the wire is fed through the hole in the little wall that locks the board into place. I found that wrapping the stripped wire over the end and crimping it there with a pair of plyers provided a better, more stable connection to the Micro:bit.

![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462801/1350-900/IMG_2054.jpg)

Here you can see how I looped them over the back, and then crimped with a pair of plyers. If your board is having a hard time locking into place after doing this, you may have to use a small file to file a slight groove into the plastic so that the wires can recess slightly.

![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462802/1350-900/IMG_2056.jpg)

Once I test that the board is powering the pixel strips, I add a small line of hot glue to lock the board to the plastic connector. This is not really needed if you are experimenting, but since candy will be tossed on top of this, and the bucket will be bouncing around all night, a little hot glue should prevent it from coming apart.

## The Program

![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462805/1600-686/2017-09-27+02_40_05-Rainbow+8+led+Neopixel+-+makecode.microbit.org.png)

Like I mentioned earlier, I want this project to be family friendly, especially for families with younger children who might show interest in tinkering with electronics and programming. With that goal in mind, I decided to program the Micro:bit using the [Micro:bit Blocks Editor By Microsoft](https://www.element14.com/community/external-link.jspa?url=https%3A%2F%2Fmakecode.Microbit.org%2F) which is an easy to use "_Click and Drag_" programming interface that makes programming less scary for those wanting to learn.

I also wanted to make the Illuminated Candy Bucket friendly for children who might be at risk of epileptic episodes due to flashing LEDs, so I wanted to program a static lighting effect in, as well as something that was a little interactive. So to figure out what I wanted to happen, I wrote some simple pseudo-code to help me get started. I wanted the program to do the following:

    * Upon power up display a static color pattern
    * Look for button Presses
      * If Button A is pressed
        * Display static color pattern
        * Display numeral 1 on onboard LED matrix
      * If Button B is pressed
        * Display an interactive lighting animation based on input from the built-in accelerometer.
        * Display numeral 2 on onboard LED matrix

With the pseudo-code written, I could easily translate that to the blocks editor. If you would like to see how I created the code, and learn what each of the blocks do, watch the video above. If you would like to look at the code for yourself, or to just upload it to your Micro:bit, I have shared the project on [makecode.Micro:bit.org](https://www.element14.com/community/external-link.jspa?url=https%3A%2F%2Fmakecode.microbit.org%2F_2Xkcw4XLP8i2). If you need a tutorial on how to use your BBC Micro:bit, head over to the [Micro:bit Website and follow their tutorial](https://www.element14.com/community/external-link.jspa?url=http%3A%2F%2FMicrobit.org%2F).

Alternatively you can paste the following JavaScript into the blocks editor when in JavaScript mode.

  1. strip.clear() 
  2. . . # . . 
  3. . . # . . 
  4. . # # # . 
  5. . # # # . 
  6. . # # # . 
  7. . # # # . 
  8. } 
  9. } 
![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462807/IMG_2057.jpg)

If you programmed your Micro:bit exactly as I did, or copied and uploaded the code I provided, then you should be able to power up the Micro:bit and see a static rainbow effect across the NeoPixel strip like above. If your pixels are dim, or not working, check the connection of the wires to the board. If everything is working correctly, you can now press button B and then move the Micro:bit around. The LEDs should randomly change colors and scroll down the line based on how hard you move the Micro:bit in 3 dimensions. The LED matrix on the Micro:bit should also be displaying the number 2. If you set the bucket down, the animation should stop, and the NeoPixels should all be the same color. Finally, if you press button A, the static rainbow pattern should return, and the number 1 will be displayed on the on board LED matrix. I tried to shoot video of the LED animation in the bucket several times, but issues arose with the LED's refresh rate, and my camera's frames per second settings, as well as the buckets mottling the animated light-show through its thick plastic shell. Basically what happens is the LEDs begin to change color and rotate when the bucket is in motion.

## Finishing up

![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462806/1350-900/IMG_2058.jpg)

Now is where thing get messy, or at least there is the potential for that to happen. Typical pumpkin shaped Halloween candy buckets are made out of a plastic called High-density polyethylene or HDPE for short. HDPE is an extremely flexible, yet rigid thermoplastic designed for the blow molding industry. It's the same plastic that milk jugs are made of, and most food-safe 5-gallon buckets. It has many advantages that make it an excellent manufacturing plastic, one of them being that almost nothing sticks to it. Without diving deep into the physics of why this happens, let me just tell you that I spent well over $70 trying to find the perfect glue to use to mount these LED strips to the bucket.

I tried every glue, epoxy, and glaze that I could find that claimed to bond ultra-slick surfaces like glass and polished metals. In the end, my trusty old friend, E6000, won the competition. I really wish I would have tried it from the start, but unfortunately I somehow had a lapse in brain activity and forgot all about it despite having more than five tubes laying around my office. Oh well, we can't win them all can we?

![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462808/1350-900/IMG_2009.jpg)

While E6000 is quickly proving itself to me as the stickiest substance on earth, even its physics defying magical powers are not enough to form a strong bond on plastic pumpkin skin, aka fresh HDPE. I found that heavily scoring the surface of the inside of the bucket with 80-grit sandpaper was the best way to ensure a strong bond. Even then, it is possible to pull the strips off.

![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462812/600-900/IMG_2010.jpg)

Here you can see the deep score marks I had to make to get the glue to stick well enough to keep the strips up under use. While I forgot to photograph it, you should also gently score the backside of the NeoPixel strips. Not heavy enough to remove any copper, but enough to scratch up the super slick solder mask that coast the strips. Failure to score the strips as well will cause delamination of the strips from the bucket walls.

![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462813/1350-900/IMG_2060.jpg)

After being super frustrated with failed attempts to glue the LED strips to the bucket, I forgot to take a photo of them being glued in using E6000. This is a terrible oversight on my part, but honestly it would have been pretty hard, if not impossible to get a decent shot of the process anyway. To break it down, I simply applied a medium sized bead of E6000 down the length of one strip, then used some spring clamps to hold that strip tight to the bucket wall. Then I did the next strip in line the same way. You can only do two strips at a time due to the limited working space inside the bucket. So at this point, it will take a couple of hours for the E6000 to cure enough to remove the clamps. Airflow will speed this process up some. Once dry, remove the clamps and glue up the second set of NeoPixel strips.

![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462814/1350-900/IMG_2062.jpg)

While the first set of strips is drying let's prepare the battery pack for mounting. If you are wondering where I got this battery pack from, it was from a big box store near the checkout registers for $5 each. Any USB power bank will work. I also picked up a pack of Velcro dots, to hopefully help secure things a bit better inside the bucket.

![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462815/1350-900/IMG_2066.jpg)

With the LED strips mounted and the glue dry, I placed 2 velcro dots onto the back of the USB battery pack, and added some E6000 to them so that I could place it in the bottom of the bucket. Only a little E600 is needed here. You do not want it squishing out and gluing the battery to the bucket.

![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462816/1350-900/IMG_2068.jpg)

With the velcro dots attached together and one side ready with glue, I pressed it into the bottom of the bucket, then weighed it down with a water bottle for a couple of hours.

![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462817/1350-900/IMG_2069.jpg)

Once the glue was dry I added a small dab of hot glue onto the 3D printed quick connector and pressed it down to the battery pack to stabilize the Micro:bit.

![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462818/1350-900/IMG_2080.jpg)

![](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-27407-462819/1350-900/IMG_2079.jpg)

Finally, I finished things up with a circle of craft foam to line the bottom and protect the electronics.

Well that is going to wrap up this project! I had fun building it, and I hope that you do as well. If you build this, I would love to see photos of it finished! Happy Halloween from myself and everyone else here at Element14!
