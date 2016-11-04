'''
Created on 31 oct. 2016

@author: Camelia
'''
def readGrade():
    '''
    this fucntion reads an element and returns it if it is valid, otherwise the compiler raises an ValueError and
    forces the user to enter valid data
    '''
    result = -1
    while True:
        try:
            result = int(input(""))
            if int(result) >= 0 and int(result) <= 10:
                return result
            else:
                raise ValueError
        except ValueError:
            print ("You entered an invalid grade, try again.")

def ReadNewData():
    '''
    The function reads new data, three integers consisting of the grades obtained by the student at each
    problem;
    Input: -
    Output: a triplet, grades, with valid elements with respect to the contest's requirements, the grades must be
    from 0 to 10;
    '''
    while True:
        print("Enter the grade obtained for the first problem: ")
        p1 = readGrade()
        print("Now the grade obtain for the second problem: ")
        p2 = readGrade()
        print("And the third obtained grade: ")
        p3 = readGrade()
        grades = (p1, p2, p3)
        break
    return grades
