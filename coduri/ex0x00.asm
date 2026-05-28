#ex 0x00
.data
#intializare
    matrix: .space 1600
    qmatrix: .space 1600
    qcolumnIndex: .space 4
    qlineIndex: .space 4
    afis1: .space 4
    afis2: .space 4
    x: .space 4
    y: .space 4
    m: .space 4
    n: .space 4
    p: .space 4
    k: .space 4
    s: .space 4
    d: .space 4
    left: .space 4
    right: .space 4
    index: .space 4
    cnt: .space 4
    columnIndex: .space 4
    lineIndex: .space 4
    tripleScanf: .asciz "%d %d %d"
    doubleScanf: .asciz "%d %d"
    formatScanf: .asciz "%d"
    formatPrintf: .asciz "%d "
    newLine: .asciz "\n"

.text

.global main

main:

#citire m,n,p
    pushl $p
    pushl $n
    pushl $m
    pushl $tripleScanf
    call scanf
    popl %ebx
    popl %ebx
    popl %ebx
    popl %ebx
#for int i=1, i<=p,i++
#   cin left
#   cin right
#   eax=lineindex*n+columnindex
    lea matrix, %edi
#   mov $1,(edi,eax,4)
    movl $0, %ebx
    movl %ebx, index
#index = i (for int i=...)
et_for_citire:
    movl index, %ecx
    cmp p, %ecx
    je et_k
#citire left right si transformare celule moarte-->vii
    pushl $left
    pushl $formatScanf
    call scanf
    popl %ebx
    popl %ebx

    pushl $right
    pushl $formatScanf
    call scanf
    popl %ebx
    popl %ebx
#mut left si right in eax cum trebuie
    movl left, %eax
    movl $0, %edx
    addl $1, %eax
    addl $2, n
    mull n
    addl right, %eax
    addl $1, %eax
    subl $2, n
    #lea array, fac din 0 in 1
    movl $1, %ebx
    lea matrix, %edi
    movl %ebx, (%edi, %eax, 4)
    movl $1, %ebx
    lea qmatrix, %esi
    movl %ebx, (%esi, %eax, 4)
    incl index
    jmp et_for_citire
et_k:
    pushl $k
    pushl $formatScanf
    call scanf
    popl %ebx
    popl %ebx
    jmp et_b
    

et_b:
    movl $0, %ebx
    movl %ebx, index
    movl $1, %ebx
    movl %ebx, afis1
    movl $1, %ebx
    movl %ebx, afis2
    movl $0, %ebx
    movl %ebx, index
    jmp et_index

et_index:
    movl index, %ecx
    cmp k, %ecx
    je et_print1 #et t


    movl $1, %ebx
    movl %ebx, lineIndex
    et_lineIndex:
        movl lineIndex, %ecx
        cmp m, %ecx
        jg et_altaeticheta #et lineindex1


        movl $1, %ebx
        movl %ebx, columnIndex
        et_columnIndex:
            movl columnIndex, %ecx
            cmp n, %ecx
            jg et_continuare #et columnindex1


            movl lineIndex, %eax
            movl $0, %edx
            addl $2, n
            mull n
            addl columnIndex, %eax
            subl $2, n  #calc poz

            lea matrix, %edi
            movl (%edi,%eax,4), %ebx
            lea qmatrix, %esi
            movl %ebx, (%esi,%eax,4)

            incl columnIndex #et columnindex1
            jmp et_columnIndex

        et_continuare:
            incl lineIndex  #et lineindex1
            jmp et_lineIndex
        et_altaeticheta:
            movl $1, %ebx
            movl %ebx, qlineIndex
 




    
    et_qlineIndex:
        movl qlineIndex, %ecx
        cmp m, %ecx
        jg et_contindex #et lineindex2


        movl $1, %ebx
        movl %ebx, qcolumnIndex
        et_qcolumnIndex:
            movl qcolumnIndex, %ecx
            cmp n, %ecx
            jg et_qcontinuare #et columnindex2


            movl $0, %ebx
            movl %ebx, cnt #prel

            movl $0, %ebx
            movl %ebx, x
            et_x:
                movl x, %ecx
                cmp $3, %ecx
                je et_ifx #et i


                movl $0, %ebx
                movl %ebx, y
                et_y:
                    movl y, %ecx
                    cmp $3, %ecx
                    je et_ycontinuare #et j


                    movl qlineIndex, %ebx
                    movl %ebx, s
                    movl x, %ebx
                    addl %ebx, s
                    subl $1, s
                    movl s, %eax
                    movl $0, %edx
                    addl $2, n
                    mull n
                    subl $2, n
                    movl qcolumnIndex, %ebx
                    movl %ebx, d
                    movl y, %ebx
                    addl %ebx, d
                    subl $1, d
                    addl d, %eax #calc poz
                    lea qmatrix, %esi
                    movl (%esi, %eax, 4), %ebx
                    cmp $1, %ebx
                    je et_adunare
                    jmp et_nuadun

                    et_adunare:
                        addl $1, cnt

                    et_nuadun:
                        incl y  #et j
                        jmp et_y
                    et_ycontinuare:
                        incl x #et i
                        jmp et_x
            

                
            et_ifx:

                movl qlineIndex, %eax
                movl $0, %edx
                addl $2, n
                mull n
                subl $2, n
                addl qcolumnIndex, %eax    #calculcat poz elem
                et_cond1:
                    lea qmatrix, %esi
                    movl (%esi, %eax, 4), %ebx 
                    cmp $1, %ebx
                    je et_cond20
                    jmp et_cond3
                et_cond20:
                    movl $3, %ebx
                    cmp cnt, %ebx
                    jg et_zero
                    jmp et_cond21
                et_cond21:
                    movl $4, %ebx
                    cmp cnt, %ebx
                    jl et_zero
                    jmp et_unu
                et_cond3:
                    lea qmatrix, %esi
                    movl (%esi, %eax, 4), %ebx
                    cmp $0, %ebx
                    je et_cond4
                et_cond4:
                    movl $3, %ebx
                    cmp cnt, %ebx
                    je et_unu
                    jmp et_zero
                et_zero:
                    movl $0, %ebx
                    lea matrix, %edi
                    movl %ebx, (%edi, %eax, 4)
                    jmp et_jump
                et_unu:
                    movl $1, %ebx
                    lea matrix, %edi
                    movl %ebx, (%edi, %eax, 4)
                    jmp et_jump

            et_jump:
                incl qcolumnIndex #et columnindex2
                jmp et_qcolumnIndex

            et_qcontinuare:
                incl qlineIndex #et lineindex2
                jmp et_qlineIndex

        
    et_contindex:
        incl index   #et t
        jmp et_index







et_print1:
    movl afis1, %ecx
    cmp m, %ecx
    jg et_exit  #et print1
    movl $1, afis2

    et_print2:
        movl afis2, %ecx
        cmp n, %ecx
        jg et_cont  #et print2

        movl afis1, %eax
        movl $0, %edx
        addl $2, n
        mull n 
        addl afis2, %eax
        subl $2, n
        
        lea matrix, %edi
        movl (%edi, %eax, 4), %ebx

        pushl %ebx
        pushl $formatPrintf
        call printf
        popl %ebx
        popl %ebx

        pushl $0
        call fflush
        popl %ebx

        incl afis2  #et print2
        jmp et_print2

    et_cont:   # foloseste \n dupa ce se
               #termina for-ul cu coloanele
        movl $4, %eax
        movl $1, %ebx
        movl $newLine, %ecx
        movl $2, %edx
        int $0x80

        addl $1, afis1
        jmp et_print1

et_exit:
#exit
    pushl $0
    call fflush
    popl %ebx
    movl $1, %eax
    movl $0, %ebx
    int $0x80