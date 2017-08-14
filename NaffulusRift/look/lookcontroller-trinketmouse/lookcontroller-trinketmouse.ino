/**************************************************************************/
/*!
 * 
 * Based on ProTrinketMouseAccel.ino by Mike Barela, Adafruit Industries
 * (BSD License)
 * 
 * Modified by Jonathan Sanderson, Northumbria University
 * 
 * This version: 2016-06-03
*/
/**************************************************************************/
 
#include <ProTrinketMouse.h>    // Pro Trinket V-USB mouse emulator
#define  DEBUG  1               // Set to 1 for serial console debugging, 0 otherwise

const uint8_t LEFTBUTTON  = 8;  // Left Mouse Button on this Pro Trinket Pin
const uint8_t RIGHTBUTTON = 9;  // Right Mouse Button on Pro Trinket

const int X_INPUT = A1;
const int Y_INPUT = A0;
const int Z_INPUT = A2;

//Change these values if accelerometer reading are different:
//How far the accerometer is tilted before
//starting to move the mouse:
const int DEADZONE = 18;

//The average zero acceleration values read
//from the accelerometer for each axis:
//JJS: Found by inspection (I'm using a Kitronik accelerometer board, not the Adafruit one. Sorry)
const int ZeroXValue = 340;
const int ZeroYValue = 330;
const int ZeroZValue = 412;
 
//The maximum (positive) acceleration values read
//from the accelerometer for each axis:
// JJS: Again, found via inspection.
const int MaxXValue = 664;
const int MaxYValue = 664;
const int MaxZValue = 664;
 
//The minimum (negative) acceleration values read
//from the accelerometer for each axis:
// JJS: Again, found via inspection
const int MinXValue = 0;
const int MinYValue = 0;
const int MinZValue = 0;
 
//The sign of the mouse movement relative to the acceleration.
//If your cursor is going in the opposite direction you think it
//should go, change the sign for the appropriate axis.
const int XSign = 1;
const int YSign = -1;
const int ZSign = 1;
 
//The maximum speed in each axis (x and y)
//that the cursor should move. Set this to a higher or lower
//number if the cursor does not move fast enough or is too fast.
const int MaxMouseMovement = 150;  
 
//This reduces the 'twitchiness' of the cursor by calling
//a delay function at the end of the main loop.
//There are better way to do this without delaying the whole
//microcontroller, but that is left for another tutorial or project.
const int MouseDelay = 12;
  
void setup(void) {
#if DEBUG  
  Serial.begin(9600);
  Serial.println("Pro Trinket Accelerometer Mouse");
#endif
  
  TrinketMouse.begin();               // Initialize mouse library
  pinMode(LEFTBUTTON,  INPUT_PULLUP); // Left and right mouse button pins initialized
  pinMode(RIGHTBUTTON, INPUT_PULLUP); //   with internal pullup resistors (bring Low with button)
}
 
void loop() {
  
  int16_t x_val = analogRead(X_INPUT);
  int16_t y_val = analogRead(Y_INPUT);
  int16_t z_val = analogRead(Z_INPUT);

#if DEBUG
  Serial.print("X:\t"); Serial.print(x_val); 
  Serial.print("\tY:\t"); Serial.print(y_val); 
  Serial.print("\tZ:\t"); Serial.println(z_val); 
#endif
 
  processAccelerometer(x_val, y_val, z_val);  // Work with the read data
  
  delay(MouseDelay);  // wait until next reading - was 500 in Adafruit example
}
 
//Function to process the acclerometer data
//and send mouse movement information via USB
void processAccelerometer(int16_t XReading, int16_t YReading, int16_t ZReading)
{
  //Initialize values for the mouse cursor movement.
  int16_t MouseXMovement = 0;
  int16_t MouseYMovement = 0;
  
  //Calculate mouse movement
  //If the analog X reading is ouside of the zero threshold...
  if( DEADZONE < abs( XReading - ZeroXValue ) )
  {
    //...calculate X mouse movement based on how far the X acceleration is from its zero value.
    MouseXMovement = XSign * ( ( ( (float)( 2 * MaxMouseMovement ) / ( MaxXValue - MinXValue ) ) * ( XReading - MinXValue ) ) - MaxMouseMovement );
    //it could use some improvement, like making it trigonometric.
  }
  else
  {
    //Within the zero threshold, the cursor does not move in the X.
    MouseXMovement = 0;
  }
 
  //If the analog Y reading is ouside of the zero threshold... 
  if( DEADZONE < abs( YReading - ZeroYValue ) )
  {
    //...calculate Y mouse movement based on how far the Y acceleration is from its zero value.
    MouseYMovement = YSign * ( ( ( (float)( 2 * MaxMouseMovement ) / ( MaxYValue - MinYValue ) ) * ( YReading - MinYValue ) ) - MaxMouseMovement );
    //it could use some improvement, like making it trigonometric.
  }
  else
  {
    //Within the zero threshold, the cursor does not move in the Y.
    MouseYMovement = 0;
  }
 
  if(digitalRead(LEFTBUTTON) == LOW) {             // If left button pressed
#if DEBUG
    Serial.println("Left Mouse Button");
#endif
    TrinketMouse.move(0,0,0,MOUSEBTN_LEFT_MASK);   //  tell PC
  }
  else if (digitalRead(RIGHTBUTTON) == LOW) {      // If right button pressed
#if DEBUG
    Serial.println("Right Mouse Button");
#endif
    TrinketMouse.move(0,0,0,MOUSEBTN_RIGHT_MASK);  //  tell PC 
  }
  else {
    TrinketMouse.move(MouseXMovement, MouseYMovement, 0, 0);  // otherwise just move mouse
  }
 
}
