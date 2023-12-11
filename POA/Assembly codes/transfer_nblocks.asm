DATA SEGMENT
    SEG1 DB 1H, 2H, 3H
DATA ENDS

EXTRA SEGMENT
    SEG2 DB ?
EXTRA ENDS


CODE SEGMENT 
    START: 
    
    MOV AX,DATA
    MOV DS,AX
    
    MOV AX,EXTRA
    MOV ES,AX
    
    LEA SI, SEG1
    LEA DI, SEG2
    
    MOV CX,03H
    
    L1:
    
    MOV AH,DS:[SI]
    MOV ES:[DI],AH
    
    INC SI
    INC DI
    DEC CX
    
    JNZ L1  
    INT 3
    
ENDS
END START