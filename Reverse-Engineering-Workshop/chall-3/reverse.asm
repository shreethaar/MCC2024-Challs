section .data
    result dd 0xF298DC9E  ; Value at .text:004013E1

section .text
    global _start

_start:
    mov eax, [result]      ; Start with the given value of eax (0xF298DC9E)

    ; Reverse xor eax, ecx (ecx = 0x8E67212B)
    mov ecx, 0x8E67212B
    xor eax, ecx

    ; Reverse shr eax, 1
    shl eax, 1

    ; Reverse ror eax, 7
    rol eax, 7

    ; Reverse add eax, ecx (ecx = 0xFFA3887A)
    mov ecx, 0xFFA3887A
    sub eax, ecx

    ; Reverse xor ecx, 0xCB89034
    mov ecx, eax
    xor ecx, 0xCB89034

    ; Reverse add eax, 0xFFA3887A
    sub eax, 0xFFA3887A

    ; Reverse lea ecx, [eax - 0xD1507BA]
    add ecx, 0xD1507BA

    ; Reverse shr eax, 9
    shl eax, 9

    ; Reverse xor eax, 0xB20083FF
    xor eax, 0xB20083FF

    ; Exit
    mov ebx, 0
    mov eax, 1
    int 0x80
