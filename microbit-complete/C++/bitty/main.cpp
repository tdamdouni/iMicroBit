#include "MicroBit.h"

MicroBit uBit;


int main()
{
    // Initialise the micro:bit runtime.
    uBit.init();
    // Display a start-up message
    uBit.display.scroll("BUGGYY");
    
    // Application code will go here and in functions outside of main()
    
    
    
    
    
    // end of application code in main()    
    
    // If main exits, there may still be other fibers running or registered event handlers etc.
    // Simply release this fiber, which will mean we enter the scheduler. Worse case, we then
    // sit in the idle task forever, in a power efficient sleep.
    release_fiber();
}
