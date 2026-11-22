.section .text.boot,"ax"
.global _start
.type _start,%function
_start:
    msr daifset, #0xf
    msr spsel, #1
    ldr x0, =_stack_top
    mov sp, x0
    bl render_menu
1:  wfe
    b 1b
.section .bss.stack,"aw",%nobits
.balign 16
_stack_bottom:
    .skip 65536
_stack_top:
