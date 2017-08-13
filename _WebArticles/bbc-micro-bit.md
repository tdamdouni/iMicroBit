# BBC micro:bit

_Captured: 2017-08-08 at 17:28 from [bluetooth-mdw.blogspot.de](http://bluetooth-mdw.blogspot.de/p/bbc-microbit.html?m=1)_

###  _Code it. Connect it. _

###  _[Bitty Software](http://www.bittysoftware.com/) \- mobile apps for micro:bit and free coding tutorials_

###  Table of Contents

  * [External Resources](http://bluetooth-mdw.blogspot.co.uk/p/bbc-microbit.html#external)

###  Documentation

###  Development Tools

###  Hex Files

Hex files are now located at the downloads page of the [Bitty Software](http://www.bittysoftware.com/downloads.html) web site.

###  micro:bit Blue - The micro:bit Bluetooth demo app for Android

Most of the videos below feature an Android application I wrote to enable the testing and demonstration of the many Bluetooth capabilities which the BBC micro:bit has.

###  External Resources

###  Videos

![](https://1.bp.blogspot.com/-j58b_2MmExw/VtlezkQy0gI/AAAAAAAACpY/PxQWDMCgv-E/s280/hrm_zones.jpg)

![](https://1.bp.blogspot.com/-8bhLQMqiko8/VtlgE02f1dI/AAAAAAAACpk/HHi7BR-9xlg/s280/microbit_hrm_zones.jpg)

> _micro:bit Bluetooth heart rate zone monitor_
    
    
    #include "MicroBit.h" /* * Temperature Alarm * Uses the Bluetooth Event Service to inform registered clients whenever the temperature falls below xx or rises above yy */ MicroBit uBit; uint16_t state = 0; // 0=ok, 1=alarming because it's cold, 2=alarming because it's hot uint16_t ok = 0; uint16_t any = 0; uint16_t temp_alarm = 9000; uint16_t set_lower = 9001; uint16_t set_upper = 9002; uint16_t cold = 1; uint16_t hot = 2; uint8_t upper = 24; uint8_t lower = 19; int reading_count = 0; void onSetLower(MicroBitEvent e) { lower = e.value; uBit.display.scroll("L="); uBit.display.scrollAsync(lower); } void onSetUpper(MicroBitEvent e) { upper = e.value; uBit.display.scroll("U="); uBit.display.scrollAsync(upper); } void onTemperatureReading(MicroBitEvent e) { int temperature = uBit.thermometer.getTemperature(); reading_count++; if (reading_count == 10) { uBit.display.scrollAsync(temperature); reading_count = 0; } if (temperature > upper && state == ok) { MicroBitEvent evt(temp_alarm, hot); state = hot; return; } if (temperature < lower && state == ok) { MicroBitEvent evt(temp_alarm, cold); state = cold; return; } if (temperature >= lower && temperature <= upper && state != ok) { MicroBitEvent evt(temp_alarm, ok); state = ok; } } void app_main() { uBit.display.scrollAsync("TEMP ALARM"); new MicroBitTemperatureService(*uBit.ble, uBit.thermometer); // listen for client events which set the upper and lower temperature limits uBit.MessageBus.listen(set_lower, any, onSetLower); uBit.MessageBus.listen(set_upper, any, onSetUpper); // listen to the temperature sensor uBit.MessageBus.listen(MICROBIT_ID_THERMOMETER, MICROBIT_THERMOMETER_EVT_UPDATE, onTemperatureReading); } 

Kitronik sell a [nice buggy kit](https://www.kitronik.co.uk/blog/bbc-microbit-line-following-buggy/) which is designed to follow lines on the ground. I reprogrammed it to respond to event messages delivered over Bluetooth from a smartphone application using the Bluetooth Event Service so I could remote control it.
    
    
    /* /* The MIT License (MIT) Copyright (c) 2016 British Broadcasting Corporation. This software is provided by Lancaster University by arrangement with the BBC. Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. */ #include "MicroBit.h" MicroBit uBit; int pin0, pin8, pin12, pin16 = 0; int drive = 0; void onConnected(MicroBitEvent e) { uBit.display.print("C"); } void onDisconnected(MicroBitEvent e) { uBit.display.scroll("D"); } void onControllerEvent(MicroBitEvent e) { uBit.serial.printf("event %d\n",e.value); if (e.value == MES_DPAD_BUTTON_1_DOWN) { pin12 = 1; pin16 = 1; drive = 1; } else { if (e.value == MES_DPAD_BUTTON_1_UP) { uBit.serial.printf("2\n"); pin12 = 0; pin16 = 0; drive = 0; } } if (drive == 1) { if (e.value == MES_DPAD_BUTTON_C_DOWN) { uBit.serial.printf("3\n"); pin12 = 1; pin16 = 0; } else { if (e.value == MES_DPAD_BUTTON_D_DOWN) { uBit.serial.printf("4\n"); pin12 = 0; pin16 = 1; } else { if (e.value == MES_DPAD_BUTTON_C_UP || e.value == MES_DPAD_BUTTON_D_UP) { uBit.serial.printf("5\n"); pin12 = 1; pin16 = 1; } else { uBit.serial.printf("6\n"); } } } } uBit.io.P0.setDigitalValue(pin0); uBit.io.P8.setDigitalValue(pin8); uBit.io.P12.setDigitalValue(pin12); uBit.io.P16.setDigitalValue(pin16); } int main() { // Initialise the micro:bit runtime. uBit.init(); uBit.display.scroll("BUGGY!"); uBit.messageBus.listen(MES_DPAD_CONTROLLER_ID, 0, onControllerEvent); uBit.messageBus.listen(MICROBIT_ID_BLE, MICROBIT_BLE_EVT_CONNECTED, onConnected); uBit.messageBus.listen(MICROBIT_ID_BLE, MICROBIT_BLE_EVT_DISCONNECTED, onDisconnected); // If main exits, there may still be other fibers running or registered event handlers etc. // Simply release this fiber, which will mean we enter the scheduler. Worse case, we then // sit in the idle task forever, in a power efficient sleep. release_fiber(); } 

![](https://2.bp.blogspot.com/-IWX6I-U1FTQ/V5s80SVqcII/AAAAAAAAEOQ/J_EtelvBIaUitJ0B6kvEB1SUIxOTqTjWwCLcB/s280/buggy_controller_pxt_blocks.png)

###  and the corresponding JavaScript:
    
    
    let pin0 = 0; let pin8 = 0; let pin12 = 0; let pin16 = 0; let drive = 0; basic.showString("ROBOT WARS!"); bluetooth.onBluetoothConnected(() => { basic.showString("C"); }); bluetooth.onBluetoothDisconnected(() => { basic.showString("D"); }); control.onEvent(control.eventSourceId(EventBusSource.MES_DPAD_CONTROLLER_ID), control.eventValueId(EventBusValue.MICROBIT_EVT_ANY), () => { if (control.eventValue() == control.eventValueId(EventBusValue.MES_DPAD_BUTTON_1_DOWN)) { pin12 = 1; pin16 = 1; drive = 1; } else if (control.eventValue() == control.eventValueId(EventBusValue.MES_DPAD_BUTTON_1_UP)) { pin12 = 0; pin16 = 0; drive = 0; } else { } if (drive == 1) { if (control.eventValue() == control.eventValueId(EventBusValue.MES_DPAD_BUTTON_C_DOWN)) { pin12 = 1; pin16 = 0; } else { if (control.eventValue() == control.eventValueId(EventBusValue.MES_DPAD_BUTTON_D_DOWN)) { pin12 = 0; pin16 = 1; } else { if (control.eventValue() == control.eventValueId(EventBusValue.MES_DPAD_BUTTON_C_UP) || control.eventValue() == control.eventValueId(EventBusValue.MES_DPAD_BUTTON_D_UP)) { pin12 = 1; pin16 = 1; } else { } } } } pins.digitalWritePin(DigitalPin.P0, pin0); pins.digitalWritePin(DigitalPin.P8, pin8); pins.digitalWritePin(DigitalPin.P12, pin12); pins.digitalWritePin(DigitalPin.P16, pin16); }); 

micro:bit contains a magnetometer or digital compass. The Bluetooth profile includes a service called the Magnetometer Service and this allows connected devices to obtain the compass bearing of the micro:bit and for it to be updated in real-time. Here's a demo.....
    
    
    /* #include "MicroBit.h" #include "MicroBitSamples.h" #ifdef MICROBIT_BLE_MAGNETOMETER MicroBit uBit; int main() { // Initialise the micro:bit runtime. uBit.init(); // Note GATT table size increased from default in MicroBitConfig.h // #define MICROBIT_SD_GATT_TABLE_SIZE 0x500 new MicroBitMagnetometerService(*uBit.ble, uBit.compass); uBit.display.scroll("MAGNETOMETER"); // If main exits, there may still be other fibers running or registered event handlers etc. // Simply release this fiber, which will mean we enter the scheduler. Worse case, we then // sit in the idle task forever, in a power efficient sleep. release_fiber(); } #endif 

micro:bit now has a Bluetooth UART service which emulates serial data comms over Bluetooth low energy. I used it to implement the classic two player guessing game Animal Vegetable or Mineral. Simples!
    
    
    #include "MicroBit.h" #include "MicroBitSamples.h" #include "MicroBitUARTService.h" #ifdef MICROBIT_UART MicroBit uBit; MicroBitUARTService *uart; int connected = 0; void onConnected(MicroBitEvent e) { uBit.display.scroll("C"); connected = 1; // my client will send ASCII strings terminated with the colon character ManagedString eom(":"); while(1) { ManagedString msg = uart->readUntil(eom); uBit.display.scroll(msg); } } void onDisconnected(MicroBitEvent e) { uBit.display.scroll("D"); connected = 0; } void onButtonA(MicroBitEvent e) { if (connected == 0) { uBit.display.scroll("NC"); return; } uart->send("YES"); uBit.display.scroll("YES"); } void onButtonB(MicroBitEvent e) { if (connected == 0) { uBit.display.scroll("NC"); return; } uart->send("NO"); uBit.display.scroll("NO"); } void onButtonAB(MicroBitEvent e) { if (connected == 0) { uBit.display.scroll("NC"); return; } uart->send("GOT IT!!"); uBit.display.scroll("GOT IT!!"); } /* Recommend disabling the DFU and Event services in MicroBitConfig.h since they are not needed here: #ifndef MICROBIT_BLE_DFU_SERVICE #define MICROBIT_BLE_DFU_SERVICE 0 #endif #ifndef MICROBIT_BLE_EVENT_SERVICE #define MICROBIT_BLE_EVENT_SERVICE 0 #endif */ int main() { // Initialise the micro:bit runtime. uBit.init(); uBit.messageBus.listen(MICROBIT_ID_BLE, MICROBIT_BLE_EVT_CONNECTED, onConnected); uBit.messageBus.listen(MICROBIT_ID_BLE, MICROBIT_BLE_EVT_DISCONNECTED, onDisconnected); uBit.messageBus.listen(MICROBIT_ID_BUTTON_A, MICROBIT_BUTTON_EVT_CLICK, onButtonA); uBit.messageBus.listen(MICROBIT_ID_BUTTON_B, MICROBIT_BUTTON_EVT_CLICK, onButtonB); uBit.messageBus.listen(MICROBIT_ID_BUTTON_AB, MICROBIT_BUTTON_EVT_CLICK, onButtonAB); // Note GATT table size increased from default in MicroBitConfig.h // #define MICROBIT_SD_GATT_TABLE_SIZE 0x500 uart = new MicroBitUARTService(*uBit.ble, 32, 32); uBit.display.scroll("AVM"); // If main exits, there may still be other fibers running or registered event handlers etc. // Simply release this fiber, which will mean we enter the scheduler. Worse case, we then // sit in the idle task forever, in a power efficient sleep. release_fiber(); } #endif 

The BBC micro:bit has a default Bluetooth profile which includes a range of "services". Access to the full set of extensive Bluetooth capabilities on the micro:bit is not currently available if you use the on-line code editors Blocks, Touch Develop or the one from Code Kingdom. No Bluetooth functionality is available from mico:python either. So if you want to exploit Bluetooth on your micro:bit beyond the small number of canned use cases supported by these code editors, it is recommended that you use ARM's mbed IDE. This video shows you how, explains the issues and the workarounds to those issues.
