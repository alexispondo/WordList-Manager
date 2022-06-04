"""
Coded By Alexis Pondo
Github: http://github.com/alexispondo/
Linkedin: https://www.linkedin.com/in/alexis-pondo/
"""
from datetime import datetime
import time
import os
from pathlib import Path
import tempfile
import itertools as IT
import platform
import sys
import random

import argparse
from argparse import RawTextHelpFormatter, SUPPRESS

Black = "\u001b[30m"
Red = "\u001b[31m"
Green = "\u001b[32m"
Bold_Green = "\u001b[1;92m"
Yellow = "\u001b[33m"
Blue = "\u001b[34m"
Magenta = "\u001b[35m"
Cyan = "\u001b[36m"
White = "\u001b[37m"
Reset = "\u001b[0m"
Underline = "\u001b[4m"

# Exit function with message
exit_err = lambda x: sys.exit(Red + str(x) + Reset)
exit_success = lambda x: sys.exit(Green + str(x) + Reset)


###################################################################


##############################################################################################################################################
################################################################## Banner ####################################################################

# Display banner
def banner():
    infos = """
[+] Name: WordList-Manager
[+] Version: v1.0.0
[+] Github: https://github.com/alexispondo/
[+] Linkedin: https://www.linkedin.com/in/alexis-pondo/
"""

    ban1 ="""

 __       __                            __  __        __              __             __       __                                                             
/  |  _  /  |                          /  |/  |      /  |            /  |           /  \     /  |                                                            
$$ | / \ $$ |  ______    ______    ____$$ |$$ |      $$/   _______  _$$ |_          $$  \   /$$ |  ______   _______    ______    ______    ______    ______  
$$ |/$  \$$ | /      \  /      \  /    $$ |$$ |      /  | /       |/ $$   |  ______ $$$  \ /$$$ | /      \ /       \  /      \  /      \  /      \  /      \ 
$$ /$$$  $$ |/$$$$$$  |/$$$$$$  |/$$$$$$$ |$$ |      $$ |/$$$$$$$/ $$$$$$/  /      |$$$$  /$$$$ | $$$$$$  |$$$$$$$  | $$$$$$  |/$$$$$$  |/$$$$$$  |/$$$$$$  |
$$ $$/$$ $$ |$$ |  $$ |$$ |  $$/ $$ |  $$ |$$ |      $$ |$$      \   $$ | __$$$$$$/ $$ $$ $$/$$ | /    $$ |$$ |  $$ | /    $$ |$$ |  $$ |$$    $$ |$$ |  $$/ 
$$$$/  $$$$ |$$ \__$$ |$$ |      $$ \__$$ |$$ |_____ $$ | $$$$$$  |  $$ |/  |       $$ |$$$/ $$ |/$$$$$$$ |$$ |  $$ |/$$$$$$$ |$$ \__$$ |$$$$$$$$/ $$ |      
$$$/    $$$ |$$    $$/ $$ |      $$    $$ |$$       |$$ |/     $$/   $$  $$/        $$ | $/  $$ |$$    $$ |$$ |  $$ |$$    $$ |$$    $$ |$$       |$$ |      
$$/      $$/  $$$$$$/  $$/        $$$$$$$/ $$$$$$$$/ $$/ $$$$$$$/     $$$$/         $$/      $$/  $$$$$$$/ $$/   $$/  $$$$$$$/  $$$$$$$ | $$$$$$$/ $$/       
                                                                                                                               /  \__$$ |                    
                                                                                                                               $$    $$/                     
                                                                                                                                $$$$$$/                      

                                                                  ==============================                                                      
                                                                  === by Alexis PONDO @pkaba ===                                                
                                                                  ==============================                                                       

"""+infos+"""
"""
    ban2="""

 _       __               ____    _      __        __  ___                                 
| |     / /___  _________/ / /   (_)____/ /_      /  |/  /___ _____  ____ _____ ____  _____
| | /| / / __ \/ ___/ __  / /   / / ___/ __/_____/ /|_/ / __ `/ __ \/ __ `/ __ `/ _ \/ ___/
| |/ |/ / /_/ / /  / /_/ / /___/ (__  ) /_/_____/ /  / / /_/ / / / / /_/ / /_/ /  __/ /    
|__/|__/\____/_/   \__,_/_____/_/____/\__/     /_/  /_/\__,_/_/ /_/\__,_/\__, /\___/_/     
                                                                        /____/             

                               ==============================                                                      
                               === by Alexis PONDO @pkaba ===                                                
                               ==============================                                                       

"""+infos+"""
"""
    ban =[ban1,ban2]
    return Cyan+random.choice(ban)+Reset

##############################################################################################################################################
##############################################################################################################################################


##############################################################################################################################################
############################################################### Functions used ###############################################################

# Get file encoding
def get_encoding(file):
    try:
        import magic
        return magic.Magic(mime_encoding=True).from_file(file)
    except:
        return "utf-8"  # By default


# Function to transform wordlist file in list
def file_to_list(file):
    try:
        encoding = get_encoding(file)  # We get encoding of file
        with open(file, "r", encoding=encoding, errors="ignore") as line:  # We open file with encoding
            lines = [i.split("\n")[0] for i in line.readlines()]  # add all line of file in the list call lines
        return lines  # return list
    except Exception as e:
        exit_err(str(e))  # if error return it

# Function for format0
def format_0(user_list, pass_list, sep, output):
    #start_time = str(datetime.now()).split(".")[0] # Start Time
    start_time = int(str(time.time()).split(".")[0]) # Start Time
    encoding = get_encoding(pass_list)  # We get encoding of file
    with open(output, "w", encoding=encoding) as creds:
        for u in user_list:
            for p in pass_list:
                line = str(u)+str(sep)+str(p)+"\n"
                creds.writelines(line)
    #end_time = str(datetime.now()).split(".")[0]  # End Time
    end_time = int(str(time.time()).split(".")[0])  # End Time
    sec = int(end_time) - int(start_time)

    min, sec = divmod(sec, 60)
    hours, min = divmod(min, 60)

    print("Time passed: {}h:{}m:{}s".format(hours,min,sec))
    if Path(output).is_file():
        output_file = os.path.abspath(str(output))
    print("Your output file is stored: {}".format(output_file))

##############################################################################################################################################
##############################################################################################################################################


##############################################################################################################################################
################################################################### Parser ###################################################################
parser = argparse.ArgumentParser(
    description=banner(),
    formatter_class=RawTextHelpFormatter,
    usage=SUPPRESS,
    epilog="""Exemples:
    python3 wl-manager.py format0 -uL unsernames.txt -pL passwords.txt --sep : -o credentials.txt
    python3 wl-manager.py format1 -wL Wodlist.txt --sep ":"
    python3 wl-manager.py format2 -wL Wodlist.txt n 5
    python3 wl-manager.py format3 -wL Wodlist.txt
    python3 wl-manager.py format3 -wL Wodlist.txt --order 1
    python3 wl-manager.py generate
    """
)
subparser = parser.add_subparsers(dest='command')

format0 = subparser.add_parser('format0', help="Create Login credentials wordlist from usernames and passwords wordlists with separator")
format0.formatter_class = RawTextHelpFormatter
format1 = subparser.add_parser('format1', help="Split Login credentials wordlist in two wordlists (username and password) by separator")
format1.formatter_class = RawTextHelpFormatter
format2 = subparser.add_parser('format2', help="Split wordlist in many wordlist with same size")
format2.formatter_class = RawTextHelpFormatter
format3 = subparser.add_parser('format3', help="Shuffle Wordlist")
format3.formatter_class = RawTextHelpFormatter
format4 = subparser.add_parser('format4', help="Sort wordlist in ascending order or descending order")
format4.formatter_class = RawTextHelpFormatter
generate = subparser.add_parser('generate', help="Password list generator")
generate.formatter_class = RawTextHelpFormatter

format0.add_argument("-uL", type=str, required=True, help="Usernames wordlist path")
format0.add_argument("-pL", type=str, required=True, help="Passwords wordlist path")
format0.add_argument("--sep", type=str, default=":", help="Separator default (\":\") "
                                                          "\nex: "
                                                          "\n  If sep= \":\""
                                                          "\n    Creds will be like admin:passord, "
                                                          "\n  If sep= \"<==>\""
                                                          "\n    Creds will be like admin<==>passord")
format0.add_argument("-o", type=str, default="output.txt", help="Separator default (\"output.txt\")")

format1.add_argument("-wL", type=str, required=True, help="Credentials wordlist path")
format1.add_argument("--sep", type=str, default=":", help="Separator default (\":\")")

format2.add_argument("-wL", type=str, required=True, help="Wordlist path")
format2.add_argument("-n", type=str, required=True, help="split in n wordlist equal")

format3.add_argument("-wL", type=str, required=True, help="Wordlist path")

format4.add_argument("-wL", type=str, required=True, help="Wordlist path")
format4.add_argument("--order", type=str, choices=['0', '1'], default="0", help="Order of sorting (default 0):\n"
                                                                                "    0: Ascending order\n"
                                                                                "    1: Descending order")

parser.add_argument("-uL", type=str, required=False, help="Usernames wordlist path")
parser.add_argument("-pL", type=str, required=False, help="Passwords wordlist path")
parser.add_argument("-wL", type=str, required=False, help="Wordlist path")
parser.add_argument("--sep", type=str, required=False, help="Separator default (\":\") "
                                                            "\nex: "
                                                            "\n  If sep= \":\""
                                                            "\n    Creds will be like admin:passord, "
                                                            "\n  If sep= \"<==>\""
                                                            "\n    Creds will be like admin<==>passord")
parser.add_argument("-o", type=str, required=False, help="Separator default (\"output.txt\")")
parser.add_argument("-n", type=str, required=False, help="split in n wordlist equal")
parser.add_argument("--order", type=str, required=False, default="0", help="Order of sorting (default 0):\n"
                                                                           "    0: Ascending order\n"
                                                                           "    1: Descending order")

args = parser.parse_args()
##############################################################################################################################################
##############################################################################################################################################


##############################################################################################################################################
################################################################ Main Porgram ################################################################
if __name__ == '__main__':
    print(banner())
    if args.command == "format0":
        #print("format0")
        usernames = args.uL
        passwords = args.pL
        separator = args.sep
        output = args.o
        usernames_liste = file_to_list(usernames)
        passwords_liste = file_to_list(passwords)
        # print(usernames_liste)
        # print(passwords_liste)
        format_0(usernames_liste, passwords_liste, separator, output)
    elif args.command == "format1":
        print("format1")
        wordlist = args.wL
        separator = args.sep
        print(wordlist, separator)
    elif args.command == "format2":
        print("format2")
        wordlist = args.wL
        number = args.n
        print(wordlist, number)
    elif args.command == "format3":
        print("format3")
        wordlist = args.wL
        print(wordlist)
    elif args.command == "format4":
        print("format4")
        wordlist = args.wL
        order = args.order
        print(wordlist, order)
##############################################################################################################################################
##############################################################################################################################################
