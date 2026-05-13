import os

files = {
    "Q1/16_bit_addition.asm": """ORG 0000H
MOV A, 30H ; Load lower byte of first number
ADD A, 40H ; Add lower byte of second number
MOV 50H, A ; Store lower byte of result
MOV A, 31H ; Load higher byte of first number
ADDC A, 41H ; Add higher byte of second number with carry
MOV 51H, A ; Store higher byte of result
MOV A, #00H ; Clear accumulator
ADDC A, #00H ; Add carry to accumulator
MOV 52H, A ; Store carry
END""",
    "Q1/toggle_p2_1.c": """#include <reg51.h>
sbit myBit = P2^1; // Declare P2.1
void main(void) {
unsigned int counter;
for(counter = 0; counter < 25000; counter++) {
myBit = ~myBit; // Toggle P2.1
}
while(1); // Stay in infinite loop
}""",
    "Q2/16_bit_subtraction.asm": """ORG 0000H
CLR C ; Clear carry flag initially
MOV A, 30H ; Load lower byte of first number
SUBB A, 40H ; Subtract lower byte of second number
MOV 50H, A ; Store lower byte of result
MOV A, 31H ; Load higher byte of first number
SUBB A, 41H ; Subtract higher byte of second number with borrow
MOV 51H, A ; Store higher byte of result
END""",
    "Q2/toggle_p4_delay.c": """#include <reg51.h>
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
}""",
    "Q3/8_bit_multiplication.asm": """ORG 0000H
MOV A, 30H ; Load first number into accumulator
MOV B, 40H ; Load second number into B register
MUL AB ; Multiply A and B
MOV 50H, A ; Store lower byte of product
MOV 51H, B ; Store higher byte of product
END""",
    "Q3/read_p2_to_p3.c": """#include <reg51.h>
void delay_1sec(void) {
unsigned int i, j;
for(i = 0; i < 1000; i++)
for(j = 0; j < 1275; j++);
}
void main(void) {
unsigned char myData;
P2 = 0xFF; // Configure P2 as input
myData = P2; // Read data from P2
delay_1sec(); // Wait 1 second
P3 = myData; // Send data to P3
while(1); // Stay in loop
}""",
    "Q4/8_bit_division.asm": """ORG 0000H
MOV A, 30H ; Load dividend into accumulator
MOV B, 40H ; Load divisor into B register
DIV AB ; Divide A by B
MOV 50H, A ; Store quotient
MOV 51H, B ; Store remainder
END""",
    "Q4/add_two_8_bit_c.c": """#include <reg51.h>
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
}""",
    "Q5/sub_two_8_bit_c.c": """#include <reg51.h>
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
}""",
    "Q5/find_least_mark.asm": """ORG 0000H
MOV R0, #40H ; Point to start of marks array
MOV R1, #05 ; Counter for 5 marks
MOV A, @R0 ; Load first mark as initial minimum
MOV R2, A ; Store minimum in R2
LOOP:
INC R0 ; Point to next mark
MOV A, @R0 ; Load next mark
CLR C ; Clear carry for subtraction
SUBB A, R2 ; Compare with current minimum
JNC NEXT ; If A >= R2, skip update
MOV A, @R0 ; Reload the smaller value
MOV R2, A ; Update minimum
NEXT:
DJNZ R1, LOOP ; Decrement counter, repeat if not zero
MOV 50H, R2 ; Store final minimum
END""",
    "Q6/transfer_block.asm": """ORG 0000H
MOV R0, #10 ; Number of bytes to transfer (example: 10 bytes)
MOV DPTR, #4500H ; Source address
MOV R1, #55H ; Upper byte of destination
MOV R2, #00H ; Lower byte of destination
LOOP:
CLR A
MOVX A, @DPTR ; Read from source
INC DPTR ; Increment source pointer
MOV DPL, R2 ; Load destination lower byte
MOV DPH, R1 ; Load destination upper byte
MOVX @DPTR, A ; Write to destination
INC R2 ; Increment destination lower byte
MOV DPL, DPL ; Restore source pointer
DJNZ R0, LOOP ; Repeat for all bytes
END""",
    "Q6/mul_two_8_bit_c.c": """#include <reg51.h>
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
}""",
    "Q7/total_marks.asm": """ORG 0000H
MOV R0, #40H ; Pointer to marks array
MOV R1, #05 ; Counter for 5 subjects
MOV A, #00H ; Clear accumulator
MOV R2, #00H ; High byte of sum
LOOP:
ADD A, @R0 ; Add mark to accumulator
JNC NEXT ; If no carry, skip
INC R2 ; Increment high byte on carry
NEXT:
INC R0 ; Point to next mark
DJNZ R1, LOOP ; Repeat for all marks
MOV 50H, A ; Store lower byte of total
MOV 51H, R2 ; Store higher byte of total
END""",
    "Q7/div_two_8_bit_c.c": """#include <reg51.h>
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
}""",
    "Q8/toggle_p2_500ms.c": """#include <reg51.h>
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
}""",
    "Q8/bit_operations.asm": """ORG 0000H
; Load initial value
MOV A, #55H ; 0101 0101
MOV 30H, A ; Store initial value
; AND operation - clear upper nibble
MOV A, 30H
ANL A, #0FH ; Mask: 0000 1111
MOV 31H, A ; Result: 0000 0101
; OR operation - set upper nibble
MOV A, 30H
ORL A, #0F0H ; Mask: 1111 0000
MOV 32H, A ; Result: 1111 0101
; XOR operation - toggle upper nibble
MOV A, 30H
XRL A, #0F0H ; Toggle upper bits
MOV 33H, A ; Result: 1010 0101
; Complement operation
MOV A, 30H
CPL A ; Invert all bits
MOV 34H, A ; Result: 1010 1010
; Bit manipulation
SETB C ; Set carry flag
CLR P1.0 ; Clear bit P1.0
SETB P1.1 ; Set bit P1.1
CPL P1.2 ; Complement bit P1.2
; Rotate operations
MOV A, 30H
RL A ; Rotate left
MOV 35H, A ; Result: 1010 1010
MOV A, 30H
RR A ; Rotate right
MOV 36H, A ; Result: 1010 1010
END""",
    "Q9/iot_communication_models.md": """# IoT Communication Models
1. Device-to-Device
2. Device-to-Cloud
3. Device-to-Gateway
4. Back-End Data-Sharing Model""",
    "Q9/toggle_p2_continuous.c": """#include <reg51.h>
void main(void) {
while(1) {
P2 = ~P2; // Toggle all bits of P2 continuously
}
}""",
    "Q10/count_led.c": """#include <reg51.h>
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
}""",
    "Q10/compare_route.c": """#include <reg51.h>
void main(void) {
unsigned char myData;
P1 = 0xFF; // Configure P1 as input
while(1) {
myData = P1; // Read data from P1
if(myData > 244) { // Since max is 255, threshold adjusted
P2 = myData; // Send to P2 if "high value"
} else {
P3 = myData; // Send to P3 otherwise
}
}
}""",
    "Q11/toggle_p3_6.c": """#include <reg51.h>
sbit myPin = P3^6; // Declare P3.6
void delay(void) {
unsigned int i;
for(i = 0; i < 50000; i++);
}
void main(void) {
while(1) {
myPin = ~myPin; // Toggle only P3.6
delay(); // Visible delay
}
}""",
    "Q11/arduino_integration.md": """# Integration of Sensors and Actuators with Arduino
1. Identify sensor/actuator specifications
2. Design appropriate interface circuit
3. Write Arduino code for reading/controlling
4. Implement processing logic
5. Create feedback loop if required""",
    "Q12/door_alarm.c": """#include <reg51.h>
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
}""",
    "Q12/toggle_p0_p1_p2.c": """#include <reg51.h> // Contains standard SFR definitions
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
}"""
}

for filepath, content in files.items():
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        f.write(content)
