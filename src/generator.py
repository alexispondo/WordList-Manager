# Modules imported
import os
from pathlib import Path
##########################################################################

# Terminal colors
Cyan = "\u001b[36m"
Bold_Cyan = "\u001b[1;36m"
Bold_Green = "\u001b[1;92m"
Bold_Yellow = "\u001b[1;33m"
Blue = "\u001b[34m"
Reset = "\u001b[0m"
##########################################################################


# Sort of sort() function
def remove_duplicate(x):
  return list(dict.fromkeys(x))
##########################################################################

# reverse data
def reverse(data):
    l = len(data)
    data = list(data)
    n_d = []
    for i in range(l):
        n_d.append(data[(l-1)-i])
    return "".join(n_d)
##########################################################################

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
##########################################################################

# replace letter by number or special character
def letter_to_spec_char_num(data):
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
        # For 8
        for i in range(number_of):
            for j in range(i, number_of):
                d = replacer_letter(data, "b", "8", number_of - j, i + 1)
                list_change.append(d)
        # For 3
        for i in range(number_of):
            for j in range(i, number_of):
                d = replacer_letter(data, "b", "3", number_of - j, i + 1)
                list_change.append(d)

    if "e" in data:
        number_of = data.count("e")
        # For 3
        for i in range(number_of):
            for j in range(i, number_of):
                d = replacer_letter(data, "e", "3", number_of - j, i + 1)
                list_change.append(d)
        # For &
        for i in range(number_of):
            for j in range(i, number_of):
                d = replacer_letter(data, "e", "&", number_of - j, i + 1)
                list_change.append(d)

    if "l" in data:
        number_of = data.count("l")
        # For 1
        for i in range(number_of):
            for j in range(i, number_of):
                d = replacer_letter(data, "l", "1", number_of - j, i + 1)
                list_change.append(d)
        # For !
        for i in range(number_of):
            for j in range(i, number_of):
                d = replacer_letter(data, "l", "!", number_of - j, i + 1)
                list_change.append(d)

    if "i" in data:
        number_of = data.count("i")
        # For 1
        for i in range(number_of):
            for j in range(i, number_of):
                d = replacer_letter(data, "i", "1", number_of - j, i + 1)
                list_change.append(d)
        # For !
        for i in range(number_of):
            for j in range(i, number_of):
                d = replacer_letter(data, "i", "!", number_of - j, i + 1)
                list_change.append(d)

    if "s" in data:
        number_of = data.count("s")
        # For 5
        for i in range(number_of):
            for j in range(i, number_of):
                d = replacer_letter(data, "s", "5", number_of - j, i + 1)
                list_change.append(d)
        # For $
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

def transformation_name_surname(name, surname):
    s_name = []
    for s in surname.split(" "):
        s_name = s_name + transformation_surname(name + " " + s)
    s_name = s_name + transformation_surname(name + " " + surname)
    return s_name

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
############################################################################################################
def program(all_info:dict):
    wordlist_list = []
    print(Cyan+"\n\n#####################################################################")
    print("######################## Starting Generation ########################")
    print(Cyan + "#####################################################################\n"+Reset)

    if "personal_info" in all_info:
        # Personal Info
        personal = all_info["personal_info"]
        print("\n================================================================")
        print(Bold_Cyan+"[+] Transformations Personal"+Reset)
        print("================================================================\n")
        if personal["Personal_Name"] is not None:
            print(Bold_Yellow+"[*] Transformation Name... "+Reset,end="")
            personal_name = sorted(remove_duplicate(transformation_name(personal["Personal_Name"])))
            wordlist_list = wordlist_list + personal_name
            print(Bold_Green+"OK"+Reset)

        if personal["Personal_Surnames"] is not None:
            print(Bold_Yellow+"[*] Transformation surname... "+Reset,end="")
            personal_surname = sorted(remove_duplicate(transformation_surname(personal["Personal_Surnames"])))
            wordlist_list = wordlist_list + personal_surname
            print(Bold_Green+"OK"+Reset)

        if personal["Personal_Nickname"] is not None:
            print(Bold_Yellow+"[*] Transformation nickname... "+Reset,end="")
            personal_nickname = sorted(remove_duplicate(transformation_name(personal["Personal_Nickname"])))
            wordlist_list = wordlist_list + personal_nickname
            print(Bold_Green+"OK"+Reset)

        if personal["Personal_Birthday"] is not None:
            print(Bold_Yellow+"[*] Transformation birthday... "+Reset,end="")
            personal_birthday = sorted(remove_duplicate(transformation_date(personal["Personal_Birthday"])))
            wordlist_list = wordlist_list + personal_birthday
            print(Bold_Green+"OK"+Reset)

        if personal["Pet_Name"] is not None:
            print(Bold_Yellow+"[*] Transformation petname... "+Reset,end="")
            pet_name = sorted(remove_duplicate(transformation_name(personal["Pet_Name"])))
            wordlist_list = wordlist_list + pet_name
            print(Bold_Green+"OK"+Reset)

        if personal["Company_Name"] is not None:
            print(Bold_Yellow+"[*] Transformation company... "+Reset,end="")
            company_name = sorted(remove_duplicate(transformation_company_school(personal["Company_Name"])))
            wordlist_list = wordlist_list + company_name
            print(Bold_Green+"OK"+Reset)

        if personal["Personal_Name"] is not None and personal["Personal_Surnames"] is not None:
            print(Bold_Yellow+"[*] Transformation name & surname... "+Reset,end="")
            personal_name_surname = sorted(remove_duplicate(transformation_name_surname(personal["Personal_Name"],personal["Personal_Surnames"])))
            wordlist_list = wordlist_list + personal_name_surname
            print(Bold_Green+"OK"+Reset)

        if personal["Personal_Name"] is not None and personal["Personal_Nickname"] is not None:
            print(Bold_Yellow+"[*] Transformation name & nickname... "+Reset,end="")
            personal_name_nickname = sorted(remove_duplicate(transformation_name_surname(personal["Personal_Name"],personal["Personal_Nickname"])))
            wordlist_list = wordlist_list + personal_name_nickname
            print(Bold_Green+"OK"+Reset)

        if personal["Personal_Surnames"] is not None and personal["Personal_Nickname"] is not None:
            print(Bold_Yellow+"[*] Transformation nickname & surname... "+Reset,end="")
            personal_nickname_surname = sorted(remove_duplicate(transformation_name_surname(personal["Personal_Nickname"],personal["Personal_Surnames"])))
            wordlist_list = wordlist_list + personal_nickname_surname
            print(Bold_Green+"OK"+Reset)

        if personal["Personal_Name"] is not None and personal["Pet_Name"] is not None:
            print(Bold_Yellow+"[*] Transformation name & petname... "+Reset,end="")
            personal_name_petname = sorted(remove_duplicate(transformation_name_surname(personal["Personal_Name"],personal["Pet_Name"])))
            wordlist_list = wordlist_list + personal_name_petname
            print(Bold_Green+"OK"+Reset)

        if personal["Personal_Nickname"] is not None and personal["Pet_Name"] is not None:
            print(Bold_Yellow+"[*] Transformation name & petname... "+Reset,end="")
            personal_nickname_petname = sorted(remove_duplicate(transformation_name_surname(personal["Personal_Nickname"],personal["Pet_Name"])))
            wordlist_list = wordlist_list + personal_nickname_petname
            print(Bold_Green+"OK"+Reset)


        if personal["Personal_Birthday"] is not None:
            dat00 = wordlist_list.copy()
            print(Bold_Yellow+"[*] Transformation name & surname & nickname & birthday... "+Reset,end="")
            personal_nsk_birthday = sorted(remove_duplicate(transformation_nsk_birthday(dat00, personal["Personal_Birthday"])))
            wordlist_list = wordlist_list + personal_nsk_birthday
            print(Bold_Green+"OK"+Reset)

    if "conjoint_info" in all_info:
        conjoint = all_info["conjoint_info"]
        print("\n================================================================")
        print(Bold_Cyan+"[+] Transformation Conjoint"+Reset)
        print("================================================================\n")
        if conjoint["Conjoint_Name"] is not None:
            print(Bold_Yellow+"[*] Transformation Conjoint Name... "+Reset,end="")
            conjoint_name = sorted(remove_duplicate(transformation_name(conjoint["Conjoint_Name"])))
            wordlist_list = wordlist_list + conjoint_name
            print(Bold_Green+"OK"+Reset)

        if conjoint["Conjoint_Surnames"] is not None:
            print(Bold_Yellow+"[*] Transformation Conjoint Surname... "+Reset,end="")
            conjoint_surname = sorted(remove_duplicate(transformation_surname(conjoint["Conjoint_Surnames"])))
            wordlist_list = wordlist_list + conjoint_surname
            print(Bold_Green+"OK"+Reset)

        if conjoint["Conjoint_Birthday"] is not None:
            print(Bold_Yellow+"[*] Transformation Conjoint Birthday... "+Reset,end="")
            conjoint_birthday = sorted(remove_duplicate(transformation_date(conjoint["Conjoint_Birthday"])))
            wordlist_list = wordlist_list + conjoint_birthday
            print(Bold_Green+"OK"+Reset)

        if conjoint["Conjoint_Name"] is not None and conjoint["Conjoint_Surnames"] is not None:
            print(Bold_Yellow+"[*] Transformation conjoint name & surname... "+Reset,end="")
            conjoint_name_surname = sorted(remove_duplicate(transformation_name_surname(conjoint["Conjoint_Name"],conjoint["Conjoint_Surnames"])))
            wordlist_list = wordlist_list + conjoint_name_surname
            print(Bold_Green+"OK"+Reset)

        if conjoint["Conjoint_Name"] is not None and personal["Personal_Name"] is not None:
            print(Bold_Yellow+"[*] Transformation conjoint name & personal name... "+Reset,end="")
            conjoint_personal_name = sorted(remove_duplicate(transformation_name_surname(conjoint["Conjoint_Name"],personal["Personal_Name"])))
            wordlist_list = wordlist_list + conjoint_personal_name
            print(Bold_Green+"OK"+Reset)

        if conjoint["Conjoint_Name"] is not None and personal["Personal_Name"] is not None and conjoint["Conjoint_Surnames"] is not None and conjoint["Conjoint_Birthday"] is not None:
            print(Bold_Yellow+"[*] Transformation conjoint name & surname & birthday... "+Reset,end="")
            conjoint_ns = conjoint_name_surname + conjoint_personal_name
            conjoint_nsb = sorted(remove_duplicate(transformation_nsk_birthday(conjoint_ns,conjoint["Conjoint_Birthday"])))
            wordlist_list = wordlist_list + conjoint_nsb
            print(Bold_Green+"OK"+Reset)


    if "Child_info" in all_info:
        Child = all_info["Child_info"]
        print("\n================================================================")
        print(Bold_Cyan+"[+] Transformation Child"+Reset)
        print("================================================================\n")
        if Child["Child_Name"] is not None:
            print(Bold_Yellow+"[*] Transformation Child Name... "+Reset,end="")
            Child_name = sorted(remove_duplicate(transformation_name(Child["Child_Name"])))
            wordlist_list = wordlist_list + Child_name
            print(Bold_Green+"OK"+Reset)

        if Child["Child_Surnames"] is not None:
            print(Bold_Yellow+"[*] Transformation Child Surname... "+Reset,end="")
            Child_surname = sorted(remove_duplicate(transformation_surname(Child["Child_Surnames"])))
            wordlist_list = wordlist_list + Child_surname
            print(Bold_Green+"OK"+Reset)

        if Child["Child_Birthday"] is not None:
            print(Bold_Yellow+"[*] Transformation Child Birthday... "+Reset,end="")
            Child_birthday = sorted(remove_duplicate(transformation_date(Child["Child_Birthday"])))
            wordlist_list = wordlist_list + Child_birthday
            print(Bold_Green+"OK"+Reset)

        if Child["Child_School"] is not None:
            print(Bold_Yellow+"[*] Transformation School... "+Reset,end="")
            School_name = sorted(remove_duplicate(transformation_company_school(Child["Child_School"])))
            wordlist_list = wordlist_list + School_name
            print(Bold_Green+"OK"+Reset)

        if Child["Child_Name"] is not None and Child["Child_Surnames"] is not None:
            print(Bold_Yellow+"[*] Transformation Child name & surname... "+Reset,end="")
            Child_name_surname = sorted(remove_duplicate(transformation_name_surname(Child["Child_Name"],Child["Child_Surnames"])))
            wordlist_list = wordlist_list + Child_name_surname
            print(Bold_Green+"OK"+Reset)

        if Child["Child_Name"] is not None and personal["Personal_Name"] is not None:
            print(Bold_Yellow+"[*] Transformation Child name & personal name... "+Reset,end="")
            Child_personal_name = sorted(remove_duplicate(transformation_name_surname(Child["Child_Name"],personal["Personal_Name"])))
            wordlist_list = wordlist_list + Child_personal_name
            print(Bold_Green+"OK"+Reset)

        if Child["Child_Name"] is not None and personal["Personal_Name"] is not None and Child["Child_Surnames"] is not None and Child["Child_Birthday"] is not None:
            print(Bold_Yellow+"[*] Transformation Child name & surname & birthday... "+Reset,end="")
            Child_ns = Child_name_surname + Child_personal_name
            Child_nsb = sorted(remove_duplicate(transformation_nsk_birthday(Child_ns,Child["Child_Birthday"])))
            wordlist_list = wordlist_list + Child_nsb
            print(Bold_Green+"OK"+Reset)


    if "Father_info" in all_info:
        Father = all_info["Father_info"]
        print("\n================================================================")
        print(Bold_Cyan+"[+] Transformation Father"+Reset)
        print("================================================================\n")
        if Father["Father_Name"] is not None:
            print(Bold_Yellow+"[*] Transformation Father Name... "+Reset,end="")
            Father_name = sorted(remove_duplicate(transformation_name(Father["Father_Name"])))
            wordlist_list = wordlist_list + Father_name
            print(Bold_Green+"OK"+Reset)

        if Father["Father_Surnames"] is not None:
            print(Bold_Yellow+"[*] Transformation Father Surname... "+Reset,end="")
            Father_surname = sorted(remove_duplicate(transformation_surname(Father["Father_Surnames"])))
            wordlist_list = wordlist_list + Father_surname
            print(Bold_Green+"OK"+Reset)

        if Father["Father_Birthday"] is not None:
            print(Bold_Yellow+"[*] Transformation Father Birthday... "+Reset,end="")
            Father_birthday = sorted(remove_duplicate(transformation_date(Father["Father_Birthday"])))
            wordlist_list = wordlist_list + Father_birthday
            print(Bold_Green+"OK"+Reset)

        if Father["Father_Name"] is not None and Father["Father_Surnames"] is not None:
            print(Bold_Yellow+"[*] Transformation Father name & surname... "+Reset,end="")
            Father_name_surname = sorted(remove_duplicate(transformation_name_surname(Father["Father_Name"],Father["Father_Surnames"])))
            wordlist_list = wordlist_list + Father_name_surname
            print(Bold_Green+"OK"+Reset)

        if Father["Father_Name"] is not None and personal["Personal_Name"] is not None:
            print(Bold_Yellow+"[*] Transformation Father name & personal name... "+Reset,end="")
            Father_personal_name = sorted(remove_duplicate(transformation_name_surname(Father["Father_Name"],personal["Personal_Name"])))
            wordlist_list = wordlist_list + Father_personal_name
            print(Bold_Green+"OK"+Reset)

        if Father["Father_Name"] is not None and personal["Personal_Name"] is not None and Father["Father_Surnames"] is not None and Father["Father_Birthday"] is not None:
            print(Bold_Yellow+"[*] Transformation Father name & surname & birthday... "+Reset,end="")
            Father_ns = Father_name_surname + Father_personal_name
            Father_nsb = sorted(remove_duplicate(transformation_nsk_birthday(Father_ns,Father["Father_Birthday"])))
            wordlist_list = wordlist_list + Father_nsb
            print(Bold_Green+"OK"+Reset)

    if "Mother_info" in all_info:
        Mother = all_info["Mother_info"]
        print("\n================================================================")
        print(Bold_Cyan+"[+] Transformation Mother"+Reset)
        print("================================================================\n")
        if Mother["Mother_Name"] is not None:
            print(Bold_Yellow+"[*] Transformation Mother Name... "+Reset,end="")
            Mother_name = sorted(remove_duplicate(transformation_name(Mother["Mother_Name"])))
            wordlist_list = wordlist_list + Mother_name
            print(Bold_Green+"OK"+Reset)

        if Mother["Mother_Surnames"] is not None:
            print(Bold_Yellow+"[*] Transformation Mother Surname... "+Reset,end="")
            Mother_surname = sorted(remove_duplicate(transformation_surname(Mother["Mother_Surnames"])))
            wordlist_list = wordlist_list + Mother_surname
            print(Bold_Green+"OK"+Reset)

        if Mother["Mother_Birthday"] is not None:
            print(Bold_Yellow+"[*] Transformation Mother Birthday... "+Reset,end="")
            Mother_birthday = sorted(remove_duplicate(transformation_date(Mother["Mother_Birthday"])))
            wordlist_list = wordlist_list + Mother_birthday
            print(Bold_Green+"OK"+Reset)

        if Mother["Mother_Name"] is not None and Mother["Mother_Surnames"] is not None:
            print(Bold_Yellow+"[*] Transformation Mother name & surname... "+Reset,end="")
            Mother_name_surname = sorted(remove_duplicate(transformation_name_surname(Mother["Mother_Name"],Mother["Mother_Surnames"])))
            wordlist_list = wordlist_list + Mother_name_surname
            print(Bold_Green+"OK"+Reset)

        if Mother["Mother_Name"] is not None and personal["Personal_Name"] is not None:
            print(Bold_Yellow+"[*] Transformation Mother name & personal name... "+Reset,end="")
            Mother_personal_name = sorted(remove_duplicate(transformation_name_surname(Mother["Mother_Name"],personal["Personal_Name"])))
            wordlist_list = wordlist_list + Mother_personal_name
            print(Bold_Green+"OK"+Reset)

        if Mother["Mother_Name"] is not None and personal["Personal_Name"] is not None and Mother["Mother_Surnames"] is not None and Mother["Mother_Birthday"] is not None:
            print(Bold_Yellow+"[*] Transformation Mother name & surname & birthday... "+Reset,end="")
            Mother_ns = Mother_name_surname + Mother_personal_name
            Mother_nsb = sorted(remove_duplicate(transformation_nsk_birthday(Mother_ns,Mother["Mother_Birthday"])))
            wordlist_list = wordlist_list + Mother_nsb
            print(Bold_Green+"OK"+Reset)


    if "Brother_info" in all_info:
        Brother = all_info["Brother_info"]
        print("\n================================================================")
        print(Bold_Cyan+"[+] Transformation Brother"+Reset)
        print("================================================================\n")
        if Brother["Brother_Name"] is not None:
            print(Bold_Yellow+"[*] Transformation Brother Name... "+Reset,end="")
            Brother_name = sorted(remove_duplicate(transformation_name(Brother["Brother_Name"])))
            wordlist_list = wordlist_list + Brother_name
            print(Bold_Green+"OK"+Reset)

        if Brother["Brother_Surnames"] is not None:
            print(Bold_Yellow+"[*] Transformation Brother Surname... "+Reset,end="")
            Brother_surname = sorted(remove_duplicate(transformation_surname(Brother["Brother_Surnames"])))
            wordlist_list = wordlist_list + Brother_surname
            print(Bold_Green+"OK"+Reset)

        if Brother["Brother_Birthday"] is not None:
            print(Bold_Yellow+"[*] Transformation Brother Birthday... "+Reset,end="")
            Brother_birthday = sorted(remove_duplicate(transformation_date(Brother["Brother_Birthday"])))
            wordlist_list = wordlist_list + Brother_birthday
            print(Bold_Green+"OK"+Reset)

        if Brother["Brother_Name"] is not None and Brother["Brother_Surnames"] is not None:
            print(Bold_Yellow+"[*] Transformation Brother name & surname... "+Reset,end="")
            Brother_name_surname = sorted(remove_duplicate(transformation_name_surname(Brother["Brother_Name"],Brother["Brother_Surnames"])))
            wordlist_list = wordlist_list + Brother_name_surname
            print(Bold_Green+"OK"+Reset)

        if Brother["Brother_Name"] is not None and personal["Personal_Name"] is not None:
            print(Bold_Yellow+"[*] Transformation Brother name & personal name... "+Reset,end="")
            Brother_personal_name = sorted(remove_duplicate(transformation_name_surname(Brother["Brother_Name"],personal["Personal_Name"])))
            wordlist_list = wordlist_list + Brother_personal_name
            print(Bold_Green+"OK"+Reset)

        if Brother["Brother_Name"] is not None and personal["Personal_Name"] is not None and Brother["Brother_Surnames"] is not None and Brother["Brother_Birthday"] is not None:
            print(Bold_Yellow+"[*] Transformation Brother name & surname & birthday... "+Reset,end="")
            Brother_ns = Brother_name_surname + Brother_personal_name
            Brother_nsb = sorted(remove_duplicate(transformation_nsk_birthday(Brother_ns,Brother["Brother_Birthday"])))
            wordlist_list = wordlist_list + Brother_nsb
            print(Bold_Green+"OK"+Reset)

    if Path("src/rockyou10000.txt").is_file():
        print(Bold_Cyan+"\n[+] Addition the first 10000 lines of rockyou... "+Reset, end="")
        with open("src/rockyou10000.txt", "r") as r10:
            lines = [i.split("\n")[0] for i in r10.readlines()]
            wordlist_list = wordlist_list + lines
        print(Bold_Green+"OK"+Reset)
        print("================================================================\n")
    print(Bold_Cyan+"[*] Join all and writing... "+Reset,end="")
    wordlist_list = sorted(remove_duplicate(wordlist_list))
    output = "dict.txt"
    with open(output, "w") as d:
        d.write("\n".join(str(i) for i in wordlist_list))
        d.write("\n")
    print(Bold_Green+": OK"+Reset)

    print(Bold_Green+"\nThe Output of your wordlist can be found in: {}".format(os.path.abspath(output))+Reset)

#all_info = {
#    "personal_info": {
#        "Personal_Name": "Keen",
#        "Personal_Surnames": "Elisabeth",
#        "Personal_Nickname": "Profiler",
#        "Personal_Birthday": "15/12/1980",
#        "Pet_Name": null,
#        "Company_Name": "FBI"
#    },

#    "conjoint_info": {
#        "Conjoint_Name": "Keen",
#        "Conjoint_Surnames": "Tom",
#        "Conjoint_Birthday": "15/01/1982"
#    },

#    "Child_info": {
#        "Child_Name": "Keen",
#        "Child_Surnames": "Agness",
#        "Child_Birthday": "15/12/2015",
#        "Child_School": null
#    },

#    "Father_info": {
#        "Father_Name": "Reddington",
#        "Father_Surnames": "Raimond ray",
#        "Father_Birthday": "15/12/1940"
#    },

#    "Mother_info": {
#        "Mother_Name": "Rostova",
#        "Mother_Surnames": "Catalinna",
#        "Mother_Birthday": "10/10/1950"
#    },

#    "Brother_info": {
#        "Brother_Name": "Reddington",
#        "Brother_Surnames": "Jennifer",
#        "Brother_Birthday": "02/02/1985"
#    }
#}
#program(all_info)
############################################################################################################
############################################################################################################