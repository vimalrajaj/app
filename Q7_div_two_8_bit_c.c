#include <reg51.h>
void main(void) {
unsigned char dividend = 200; // Dividend
unsigned char divisor = 30; // Divisor
unsigned char quotient;
unsigned char remainder;
unsigned char error = 0;
if(divisor == 0) {
error = 1; // Division by zero error
quotient = 0;
remainder = 0;
} else {
quotient = dividend / divisor; // Quotient
remainder = dividend % divisor; // Remainder
}
P1 = quotient; // Output quotient to P1
P2 = remainder; // Output remainder to P2
P3 = error; // Output error status to P3
while(1);
}