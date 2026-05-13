ORG 0000H
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
END