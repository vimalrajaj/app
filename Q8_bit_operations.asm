ORG 0000H
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
END