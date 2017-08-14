# micro:bit games

Here are some games I've written for the [BBC micro:bit](https://www.microbit.co.uk/). The games will display a 'title' screen, then play when you press A and B together. When you lose, your score will be displayed. Press A and B to return to the title screen.

## micro:tetris [py](games/tetris.py) | [hex](games/tetris.hex)
Press A or B to move a block left or right. Press both buttons at once to rotate a block. The blocks are smaller than in real Tetris (and you can't do that stupid cheat where you endlessly rotate a block so it never settles that licensed Tetris games are obliged to put in.)

## micro:snake [py](games/snake.py) | [hex](games/snake.hex)
Press A or B to turn left or right.

## TO COME:
### micro:maze [py](games/tetris.py) | [hex](games/tetris.hex)
A very crude first-person 3D maze game. Press A or B to turn 90º, or press A and B together to walk forward one square.

### 2:cars [py](games/2cars.py) | [hex](games/2cars.hex)
The "two cars" phone app: on each side of the screen is a car driving past a series of obstacles. Press A to switch lanes for the left hand car, or B to switch lanes for the right hand car.

# micro:bit offline compiler

Because the Python `.hex` files contain the entirety of your script, I have managed to reverse-engineer [a crude compiler](./py2hex.js). It requires Nodejs and a unix-like system (including OSX) to use [the batch build tool](./build.sh).

    ./py2hex.js game.py

This creates a `.hex` file of your game.

    ./py2hex.js game.py global.py

This creates a `.hex` file of your game *after* importing all of my boilerplate code which I use for all of my games. This code handles keypresses and the like.
