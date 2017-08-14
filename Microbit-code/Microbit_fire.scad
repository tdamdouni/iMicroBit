// The Microbit is a cool new thing from eth BBC.
// It runs micropython.

// I wrote a flam simulator on it and this panel fits on top
// So you can adjust the parameters with the buttons and// see a diffuse fire display through the plastic shell

// Can be found on Thingiverse http://www.thingiverse.com/thing:1165549


board_w = 52;    // Width of the Microbit
board_h = 44;    // Height of the Microbit
board_d = 1.7;   // Thickness of the circuit board
standoff = 2;    // How far off does the fire_place stand from the board
thickness = 1.5; // Thickness of the 3D print in general.
//
fire_pane_w = 25;    // Height of the display LEDs
fire_pane_h = 22;    // Width of the display LEDs
fire_pane_off = 10;  // Distance from base to bottom of display recess
fire_pane_d = 0.5;   // Thin section over the LEDs to diffuse them.
//
button_off_w = 4;   // Offset of buttons from side
button_off_h = 17;  // Offset of buttons from base of Microbit
button_w = 8;       // Width of buttons
//
usb_w = 15;     // width of recess for the USB plug


Delta = 0.1; // used to make sure things overlap properly for a nice 3D model

//--------------------------------------------------------------------------
// The base plate or panel
module plate() {
	translate([0,board_h/2,thickness/2])
		cube(size=[board_w,board_h, thickness], center=true);
}

// hole for a button (mirrored for other side)
module button() {
	translate([(board_w-button_off_w-button_w)/2, button_off_h+button_w/2,0])
		cube(size=[button_w,button_w,button_w], center=true);
}

// Recess for USB plug
module usb() {
	h = board_d+standoff+thickness+Delta*2;
	translate([0,-thickness/2,-thickness-Delta])
		cube([usb_w,thickness*2,h*2],center=true);
}

// Little standoffs to seat board height properly
module standoff() {
	translate([(board_w-button_off_w-button_w)/2, board_h-button_off_h, Delta-standoff/2])
		cube([standoff,standoff,standoff], center=true);
	translate([(board_w-button_off_w-button_w)/2, thickness, Delta-standoff/2])
		cube([standoff,standoff,standoff], center=true);
}

// Sides and bottom lip
module sides() {
	h = board_d+standoff+thickness;
	// bottom
	translate([0,-thickness/2+Delta, thickness-h/2])
		cube([board_w, thickness, h ], center=true);
	// side 1
	translate([-(thickness+board_w)/2+Delta,(board_h-thickness)/2+Delta, thickness-h/2])
		cube([thickness, board_h+thickness, h ], center=true);
	// side 2
	translate([(thickness+board_w)/2-Delta,(board_h-thickness)/2+Delta, thickness-h/2])
		cube([thickness, board_h+thickness, h ], center=true);
}


//The entire object made of parts
module fire_place() {
	difference() {
		// baseplate and sides
		union() {
			plate();
			sides();
		}
		// subtracting USB, buttons, LED region
		usb();
		button();
		mirror([1,0,0])
			button();
		// flame region
		translate([0,fire_pane_h,thickness/2-fire_pane_d])
			cube([fire_pane_w,fire_pane_h,thickness], center=true);
	}
	// Add standoffs
	standoff();
	mirror([1,0,0])
			standoff();
	// Some measures to make sure its all working right :)
	// color([1,0,0])
		// cube([32,1,1], center=true);
	// color([1,0,0])
	// translate([board_w/2,button_off_h/2,3])
		// cube([1,button_off_h,1], center=true);
}

// Make it upside down so can be printed easily.
rotate([180,0,0])
	fire_place();