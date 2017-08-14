# Eggdrop example
For this example you need two microbits and one computer. The first microbit will sense its acceleration on the X axis, and send these values over radio to the second microbit. This microbit will send the values on to the computer via a usb cable. The computer will run a Processing program that receives the values and shows them as a graph on your screen.

## What you need
- 2 microbits
- 1 battery pack for a microbit (optional, can be replaced with a usb cable)
- 1 micro usb cable
- 1 computer
  - Processing installed (see below)
  - Mu editor installed (optional) (see below)

## How to use
- Download the Mu editor from http://codewith.mu/
- Download and install Processing from https://processing.org/download/
- Connect the first microbit to your computer with the usb cable
- Open eggdrop-sender.py with the Mu editor and press **flash**
- Unplug the first microbit, and connect the second microbit
- Open eggdrop-receiver.py with the Mu edito and press **flash**
- Keep this microbit connected. It will show the letter **F** as long as it does not receive data from the first microbit
- Turn on the battery on the first microbit
  - If you do not have a batterypack you can power it with a second usb cable and a usb charger or usb battery
  - Now the F should dissapear from the second microbit
- Open eggdrop-graph.pde with Processing
  - It might tell you that the file needs to be inside a folder with the same name as the file, which it should do automatically
- Start the processing code by pressing the play button in the top left corner
  - If you get an error, it probably did not find your microbit. In the code [on line 17](https://github.com/tiigbg/microbit-examples/blob/master/eggdrop/eggdrop-graph.pde#L17) it is hardcoded to choose the first usb device it finds. Experiment with a higher number until it works.
- Now you should get a purple graph on the black window
  - There might be tiny gaps in the graph. That is because the code is not perfect.
  - Sometimes the graph might stop for a short moment. This means something went wrong with the radio transmission. This is a known bug.


## Credits
- The graph code is based on an example from Tom Igoe
