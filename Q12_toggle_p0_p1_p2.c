#include <reg51.h> // Contains standard SFR definitions
// Alternative explicit sfr declarations (if header not used):
// sfr P0 = 0x80; // Port 0 at address 0x80
// sfr P1 = 0x90; // Port 1 at address 0x90
// sfr P2 = 0xA0; // Port 2 at address 0xA0
void delay_500ms(void) {
unsigned int i, j;
for(i = 0; i < 500; i++)
for(j = 0; j < 1275; j++);
}
void main(void) {
while(1) {
P0 = ~P0; // Toggle all bits of P0
P1 = ~P1; // Toggle all bits of P1
P2 = ~P2; // Toggle all bits of P2
delay_500ms(); // 500ms delay
}
}