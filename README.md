# TUTORIAL
Click on the video to see the tutorial:




# DESCRIPTION
WordList-Manager is a tool written in python that allows you to manage wordlists.
Several advantages appear when using this tool:

**Written in python:** so it can be modified according to your needs

**Independent of the operating system:** 
It can be used under Windows, Linux etc.. 

**easy to use:**
It uses explicit flags allowing easy understanding.

**Gathers several tools:** allowing to work with wordlist.
From modifying wordlists to creating new wordlists based on personal information WordList-Manager is a real arsenal that every pentester must have to increase his chances of BruteForce

# INSTALLATION

```
$ git clone https://github.com/alexispondo/WordList-Manager.git
```

```
$ cd WordList-Manager 
```

```
$ python3 installer.py 
```

# USAGE
```
$ python3 wl-manager.py -h


 _       __               ____    _      __        __  ___                                 
| |     / /___  _________/ / /   (_)____/ /_      /  |/  /___ _____  ____ _____ ____  _____
| | /| / / __ \/ ___/ __  / /   / / ___/ __/_____/ /|_/ / __ `/ __ \/ __ `/ __ `/ _ \/ ___/
| |/ |/ / /_/ / /  / /_/ / /___/ (__  ) /_/_____/ /  / / /_/ / / / / /_/ / /_/ /  __/ /    
|__/|__/\____/_/   \__,_/_____/_/____/\__/     /_/  /_/\__,_/_/ /_/\__,_/\__, /\___/_/     
                                                                        /____/             

                               ==============================                                                      
                               === by Alexis PONDO @pkaba ===                                                
                               ==============================                                                       

[+] Name: WordList-Manager
[+] Version: v1.0.0
[+] Github: https://github.com/alexispondo/
[+] Linkedin: https://www.linkedin.com/in/alexis-pondo/



positional arguments:
  {format0,format1,format2,format3,format4,generate}
    format0             Create Login credentials wordlist from usernames and passwords wordlists with separator
    format1             Split Login credentials wordlist in two wordlists (username and password) by separator
    format2             Split wordlist in many wordlist with same size
    format3             Shuffle Wordlist
    format4             Sort wordlist in ascending order or descending order
    generate            Password list generator

optional arguments:
  -h, --help            show this help message and exit
  -uL UL                Usernames wordlist path
  -pL PL                Passwords wordlist path
  -wL WL                Wordlist path
  --sep SEP             Separator default (":") 
                        ex: 
                          If sep= ":"
                            Creds will be like admin:passord, 
                          If sep= "<==>"
                            Creds will be like admin<==>passord
  -o O                  Separator default ("output.txt")
  -n N                  split in n wordlist equal
  --order ORDER         Order of sorting (default 0):
                            0: Ascending order
                            1: Descending order
  --load LOAD           Generation: Loading the personal data model.
                        if not specified, the interactive mode will be used
 
```
We have different formats that allow us to determine what type of modification we want to apply

- format0: 
```
$ python3 wl-manager.py format0 -uL ./exemples/usernames.txt -pL ./exemples/passwords.txt --sep : -o credentials.txt 
```

- format1: 
```
$ python3 wl-manager.py format1 -wL credentials.txt --sep ":"
```

- format2: 

**For split "passwords.txt" in 10 wordlists**
```
$ python3 wl-manager.py format2 -wL ./exemples/passwords.txt -n 10
```

- format3: 
```
$ python3 wl-manager.py format3 -wL ./exemples/passwords.txt
```

- format4: 

**Ascending order**
```
$ python3 wl-manager.py format4 -wL Wordlist.txt --order 0
```
**Descending order**
```
$ python3 wl-manager.py format4 -wL Wordlist.txt --order 1
```

- generate:

**Using Interactive Mode**
```
$ python3 wl-manager.py generate
```
**Using Template Data**
```
$ python3 wl-manager.py generate --load exemples/personal_data.txt
```


# Additional

All information about this code can be found in the comments of the code.
Please contact me for any bug or anomaly detected in connection with this tool:

Linkedin: https://www.linkedin.com/in/alexis-pondo/

GitHub: https://github.com/alexispondo/

WordList-Manager Tool: https://github.com/alexispondo/WordList-Manager
