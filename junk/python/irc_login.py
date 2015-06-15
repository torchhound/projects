import irc
import irclib
def main():
    IRC_HOST = "irc.rizon.net"
    IRC_PORT = 6667
    FROM = "username"
    TO = "NickServ"
    MESSAGE = "/msg NickServ IDENTIFY password"
    irc = irclib.IRC()
    try:
        c = irc.server().connect(TO, IRC_PORT, FROM)
        irc.send(MESSAGE, FROM)
    except irclib.ServerConnectionError, x:
        print x
        sys.exit(1)
    
    
if __name__ == "__main__":
    main()
