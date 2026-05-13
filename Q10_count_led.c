#include <reg51.h>
void delay(void) {
unsigned int i;
for(i = 0; i < 50000; i++);
}
void main(void) {
unsigned int count;
unsigned char lowByte, highByte;
while(1) {
for(count = 0; count <= 0xFF; count++) {
lowByte = (unsigned char)(count & 0xFF);
highByte = (unsigned char)((count >> 8) & 0xFF);
P3 = lowByte; // Lower byte to P3
P4 = highByte; // Higher byte to P4
delay(); // Visible delay
}
}
}