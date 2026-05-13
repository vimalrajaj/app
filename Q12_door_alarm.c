#include <reg51.h>
sbit doorSensor = P2^1; // Door sensor input
sbit buzzer = P2^7; // Buzzer output
void delay_1ms(void) {
unsigned int i;
for(i = 0; i < 1275; i++); // Approx 1ms delay
}
void main(void) {
while(1) {
if(doorSensor == 1) { // Door open detected
buzzer = ~buzzer; // Toggle buzzer
delay_1ms(); // ~500Hz square wave
} else {
buzzer = 1; // Turn off buzzer
}
}
}