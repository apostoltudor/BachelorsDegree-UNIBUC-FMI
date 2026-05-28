.data

x: .space 4
s: .space 4
n: .space 4
index: .space 4
j: .space 4
da: .asciz "Numarul este perfect!"
nu: .asciz "Numarul NU este perfect!"
formatScanf: .asciz "%d"
formatPrinf: .asciz "%d"


.text



.global main

pushl $x
pushl $formatScanf
call scanf
popl %ebx
popl %ebx

perfect:
    //%esp:(adr intoarcere) (x)(y)
    //aplic coneventiile
    //1. punem %ebp pe stiva
    //2. il facem pointer in cadrul de apel

    pushl $ebp
    
    //%esp: (%ebp v)(adr intoarcere) (x)(y)
    
    movl %esp, %ebp
    
    //%esp: %ebp:(%ebp v)(adr intoarcere) (x)(y)
    
    movl 8(%ebp), %eax
    
    //in momentul acesta, %eax contine valoarea lui x
    //trebuie sa calculez %eax = x + y + %eax + %ecx
    
    addl %ecx, %eax
    
    //in acest moment, %eax-ul contine rezultatul
    //trebuie sa fac o restaurare a cadrului de apel
    
    popl %ebp
    movl %ebp, %esp
    //cod
    movl $1, index
    movl x, %eax
    movl $2, %ecx
    divl %ecx
    movl %eax, j
    movl $0, %eax
    movl %eax, s
    et_for:
        movl index, %ecx
        cmp j, %ecx
        jg et_urmatoare

        movl x, %eax
        divl index
        cmp $0, %edx
        je et_suma
        jmp et_repeta

        et_suma:
            movl index, %eax
            addl %eax, s
            jmp et_repeta

        et_repeta:
            incl index
            jmp et_for



    et_urmatoare:
        movl s, %eax
        cmp %eax, x
        je et_printDA
        jmp et_printNU

et_printDA:
    movl da, %ebx
    pushl %ebx
    pushl $formatPrintf
    call printf
    popl %ebx
    popl %ebx

et_printNU:
    movl nu, %ebx
    pushl %ebx
    pushl $formatPrintf
    call printf
    popl %ebx
    popl %ebx



et_exit:
    pushl $0
    call fflush
    popl %ebx
    movl $1, %eax
    movl $0, %ebx
    int $0x80