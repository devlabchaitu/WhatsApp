#! /usr/bin/env/ python
import fcntl, os, sys

if __name__ == "__main__":
    f = open("/dev/urandom", "r")
    fd = f.fileno()
    fl = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)

    ready = False
    line = ""
    while True:
        try:
            char = f.read()
            if char == '\r':
                continue
            elif char = '\n':
                ready = True
            else:
                line += char
        except:
            continue
        if ready:
            print line