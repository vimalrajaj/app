ORG 0000H
MOV A, 30H ; Load lower byte of first number
ADD A, 40H ; Add lower byte of second number
MOV 50H, A ; Store lower byte of result
MOV A, 31H ; Load higher byte of first number
ADDC A, 41H ; Add higher byte of second number with carry
MOV 51H, A ; Store higher byte of result
MOV A, #00H ; Clear accumulator
ADDC A, #00H ; Add carry to accumulator
MOV 52H, A ; Store carry
END