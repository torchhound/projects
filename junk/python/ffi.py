import ctypes

libc = ctypes.CDLL("/usr/lib/libc.dylib")

print(libc.rand())
print(libc.time())
cPrintF = libc.printf
value = b"I'm a C function!"
print(value)
printValue = ctypes.c_char_p(value)
print(printValue.value)
print(printValue)
cPrintF("%s", printValue)
