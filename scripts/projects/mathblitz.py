#!/usr/bin/env python3

op_dict = {'add': ['Addition', 'adding', '+'],
           'sub': ['Subtraction', 'subtracting', '-'],
           'mult': ['Multiplicaiton', 'multiplying', '\u00D7'],
           'div': ['Division', 'dividing', '\u00F7']
               }

def mathblitz():
    
    sp = '                                                        '
    print('\n\n\n')
    print(sp+"          ++++           |                         ")
    print(sp+"          ++++           |                         ")
    print(sp+"          ++++           |                         ")
    print(sp+"   ++++++++++++++++++    |    |||||||||||||||||    ")
    print(sp+"   ++++++++++++++++++    |    |||||||||||||||||    ")
    print(sp+"          ++++           |                         ")
    print(sp+"          ++++           |                         ")
    print(sp+"          ++++           |                         ")
    print(sp+"                         |                         ")
    print(sp+" ________________________|_______________________  ")
    print(sp+"                         |                         ")
    print(sp+"                         |            _            ")              
    print(sp+"       XXX    XXX        |           ( )           ")          
    print(sp+"        XXX  XXX         |            ‾            ")
    print(sp+"          XXXX           |      |||||||||||||      ")
    print(sp+"        XXX  XXX         |            _            ")
    print(sp+"       XXX    XXX        |           ( )           ")
    print(sp+"                         |            ‾            ")
    print(sp+"                         |                         ")
    print("\n\n"+sp+"             ***Welcome to MathBlitz!!*** \n\n")

        
    main_loop = True
    
    input()
    
    while main_loop:
        
        print("\n\n\n")
        print(sp+"Main menu: ")
        print(sp+"----------")
        
        print(sp+"1) Addition ")
        print(sp+"2) Subtraction ")
        print(sp+"3) Multiplication ")
        print(sp+"4) Division ")
        print('\n')
        
        score=0
        
        print('Score: '+ str(score))
    
        
        op = input(sp+"Which arithmetic operation would you like to practice? " 
                  "(Enter 'Q' to quit) ")
        
        if op == 'Q' or op == 'q':
            
            main_loop = False
 
        elif op  == '1':

            op_menu('add')

        elif op  == '2':

            op_menu('sub')
            
        elif op  == '3':

            op_menu('mult')
            
        elif op == '4':
            op_menu('div')
            
        else:            
            print('\n'+sp+"Please enter a digit 1-4 or 'Q' to quit! ")
            
            


def op_menu_message(op):

    message = f'***Welcome to MathBlitz: {op_dict[op][0]}***'
    print("\n\n" + message + " \n"+len(message)*"_"+"\n")
    if op != 'div':
          print(f"\nHow many digits would you like to practice {op_dict[op][1]}?") 
    
def num_gen(num_digit=None, numer_digit=None, denom_digit=None):
    
    import random as rnd
    
    if num_digit==None:
        
        num2 = rnd.randint(1,10**denom_digit)
        
        num1=10**100
        
        while num1/(10**numer_digit) > 1:
            
            num1 = num2*rnd.randint(1,10**(numer_digit-denom_digit+1))
    
    else:
        # generate the random numbers
        num1 = rnd.randint(1,10**num_digit)
        num2 = rnd.randint(1,10**num_digit)
    
    return num1, num2

def op_menu(op):
    

    op_loop = True
    
    while op_loop:
        op_menu_message(op)
        
        if op == 'div':
            numer_digit = input("How many digits would you like the dividend to be?"
                        "(or enter 'M' to return to the menu) ")
            
            if numer_digit == 'M' or numer_digit == 'm':
                op_loop = False
                break
            
            while type(numer_digit) != int:
                
                try:
                    numer_digit = int(numer_digit)
                except:
                    numer_digit = input("Please enter only a positive integer!\n")
                
            denom_digit = input("How many digits would you like the divisor to be? ")
            
            while type(denom_digit) != int:
                
                try:
                    denom_digit = int(denom_digit)
                except:
                    denom_digit = input("Please enter only a positive integer!\n")
            
            
        else: 
            
            num_digit = input("(Enter a positive integer, or 'M' to return to the menu): ")
        
            if num_digit == 'M' or num_digit == 'm':
                
                op_loop = False
                break
            
            while type(num_digit) != int:
                
                    try:
                        num_digit = int(num_digit)
                    except:
                        num_digit = input("Please enter only a positive integer!\n")
        

        
        # Initialize for inner while loop
        op_solver = True

        while op_solver:
            
            if op == 'div': 
                num1, num2 = num_gen(numer_digit=numer_digit, denom_digit=denom_digit)
                ans = num1/num2
                
            else:
                
                num1, num2 = num_gen(num_digit=num_digit)

                if op == 'add':
                    ans = num1+num2
                elif op == 'sub':
                    ans = num1-num2
                elif op == 'mult':
                    ans = num1*num2
                

            op_solver = get_usr_answer(num1, num2, ans, op)

def get_usr_answer(num1, num2, ans, op):
  
    right_justify = max(len(str(num1)),len(str(num2)))
    
    usr_in = input(f'Hey! Can you solve this? \n \n  {num1:>{right_justify}}\n'
                   f'{op_dict[op][2]} {num2:>{right_justify}}\n' 
                   + (2+right_justify)*'-'+'\n')
    
    try:
        usr_in = int(usr_in)
        
    
        if usr_in == ans:

            return answer_processing(num1, num2, ans, flag='C')

        else:
            
            return answer_processing(num1, num2, ans, flag='I')

    except:

        print("\n\nPlease enter integer values only!")
        
        return get_usr_answer(num1, num2, ans)


def answer_processing(num1, num2, ans, flag='C'):
    
    if flag == 'C':
        
        usr_in = input("\nCongratulations! Enter 'M' to return to the previous menu, or enter any other key to try another problem: ")
        
    else:
        
        usr_in = input("\nOooof! Not quite. Enter 'M' to return to the previous menu, or enter any other key to try again: ")

    
    if usr_in == "M" or usr_in == 'm':

        return False

    elif flag == 'C':

        return True 

    else:
        return get_usr_answer(num1, num2, ans)
mathblitz()