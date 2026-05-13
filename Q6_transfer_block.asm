ORG 0000H
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
END