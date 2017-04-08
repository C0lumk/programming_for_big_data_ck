# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 21:25:55 2017

@author: Colum
"""

#file no. 2 - defines the class Menu and its methods/instances

class Menu(object):
    
    def functionmenu():
            
        from Calculator import Calculator    
        
        def numinputs(user_prompt):
            while True:
                value = raw_input(user_prompt)
                try:
                    value = float(value)
                    return True
                    break
                except:    
                    print 'enter a numeric value'
    
        print 'Start by entering the first and second number'
        print 'Then, select a calculator function from the menu provided:'
        print 'Press 1 for add function'
        print 'Press 2 for subtract function'
        print 'Press 3 for multiply function'
        print 'Press 4 for divide function'
        print 'Press 5 for exponent function'
        print 'Press 6 for cube function'
        print 'Press 7 for square function'
        print 'Press 8 for exponential function'
        print 'Press 9 for rectangle perimeter function'
        print 'Press 10 for pythagorus function'
        print 'Press 11 for sine function'
        
        while True:
            myCalc = Calculator()
            
            first = numinputs('Enter first number: ')
            second = numinputs('Enter second number: ')
            
            operator = raw_input('Please select the calculator function required: ')
            if operator == '1':
                print myCalc.add(first,second)
            elif operator == '2':
                print myCalc.subtract(first,second)
            elif operator == '3':
                print myCalc.multiply(first,second)
            elif operator == '4':
                print myCalc.divide(first,second)
            elif operator == '5':
                print myCalc.exponent(first,second)
            elif operator == '6':
                print myCalc.cube(first)
            elif operator == '7':
                print myCalc.square(first)
            elif operator == '8':
                print myCalc.exponential(first)
            elif operator == '9':
                print myCalc.rectangleperimeter(first,second)
            elif operator == '10':
                print myCalc.pythagoras(first,second)
            elif operator == '11':
                print myCalc.sin(first)
            elif operator == 'done':    
                break
            else:
                print 'Invalid input'
                
    functionmenu()