# ida_scripts

* IDA pwntools auto attach
Put idapwntools.py in IDA plugins folder. After loading binary, press Shift+Z to open XMLRPC server.

Script for pwntools:
[code]
p = process(["./test"], env={"LD_PRELOAD" : "./libc-2.23.so"})
proxy = xmlrpclib.ServerProxy("http://localhost:1337")#IDA_Server
proxy.Attach(str(p.pid))
raw_input()
[code]

Then switch to IDA windows and press Shift+Z to attach running process in pwntools.
