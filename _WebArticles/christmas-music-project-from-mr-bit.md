# Christmas Music Project from Mr Bit

_Captured: 2017-12-10 at 14:45 from [www.insightresources.co.uk](http://www.insightresources.co.uk/page68.html)_

Make your micro:bit play a Christmas tune.

Mr Bit shows you how to take a tune from a music score and enter the notes into a program for the BBC micro:bit.

Whether loud or soft, fast or slow, sad or happy, a tune always has a series of notes, one after another. A note can be high or low in pitch or short or long in duration. To make music with your micro:bit all you have to do is to put notes in the right order and specify the pitch and duration of each note.

The notes on a music score show all that you need to know about pitch and duration.

Pitch is shown by the height of the note on the 5-line stave; with 5 lines and 4 spaces the stave can indicate 9 different notes. By adding floating notes above and below the stave you can increase this number. Each pitch has a letter as shown here.

Duration is shown by the style of the note and its stalk.

The most common note is the crotchet, a solid blob with a plain stalk. When a tune has a regular beat, this is the note that shows the beat. Most tunes have between 60 and 120 beats per minute making the duration of a crotchet typically between 1000 milliseconds and 500 milliseconds.

In our Christmas tune, as well as having crotchets, we have two other types of notes:

Quaver: this has half the duration of a crotchet, so 2 quavers last as long a one crotchet.

Minim: this has twice the duration of a crotchet, so 2 crotchets last as long a one minim.

The quaver looks like a crotchet with a tail.

The minim looks like a crotchet with a hole in the blob.

Scientific notation of pitch

Since the letters for notes are used in a repeating cycle, at several different pitches, we need an additional code to give a unique indication of pitch. Scientific notation does this by adding a number to indicate in which octave (sequence of 8 notes) the note occurs. C4 is middle C on a piano; C5 is an octave above; C3 is an octave below. The octave number increases by one every time you go from B to C. Insight Mr Bit uses this notation for pitch.

![](http://www.insightresources.co.uk/wpimages/wpe66d53e6_05_06.jpg)

That's enough explanation. Let's get started on our tune "We wish you a Merry Christmas"

Step 1 - Prepare the tune

To prepare for making our program, the first step is to write underneath the stave the letter name for each note:

Step 2 - Select the control blocks

We are now ready to build and program the control system:

The dialogue for coding the tune now appears.

Step 3 - Type the tune notation

When a different duration is needed, type the new note value.

When the note is F, type a sharp # as well.

Step 4 - Program button A to start and stop the music

The control program should read "When button A gets pressed, switch on the piezo sounder, until button A gets pressed again."

Step 5 - Prepare the micro:bit

To hear the tune, you need to connect an earpiece or headphones to pins GND and P0. You can use crocodile clip leads as shown here.

Step 6 - Select 'Control' mode

You are now ready to play the tune:

Taking it further

You can extend the control system to show a "Merry Christmas" message on the LEDs while the tune is playing:

![](http://www.insightresources.co.uk/wpimages/wp35ed7be4_05_06.jpg)

Mr Bit rule for duration: The next note will have the same duration, unless you choose a quaver (2 units) or a minim (8 units).

Mr Bit rule for pitch: The next note will have the same octave number, unless you choose the up (a) button or down (a) button.

![](http://www.insightresources.co.uk/wpimages/wp8582511c_06.png)
