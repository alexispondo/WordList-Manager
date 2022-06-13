Cyan = "\u001b[36m"
Bold_Cyan = "\u001b[1;36m"
Bold_Green = "\u001b[1;92m"
Bold_Yellow = "\u001b[1;33m"
Blue = "\u001b[34m"
Reset = "\u001b[0m"


def getparams():
    params = {}
    welcome = """
Hi, Welcome to interactive mode. You should answered for all question to create a personalize wordlist. If you have note answer for any question you should tap "ENTER" keyboard to continue.

Great, we can start now.
"""

    print(Bold_Yellow+welcome+Reset)

    # Personal Information ################################################################################
    personal_info = {}
    print("\n"+Bold_Cyan)
    print("[+] Personal Informations")
    print("\n"+Reset)


    print("\n[*] Enter the personal name (ex: Keen)")
    Personal_Name = input(">> Personal Name: "+Bold_Green)
    if Personal_Name == "":
        Personal_Name = None
    personal_info["Personal_Name"] = Personal_Name
    print(Reset)

    print("\n[*] Enter the personal surname (ex: elisabeth)")
    Personal_Surnames = input(">> Personal Surname: " + Bold_Green)
    if Personal_Surnames == "":
        Personal_Surnames = None
    personal_info["Personal_Surnames"] = Personal_Surnames
    print(Reset)

    print("\n[*] Enter the personal Nickname (ex: MrRobot)")
    Personal_Nickname = input(">> Personal Nickname: " + Bold_Green)
    if Personal_Nickname == "":
        Personal_Nickname = None
    personal_info["Personal_Nickname"] = Personal_Nickname
    print(Reset)

    print("\n[*] Enter the personal birthday (format: jj/mm/yyyy)")
    Personal_Birthday = input(">> Personal Birthday: " + Bold_Green)
    if Personal_Birthday == "":
        Personal_Birthday = None
    personal_info["Personal_Birthday"] = Personal_Birthday
    print(Reset)

    print("\n[*] Enter the pet name (ex: bibou)")
    Pet_Name = input(">> Pet Name: " + Bold_Green)
    if Pet_Name == "":
        Pet_Name = None
    personal_info["Pet_Name"] = Pet_Name
    print(Reset)

    print("\n[*] Enter the company name (ex: FBI Compagny)")
    Company_Name = input(">> Company Name: " + Bold_Green)
    if Company_Name == "":
        Company_Name = None
    personal_info["Company_Name"] = Company_Name
    print(Reset)

    params["personal_info"] = personal_info
    print()

    # Conjoint Information ################################################################################
    conjoint_info = {}
    print("\n" + Bold_Cyan)
    print("[+] Conjoint Informations")
    print("\n" + Reset)

    print("\n[*] Enter the Conjoint name (ex: Keen)")
    Conjoint_Name = input(">> Conjoint Name: " + Bold_Green)
    if Conjoint_Name == "":
        Conjoint_Name = None
    conjoint_info["Conjoint_Name"] = Conjoint_Name
    print(Reset)

    print("\n[*] Enter the Conjoint surname (ex: elisabeth)")
    Conjoint_Surnames = input(">> Conjoint Surname: " + Bold_Green)
    if Conjoint_Surnames == "":
        Conjoint_Surnames = None
    conjoint_info["Conjoint_Surnames"] = Conjoint_Surnames
    print(Reset)

    print("\n[*] Enter the Conjoint birthday (format: jj/mm/yyyy)")
    Conjoint_Birthday = input(">> Conjoint Birthday: " + Bold_Green)
    if Conjoint_Birthday == "":
        Conjoint_Birthday = None
    conjoint_info["Conjoint_Birthday"] = Conjoint_Birthday
    print(Reset)


    params["conjoint_info"] = conjoint_info
    print()

    # Child Information ################################################################################
    Child_info = {}
    print("\n" + Bold_Cyan)
    print("[+] Child Informations")
    print("\n" + Reset)

    print("\n[*] Enter the Child name (ex: Keen)")
    Child_Name = input(">> Child Name: " + Bold_Green)
    if Child_Name == "":
        Child_Name = None
    Child_info["Child_Name"] = Child_Name
    print(Reset)

    print("\n[*] Enter the Child surname (ex: Tom)")
    Child_Surnames = input(">> Child Surname: " + Bold_Green)
    if Child_Surnames == "":
        Child_Surnames = None
    Child_info["Child_Surnames"] = Child_Surnames
    print(Reset)

    print("\n[*] Enter the Child birthday (format: jj/mm/yyyy)")
    Child_Birthday = input(">> Child Birthday: " + Bold_Green)
    if Child_Birthday == "":
        Child_Birthday = None
    Child_info["Child_Birthday"] = Child_Birthday
    print(Reset)

    print("\n[*] Enter the Child School (ex: baby school)")
    Child_School = input(">> Child School: " + Bold_Green)
    if Child_School == "":
        Child_School = None
    Child_info["Child_School"] = Child_School
    print(Reset)

    params["Child_info"] = Child_info
    print()

    # Father Information ################################################################################
    Father_info = {}
    print("\n" + Bold_Cyan)
    print("[+] Father Informations")
    print("\n" + Reset)

    print("\n[*] Enter the Father name (ex: Reddington)")
    Father_Name = input(">> Father Name: " + Bold_Green)
    if Father_Name == "":
        Father_Name = None
    Father_info["Father_Name"] = Father_Name
    print(Reset)

    print("\n[*] Enter the Father surname (ex: Raimond ray)")
    Father_Surnames = input(">> Father Surname: " + Bold_Green)
    if Father_Surnames == "":
        Father_Surnames = None
    Father_info["Father_Surnames"] = Father_Surnames
    print(Reset)

    print("\n[*] Enter the Father birthday (format: jj/mm/yyyy)")
    Father_Birthday = input(">> Father Birthday: " + Bold_Green)
    if Father_Birthday == "":
        Father_Birthday = None
    Father_info["Father_Birthday"] = Father_Birthday
    print(Reset)

    params["Father_info"] = Father_info
    print()

    # Mother Information ################################################################################
    Mother_info = {}
    print("\n" + Bold_Cyan)
    print("[+] Mother Informations")
    print("\n" + Reset)

    print("\n[*] Enter the Mother name (ex: Rostova)")
    Mother_Name = input(">> Mother Name: " + Bold_Green)
    if Mother_Name == "":
        Mother_Name = None
    Mother_info["Mother_Name"] = Mother_Name
    print(Reset)

    print("\n[*] Enter the Mother surname (ex: Catalinna)")
    Mother_Surnames = input(">> Mother Surname: " + Bold_Green)
    if Mother_Surnames == "":
        Mother_Surnames = None
    Mother_info["Mother_Surnames"] = Mother_Surnames
    print(Reset)

    print("\n[*] Enter the Mother birthday (format: jj/mm/yyyy)")
    Mother_Birthday = input(">> Mother Birthday: " + Bold_Green)
    if Mother_Birthday == "":
        Mother_Birthday = None
    Mother_info["Mother_Birthday"] = Mother_Birthday
    print(Reset)

    params["Mother_info"] = Mother_info
    print()

    # Brother Information ################################################################################
    Brother_info = {}
    print("\n" + Bold_Cyan)
    print("[+] Brother Informations")
    print("\n" + Reset)

    print("\n[*] Enter the Brother name (ex: Reddington)")
    Brother_Name = input(">> Brother Name: " + Bold_Green)
    if Brother_Name == "":
        Brother_Name = None
    Brother_info["Brother_Name"] = Brother_Name
    print(Reset)

    print("\n[*] Enter the Brother surname (format: Jennifer)")
    Brother_Surnames = input(">> Brother Surname: " + Bold_Green)
    if Brother_Surnames == "":
        Brother_Surnames = None
    Brother_info["Brother_Surnames"] = Brother_Surnames
    print(Reset)

    print("\n[*] Enter the Brother birthday (format: jj/mm/yyyy)")
    Brother_Birthday = input(">> Brother Birthday: " + Bold_Green)
    if Brother_Birthday == "":
        Brother_Birthday = None
    Brother_info["Brother_Birthday"] = Brother_Birthday
    print(Reset)

    params["Brother_info"] = Brother_info
    print()
    return params
