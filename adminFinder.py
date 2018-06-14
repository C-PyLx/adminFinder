#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#Admin page finder
#Version: 1.0
#Coded by: Learning :~#
#For website attacks

#Follow me on github:
#https://github.com/C-PyLx
#Report bugs to:
#https://t.me/Ac3ess

import os
import sys
import time
import argparse
from urllib.request import (Request, urlopen,
                            HTTPError,
                            URLError)

#Terminal colors code:
green = '\033[0;32m'
blue = '\033[0;4m'
red = '\033[0;31m'
cyan = '\033[0;96m'
orange = '\033[0;38;5;166m'
end = '\033[0;37m'

class Program:

    def logo():
        os.system('clear')

        print (green + ''' _ __ _    _  _ ____ _ (_) _ __ _
| |__| |  | || | || | || || // | |
| |  | |__| || | || | || || |  | | 
|_|  |_(__)_||_| || |_||_||_|  |_|            
      ____(_) _ __ _    _  ____ _ __
     | __/| || // | |  | |//___|-//  
     | __|| || |  | |__| |||   |-|
     |_|  |_||_|  |_(__)_| \___|_| { Version: 1.0 }
{ Coded by: Learning :~# }
        ''', end)

    def adminFinder(page, path):
        if len(sys.argv) < 2:
            Program.logo()
            print ('[ + ] Usage:')
            print (cyan + 'python3 adminFinder.py -u [target-url] -p [admin-path(txt)] -v [enable-verbosity]', end)
            print (cyan + 'python3 adminFinder.py -u [target-url] -p [admin-path(txt)]', end)
            sys.exit()

        start = time.time()
        try:
            f = open(path,"r");
        except:
            print (red + '\n[ ! ] Admin filepath not found !\n', end)
            sys.exit()

        os.system('clear')
        Program.logo()

        print (blue + 'Available links:', end)
        while True:
            line = f.readline()
            if not line:
                break

            panel = "http://"+str(page)+"/"+line
            req = Request(panel)

            try:
                response = urlopen(req)
            except HTTPError as e:
                continue
            except URLError as e:
                continue

            else:
                endTime = time.time()
                print (green + '[ ✔ ] Found page %s' %panel, end)
        print (orange + '\n[ + ] Time elapsed: %s seconds.' %(round(endTime-start, 2)), end)

    def main():
        parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=green+'Python admin page finder'+end,
            usage='\npython3 adminFinder.py -u [url] -p [panel-word(TXT)]')

        parser.add_argument('-u', '--url',
        help='target url address',
        default=None)
        parser.add_argument('-p', '--panel',
        help='panel wordlist path',
        default='page.txt')

        args = parser.parse_args()

        Program.adminFinder(args.url, args.panel)

if __name__ == '__main__':
    try:
        Program.main()
    except KeyboardInterrupt:
        sys.exit()
    except argparse.ArgumentError:
        print (red + '\n[ ! ] Argument error occurred !', end)
        sys.exit()

else:
    Program.logo()
    sys.exit()
