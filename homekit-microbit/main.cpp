#include "MicroBit.h"
MicroBit uBit;

int a = 0;
const int heart_w = 10; 
const int heart_h = 5; 
const uint8_t heart[] = { 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, }; 
#define EVENT_ID    8888

// struct for the data
struct DATA_STRUCT {
    char c;
};
struct DATA_STRUCT data;


void onConnected(MicroBitEvent) {
  //uBit.display.print("C");
}

 
void onDisconnected(MicroBitEvent){
  //uBit.display.print("D");
}

void onButtonA(MicroBitEvent e) {
   MicroBitEvent evt(EVENT_ID, 18);
   uBit.display.scroll("x");
}


void showHeart() {
    while (1) {
        if (data.c == 'B') {
            MicroBitImage i(heart_w,heart_h,heart); 
            uBit.display.animate(i,100,5); 
            uBit.sleep(50); 
        }

        uBit.sleep(500);    
    }
}


void onControllerEvent(MicroBitEvent e) {
  //uBit.display.print(e.value);
  if(e.value == 1) {
    data.c = 'B';
  }

  if(e.value == 2)
    data.c = 'A';
}

int main() {
    uBit.init();
    uBit.display.scroll("DC");

    data.c = 'A';
    create_fiber(showHeart);

    new MicroBitLEDService(*uBit.ble, uBit.display);
    new MicroBitAccelerometerService(*uBit.ble, uBit.accelerometer);
    new MicroBitButtonService(*uBit.ble);
    new MicroBitIOPinService(*uBit.ble, uBit.io);
    //new MicroBitMagnetometerService(*uBit.ble, uBit.compass); 
    new MicroBitTemperatureService(*uBit.ble, uBit.thermometer);
    

    uBit.messageBus.listen(MICROBIT_ID_BLE, MICROBIT_BLE_EVT_CONNECTED, onConnected);
    uBit.messageBus.listen(MICROBIT_ID_BLE, MICROBIT_BLE_EVT_DISCONNECTED, onDisconnected);
    uBit.messageBus.listen(MICROBIT_ID_BUTTON_A, MICROBIT_BUTTON_EVT_CLICK, onButtonA);
    uBit.messageBus.listen(EVENT_ID, MICROBIT_EVT_ANY, onControllerEvent);

    release_fiber();
}