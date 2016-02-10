#!/usr/bin/env python
from os import listdir
from os.path import isfile, join
import random
from subprocess import call, check_output

mypath = "./imgs"
files = [ f for f in listdir(mypath) if isfile(join(mypath, f)) ]
pastardhe = random.choice(files)

# because magik
for jean in check_output(["xrandr"])[:].split("\n"):
    if "*" in jean:
        klod = next(s for s in jean.split(" ") if s)
        break
van = int(klod.split('x')[0])
dam = int(klod.split('x')[1])
_ = ["animate", "{}/{}".format(mypath, pastardhe), "-immutable", "-quiet", "-loop", "1", "-geometry", "{}+{}+{}".format(klod, van/3, dam/3), "-resize", "{}x{}".format(van/2, dam/2)]
__, ___ = _[:], _[:]
__.extend(("-alpha", "copy"))
___.extend(("-title", "1231507051321"))

# special treatment for our special friends.
if pastardhe == "zimba.gif":
    call(__)
elif pastardhe == "the-future-is-now.gif":
    call(___)
else:
    call(["animate", "{}/{}".format(mypath, pastardhe), "-immutable", "-quiet", "-loop", "4", "-geometry", "{}+{}+{}".format(klod, 0, dam/3), "-resize", str(klod)])
