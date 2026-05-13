ORG 0000H
CLR C ; Clear carry flag initially
MOV A, 30H ; Load lower byte of first number
SUBB A, 40H ; Subtract lower byte of second number
MOV 50H, A ; Store lower byte of result
MOV A, 31H ; Load higher byte of first number
SUBB A, 41H ; Subtract higher byte of second number with borrow
MOV 51H, A ; Store higher byte of result
END