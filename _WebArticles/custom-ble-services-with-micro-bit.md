# Custom BLE Services with Micro:bit

_Captured: 2017-08-12 at 10:37 from [www.hackster.io](https://www.hackster.io/pelikhan/custom-ble-services-with-micro-bit-6c9879)_

![Custom BLE Services with Micro:bit](https://hackster.imgix.net/uploads/attachments/288848/img_3070_kVoaR6hk78.PNG?auto=compress%2Cformat&w=900&h=675&fit=min)

The Micro:bit comes with a number of pre-defined Bluetooth low energy services. The services are implemented in [C++ in the Lancaster DAL](https://github.com/lancaster-university/microbit-dal/tree/master/source/bluetooth) and [wrapped into blocks in Microsoft MakeCode](https://github.com/Microsoft/pxt-microbit/blob/master/libs/bluetooth/bluetooth.cpp) (also known as PXT). Using the blocks (or JavaScript), the user can select to turn on various services and use Apps on his phone/computer to use them.

![](https://hackster.imgix.net/uploads/attachments/288459/microbit-screenshot_\(1\)_Ny05EDrGul.png?auto=compress%2Cformat&w=680&h=510&fit=max)

The built-in services have a pretty good coverage of the sensors, GPIO and other features of the Micro:bit. Of course, it not might not be enough and we'll show how to build, package and roll out your own custom BLE service for the Micro:bit.

The Lancaster DAL provides a reading of the [temperature on the nrf51 surface](https://lancaster-university.github.io/microbit-docs/ubit/thermometer/). It is a rough approximation of the ambient temperature that is okay for learning purposes. The [Bluetooth temperature service](https://lancaster-university.github.io/microbit-docs/ble/temperature-service/) exposes this sensor value.

Unfortunately, if we connected a better thermometer or any kind of device that measured temperature, we wouldn't be able to change the temperature provided by the BLE service. To fix this, **we will create ****[a slightly modified temperature service](https://github.com/Microsoft/pxt-bluetooth-temperature-sensor/)**** that allows to custom the sensor value.**

While MakeCode exposes blocks or JavaScript, it is possible to bundle a mix of C++, ASM and JavaScript to create packages.

In this case, we will do the BLE stuff in C++ and finish with a small layer of Blocks/JavaScript by providing 2 blocks: a block to register a callback, `bluetooth temperature sensor service` and a block to update the temperature, `bluetooth set temperature sensor value`.

![](https://hackster.imgix.net/uploads/attachments/288857/microbit-screenshot_\(2\)_AIGjoyAiof.png?auto=compress%2Cformat&w=680&h=510&fit=max)

> _A temperature service using a temperature probe as input_

Under the hood, these blocks will be driving our C++ BLE service.

To get started with a bundle package, run the following commands. It sets up the Micro:bit build environment, creates a new project and add C++ development files.
    
    
    pxt target microbit
    mkdir pxt-custom-ble
    cd pxt-custom-ble
    pxt init
    pxt add cpp
    pxt deploy
    

Since we are doing a clone of the temperature service, we can start from the Lancaster DAL implementation of the service: [.cpp](https://github.com/lancaster-university/microbit-dal/blob/master/source/bluetooth/MicroBitTemperatureService.cpp) / [.h](https://github.com/lancaster-university/microbit-dal/blob/master/inc/bluetooth/MicroBitTemperatureService.h) . A lot of the code is typical BLE boiler platter -- creating a service, characteristics, etc.

The difference with the original is a subtle: there is a member function `setTemperature` to update the data characteristic value and the service listens for a `MICROBIT_ID_SENSOR_TEMPERATURE` event to notify the BLE client that an update occurred
    
    
    #define MICROBIT_ID_SENSOR_TEMPERATURE 9500
       if (EventModel::defaultEventBus)
           EventModel::defaultEventBus->listen(MICROBIT_ID_SENSOR_TEMPERATURE, MICROBIT_THERMOMETER_EVT_UPDATE, this, &TemperatureSensorService::temperatureUpdate, MESSAGE_BUS_LISTENER_IMMEDIATE);
    void TemperatureSensorService::setTemperature(int value)  {
       temperatureDataCharacteristicBuffer = value;    
    }
    void TemperatureSensorService::temperatureUpdate(MicroBitEvent) {
       if (ble.getGapState().connected) {
           ble.gattServer().notify(temperatureDataCharacteristicHandle,
               (uint8_t *)&temperatureDataCharacteristicBuffer, 
               sizeof(temperatureDataCharacteristicBuffer));
       }
    }
    

The blocks are defined as C++ with [special annotations in the comments](https://makecode.com/defining-blocks) to specify how they should be rendered in the Block editor. In this case, `startTemperatureSensorService` takes a handler and spins up a fiber that polls that handler at the period specified by the BLE service.
    
    
       /**
       * Starts a custom sensor service. The handler must call ``setSensorTemperature`` 
       * to update the temperature sent to the service.
       */
       //% blockId=bluetooth_startTemperatureSensorService 
       //% block="bluetooth temperature sensor service"
       void startTemperatureSensorService(Action handler) {       
           if (NULL != _pService) return; // this block can only be called once...
           _pService = new TemperatureSensorService(*uBit.ble);
           _handler = handler;
           // increment ref counter
           pxt::incr(_handler);
           // spin a new fiber for the worker
           create_fiber(updateTemperature);
       }
       void updateTemperature() {
           // _pService is the BLE service singleton
           while (NULL != _pService) {
               // run action that updates the temperature
               pxt::runAction0(_handler);
               // raise event to trigger notification
               MicroBitEvent ev(MICROBIT_ID_SENSOR_TEMPERATURE, 
                  MICROBIT_THERMOMETER_EVT_UPDATE);
               // wait period
               fiber_sleep(_pService->getPeriod());            
           }
       } 
    

The `setTemperatureSensorValue` function updates the temperature value in the BLE characteristic.
    
    
       /**
       * Sets the current temperature value on the external temperature sensor
       */
       //% blockId=bluetooth_setTemperatureSensorValue 
       //% block="bluetooth set temperature sensor value (°C) %temperature"
       void setTemperatureSensorValue(int temperature) {
           if (NULL == _pService) return;
           _pService->setTemperature(temperature);
       } 
    

To test your service, you can use any kind of data available. For example, we can send the light level in the service to easily change the values and use [led.plotbargraph](http://led.plotbargraph/) to chart it on the screen as well.

![](https://hackster.imgix.net/uploads/attachments/288859/microbit-screenshot_\(5\)_44UTWvkxpM.png?auto=compress%2Cformat&w=680&h=510&fit=max)

> _Sending light level instead of temperature..._

Edit [tests.ts](http://tests.ts/) in your package and add the above test case:
    
    
    bluetooth.startTemperatureSensorService(() => { 
       bluetooth.setTemperatureSensorValue(input.lightLevel()) 
       led.plotBarGraph( 
           input.lightLevel(), 
           255 
       ) 
    }) 
    

Run `**pxt deploy**` to flash your Micro:bit.

![](https://hackster.imgix.net/uploads/attachments/288855/img_3071_i84h2wfpPU.JPG?auto=compress%2Cformat&w=680&h=510&fit=max)

> _The Micro:bit displaying the light level on the screen._

On iOS or Android, you can use any BLE diagnostic tool or the [Bitty Data Logger](http://www.bittysoftware.com/apps/bitty_data_logger.html) that conveniently chats the temperature readings.

![](https://hackster.imgix.net/uploads/attachments/288852/img_3070_AUkiCtSQfW.PNG?auto=compress%2Cformat&w=680&h=510&fit=max)

> _Bitty data logger app charting light readings_

You can push your package to GitHub to make it available to other users. Simply run `**pxt bump**` to take care of reving the package version and creating a release for it. Don't forget to beef up your [README.md](http://readme.md/) file with examples ([Learn more about packages)](https://pxt.microbit.org/packages).
