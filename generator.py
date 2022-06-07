from threading import Thread
# from copy import copy
# My data test
personal_info = {
    "Personal_Name": "John",
    "Personal_Surnames": "The Ripper",
    "Personal_Nickname": "jtr",
    "Personal_Birthday": "01/01/2000",
    "Pet_Name": "Hydra",
    "Company_Name": "Hacking Corporation",
}

conjoint_info = {
    "Conjoint_Name": "Cat",
    "Conjoint_Surnames": "Hash",
    "Conjoint_Nickname": "hashcat",
    "Conjoint_Birthday": "10/10/2005",
}

child_info = {
    "Child_Name": "go",
    "Child_Surnames": "buster",
    "Child_Nickname": "gbt",
    "Child_Birthday": "15/12/2012",
    "Child_School": "fusingSchool",
}

father_info = {
    "Father_Name": "Ping",
    "Father_Surnames": "icmp",
    "Father_Birthday": "01/06/1970",
}

mother_info = {
    "Mother_Name": "ssh",
    "Mother_Surnames": "scp",
    "Mother_Birthday": "06/12/1990",
}

brother_info = {
    "Brother_Name": "ffuf",
    "Brother_Surnames": "fuzze",
    "Brother_Nickname": "fuzzer",
    "Brother_Birthday": "02/02/2002",
}

####################################################################################
"""def first_letter_up(name):
    name = list(name)
    name[0] = str(name[0]).upper()
    return "".join(name)"""

def remove_duplicate(x):
  return list(dict.fromkeys(x))

# reverse data
def reverse(data):
    l = len(data)
    data = list(data)
    n_d = []
    for i in range(l):
        n_d.append(data[(l-1)-i])
    return "".join(n_d)

# Replacer function with parameter (text, old letter, new letter, starting position, number of occurrence replaced)
def replacer_letter(text:str, old:str, new:str, pos_l:int, nb_occ:int):
    j = 0
    k = 0
    ok = 0
    text2 = text
    for i in text:
        if old == i:
            j = j+1
            if j >= pos_l:
                ok = ok +1
                text2 = list(text2)
                text2[k] = new
                text2 = "".join(text2)
                if ok == nb_occ:
                    return text2
        k=k+1

# replace letter by number or special character
def letter_to_spec_char_num(data):
    #data = str(data).lower()
    list_change = []
    if "a" in data:
        number_of = data.count("a")
        # For 4
        for i in range(number_of):
            for j in range(i,number_of):
                d = replacer_letter(data,"a","4",number_of-j,i+1)
                list_change.append(d)
        # For @
        for i in range(number_of):
            for j in range(i,number_of):
                d = replacer_letter(data,"a","@",number_of-j,i+1)
                list_change.append(d)

    if "o" in data:
        number_of = data.count("o")
        for i in range(number_of):
            for j in range(i, number_of):
                d = replacer_letter(data, "o", "0", number_of - j, i + 1)
                list_change.append(d)

    if "b" in data:
        number_of = data.count("b")
        for i in range(number_of):
            for j in range(i, number_of):
                d = replacer_letter(data, "b", "8", number_of - j, i + 1)
                list_change.append(d)
        for i in range(number_of):
            for j in range(i, number_of):
                d = replacer_letter(data, "b", "3", number_of - j, i + 1)
                list_change.append(d)

    if "e" in data:
        number_of = data.count("e")
        for i in range(number_of):
            for j in range(i, number_of):
                d = replacer_letter(data, "e", "3", number_of - j, i + 1)
                list_change.append(d)
        for i in range(number_of):
            for j in range(i, number_of):
                d = replacer_letter(data, "e", "&", number_of - j, i + 1)
                list_change.append(d)

    if "l" in data:
        number_of = data.count("l")
        for i in range(number_of):
            for j in range(i, number_of):
                d = replacer_letter(data, "l", "1", number_of - j, i + 1)
                list_change.append(d)
        for i in range(number_of):
            for j in range(i, number_of):
                d = replacer_letter(data, "l", "!", number_of - j, i + 1)
                list_change.append(d)

    if "i" in data:
        number_of = data.count("i")
        for i in range(number_of):
            for j in range(i, number_of):
                d = replacer_letter(data, "i", "1", number_of - j, i + 1)
                list_change.append(d)
        for i in range(number_of):
            for j in range(i, number_of):
                d = replacer_letter(data, "i", "!", number_of - j, i + 1)
                list_change.append(d)

    if "s" in data:
        number_of = data.count("s")
        for i in range(number_of):
            for j in range(i, number_of):
                d = replacer_letter(data, "s", "5", number_of - j, i + 1)
                list_change.append(d)
        for i in range(number_of):
            for j in range(i, number_of):
                d = replacer_letter(data, "s", "$", number_of - j, i + 1)
                list_change.append(d)

    if "t" in data:
        number_of = data.count("t")
        for i in range(number_of):
            for j in range(i, number_of):
                d = replacer_letter(data, "t", "7", number_of - j, i + 1)
                list_change.append(d)


    string = data
    for char in string:
        if char.lower() == 'a':
            string = string.replace('a', '@')
        elif char.lower() == 'b':
            string = string.replace('b', '8')
        elif char.lower() == 'e':
            string = string.replace('e', '3')
        elif char.lower() == 'l':
            string = string.replace('l', '1')
        elif char.lower() == 'i':
            string = string.replace('i', '1')
        elif char.lower() == 'o':
            string = string.replace('o', '0')
        elif char.lower() == 's':
            string = string.replace('s', '$')
        elif char.lower() == 't':
            string = string.replace('t', '7')
    list_change.append(string)
    return list_change










############################################################################################################
# Main transformations
############################################################################################################
def transformation_name(name:str):
    names_list = []

    names_list.append(name)
    names_list.append(name.capitalize())
    names_list.append(name.upper())
    names_list.append(name.lower())
    names_list.append(reverse(name))
    n_l = []
    for i in names_list:
        n_l = n_l + letter_to_spec_char_num(i)
    names_list = names_list + n_l

    names_list = list(filter(None, names_list))
    return names_list

def transformation_surname(surname:str):
    surname_list = []

    surname_list.append(surname)
    surname_list.append(" ".join([i.capitalize() for i in surname.split(" ")]))
    surname_list.append(surname.upper())
    surname_list.append(surname.lower())

    if len(surname.split(" ")) > 1:
        for i in surname.split(" "):
            surname_list.append(i)
            surname_list.append(i.upper())
            surname_list.append(i.lower())
            surname_list.append(i.capitalize())
        s_r = " ".join([i for i in list(reversed(surname.split(" ")))])
        surname_list.append(s_r)
        surname_list.append(" ".join([i.capitalize() for i in s_r.split(" ")]))
        surname_list.append(s_r.upper())
        surname_list.append(s_r.lower())

    l0 = []
    for l in surname_list:
        l0.append("-".join(l.split(" ")))
        l0.append("_".join(l.split(" ")))
        l0.append("".join(l.split(" ")))
        l0.append("@".join(l.split(" ")))
    surname_list = surname_list + l0

    n_l = []
    for i in surname_list:
        n_l = n_l + letter_to_spec_char_num(i)
    surname_list = surname_list + n_l

    #print(sorted(surname_list))
    #print(sorted(remove_duplicate(surname_list)))
    surname_list = list(filter(None, surname_list))
    return surname_list

def transformation_date(date:str):
    date_list = []

    date_list.append(date)
    d1 = date.split("/")
    d1.reverse()
    date_list.append("/".join(d1))
    l0 = []
    for l in date_list:
        l0.append(" ".join(l.split("/")))
        l0.append("-".join(l.split("/")))
        l0.append("_".join(l.split("/")))
        l0.append("".join(l.split("/")))
    date_list = date_list + l0
    date_list.append(date.split("/")[0])
    date_list.append(date.split("/")[1])
    date_list.append(date.split("/")[2])
    date_list.append(date.split("/")[2][2:])

    date_list = list(filter(None, date_list))
    return date_list


def transformation_company_school(cpt_or_sch:str):
    cs_list = []

    cs_list.append(cpt_or_sch)
    cs_list.append(" ".join([i.capitalize() for i in cpt_or_sch.split(" ")]))
    cs_list.append(cpt_or_sch.upper())
    cs_list.append(cpt_or_sch.lower())

    l0 = []
    for l in cs_list:
        l0.append("-".join(l.split(" ")))
        l0.append("_".join(l.split(" ")))
        l0.append("".join(l.split(" ")))
    cs_list = cs_list + l0

    cs_list = list(filter(None, cs_list))

    return cs_list

"""def transformation_name_surname(name_list:list, surname_list:list):
    list_returned = []
    for n in name_list:
        for s in surname_list:
            list_returned = list_returned + transformation_surname(n +" "+ s.split(" ")[0])
            list_returned = list_returned + transformation_surname(n +"_"+ s.split(" ")[0])
            list_returned = list_returned + transformation_surname(n +"-"+ s.split(" ")[0])
            list_returned = list_returned + transformation_surname(n + s.split(" ")[0])

            list_returned = list_returned + transformation_surname(n +" "+ s)
            list_returned = list_returned + transformation_surname(n +"_"+ s)
            list_returned = list_returned + transformation_surname(n +"-"+ s)
            list_returned = list_returned + transformation_surname(n + s)
    return list_returned"""

def transformation_name_surname(name, surname):
    s_name = []
    for s in surname.split(" "):
        s_name = s_name + transformation_surname(name + " " + s)
    s_name = s_name + transformation_surname(name + " " + surname)
    return s_name
"""
def transformation_nsk_birthday(name, surname, nickname, birthday):
    list_returned = []
    day, month, year = birthday.split("/")
    s_year = year[2:]
    date_liste = [day, month, year, s_year]
    n = name + " " + surname + " " + nickname
    l5 = []
    for l51 in n.split(" "):
        l5 = l5 + transformation_surname(l51)
    l5 = l5 + transformation_surname(n)

    n_l = []
    for n0 in l5:
        for d in date_liste:
            n_l.append(n0 + "" + d)
            n_l.append(n0 + "_" + d)

        n_l.append(n0 + "" + day+month+year)
        n_l.append(n0 + "" + month+year)
        n_l.append(n0 + "" +year+month)
        n_l.append(n0 + "" +year+month+day)

        n_l.append(n0 + "_" + day+month+year)
        n_l.append(n0 + "_" + month+year)
        n_l.append(n0 + "_" +year+month)
        n_l.append(n0 + "_" +year+month+day)


    list_returned = list_returned + n_l
    list_returned.append(day)
    list_returned.append(month)
    list_returned.append(year)
    list_returned.append(s_year)
    list_returned.append(day+month+year)
    list_returned.append(year+month+day)
    return list_returned"""
def transformation_nsk_birthday(data_list, birthday):
    list_returned = []
    day, month, year = birthday.split("/")
    s_year = year[2:]
    date_liste = [day, month, year, s_year]
    n_l = []
    for n0 in data_list:
        for d in date_liste:
            n_l.append(n0 + "" + d)
            n_l.append(n0 + "_" + d)

        n_l.append(n0 + "" + day + month + year)
        n_l.append(n0 + "" + month + year)
        n_l.append(n0 + "" + year + month)
        n_l.append(n0 + "" + year + month + day)

        n_l.append(n0 + "_" + day + month + year)
        n_l.append(n0 + "_" + month + year)
        n_l.append(n0 + "_" + year + month)
        n_l.append(n0 + "_" + year + month + day)
    list_returned = list_returned + n_l
    list_returned.append(day)
    list_returned.append(month)
    list_returned.append(year)
    list_returned.append(s_year)
    list_returned.append(day+month+year)
    list_returned.append(year+month+day)
    return list_returned
############################################################################################################
############################################################################################################

############################################################################################################
# Main program

def program(all_info:dict):
    wordlist_list = []

    # Target
    personal = all_info["personal_info"]
    if personal["Personal_Name"] is not None:
        print("[*] Transformation Name ... ",end="")
        personal_name = sorted(remove_duplicate(transformation_name(personal["Personal_Name"])))
        wordlist_list = wordlist_list + personal_name
        print("OK")

    if personal["Personal_Surnames"] is not None:
        print("[*] Transformation surmane ... ",end="")
        personal_surname = sorted(remove_duplicate(transformation_surname(personal["Personal_Surnames"])))
        wordlist_list = wordlist_list + personal_surname
        print("OK")

    if personal["Personal_Nickname"] is not None:
        print("[*] Transformation nickname ... ",end="")
        personal_nickname = sorted(remove_duplicate(transformation_name(personal["Personal_Nickname"])))
        wordlist_list = wordlist_list + personal_nickname
        print("OK")

    if personal["Personal_Birthday"] is not None:
        print("[*] Transformation birthday ... ",end="")
        personal_birthday = sorted(remove_duplicate(transformation_date(personal["Personal_Birthday"])))
        wordlist_list = wordlist_list + personal_birthday
        print("OK")

    if personal["Pet_Name"] is not None:
        print("[*] Transformation petname ... ",end="")
        pet_name = sorted(remove_duplicate(transformation_name(personal["Pet_Name"])))
        wordlist_list = wordlist_list + pet_name
        print("OK")

    if personal["Company_Name"] is not None:
        print("[*] Transformation company ... ",end="")
        company_name = sorted(remove_duplicate(transformation_company_school(personal["Company_Name"])))
        wordlist_list = wordlist_list + company_name
        print("OK")

    if personal["Personal_Name"] is not None and personal["Personal_Surnames"] is not None:
        print("[*] Transformation name & surname ... ",end="")
        personal_name_surname = sorted(remove_duplicate(transformation_name_surname(personal["Personal_Name"],personal["Personal_Surnames"])))
        wordlist_list = wordlist_list + personal_name_surname
        print("OK")

    if personal["Personal_Name"] is not None and personal["Personal_Nickname"] is not None:
        print("[*] Transformation name & nickname ... ",end="")
        personal_name_nickname = sorted(remove_duplicate(transformation_name_surname(personal["Personal_Name"],personal["Personal_Nickname"])))
        wordlist_list = wordlist_list + personal_name_nickname
        print("OK")

    if personal["Personal_Surnames"] is not None and personal["Personal_Nickname"] is not None:
        print("[*] Transformation nickname & surname ... ",end="")
        personal_nickname_surname = sorted(remove_duplicate(transformation_name_surname(personal["Personal_Nickname"],personal["Personal_Surnames"])))
        wordlist_list = wordlist_list + personal_nickname_surname
        print("OK")

    if personal["Personal_Birthday"] is not None:
        dat00 = wordlist_list.copy()
        print("[*] Transformation name & surname & nickname & birthday ... ",end="")
        #personal_nsk_birthday = sorted(remove_duplicate(transformation_nsk_birthday(personal["Personal_Name"],personal["Personal_Surnames"],personal["Personal_Nickname"],personal["Personal_Birthday"])))
        personal_nsk_birthday = sorted(remove_duplicate(transformation_nsk_birthday(dat00, personal["Personal_Birthday"])))
        wordlist_list = wordlist_list + personal_nsk_birthday
        print("OK")

    if personal["Personal_Birthday"] is not None and personal["Pet_Name"] is not None:
        dat00 = wordlist_list.copy()
        print("[*] Transformation PetName & birthday ... ",end="")
        #personal_nsk_birthday = sorted(remove_duplicate(transformation_nsk_birthday(personal["Personal_Name"],personal["Personal_Surnames"],personal["Personal_Nickname"],personal["Personal_Birthday"])))
        personal_nsk_birthday = sorted(remove_duplicate(transformation_nsk_birthday(dat00, personal["Personal_Birthday"])))
        wordlist_list = wordlist_list + personal_nsk_birthday
        print("OK")

    print("[*] Join all and writing ... ",end="")
    #wordlist_list = wordlist_list + personal_name + personal_surname + personal_nickname + personal_birthday + pet_name + company_name + personal_name_surname + \
    #                personal_name_nickname + personal_nickname_surname + personal_nsk_birthday
    wordlist_list = sorted(remove_duplicate(wordlist_list))
    with open("dict.txt", "w") as d:
        d.write("\n".join(str(i) for i in wordlist_list))
        d.write("\n")
    print(": OK")

all_info = {
    "personal_info" : {
        "Personal_Name": "pondo",
        "Personal_Surnames": "kouakou alexis",
        "Personal_Nickname": "pkaba",
        "Personal_Birthday": "23/12/1999",
        "Pet_Name": "Hydra",
        "Company_Name": "Hacking Corporation",
    }
}
program(all_info)
############################################################################################################
############################################################################################################