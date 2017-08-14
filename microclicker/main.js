#! /usr/bin/env node

const BBCMicrobit = require('bbc-microbit');
const robot = require('robotjs');
let microbit;

const {
  clear,
  drawPattern,
  drawProgress,
  MATRIX_SIZE
} = require('./draw');

let shuttingDown = false;
let showingProgress = false;

let slideCount = 0;
const heldButtons = {
  left: false,
  right: false
};

const BUZZER_PIN = 0; // pin the buzzer is connected to for MI:power board
const PERIOD = 150; // time to check accelerometer in ms
const BUTTON_ACTIONS = ['released', 'pressed', 'held'];

console.info('🔎 🖱️  micro:clicker\n');

function connectToMicrobit() {
  console.info('🔮  Scanning for micro:bit...');
  console.info('    Hold your micro:bit level!\n');
  BBCMicrobit.discover(microbitDiscovered => {
    console.info(`🤖  micro:bit found!\n`);
    microbit = microbitDiscovered;

    microbit.on('disconnect', _ => {
      console.info('🤖  micro:bit disconnected.an');
    });

    console.info('🔌  Connecting to micro:bit');
    microbit.connectAndSetUp(_ => {
      console.info('🤖  micro:bit connected!\n');
      console.info('     ➡️️  Press right arrow to move right.');
      console.info('     ⬅️  Press left arrow to move left.');
      console.info('   ⬅️ ➡️ ️ Hold both buttons to disconnect.');
      console.info('    🔀  Tilt up to show current progress in slides.\n');

      // listen for button presses
      microbit.on('buttonAChange', value => handleButton('left', BUTTON_ACTIONS[value]));
      microbit.on('buttonBChange', value => handleButton('right', BUTTON_ACTIONS[value]));
      microbit.subscribeButtons();

      // poll the accelerometer
      microbit.on('accelerometerChange', (x, y, z) => handleAccelerometer(x, y, z));
      microbit.writeAccelerometerPeriod(PERIOD, microbit.subscribeAccelerometer());

      // set up the sounder on pin 0
      microbit.pinOutput(BUZZER_PIN, _ => microbit.pinAnalog(BUZZER_PIN, playTune));

      // show a pattern on load
      microbit.writeLedMatrixState(drawPattern('noiseOne'), _ => {
        setTimeout(_ => microbit.writeLedMatrixState(drawPattern('noiseTwo'), _ => {
          setTimeout(_ => microbit.writeLedMatrixState(drawPattern('right')), 100);
        }), 50);
      });
    });
  });
}

function disconnectFromMicrobit() {
  // time to wait for anyting to finish
  setTimeout(_ => {
    microbit.disconnect(_ => {
      console.log('👋  Bye-bye\n');
      process.exit(1);
    });
  }, 500);
}

function handleSlideCount(type) {
  if (type === 'left') {
    if (slideCount > 0) {
      slideCount--;
    }
  } else {
    if (slideCount < MATRIX_SIZE) {
      slideCount++;
    }
  }
}

function handleButton(direction, action) {
  // console.info(`⏺️  Button ${direction} ${action}\n`);

  if (shuttingDown) {
    return;
  }

  if (action === 'released') {
    heldButtons[direction] = false;
    microbit.writeLedMatrixState(drawPattern('diamond'));
  }

  if (action === 'pressed') {
    robot.keyTap(direction);
    handleSlideCount(direction);
    microbit.writeLedMatrixState(drawPattern(direction));
  }

  if (action === 'held') {
    heldButtons[direction] = true;

    // if both buttons are held
    if (heldButtons['left'] && heldButtons['right']) {
      shuttingDown = true;
      console.log('\n🔌  Disconnecting micro:bit!');
      microbit.writeLedMatrixState(clear(), _ => {
        microbit.writeLedMatrixState(drawPattern('heart'), _ => {
          playTune();
          setTimeout(_ => {
            microbit.writeLedMatrixState(clear(), _ => disconnectFromMicrobit());
          }, 500)
        });
      });
    }
  }
}

function handleAccelerometer(x, y, z) {
  const tilted = z > 0;
  if (tilted && !showingProgress) {
    // console.info('🤖  micro:bit titled');
    showingProgress = true;
    microbit.writeLedMatrixState(drawProgress(slideCount), _ => {
      setTimeout(_ => {
        showingProgress = false;
        microbit.writeLedMatrixState(drawPattern('diamond'));
      }, 1000);
    });
  }
}

function playNote(note, duration) {
  return new Promise(resolve => {
    microbit.writePin(BUZZER_PIN, note, _ => {
      setTimeout(_ => microbit.writePin(BUZZER_PIN, 0, resolve), duration);
    });
  });
}

function playTune() {
  playNote(15, 50).then(_ => playNote(5, 100)).then(_ => playNote(1, 150));
}

connectToMicrobit();
