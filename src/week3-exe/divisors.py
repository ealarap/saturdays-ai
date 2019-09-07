#!/usr/bin/python

class Divisors:
	
    def __init__(self, number = 0):
        self.number = number
    
    def getData(self):
        print("Enter a number, to obtain divisors:")
        self.number=int(input())
        
    def isDivisor(self,elem):
        return True if self.number % elem == 0 else False 

    def getDivisors(self):
        filterDivisors = filter(self.isDivisor, list(range(1, self.number+1)))
        print("Divisor(s) of number {}  are {}".format(self.number, list(filterDivisors)))

def main():
    divisors = Divisors()
    divisors.getData()
    divisors.getDivisors()

if __name__ == '__main__':
    main()
