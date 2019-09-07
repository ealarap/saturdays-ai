#!/usr/bin/python

class ListsIntersection:
	
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2
    
    def getListsIntersection(self):
        return list ( set( self.list1) & set( self.list2) )

def main():
	
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    lIntersection = ListsIntersection(a,b)
    intersec = lIntersection.getListsIntersection()
    print("Intersection of list a= {}, and b = {}, is: {}".format(a, b, intersec))

if __name__ == '__main__':
    main()
