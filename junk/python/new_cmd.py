import subprocess
import atexit
import os
def new_cmd():
	prgrm = raw_input("Input program name: ")
	path = "C:\Users\Sorcerer\Programs"
	os.chdir(path)
	os.popen(['cmd', '/K', '%s' %prgrm])
	procs = [cmd.exe]
def kill_subprocesses():
    for proc in procs:
        proc.kill()
def main():
	new_cmd()
	atexit.register(kill_subprocesses)

main()