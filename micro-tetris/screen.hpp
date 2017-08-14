#ifndef SCREEN_HPP_INCLUDED
#define SCREEN_HPP_INCLUDED
#include "MicroBitDisplay.h"
#include <vector>
#include <string>

/*
Copyright Rafael 'rfthejakohead' Fernandes 2016

This file is part of micro:tetris.

micro:tetris is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

micro:tetris is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with micro:tetris.  If not, see <http://www.gnu.org/licenses/>.
*/

class Screen {
    vector < vector < unsigned char > > bufferData; // Pixels in screen
    MicroBitDisplay displayObj; // Display object
public:
    Screen(unsigned short width = 5, unsigned short height = 5, unsigned char clearState = 0) :
        bufferData(width, vector < unsigned char > (height, clearState))
    { }
    
    MicroBitImage getImage(unsigned short x = 0, unsigned short y = 0) {
        unsigned char tempBufferData[25],
                      n = 0;
        for(unsigned short yN = y; yN < y + 5; ++yN) {
            for(unsigned short xN = x; xN < x + 5; ++xN) {
                if((yN >= bufferData[0].size()) || (xN >= bufferData.size()))
                    tempBufferData[n++] = 0;
                else
                    tempBufferData[n++] = bufferData[xN][yN];
            }
        }
        return MicroBitImage(5, 5, tempBufferData);
    }
    
    void clear(unsigned char clearState = 0) {
        for(unsigned short x = 0; x < bufferData.size(); ++x) {
            for(unsigned short y = 0; y < bufferData[0].size(); ++y) {
                bufferData[x][y] = clearState;
            }
        }
    }
    
    void setPixel(unsigned char value, unsigned short x, unsigned short y) {
        bufferData[x][y] = value;
    }
    
    void setImage(unsigned char thisData[], unsigned short width = 5, unsigned short height = 5) {
        for(unsigned short y = 0; y < height; ++y) {
            for(unsigned short x = 0; x < width; ++x) {
                bufferData[x][y] = thisData[(y * width) + x];
            }
        }
    }
    
    void display(unsigned short xOffset = 0, unsigned short yOffset = 0) {
        displayObj.print(getImage(xOffset, yOffset));
    }
    
    MicroBitDisplay* getDisplay() {
        return &displayObj;
    }
};

#endif