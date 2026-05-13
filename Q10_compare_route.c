#include <reg51.h>
void main(void) {
unsigned char myData;
P1 = 0xFF; // Configure P1 as input
while(1) {
myData = P1; // Read data from P1
if(myData > 244) { // Since max is 255, threshold adjusted
P2 = myData; // Send to P2 if "high value"
} else {
P3 = myData; // Send to P3 otherwise
}
}
}