'''
Author: Daryll Osis
Date: April 5, 2018
Description: This program just adds and substracts numbers(list, tuple, float, int) and print it in the end. 
             The program takes multiple arguments, and thats the focus of this assignment, to be able to run 
             a program with one param, but with multiple arguments. also, a good practice for chaining methods.
'''

class MathDojo:
    def __init__(self):
        self.num = 0

    #adds 
    def add(self, *num): 
        for x in num:
            if type(x) == list:
                for y in x:
                    self.num += y
            elif type(x) == int:
                self.num += x
            elif type(x) == tuple:
                for y in x:
                    self.num += y
        return self

    #subtracts
    def subtract(self, *num):
        for x in num:
            if type(x) == list:
                for y in x:
                    self.num -= y
            elif type(x) == int:
                self.num -= x
            elif type(x) == tuple:
                for y in x:
                    self.num -= y
        return self

    #method to print out the result
    def result(self):
        print(self.num)


md = MathDojo()
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract((2,2), [2,3], [1.1,2.3]).result()





