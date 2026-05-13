#include <reg51.h>
void delay(void) {
unsigned int i, j;
for(i = 0; i < 1000; i++)
for(j = 0; j < 100; j++);
}
void main(void) {
while(1) {
P4 = ~P4; // Toggle all bits of P4
delay(); // Wait for some time
}
}