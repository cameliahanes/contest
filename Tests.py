'''
Created on 31 oct. 2016

@author: Camelia
'''
from operationsRequired import*

def TestInit(l):
    a = (5, 6, 10)
    l.append(a)
    a = (3, 9, 8)
    l.append(a)
    a = (7, 7, 5)
    l.append(a)
    a = (10, 6, 9)
    l.append(a)    
    a = (7, 8, 7)
    l.append(a)
    a = (2, 10, 3)
    l.append(a)
    a = (9, 4, 8)
    l.append(a)
    a = (8, 8, 2)
    l.append(a)
    a = (10, 10, 10)
    l.append(a)
    a = (9, 8, 10)
    l.append(a)
    a = (5, 10, 9)
    l.append(a)

def TestAddResultsToList():
    l = []
    TestInit(l)
    assert len(l)==11
    a = (10, 9, 9)
    AddResultsToList(l, a)
    assert len(l)==12
    assert l[len(l)-1]==(10, 9, 9)

def TestInsertResultsInList():
    l = []
    TestInit(l)
    assert len(l) == 11
    a = (1, 1, 1)
    InsertResultsInList(l, a, 2)
    assert len(l) == 12
    assert l[3]==(7, 7, 5)
    assert l[2]==(1, 1, 1)

def TestRemoveAtPositionGiven():
    l = []
    TestInit(l)
    RemoveAtPositionGiven(l, 2)
    assert l[2]==(0, 0, 0)

def TestRemoveFromStartToEnd():
    l = []
    TestInit(l)
    start = 5
    end = 7
    RemoveFromStartToEnd(l, start, end)
    assert l[5]==(0, 0, 0)
    assert l[6]==(0, 0, 0)
    assert l[7]==(0, 0, 0)
    assert l[8]==(10, 10, 10)

def TestReplaceDatesAtPositionGiven():
    l = []
    TestInit(l)
    #5,6,10 initially at position 0
    ReplaceDatesAtPositionGiven(0, l, 2, 7)
    assert l[0] == (5, 7, 10)
    #(2, 10, 3) at pos 5 initially
    ReplaceDatesAtPositionGiven(5, l, 3, 10)
    assert l[5] == (2, 10, 10)

def TestSortList():
    l = []
    TestInit(l)
    arr = []
    for i in range(len(l)):
        arr.append((AveragePerStudent(l[i])))
    listt = sortList(l, arr)


def TestThan():
    l = []
    TestInit(l)
    assert len(LessThan(l, 5))==0
    assert len(GreaterThan(l, 6))==9
    assert len(EqualTo(l, 10)==1)
    

def TestAverage():
    l = []
    TestInit(l)
    assert AverageOfAveragesBetweenPositions(l, 1, 4)==7.166666666666667
    assert AverageOfAveragesBetweenPositions(l, 2, 4)==7.333333333333333
    assert AverageOfAveragesBetweenPositions(l, 6, 7)==6.5

def TestMin():
    l = []
    TestInit(l)
    assert MinOfAveragesBetweenPositions(l, 1, 3)==6.333333333333333
    assert MinOfAveragesBetweenPositions(l, 2, 7)==5.0
    assert MinOfAveragesBetweenPositions(l, 7, 9)==6.0

def RunAllTests():
    TestAddResultsToList()
    TestInsertResultsInList()
    TestRemoveAtPositionGiven()
    TestRemoveFromStartToEnd()
    TestReplaceDatesAtPositionGiven()
    TestSortList()
    TestAverage()
    TestMin()
