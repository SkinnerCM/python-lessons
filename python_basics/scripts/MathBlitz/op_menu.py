import problem_generator
import input_processing

class OpMenu:
    
    def __init__(self, game_instance, op):
        
        self.game_instance = game_instance
        self.op = op
        
        pass

    def op_menu_message(self):
    
        message = f'***Welcome to MathBlitz: {self.game_instance.op_dict[self.op][0]}***'
        print("\n\n" + message + " \n"+len(message)*"_"+"\n")
    
        if self.op != 'div':
              print(f"\nHow many digits would you like to practice {self.game_instance.op_dict[self.op][1]}?")

    def op_menu(self):
        
        op_loop = True
        
        while op_loop:
    
            self.op_menu_message()
            
            if self.op == 'div':
    
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
            
            ProblemGenerator = problem_generator.ProblemGenerator(self.game_instance, self.op)
            
            
    
            while op_solver:
                
                if self.op == 'div': 
                    num1, num2 = ProblemGenerator.num_gen(numer_digit=numer_digit, denom_digit=denom_digit)
                    ans = num1/num2
                    
                else:
                    
                    num1, num2 = ProblemGenerator.num_gen(num_digit=num_digit)
    
                    ans = input_processing.calculate_answer(num1, num2, self.op)
                    
                op_solver = ProblemGenerator.get_usr_answer(num1, num2, ans)