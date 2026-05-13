#include <reg51.h>
sbit myPin = P3^6; // Declare P3.6
void delay(void) {
unsigned int i;
for(i = 0; i < 50000; i++);
}
void main(void) {
while(1) {
myPin = ~myPin; // Toggle only P3.6
delay(); // Visible delay
}
}