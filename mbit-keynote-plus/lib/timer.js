/*
* This module provides an API to control the time between actions.
*
* Author: Humberto Rodriguez Avila
*
*/

var Time = require('time');

/*  the keynote API constructor  */
var Timer = function () {
  this.lastAction = 0
}

/*  returns TRUE if the last action occurred 1 or more seconds ago  */
Timer.prototype.isValidPeriodTime = function () { 
    if((Time.time()- this.lastAction) >= 1){
        this.lastAction =  Time.time();
        return true;
    }
    return false;
};


/*  export the API  */
module.exports = Timer;