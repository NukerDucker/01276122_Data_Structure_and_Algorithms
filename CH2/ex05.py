
class funString():

    def __init__(self,string = ""):
        self.string = string

    def __str__(self):
        return self.string

    def size(self) :
        return len(self.string)

    def changeSize(self):
        new_string = self.string.swapcase()
        return new_string
    
    def reverse(self):
        new_string = self.string[::-1]
        return new_string

    def deleteSame(self):
        new_string = ""
        for i in self.string:
            if i not in new_string:
                new_string += i
        return new_string


str1, str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())
elif str2 == "2":  print(res.changeSize())
elif str2 == "3" : print(res.reverse())
elif str2 == "4" : print(res.deleteSame())