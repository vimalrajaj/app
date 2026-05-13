#include <reg51.h>
sbit myBit = P2^1; // Declare P2.1
void main(void) {
unsigned int counter;
for(counter = 0; counter < 25000; counter++) {
myBit = ~myBit; // Toggle P2.1
}
while(1); // Stay in infinite loop
}