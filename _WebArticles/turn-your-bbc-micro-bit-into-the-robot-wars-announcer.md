# Turn your BBC micro:bit into the Robot Wars announcer

_Captured: 2017-09-03 at 13:07 from [www.microbit.co.uk](https://www.microbit.co.uk/robot-wars/announcer)_

![A crowd cheering in the Robot Wars arena](https://az742082.vo.msecnd.net/pub/lnigtxjm)

Fans of Robot Wars both new and old recognise that deep booming voice of the arena announcer.

Whether its introducing a team of roboteers, starting the match or calling "Cease!", the voice is a key part of Robot Wars. Things wouldn't feel the same without it!

In this activity, we're going to show you how to turn your BBC micro:bit into the arena announcer, thanks to a fun new addition to the Python Editor: A speech synthesiser!

## What is a Speech Synthesiser?

When we speak, the sounds we make are controlled by different parts of our mouths - how open the mouth is, where the tongue is, the force of the air from our lungs and more.

Computers (obviously) don't have mouths but instead mimic the different frequencies of sound our mouths make.

Speech synthesisers aren't always perfect - while it can read the words you type out loud, if it chooses the wrong sounds the end result could be pretty strange. On the other hand, clever control of a synthesiser can create all sorts of cool and unique voices!

## Using the Mu Editor

For this activity we'll be using Python - but we won't be using the online Python Editor this time. The speech synthesiser is part of a program called Mu Editor, developed by Nicholas Tollervey. He's a friend of ours at Team BBC micro:bit, and wrote the [super-useful MicroPython micro:bit guide](http://microbit-micropython.readthedocs.io/en/latest/index.html)!

Mu Editor is a downloadable program. It will run on most computers and is available from [our Software Tools page](https://www.microbit.co.uk/software-tools).

## Step 1: Getting the voice right

In this project we're going to have our micro:bit say two iconic Robot Wars phrases: "Three, two, one... Activate!" when the A button is pressed and "Cease!"when the B button is pressed.

![](https://az742082.vo.msecnd.net/pub/ldbpqjed)

There are a few different commands we can use to get the micro:bit talking:

  * speech.say() - Your micro:bit will say the string inside the brackets. The synthesiser has been designed to use English pronunciations, but it's not quite perfect.
  * speech.pronounce() - Similar to speech.say, your micro:bit will read the string inside the brackets, but instead of looking for specific voice sounds or 'Phonemes'. There's [a full list of phonemes](http://microbit-micropython.readthedocs.io/en/latest/speech.html#phonemes) that the micro:bit can understand on the Python Guide.

There's also a 'sing' command - but that's not quite what we need here.

We can actually get our micro:bit to speak straight away with next to no fiddling:

![](https://az742082.vo.msecnd.net/pub/ncfyjnxs)

However, if you flash this to your micro:bit and play it, you'll find that it sounds very different the show announcer.

That's because we are using the default voice type. In addition to telling the micro:bit what to say, we can also dictate _how_ it's said. There are four settings we can use to change the 'timbre' of the voice:

  * Speed: How fast or how slow the speech is.
  * Pitch: How high and squeaky or low and croaky the voice is.
  * Throat: How relaxed or tense the voice sounds.
  * Mouth: Whether the voice is mumbling or pronouncing everything clearly

Would say "Hello" very quickly, in a low voice, with a not very tense voice and very clear pronunciation.

Have a go at experimenting with these values and how they sound when played back on your micro:bit. The announcer on Robot Wars has a deep and clear voice, so what would be the best setting combination for that?

## Step 2: Pronunciation lessons

Now we have a tone of voice we like, we can try out using either speech.say or speech.pronounce.

We can look at the [Speech module's Phonemes chart](http://microbit-micropython.readthedocs.io/en/latest/speech.html#phonemes) to build up the words we want the micro:bit to say. You can even use the same phoneme more than once in a row to make the sound 'longer'.

![](https://az742082.vo.msecnd.net/pub/lhclatkm)

Here I've got "Three, Two, One... Activate!" and "Cease!" both 'said' and 'pronounced'. Try out these arrangements and see how they sound to you. You might notice that the micro:bit struggles a little to say 'cease' by itself!

## Step 3: Push the button

We want our micro:bit to only start speaking once we press the A or B buttons, so lets put our new speech phrases inside if statements.

![](https://az742082.vo.msecnd.net/pub/nucgpbes)

And that's all we need! Flash your script over to your micro:bit and try the finished version of your script out. When you've made your own version, try out [our version of the Robot Wars announcer](https://microbit0.blob.core.windows.net/pub/dhfenwvt/Robot-Wars-Announcer.hex) and see how they compare!

## Taking it further

Feel like you're getting the hang of the speech module? Why not try these mini-challenges:

  * Change up the voice style to something totally different! Can you make the announcer sound younger and more excited?
  * Can you put in a countdown on the LEDs to match the spoken countdown? Tou may need to split up the speech into smaller chunks and hange the LEDs after each part.
