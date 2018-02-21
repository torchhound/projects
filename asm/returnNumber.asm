section .data
	input db 'Enter a valid integer: '
	inputLength equ $-input
	displayInput db 'Your valid integer: '
	displayLength equ $-displayInput
	
section .bss
	num resb 5
	
section .text
	global _start
_start:
	mov eax, 4 ;sys_write
	mov ebx, 1 ;print to terminal
	mov ecx, input
	mov edx, inputLength
	int 0x80 ;kernel call

	mov eax, 3 ;sys_read
	mov ebx, 2
	mov ecx, num
	mov edx, 5
	int 0x80
	
	mov eax, 4
	mov ebx, 1
	mov ecx, displayInput
	mov edx, displayLength
	int 0x80
	
	mov eax, 4
	mov ebx, 1
	mov ecx, num
	mov edx, 5
	int 0x80
	
	mov eax, 1 ;sys_exit
	mov ebx, 0
	int 0x80