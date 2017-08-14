/*
* This module allows you to control your keynote presentations using a bbc micro:bit
*
* Author: Humberto Rodriguez Avila
*
* Example:
*
* sudo node index.js
* 
*/

var BBCMicrobit = require('bbc-microbit');
var KeynoteAPI = require("./lib/keynote");
var TimerAPI = require("./lib/timer");

var keynote = new KeynoteAPI();
var timer = new TimerAPI();
var period = 80; // ms

console.log('Scanning for microbit...');
BBCMicrobit.discover(function(microbit) {
  console.log('Discovered microbit: %s', microbit.address);
  
  microbit.on('disconnect', function() {
    console.log('Microbit disconnected!');
    process.exit(0);
  });

  microbit.on('accelerometerChange', function(x, y, z) {
    if(timer.isValidPeriodTime()){
      xf = x.toFixed(1);
      yf = y.toFixed(1);
      zf = z.toFixed(1);
      if((xf >= -0.3 && xf <= 0.3) && (yf >= -0.2 && yf <= 0.2) ){
        if(zf == -1 ){
          keynote.next();
        }else if(zf == 1){
          keynote.prev(); 
        } 
      } 
    }
   });

  microbit.on('buttonAChange', function(value) {
    if(value == 1) {
      console.log('Stopping presentation...');
      keynote.stop();}
  });

  microbit.on('buttonBChange', function(value) {
    if(value == 1) {
      console.log('Starting presentation...');
      keynote.start();
    }
  });

  console.log('Connecting microbit...');
  microbit.connectAndSetUp(function() {
    console.log('Status: Connected');
    console.log('Initializing...');
    microbit.subscribeButtons(function(){});
    microbit.writeAccelerometerPeriod(period, function() {
       microbit.subscribeAccelerometer(function() {});
    });
    console.log('Ready!');
    microbit.writeLedText('Ready!', function(){});
  });
});
