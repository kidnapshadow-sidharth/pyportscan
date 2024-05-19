This is a port scanning tool made with python 
in this tool we use multithreading functionality for fast port scan
also we use socat connection and we use time for print current scanning time 
and colorama for color and argparse for help description.


requirement:
pip install socket
pip install sys
pip install time
pip install queue
pip install colorama
pip install threading
pip install requests
pip install argparse

usage:
python3 port_scanner.py -d 192.168.58.1 -s 1 -e 65535 -t 15 -o out.txt

-d : target (example.com / 192.168.25.15) \n
-s : starting port (0) \n
-e : ending port (65535) \n
-t : thread value (2-20) \n
-o : output file (out.txt) \n
                                                                                          --kidnapshadow



