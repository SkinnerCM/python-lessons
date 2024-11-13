#!/usr/bin/env python3

"""
MathBlitz is an interactive math practice game that helps users improve their arithmetic skills. 
The game offers four types of operations: Addition, Subtraction, Multiplication, and Division. 
Users can select an operation and choose the difficulty level (by specifying the number of digits). 
For each operation, a random math problem is generated, and the user must provide the correct answer. 
The user's score is updated based on their performance, and they can choose to continue or exit at any point.

The game includes the following features:
- Score tracking: Users earn or lose points for correct or incorrect answers.
- Difficulty adjustment: Users can adjust the number of digits involved in the math problems.
- Repeated practice: After answering, users are given the option to try another problem or return to the main menu.
"""

class MathBlitz:

    op_dict = {'add': ['Addition', 'adding', '+'],
               'sub': ['Subtraction', 'subtracting', '-'],
               'mult': ['Multiplicaiton', 'multiplying', '\u00D7'],
               'div': ['Division', 'dividing', '\u00F7']
                   }

    def __init__(self):

        self.score = 0 

    def update_score(self, correct=True):

        if correct:
            self.score+=100
        else:
            self.score-=100

        print('\nScore: '+ str(self.score))

    def mathblitz(self):

        
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
            print(sp+"‾‾‾‾‾‾‾‾‾‾")
            
            print(sp+"1) Addition ")
            print(sp+"2) Subtraction ")
            print(sp+"3) Multiplication ")
            print(sp+"4) Division ")
            print('\n')
            
            
            print('Score: '+ str(self.score))
        
            
            op = input(sp+"Which arithmetic operation would you like to practice? " 
                      "(Enter 'Q' to quit) ")
            
            if op.lower() == 'q':
                
                main_loop = False
     
            elif op in ['1','2','3','4']:

                operation = ['add', 'sub', 'mult', 'div'][int(op)-1]
                self.op_menu(operation)
                
            else:            
                print('\n'+sp+"Please enter a digit 1-4 or 'Q' to quit! ")
                

    def op_menu_message(self, op):

        message = f'***Welcome to MathBlitz: {self.op_dict[op][0]}***'
        print("\n\n" + message + " \n"+len(message)*"_"+"\n")

        if op != 'div':
              print(f"\nHow many digits would you like to practice {self.op_dict[op][1]}?")

        
    def num_gen(self, num_digit=None, numer_digit=None, denom_digit=None):
        
        import random as rnd
        
        if num_digit==None:
            
            num2 = rnd.randint(1,10**denom_digit)
            
            num1=10**100
            
            while num1/(10**numer_digit) > 1:
                
                num1 = num2*rnd.randint(1,10**(numer_digit-denom_digit+1))
        
        else:
            # generate the random numbers
            num1 = rnd.randint(1,10**num_digit-1)
            num2 = rnd.randint(1,10**num_digit-1)
        
        return num1, num2

    def op_menu(self, op):
        
        op_loop = True
        
        while op_loop:

            self.op_menu_message(op)
            
            if op == 'div':

                numer_digit = input("Please enter 2 or greater for the"
                                    " number of digits of the dividend"
                            " (or enter 'B' to return to the menu) ")
                
                if numer_digit.lower() == 'b':
                    op_loop = False
                    break
                
                while type(numer_digit) != int:
                    
                    try:
                        numer_digit = int(numer_digit)
                        
                        if numer_digit < 2:
                            numer_digit=input("Please enter a positive integer 2 or greater!\n")
                        
                    except ValueError:
                        numer_digit = input("Please enter only a positive integer!\n")
                
                
                    
                denom_digit = input("How many digits would you like the divisor to be? ")
                
                while type(denom_digit) != int:
                    
                    try:
                        denom_digit = int(denom_digit)
                        
                        if denom_digit > numer_digit:
                            
                            denom_digit=input(f"Please enter a positive integer {numer_digit} or "
                                              "less!\n")

                    except ValueError:
                        denom_digit = input("Please enter only a positive integer!\n")
                
                
            else: 
                
                num_digit = input("(Enter a positive integer, or 'B' to return to the menu): ")
            
                if num_digit.lower() == 'b':
                    
                    op_loop = False
                    break
                
                while type(num_digit) != int:
                    
                        try:
                            num_digit = int(num_digit)
                        except ValueError:
                            num_digit = input("Please enter only a positive integer!\n")
            

            
            # Initialize for inner while loop
            op_solver = True

            while op_solver:
                
                if op == 'div': 
                    num1, num2 = self.num_gen(numer_digit=numer_digit, denom_digit=denom_digit)
                    ans = num1/num2
                    
                else:
                    
                    num1, num2 = self.num_gen(num_digit=num_digit)

                    ans = self.calculate_answer(num1, num2, op)
                    
                op_solver = self.get_usr_answer(num1, num2, ans, op)


    def calculate_answer(self, num1, num2, op):

        if op == 'add':
            ans = num1+num2

        elif op == 'sub':
            ans = num1-num2

        elif op == 'mult':
            ans = num1*num2

        return ans


    def get_usr_answer(self, num1, num2, ans, op):
      
        right_justify = max(len(str(num1)),len(str(num2)))
        
        usr_in = input(f'Hey! Can you solve this? \n \n  {num1:>{right_justify}}\n'
                       f'{self.op_dict[op][2]} {num2:>{right_justify}}\n' 
                       + (2+right_justify)*'-'+'\n')
        
        try:
            usr_in = int(usr_in)
            
        
            if usr_in == ans:

                self.update_score()
                return self.answer_processing(num1, num2, ans, op,'C')

            else:

                self.update_score(correct=False)                
                return self.answer_processing(num1, num2, ans, op,'I')

        except ValueError:

            print("\n\nPlease enter integer values only!")
            
            return self.get_usr_answer(num1, num2, ans,op)


    def answer_processing(self,num1, num2, ans, op, flag):
        
        if flag == 'C':
            
            usr_in = input("\nCongratulations! Enter 'B' to return to the previous menu, or enter any other key to try another problem: ")
            
        else:
            
            usr_in = input("\nOooof! Not quite. Enter 'B' to return to the previous menu, or enter any other key to try again: ")

        
        if usr_in.lower() == 'b':

            return False

        elif flag == 'C':

            return True 

        else:
            return self.get_usr_answer(num1, num2, ans, op)
        
MathBlitz().mathblitz()