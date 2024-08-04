class Person:
    __name = ""
    __kor = 0
    __eng = 0
    __math = 0
    __summ = 0
    __avg = 0.0

    def setName(self, name):
        self.__name = name
    def setKorScore(self, kor):
        self.__kor = kor
    def setEngScore(self, eng):
        self.__eng = eng
    def setMathScore(self, math):
        self.__math = math
    def setAll(self, name, kor, eng, math):
        self.__name = name
        self.__kor = kor
        self.__eng = eng
        self.__math = math
    def calculateAll(self):
        self.__summ = self.__kor + self.__eng + self.__math
        self.__avg = self.__summ / 3.0
    def getName(self):
        return self.__name
    def getKor(self):
        return self.__kor
    def getEng(self):
        return self.__eng
    def getMath(self):
        return self.__math
    def getSum(self):
        return self.__summ
    def getAvg(self):
        return self.__avg
    def showStatus(self):
        print "name:", self.__name
        print "kor: %3d, eng: %3d, math: %3d" % (self.__kor, self.__eng, self.__math)
        print "sum: %3d, avg: %.2f" % (self.__summ, self.__avg)

JohnKim = Person()

JohnKim.setName("John Kim")
JohnKim.setKorScore(76)
JohnKim.setEngScore(98)
JohnKim.setMathScore(79)
JohnKim.calculateAll()
JohnKim.showStatus()
