#include <reg51.h>
void main(void) {
unsigned char num1 = 150; // First 8-bit number
unsigned char num2 = 180; // Second 8-bit number
unsigned int sum; // 16-bit to hold result + carry
unsigned char carry = 0;
sum = (unsigned int)num1 + (unsigned int)num2;
if(sum > 255) {
carry = 1; // Carry occurred
sum = sum & 0xFF; // Keep only lower 8 bits
}
P1 = (unsigned char)sum; // Output lower byte to P1
P2 = carry; // Output carry to P2
while(1);
}