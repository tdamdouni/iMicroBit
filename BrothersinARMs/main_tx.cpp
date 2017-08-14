/*
The MIT License (MIT)

Copyright (c) 2016 British Broadcasting Corporation.
This software is provided by Lancaster University by arrangement with the BBC.

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
*/

#include "MicroBit.h"

MicroBit uBit;

//
// Print details of all events received to the serial port.
// Default settings are 115200 baud, 8N1 over the USB interface.
//



uint8_t mode;
uint8_t last_mode;
//all the available images
static const uint8_t img0[] __attribute__ ((aligned (4))) = {0xff, 0xff, 5, 0, 5, 0, 
     0,1,0,1,0,
     1,1,1,1,1, 
     1,1,1,1,1,
     0,1,1,1,0,
     0,0,1,0,0};
MicroBitImage i0((ImageData*)(void*)img0);


static const uint8_t img1[] __attribute__ ((aligned (4))) = {0xff, 0xff, 5, 0, 5, 0,
	0,1,1,1,0,
    1,0,1,0,1,
    1,1,1,1,1,
    1,1,1,1,1,
    1,0,1,0,1};
MicroBitImage i1((ImageData*)(void*)img1);


static const uint8_t img2[] __attribute__ ((aligned (4))) = { 0xff, 0xff, 5, 0, 5, 0,
	0,0,0,0,0,
    0,1,0,1,0,
    0,0,0,0,0,
    0,1,1,1,0,
    0,1,0,1,0};
MicroBitImage i2((ImageData*)(void*)img2);


static const uint8_t img3[] __attribute__ ((aligned (4))) = { 0xff, 0xff, 5, 0, 5, 0,
    0,0,1,0,0,
    0,1,1,1,0,
    0,0,1,0,0,
    1,1,1,1,1,
    0,1,0,1,0};
MicroBitImage i3((ImageData*)(void*)img3);



#define MAX_IMG 3
#define ARR_LEN 31
#define HIGH_VOL 100
#define LOW_VOL 20

void send_image(const uint8_t * data);

MicroBitPin speaker(MICROBIT_ID_IO_P0, MICROBIT_PIN_P0, PIN_CAPABILITY_ALL);//initialise P0 as an output
void onButton(MicroBitEvent e)
{
    if (e.source == MICROBIT_ID_BUTTON_A){//If button A is pressed change to previous image
        if(mode == 0)
            mode = MAX_IMG;
        else
            mode--;
    }
    else if (e.source == MICROBIT_ID_BUTTON_B){//If button B is pressed change to next image
        if(mode >= MAX_IMG)
            mode = 0;
        else
            mode++;
    }
    else if (e.source == MICROBIT_ID_BUTTON_AB){//If both are pressed send the image

        switch(mode){
            case 0:
                send_image(img0);
                break;
            case 1:
                send_image(img1);
                break;
            case 2:
                send_image(img2);
                break;
            case 3:
                send_image(img3);
                break;
            default:
                send_image(img0);
                break;
        };
    }

}
void send_image(const uint8_t * data)
{
	speaker.setDigitalValue(1);//Initialise the transmission with a high bit
    uBit.sleep(300);//300ms of sound
    speaker.setDigitalValue(0);
    uBit.sleep(450);//450ms quite, overall 750ms for each bit
    for( int i = 6 ; i < ARR_LEN ; i++ )
    {
        if(data[i] == 1)//if the data in the image is 1
            speaker.setDigitalValue(1);//send a high volume sound
        else
            speaker.setAnalogValue(LOW_VOL);//else send a low volume sound
        uBit.sleep(300);
        speaker.setAnalogValue(0);
        uBit.sleep(450);//750ms delay in total
    }
}


int main()
{
    mode = 0;
    uBit.init();//initialise the Micro:bit

    uBit.messageBus.listen(MICROBIT_ID_BUTTON_A, MICROBIT_BUTTON_EVT_CLICK, onButton);//Signal if Button A is pressed
    uBit.messageBus.listen(MICROBIT_ID_BUTTON_B, MICROBIT_BUTTON_EVT_CLICK, onButton);//Signal if Button B is pressed
    uBit.messageBus.listen(MICROBIT_ID_BUTTON_AB, MICROBIT_BUTTON_EVT_CLICK, onButton);//Signal if both Buttons are pressed

     
    while (1){
        switch(mode){//Display the pictures
            case 0:
                uBit.display.print(i0);
                break;
            case 1:
                uBit.display.print(i1);
                break;
            case 2:
                uBit.display.print(i2);
                break;
            case 3:
                uBit.display.print(i3);
                break;
            default:
                uBit.display.print(i0);
                break;
        };
       
        uBit.sleep(100);//Wait 100ms
    }
}

