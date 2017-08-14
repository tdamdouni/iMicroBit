// Based on example code from Kitronik; test Accelerometer module, look for min and max values.


const int xval = 0; //Define the analog pins.                 
const int yval = 1;                  
const int zval = 2;                  

int xmin = 600;
int ymin = 600;
int zmin = 600;
int xmax = 0;
int ymax = 0;
int zmax = 0;
int x, y, z;

void setup()
{
   Serial.begin(115200); //begin serial communication and set the baud rate for the serial monitor.   
}

void loop()
{
   x = analogRead(xval);
   y = analogRead(yval);
   z = analogRead(zval);


   if (x < xmin) { xmin = x; }
   if (y < ymin) { ymin = y; }
   if (z < zmin) { zmin = z; }
   if (x > xmax) { xmax = x; }
   if (y > ymax) { ymax = y; }
   if (z > zmax) { zmax = z; }

   Serial.print("x=");
   Serial.print(x);
   Serial.print("  y=");
   Serial.print(y);
   Serial.print("  z=");
   Serial.print(z);
   Serial.print(" | xmin=");
   Serial.print(xmin);
   Serial.print(" xmax=");
   Serial.print(xmax);
   Serial.print(" ymin=");
   Serial.print(ymin);
   Serial.print(" ymax=");
   Serial.print(ymax);
   Serial.print(" zmin=");
   Serial.print(zmin);
   Serial.print(" zmax=");
   Serial.println(zmax);
   
   delay(200);
}


