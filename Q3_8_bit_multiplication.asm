ORG 0000H
MOV A, 30H ; Load first number into accumulator
MOV B, 40H ; Load second number into B register
MUL AB ; Multiply A and B
MOV 50H, A ; Store lower byte of product
MOV 51H, B ; Store higher byte of product
END