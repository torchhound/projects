import ctypes
import multiprocessing
import sys
if sys.platform == "win32":
    import win32_sysinfo as sysinfo
    print(sysinfo.dwNumberOfProcessors);

libc = ctypes.CDLL("/usr/lib/libc.dylib") #probably won't work on windows

print("Standard cpu count check: {}".format(multiprocessing.cpu_count()))
sysconfCPUO = libc.sysconf(_SC_NPROCESSORS_ONLN)
sysconfCPUA = libc.sysconf(_SC_NPROCESSORS_CONF)
print("The number of processors online: {} \n The number of processors configured: {}".format(sysconfCPUO, sysconfCPUA)) #.value?
