import  re

class human:
    def __init__(self, gender):
        self.gender =gender

    def __str__(self):
        return str(self.gender)

    def getGender(self):
        return self.gender
class boy(human):
    def __init__(self, gender):
        self.gender = gender

class girl(human):
    def __init__(self, gender):
        self.gender = gender


guy = boy("M")

oneBoy = guy.getGender().__str__()

mathcherBoy = re.search(r"M", oneBoy,re.M|re.I)
mathcherGirl= re.search(r"M", oneBoy,re.M|re.I)

if mathcherBoy:
    print("公的")
elif mathcherGirl:
    print("母的")
else:
    print("跨性別者")