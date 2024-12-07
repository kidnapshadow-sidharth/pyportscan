This is a port scanning tool made with python 

in this tool we use multithreading functionality for fast port scan

also we use socat connection and we use time for print current scanning time 

and colorama for color and argparse for help description.

#Installation:

sudo git clone https://github.com/kidnapshadow-sidharth/pyportscan.git

cd pyportscan/

sudo chmod +x setup.sh

sudo bash setup.sh

# usage:

python3 port_scanner.py -d 192.168.58.1 -s 1 -e 65535 -t 15 -o out.txt

-d : target (example.com / 192.168.25.15) 

-s : starting port (0) 

-e : ending port (65535) 

-t : thread value (2-20) 

-o : output file (out.txt)

# requirement:

pip install socket

pip install sys

pip install time

pip install queue

pip install colorama

pip install threading

pip install requests

pip install argparse




                                                                                          --kidnapshadow



