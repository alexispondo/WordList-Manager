ORDER = "0123456789aàáäåæbcçdeèéêfghiìíîjklmnñoòóôöøpqrsßtuùúüvwxyzžα"
# associate each char with the index in the string
# this makes sort faster for multiple invocations when compared with
# ORDER.index(c)
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

lst = ["abc", "ab", "aá"]
lst.sort()
print(lst)

lst = ["aAbc", "ab", "aá"]
lst.sort(key = MyStrOrder)
print(lst)