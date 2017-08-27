# Making the micro:bit accelerometer available over Bluetooth

_Captured: 2017-08-15 at 19:36 from [bluetooth-mdw.blogspot.de](http://bluetooth-mdw.blogspot.de/2017/04/making-microbit-accelerometer-available.html?m=1)_

Here's a very simple C/C++ application, created using the mbed web IDE.

The project was created in the mbed IDE with the following parameters:

Platform="BBC micro:bit", Template="An example of how to use the micro:bit DAL's abstract....." and Project Name=-"microbit-ble-accelerometer"

All it does is establish event handlers for Bluetooth connect and disconnect events and adds the Bluetooth accelerometer service so that an application like micro:bit Blue or Bitty Data Logger can receive accelerometer data over Bluetooth.

```
#include "MicroBit.h"  
MicroBit uBit;  
void onConnected(MicroBitEvent)  
{  
uBit.display.print("C");  
}  
void onDisconnected(MicroBitEvent)  
{  
uBit.display.print("D");  
}  
int main()  
{  
// Initialise the micro:bit runtime.  
uBit.init();  
// Insert your code here!  
uBit.display.scroll("X");

uBit.messageBus.listen(MICROBIT_ID_BLE, MICROBIT_BLE_EVT_CONNECTED, onConnected);  
uBit.messageBus.listen(MICROBIT_ID_BLE, MICROBIT_BLE_EVT_DISCONNECTED, onDisconnected);  
new MicroBitAccelerometerService(*uBit.ble, uBit.accelerometer);  
// If main exits, there may still be other fibers running or registered event handlers etc.  
// Simply release this fiber, which will mean we enter the scheduler. Worse case, we then  
// sit in the idle task forever, in a power efficient sleep.  
release_fiber();  
}
```

I also set MICROBIT_BLE_OPEN to 1 in microbit-dal/inc/core/MicroBitConfig.h so that pairing is not required. Much easier for testing purposes.

```
#define MICROBIT_BLE_OPEN 1
```

After compiling to produce a hex file, copy the hex file onto your micro:bit. An application like nRF Connect on a smartphone or tablet should see a Bluetooth service with UUID which starts 0xe95d0753-. This is the accelerometer service. Enabling notifications on the first characteristic (Accelerometer Data) will result in its value updating when you move the micro:bit.

The project has been published here:

<https://developer.mbed.org/users/bluetooth_mdw/code/microbit-dal-ble-accelerometer-example/>
