from subprocess import call
from platform import dist, linux_distribution 

#update packages based on OS, do file backups, cleanup /tmp

def deadLinkSearch():
	call("cd ~")
	call("find . xtype l | xargs rm") #find . -type l -! -exec test -e {} \; -print
	
def archPacmanClean():
	if platform.dist() or platform.linux_distribution == 'Arch' or 'arch':
		call("paccache -r")
	elif #check /etc/issues or lsbrelease
		
	call("pacman -Rns")
	
def main():
	deadLinkSearch()
	archPacmanClean()
	
main()
