#include <reg51.h>
void delay_1sec(void) {
unsigned int i, j;
for(i = 0; i < 1000; i++)
for(j = 0; j < 1275; j++);
}
void main(void) {
unsigned char myData;
P2 = 0xFF; // Configure P2 as input
myData = P2; // Read data from P2
delay_1sec(); // Wait 1 second
P3 = myData; // Send data to P3
while(1); // Stay in loop
}