ORG 0000H
MOV A, 30H ; Load dividend into accumulator
MOV B, 40H ; Load divisor into B register
DIV AB ; Divide A by B
MOV 50H, A ; Store quotient
MOV 51H, B ; Store remainder
END