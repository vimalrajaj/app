ORG 0000H
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
END