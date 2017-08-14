import processing.serial.*;

Serial myPort;        // The serial port
int xPos = 1;         // horizontal position of the graph 
//Variables to draw a continuous line.
int lastxPos=1;
int lastheight=0;
float inByte = 0;
void setup () {
  // set the window size:
  size(1024, 600);        
  // List all the available serial ports
  println(Serial.list());
  // Check the listed serial ports in your machine
  // and use the correct index number in Serial.list()[].
  // Here we assume the first in the list (nr 0) is our Microbit. This might be wrong!
  myPort = new Serial(this, Serial.list()[0], 115200);
  
  // A serialEvent() is generated when a newline character is received :
  myPort.bufferUntil('\n');
  
  // set the initial background color
  background(0);      // set inital background:
  
  // noLoop means it does not loop through draw() like normal
  // instead we wait for a serialEvent, and from there 
  // call redraw() which causes the draw() function to be run
  noLoop();
}

void draw () {
  stroke(127,34,255);     //stroke color
  strokeWeight(2);        //stroke width
  // draw a line from the previous point to the next
  line(lastxPos, lastheight, xPos, height - inByte);
  // save the new point as the new previous point
  lastxPos = xPos;
  lastheight = int(height-inByte);

  // at the edge of the window, go back to the beginning:
    if (xPos >= width) {
      xPos = 0;
      lastxPos= 0;
      background(0);  //Clear the screen.
    } 
    else {
      // increment the horizontal position:
      xPos++;
    }
}

int lf = 10;    // Linefeed in ASCII

// this function is called every time we receive a value over usb
void serialEvent (Serial myPort) {
  // Receive the string and remove the linefeed with trim()
  String input = trim(myPort.readStringUntil(lf));
  // Print the value to the console of processing
  // so we can see what we receive
  println(input);
  
  // cast the string to an integer
  int value = int(input);
  
  // Map the value to the screen height
  inByte = map(value, 0, 255, 0, height);
  // Make the draw() function run
  // We need to draw the graph inside the draw function for it to work
  redraw();
}
