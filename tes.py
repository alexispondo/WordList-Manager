def custum_sort(lst):
    #ORDER = "0123456789aàáäåæbcçdeèéêfghiìíîjklmnñoòóôöøpqrsßtuùúüvwxyzžα"
    #ORDER = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
    ORDER = '0123456789aAàáäåbBcCçdDeEèéêfFgGhHiIìíîjJkKlLmMnNñoOòóôöøpPqQrRsSßtTuUùúüvVwWxXyYzZžα!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
    POS = {c:p for (p, c) in enumerate(ORDER)}
    class MyStrOrder:
        def __init__(self, inner):
            self.inner = inner

        def __lt__(self, other):
            for i in range(min(len(self.inner), len(other.inner))):
                a = POS.get(self.inner[i])
                b = POS.get(other.inner[i])
                if a != b:
                    return a < b
            return len(self.inner) < len(other.inner)

    lst = ["JabcJJJA", "ab", "aá"]
    lst.sort()
    print(lst)

    lst = ["JabcJ", "ab", "aá"]
    lst=sorted(lst,key = MyStrOrder)
    print(lst)

