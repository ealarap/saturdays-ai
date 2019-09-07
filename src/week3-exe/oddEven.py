#!/usr/bin/python

import datetime

class OddEven:
	
    def __init__(self):
        self.name
        self.age
        
    def readData(self):
        print("Enter a number:")
        self.number=int(input())
        print("Enter a second number:")
        self.number2=int(input())
        print("Enter a number to divide second number")
        self.div = int(input())

    def isNumEven(self):
        #currentYear = datetime.datetime.now().year
        isEven = 1 if self.number%2 == 0 else 0
        print("Number {} is {} ".format(self.number, "Even" if isEven==1 else "Odd"))

    def isNumMultOf4(self): 
        isMultof4 =  1 if self.number%4 == 0 else 0
        print("Number {} is {} multiple of number 4 ".format(self.number, "a" if isMultof4==1 else "not a"))

    def areNumsMults(self):
        areMults = 1 if self.number2 % self.div == 0 else 0
        print("Number {}, {} divide evenly by number  {}".format(self.number2, "does" if areMults == 1 else "does not", self.div))


def main():
    IsEven = OddEven();
    IsEven.readData()
    IsEven.isNumEven()
    IsEven.isNumMultOf4()
    IsEven.areNumsMults()

if __name__ == '__main__':
    main()
