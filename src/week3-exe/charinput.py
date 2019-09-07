#!/usr/bin/python

import datetime

class CharacterInput:
	
    def __init__(self):
        self.name
        self.age
        
    def readData(self):
        print("Enter your name:")
        self.name=input()
        print("Enter your age:")
        self.age=int(input())
        print("How many times do you want to receive the message?")
        self.repeat = int(input())

    def getDiffOfYears(self):
        currentYear = datetime.datetime.now().year
        diffYears = 100 - self.age
        yearTo100 = currentYear + diffYears
        print("{} you will turn into 100 years old on year: {}".format(self.name, yearTo100))
        for i in range(self.repeat):
            print("MSG {}, {} you will turn into 100 years old on year: {}".format(i, self.name, yearTo100))


def main():
    charinput = CharacterInput();
    charinput.readData()
    charinput.getDiffOfYears()

if __name__ == '__main__':
    main()
