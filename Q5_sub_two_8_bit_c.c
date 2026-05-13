#include <reg51.h>
void main(void) {
unsigned char num1 = 100; // Minuend
unsigned char num2 = 150; // Subtrahend
unsigned char result;
unsigned char borrow = 0;
if(num2 > num1) {
borrow = 1; // Borrow required
result = (256 + num1) - num2; // Compute with borrow
} else {
result = num1 - num2; // Normal subtraction
}
P1 = result; // Output result to P1
P2 = borrow; // Output borrow to P2
while(1);
}