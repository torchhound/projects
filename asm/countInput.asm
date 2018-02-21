section .data
	userInput db 'Enter a list of words to be counted: '
	inputLength equ $-userInput
	displayInput db 'Word count: '
	displayLength equ $-displayInput

section .bss
	input resb 16 ;reserve 16 bytes of memory
	count resb 8 ;reserve space for count

section .text
	global _start
_start:
	mov eax, 4
	mov ebx, 1
	mov ecx, userInput
	mov edx, inputLength
	int 0x80
	
	mov eax, 5
	mov ebx, 2
	mov ecx, input
	mov edx, 16
	int 0x80
	
	countN:
		mov ecx, count
		mov edx, input
		inc ecx
		dec edx
		cmp ecx, edx
		jz edx
		jmp countN
		
	output:
		mov eax, 4
		mov ebx, 1
		mov ecx, displayInput
		mov edx, displayLength
		int 0x80
	
		mov eax, 4
		mov ebx, 1
		mov ecx, count
		mov edx, 8
	
		mov eax, 1
		mov ebx, 0
		int 0x80