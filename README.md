# ida_scripts

* IDA pwntools auto attach:

  Place idapwntools.py into IDA plugin folder. After loading binary, press Shift+Z to open XMLRPC server.

  Script for pwntools:

  ```
  p = process(["./test"], env={"LD_PRELOAD" : "./libc-2.23.so"})
  proxy = xmlrpclib.ServerProxy("http://localhost:1337")#IDA_Server
  proxy.Attach(str(p.pid))
  raw_input()
  ```

  Then switch to IDA windows and press Shift+Z to attach running process in pwntools.

* Python DYLIB path patches for IDA (tested on 7.0)

  Place `patch.py` in IDA_DIR and execute. Working around for IDA vs brew python (2.7.15), and allow to install z3, angr, etc. on MacOS.
