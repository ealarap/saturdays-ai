#!/usr/bin/python

class LessThan:
	
    def __init__(self, listNums, th):
        self.listNums = listNums
        self.threshold =  th
        
    def isLessThan(self,elem):
        threshold = self.threshold
        return True if elem < threshold else False 

    def getFilterList(self):
        #currentYear = datetime.datetime.now().year
        filtList = filter(self.isLessThan, self.listNums)
        print("Fistered list: {} ".format(list(filtList)))

def main():
    listE = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    listEx = LessThan(listE, 5)
    listEx.getFilterList()

if __name__ == '__main__':
    main()
