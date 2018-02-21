section .bss

factorial resb 4

section .text

	global _start
_start
	mov ebp, 4
	mov eax, 64
	imul eax, eax
	cmp eax, 1
	jne sub eax, 1
	cmp eax, 1
	jne sub eax, 1
	jz END