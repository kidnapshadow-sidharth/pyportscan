#!/bin/bash

clear

#define color 
red='\e[1;31m'
green='\e[1;32m'
blue='\e[1;34m'
blink='\e[5m'
stop_blink='\e[25m'
stop_color='\e[0m'


echo -e "$red**********************************************************************$stop_color"
echo -e  """ $green  
 _____                                                                        _____ 
}
( ___ )                                                                      ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
 |   |  ____   ___  ____ _____   ____   ____    _    _   _ _   _ _____ ____   |   | 
 |   | |  _ \ / _ \|  _ \_   _| / ___| / ___|  / \  | \ | | \ | | ____|  _ \  |   | 
 |   | | |_) | | | | |_) || |   \___ \| |     / _ \ |  \| |  \| |  _| | |_) | |   | 
 |   | |  __/| |_| |  _ < | |    ___) | |___ / ___ \| |\  | |\  | |___|  _ <  |   | 
 |   | |_|    \___/|_| \_\|_|   |____/ \____/_/   \_\_| \_|_| \_|_____|_| \_\ |   | 
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
(_____)                                                                      (_____)

------------------------------------------------------------------------------------
                                                        Crafted by sidharth
                                                        Twitter: kidnapshadow_kd
------------------------------------------------------------------------------------
 $stop_color """

echo -e "$red**********************************************************************$stop_color"


echo -e "Getting Things Ready For You..... :) \n"

apt-get install python3

apt-get install python3-pip

pip3 install socket

pip3 install sys

pip3 install time

pip3 install queue

pip3 install colorama

pip3 install threading

pip3 install requests

pip3 install argparse

chmod +x port_scanning.py

cp port_scanning.py /usr/bin/port_scanning.py

echo -e "\ndone...\n"

clear

python3 port_scanning.py --help