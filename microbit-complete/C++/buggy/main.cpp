#include "MicroBit.h"

MicroBit uBit;

// ***** Motor drver functions
//                    Pin0   Pin8   Pin12  Pin16
// Stopped          : 0      0      0      0
// Forwards Straight: 0      0      1      1
// Forwards & Left  : 0      0      1      0
// Forwards & Right : 0      0      0      1
// Reverse Straight : 1      1      0      0
// Reverse & Left   : 0      0      0      0
// Reverse & Right  : 0      0      0      0

int pin0, pin8, pin12, pin16 = 0;

// 0=stopped, 1=forwards, 2=backwards
int drive = 0;

void resetPinsValues() {
  pin0 = 0;
  pin8 = 0;
  pin12 = 0;
  pin16 = 0;    
}

void forwards() {
  pin0 = 0;
  pin8 = 0;
  pin12 = 1;
  pin16 = 1;
  drive = 1;
}

void backwards() {
  pin0 = 1;
  pin8 = 1;
  pin12 = 0;
  pin16 = 0;
  drive = 2;
}

void stop() {
  resetPinsValues();
  drive = 0;
}

void left() {
  resetPinsValues();
  if (drive == 1) {
      pin12 = 1;
      pin16 = 0;
  } else {
      pin0 = 0;
      pin8 = 1;
  }
}

void right () {
  resetPinsValues();
  if (drive == 1) {
      pin12 = 0;
      pin16 = 1;
  } else {
      pin0 = 1;
      pin8 = 0;
  }    
}

void writeToPins() {
  uBit.io.P0.setDigitalValue(pin0);
  uBit.io.P8.setDigitalValue(pin8);
  uBit.io.P12.setDigitalValue(pin12);
  uBit.io.P16.setDigitalValue(pin16);
}

//****** Bluetooth event handler functions
bool connected = false;

void onConnected(MicroBitEvent)
{
    uBit.display.print("C");
    connected = true;
}

void onDisconnected(MicroBitEvent)
{
    stop();
    writeToPins();
    uBit.display.print("D");
    connected = false;
}  

void onControllerEvent(MicroBitEvent e)
{
    
  // MES_DPAD_BUTTON_1_DOWN = right hand pad, up
  // MES_DPAD_BUTTON_2_DOWN = right hand pad, down
  // MES_DPAD_BUTTON_C_DOWN = left hand pad, left
  // MES_DPAD_BUTTON_D_DOWN = left hand pad, right
  if (e.value == MES_DPAD_BUTTON_1_DOWN) {
      forwards();
  } else if (e.value == MES_DPAD_BUTTON_1_UP || e.value == MES_DPAD_BUTTON_2_UP) {
      stop();
  } else if (e.value == MES_DPAD_BUTTON_2_DOWN) {
      backwards();
  }
 
  if (drive > 0) {
    if (e.value == MES_DPAD_BUTTON_C_DOWN) {
        left();
    } else {
        if (e.value == MES_DPAD_BUTTON_D_DOWN) {
            right();
        } else {
            if (e.value == MES_DPAD_BUTTON_C_UP || e.value == MES_DPAD_BUTTON_D_UP) {
                if (drive == 1) {
                    forwards();
                } else {
                    backwards();
                }
            }
        }
    }
  }
  writeToPins();  
}

int main()
{
    // Initialise the micro:bit runtime.
    uBit.init();
    // Display a start-up message
    uBit.display.scroll("BUGGY");
    
    // Application code will go here and in functions outside of main()
    uBit.messageBus.listen(MICROBIT_ID_BLE, MICROBIT_BLE_EVT_CONNECTED, onConnected);
    uBit.messageBus.listen(MICROBIT_ID_BLE, MICROBIT_BLE_EVT_DISCONNECTED, onDisconnected);     
    uBit.messageBus.listen(MES_DPAD_CONTROLLER_ID, 0, onControllerEvent); 

    // end of application code in main()    
    
    // If main exits, there may still be other fibers running or registered event handlers etc.
    // Simply release this fiber, which will mean we enter the scheduler. Worse case, we then
    // sit in the idle task forever, in a power efficient sleep.
    release_fiber();
}
