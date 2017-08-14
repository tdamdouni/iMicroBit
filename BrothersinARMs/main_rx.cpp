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

#define ARR_LEN 25
#define THRESHOLD 100

uint8_t kostas;
uint8_t last_mode;

MicroBitPin P0(MICROBIT_ID_IO_P0, MICROBIT_PIN_P0, PIN_CAPABILITY_ANALOG);
//initialise P0 as an ADC


MicroBitImage img(5,5);


void receive_image()
{
	uint16_t count;
	uint8_t x,y;
	uBit.sleep(500);//250ms delay before branching + 500ms =750ms
	
    for( int i = 0 ; i < ARR_LEN ; i++ )
    {
		x = i%5;//change directions in the matrix every 1 step change x
		y = i/5;//every 5 
		for(int i=0;i<5;i++)
		{
			kostas=P0.getAnalogValue();//read for analog values
			count += kostas;//sum the values for 5 iterations
			uBit.sleep(50);//wait 50ms
		}//50 * 5 = 250ms delay
		if(count<700)//if the sum is lower than the threshold
			uBit.display.image.setPixelValue(x, y, 255);//set the bit to 1
		else
			uBit.display.image.setPixelValue(x, y, 0);//else set the bit to 0
		count = 0;//reset count
		uBit.sleep(500);//250 + 500 = 750ms delay per bit
    }
}


int main()
{


    uBit.init();
	uint16_t count=0;

    while(1){
		kostas=P0.getAnalogValue();//read for analog values
		if(kostas<200)//if the value is low
		{
		for(int i=0;i<5;i++)//check if it is a 1
		{
			count += kostas;
			uBit.sleep(50);
			kostas=P0.getAnalogValue();
		}
		if(count<700)//if it is a 1
			receive_image();//receive the image
		
		count = 0;//reset count
		}
	}
}

