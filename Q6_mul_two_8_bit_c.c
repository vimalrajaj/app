#include <reg51.h>
void main(void) {
unsigned char num1 = 120; // First operand
unsigned char num2 = 200; // Second operand
unsigned int product;
unsigned char lowByte, highByte;
product = (unsigned int)num1 * (unsigned int)num2;
lowByte = (unsigned char)(product & 0xFF); // Lower byte
highByte = (unsigned char)(product >> 8); // Higher byte
P1 = lowByte; // Output lower byte to P1
P2 = highByte; // Output higher byte to P2
while(1);
}