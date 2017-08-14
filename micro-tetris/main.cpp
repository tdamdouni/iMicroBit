#include "MicroBitI2C.h"
#include "MicroBitButton.h"
#include "MicroBitAccelerometer.h"
#include "screen.hpp"

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

namespace td { // Tetris data
    Screen screen(5, 16, 255);
    MicroBitI2C i2c(I2C_SDA0, I2C_SCL0);
    MicroBitButton buttonA(MICROBIT_PIN_BUTTON_A, MICROBIT_ID_BUTTON_A),
                   buttonB(MICROBIT_PIN_BUTTON_B, MICROBIT_ID_BUTTON_B);
    MicroBitAccelerometer accelerometer(i2c);
    bool blink = true,
         offset = 0,
         fastFall = false,
         restart = false;
    unsigned long long score = 0;
    short x = 1,
          y = 0;
    unsigned char thisPiece = 0, //Piece ids:
                  rotLeft = 1,   //l block 0 - 1
                  rotRight = 1;  //J block 2 - 5
                                 //L block 6 - 9
                                 //O block 10
                                 //S block 11 - 12
                                 //T block 13 - 16
                                 //Z block 17 - 18
    std::vector < std::vector < bool > > tiles(5, std::vector < bool >(16, false)),
                                         thisPieceTiles(4, std::vector < bool >(4, false));
}

unsigned char rnum(unsigned char min, unsigned char max) { // Generate random number within range
    return min + rand() % max;
}

void stylishClear() {
    for(unsigned char y = 0; y < 5; ++y) {
        for(unsigned char x = 0; x < 5; ++x) {
            td::screen.setPixel(255, x, y);
        }
        wait(0.1);
        td::screen.display();
    }
    for(unsigned char y = 0; y < 5; ++y) {
        for(unsigned char x = 0; x < 5; ++x) {
            td::screen.setPixel(0, x, y);
        }
        wait(0.1);
        td::screen.display();
    }
}

void burn() {
    unsigned char temp[150] = {0  , 0  , 0  , 0  , 0  ,0  , 0  , 0  , 0  , 0  ,0  , 0  , 255, 0  , 0  ,0  , 255, 10 , 255, 0  ,255, 10 , 0  , 10 , 255,10 , 0  , 0  , 0  , 10 ,
                               0  , 0  , 0  , 0  , 0  ,0  , 0  , 255, 0  , 0  ,0  , 255, 10 , 255, 0  ,255, 10 , 0  , 10 , 255,10 , 0  , 0  , 0  , 10 ,0  , 0  , 0  , 0  , 0  ,
                               0  , 0  , 255, 0  , 0  ,0  , 255, 10 , 255, 0  ,255, 10 , 0  , 10 , 255,10 , 0  , 0  , 0  , 10 ,0  , 0  , 0  , 0  , 0  ,0  , 0  , 0  , 0  , 0  ,
                               0  , 0  , 0  , 0  , 0  ,0  , 0  , 255, 0  , 0  ,0  , 255, 10 , 255, 0  ,255, 10 , 0  , 10 , 255,10 , 0  , 0  , 0  , 10 ,0  , 0  , 0  , 0  , 0  ,
                               0  , 0  , 0  , 0  , 0  ,0  , 0  , 0  , 0  , 0  ,0  , 0  , 255, 0  , 0  ,0  , 255, 10 , 255, 0  ,255, 10 , 0  , 10 , 255,10 , 0  , 0  , 0  , 1 };
    MicroBitImage burnAnim(30, 5, temp);
    td::screen.getDisplay()->animate(burnAnim, 100, 5);
}

void banner() {
    unsigned char temp[235] = {0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0,
                               1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
                               1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0,
                               1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0};
    MicroBitImage bannerAnim(47, 5, temp);
    td::screen.getDisplay()->animate(bannerAnim, 125, 1);
}

void laserFade(unsigned char toReplace[25]) {
    for(unsigned char y = 0; y < 5; ++y) {
        for(unsigned char x = 0; x < 5; ++x)
            td::screen.setPixel(255, x, y);
        td::screen.display();
        wait(0.1);
        for(unsigned char x = 0; x < 5; ++x)
            td::screen.setPixel(toReplace[(y * 5) + x], x, y);
    }
    td::screen.display();
}

void render() {
    for(unsigned char x = 0; x < 5; ++x) { // Render tiles
        for(unsigned char y = 0; y < 16; ++y) {
            td::screen.setPixel(td::tiles[x][y] * 255, x, y);
        }
    }
    for(unsigned char x = 0; x < 4; ++x) {
        for(unsigned char y = 0; y < 4; ++y) {
            if(td::thisPieceTiles[x][y])
                td::screen.setPixel(td::blink * 255, x + td::x, y + td::y);
        }
    }
}

void fillPieceTiles(bool value[16]) {
    for(unsigned int x = 0; x < 4; ++x) {
        for(unsigned int y = 0; y < 4; ++y) {
            td::thisPieceTiles[x][y] = value[(y * 4) + x];
        }
    }
}

void setPiece() {
    td::thisPieceTiles.clear();
    td::thisPieceTiles.resize(4, std::vector < bool >(4, false));
    switch(td::thisPiece) {
    case 0:
        {
        td::rotLeft = 1;
        td::offset = 1;
        bool tempArray[16] = {0, 0, 0, 0,
                              1, 1, 1, 1,
                              0, 0, 0, 0,
                              0, 0, 0, 0 };
        fillPieceTiles(tempArray);
        td::rotRight = 1;
        }
        break;
    case 1:
        {
        td::rotLeft = 0;
        td::offset = 0;
        bool tempArray[16] = {0, 1, 0, 0,
                              0, 1, 0, 0,
                              0, 1, 0, 0,
                              0, 1, 0, 0 };
        fillPieceTiles(tempArray);
        td::rotRight = 0;
        }
        break;
    case 2:
        {
        td::rotLeft = 5;
        td::offset = 0;
        bool tempArray[16] = {0, 1, 0, 0,
                              0, 1, 0, 0,
                              1, 1, 0, 0,
                              0, 0, 0, 0 };
        fillPieceTiles(tempArray);
        td::rotRight = 3;
        }
        break;
    case 3:
        {
        td::rotLeft = 2;
        td::offset = 0;
        bool tempArray[16] = {1, 0, 0, 0,
                              1, 1, 1, 0,
                              0, 0, 0, 0,
                              0, 0, 0, 0 };
        fillPieceTiles(tempArray);
        td::rotRight = 4;
        }
        break;
    case 4:
        {
        td::rotLeft = 3;
        td::offset = 0;
        bool tempArray[16] = {0, 1, 1, 0,
                              0, 1, 0, 0,
                              0, 1, 0, 0,
                              0, 0, 0, 0 };
        fillPieceTiles(tempArray);
        td::rotRight = 5;
        }
        break;
    case 5:
        {
        td::rotLeft = 4;
        td::offset = 1;
        bool tempArray[16] = {0, 0, 0, 0,
                              1, 1, 1, 0,
                              0, 0, 1, 0,
                              0, 0, 0, 0 };
        fillPieceTiles(tempArray);
        td::rotRight = 2;
        }
        break;
    case 6:
        {
        td::rotLeft = 9;
        td::offset = 0;
        bool tempArray[16] = {0, 1, 0, 0,
                              0, 1, 0, 0,
                              0, 1, 1, 0,
                              0, 0, 0, 0 };
        fillPieceTiles(tempArray);
        td::rotRight = 7;
        }
        break;
    case 7:
        {
        td::rotLeft = 6;
        td::offset = 1;
        bool tempArray[16] = {0, 0, 0, 0,
                              1, 1, 1, 0,
                              1, 0, 0, 0,
                              0, 0, 0, 0 };
        fillPieceTiles(tempArray);
        td::rotRight = 8;
        }
        break;
    case 8:
        {
        td::rotLeft = 7;
        td::offset = 0;
        bool tempArray[16] = {1, 1, 0, 0,
                              0, 1, 0, 0,
                              0, 1, 0, 0,
                              0, 0, 0, 0 };
        fillPieceTiles(tempArray);
        td::rotRight = 9;
        }
        break;
    case 9:
        {
        td::rotLeft = 8;
        td::offset = 0;
        bool tempArray[16] = {0, 0, 1, 0,
                              1, 1, 1, 0,
                              0, 0, 0, 0,
                              0, 0, 0, 0 };
        fillPieceTiles(tempArray);
        td::rotRight = 6;
        }
        break;
    case 10:
        {
        td::rotLeft = 10;
        td::offset = 0;
        bool tempArray[16] = {1, 1, 0, 0,
                              1, 1, 0, 0,
                              0, 0, 0, 0,
                              0, 0, 0, 0 };
        fillPieceTiles(tempArray);
        td::rotRight = 10;
        }
        break;
    case 11:
        {
        td::rotLeft = 12;
        td::offset = 0;
        bool tempArray[16] = {0, 1, 1, 0,
                              1, 1, 0, 0,
                              0, 0, 0, 0,
                              0, 0, 0, 0 };
        fillPieceTiles(tempArray);
        td::rotRight = 12;
        }
        break;
    case 12:
        {
        td::rotLeft = 11;
        td::offset = 0;
        bool tempArray[16] = {0, 1, 0, 0,
                              0, 1, 1, 0,
                              0, 0, 1, 0,
                              0, 0, 0, 0 };
        fillPieceTiles(tempArray);
        td::rotRight = 11;
        }
        break;
    case 13:
        {
        td::rotLeft = 16;
        td::offset = 1;
        bool tempArray[16] = {0, 0, 0, 0,
                              1, 1, 1, 0,
                              0, 1, 0, 0,
                              0, 0, 0, 0 };
        fillPieceTiles(tempArray);
        td::rotRight = 14;
        }
        break;
    case 14:
        {
        td::rotLeft = 13;
        td::offset = 0;
        bool tempArray[16] = {0, 1, 0, 0,
                              1, 1, 0, 0,
                              0, 1, 0, 0,
                              0, 0, 0, 0 };
        fillPieceTiles(tempArray);
        td::rotRight = 15;
        }
        break;
    case 15:
        {
        td::rotLeft = 14;
        td::offset = 0;
        bool tempArray[16] = {0, 1, 0, 0,
                              1, 1, 1, 0,
                              0, 0, 0, 0,
                              0, 0, 0, 0 };
        fillPieceTiles(tempArray);
        td::rotRight = 16;
        }
        break;
    case 16:
        {
        td::rotLeft = 15;
        td::offset = 0;
        bool tempArray[16] = {0, 1, 0, 0,
                              0, 1, 1, 0,
                              0, 1, 0, 0,
                              0, 0, 0, 0 };
        fillPieceTiles(tempArray);
        td::rotRight = 13;
        }
        break;
    case 17:
        {
        td::rotLeft = 18;
        td::offset = 0;
        bool tempArray[16] = {1, 1, 0, 0,
                              0, 1, 1, 0,
                              0, 0, 0, 0,
                              0, 0, 0, 0 };
        fillPieceTiles(tempArray);
        td::rotRight = 18;
        }
        break;
    case 18:
        {
        td::rotLeft = 17;
        td::offset = 0;
        bool tempArray[16] = {0, 0, 1, 0,
                              0, 1, 1, 0,
                              0, 1, 0, 0,
                              0, 0, 0, 0 };
        fillPieceTiles(tempArray);
        td::rotRight = 17;
        }
        break;
    }
}

void randomPiece(){
    switch(rnum(0, 6)) {
    case 0:
        td::thisPiece = 0;
        break;
    case 1:
        td::thisPiece = 2;
        break;
    case 2:
        td::thisPiece = 6;
        break;
    case 3:
        td::thisPiece = 10;
        break;
    case 4:
        td::thisPiece = 11;
        break;
    case 5:
        td::thisPiece = 13;
        break;
    case 6:
        td::thisPiece = 17;
        break;
    }
    setPiece();
}

void align() {
    for(short x = 0; x < 4; ++x) {
        for(short y = 0; y < 4; ++y) {
            while(td::thisPieceTiles[x][y] && (x + td::x < 0))
                ++td::x;
            while(td::thisPieceTiles[x][y] && (x + td::x > 4))
                --td::x;
        }
    }
}

bool collides(short x, short y) {
    for(short xN = 0; xN < 4; ++xN) {
        for(short yN = 0; yN < 4; ++yN) {
            if(yN + y < 0)
                continue;
            if(td::thisPieceTiles[xN][yN] && ((xN + x < 0) || (xN + x > 4) || (yN + y > 15) || td::tiles[xN + x][yN + y]))
                return true;
        }
    }
    return false;
}

void makeLines() {
    for(unsigned char y = 0, count = 0; y < 16; ++y, count = 0) {
        for(unsigned char x = 0; x < 5; ++x) {
            if(td::tiles[x][y])
                ++count;
            if(count == 5) {
                for(short y2 = y; y2 >= 0; --y2) {
                    for(unsigned char x2 = 0; x2 < 5; ++x2) {
                        if(y2 == 0)
                            td::tiles[x2][y2] = false;
                        else
                            td::tiles[x2][y2] = td::tiles[x2][y2 - 1];
                    }
                }
                td::score += 100;
            }
        }
    }
}

bool fall() {
    if(collides(td::x, td::y + 1)) {
        for(short x = 0; x < 4; ++x) {
            for(short y = 0; y < 4; ++y) {
                if(td::thisPieceTiles[x][y] && (y + td::y >= 0) && (y + td::y < 16) && (x + td::x >= 0) && (x + td::x < 5)) {
                    td::score += 10;
                    td::tiles[x + td::x][y + td::y] = true;
                }
            }
        }
        makeLines();
        randomPiece();
        td::x = 1;
        td::y = !td::offset;
        if(collides(1, td::y)) {
            burn();
            td::screen.getDisplay()->scroll("GAME OVER");
            while(true) {
                char numStr[20];
                itoa(td::score, numStr); //Gotta do the old way, because there isn't enough space to include streams
                td::screen.getDisplay()->scroll(numStr);
                if(td::buttonA.isPressed() || td::buttonB.isPressed())
                    break;
            }
            return true;
        }
    }
    else
        ++td::y;
    return false;
}

void moveLeft() {
    if(!collides((short)td::x - 1, td::y))
        --td::x;
}

void moveRight() {
    if(!collides(td::x + 1, td::y))
        ++td::x;
}

void rotateLeft() {
    td::thisPiece = td::rotLeft;
    setPiece();
    align();
    if(collides(td::x, td::y)) {
        td::thisPiece = td::rotRight;
        setPiece();
    }
}

void rotateRight() {
    td::thisPiece = td::rotRight;
    setPiece();
    align();
    if(collides(td::x, td::y)) {
        td::thisPiece = td::rotLeft;
        setPiece();
    }
}

int main() {
    if(td::accelerometer.configure() != MICROBIT_OK) {
        td::screen.getDisplay()->scroll("MICROBIT_I2C_ERROR");
        return 0;
    }
    {
        td::accelerometer.setRange(8);
        banner();
        td::screen.getDisplay()->setDisplayMode(DISPLAY_MODE_GREYSCALE);
        unsigned short seed = 0; //RNG seed is set by the frames passed while waiting for user to start the game.
                                 //This is used instead of time(NULL) because time in micro:bit is messed up.
        bool isB = false;
        while(true) {
            if(isB) {
                isB = false;
                unsigned char temp[25] = {255, 255, 0  , 0  , 0  ,
                                          255, 0  , 255, 0  , 0  ,
                                          255, 255, 0  , 0  , 255,
                                          255, 0  , 255, 0  , 0  ,
                                          255, 255, 0  , 0  , 0  };
                laserFade(temp);
            }
            else {
                isB = true;
                unsigned char temp[25] = {0  , 0  , 0  , 255, 0  ,
                                          0  , 0  , 255, 0  , 255,
                                          255, 0  , 255, 255, 255,
                                          0  , 0  , 255, 0  , 255,
                                          0  , 0  , 255, 0  , 255};
                laserFade(temp);
            }
            wait(0.5);
            td::screen.display();
            ++seed;
            if(td::buttonA.isPressed() || td::buttonB.isPressed()) {
                stylishClear();
                break;
            }
        }
        srand(seed);
        randomPiece();
    }
    
    unsigned char framesPerUpdate = 2, // 5 FPS. Updates every 2 frames = 2.5 UPS
                  fpuPassed = 0;
    while(true) {
        td::accelerometer.updateSample();
        td::blink = !td::blink;
        if(++fpuPassed == framesPerUpdate) {
            fpuPassed = 0;
            if(((td::accelerometer.getPitch() > 25)) && (td::accelerometer.getPitch() < 60)) //Back. Makes piece fall
                td::fastFall = true;
            if(((td::accelerometer.getRoll() > 25)) && (td::accelerometer.getRoll() < 60)) //Left. Moves block right
                moveRight();
            else if(((td::accelerometer.getRoll() < -25)) && (td::accelerometer.getRoll() > -60)) //Right. Moves block left
                moveLeft();
            
            if(td::buttonA.isPressed()) //A. Rotates block left
                rotateLeft();
            else if(td::buttonB.isPressed()) //B. Rotates block right
                rotateRight();
            for(unsigned char n = 0; n < 1 + td::fastFall; ++n) {
                if(fall()) {
                    td::restart = true;
                    break;
                }
            }
            td::fastFall = false;
            ++td::score;
        }
        if(!td::restart) {
            render();
            if(td::y <= 1)
                td::screen.display(0, 1);
            else if(td::y + 4 > 15)
                td::screen.display(0, 11);
            else
                td::screen.display(0, td::y - 1);
            wait(0.2); // Limit by 5 fps
        }
        else { //Clear data and restart game
            td::screen.clear();
            td::blink = true;
            td::offset = 0;
            td::fastFall = false;
            td::restart = false;
            td::score = 0;
            td::x = 1;
            td::y = 0;
            randomPiece();
            for(unsigned char x = 0; x < 5; ++x) {
                for(unsigned char y = 0; y < 16; ++y) {
                    td::tiles[x][y] = false;
                }
            }
            fpuPassed = 0;
        }
    }
    
}
