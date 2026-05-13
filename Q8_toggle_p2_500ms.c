#include <reg51.h>
void delay_500ms(void) {
unsigned int i, j;
for(i = 0; i < 500; i++)
for(j = 0; j < 1275; j++); // Calibrated for ~1ms per i iteration
}
void main(void) {
while(1) {
P2 = ~P2; // Toggle all bits of P2
delay_500ms(); // Wait 500 ms
}
}