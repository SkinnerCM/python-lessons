import input_processing

class ProblemGenerator:
    
    def __init__(self, game_instance, op):
        
        self.game_instance = game_instance
        self.op = op

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
    
    
    
    
    def get_usr_answer(self, num1, num2, ans):
          
        right_justify = max(len(str(num1)),len(str(num2)))
        
        usr_in = input(f'\nHey! Can you solve this? \n \n  {num1:>{right_justify}}\n'
                       f'{self.game_instance.op_dict[self.op][2]} {num2:>{right_justify}}\n' 
                       + (2+right_justify)*'-'+'\n')
        
        try:
            usr_in = int(usr_in)
            
        
            if usr_in == ans:

                self.game_instance.update_score()
                return input_processing.answer_processing(num1, num2, ans, self.op,'C')

            else:

                self.game_instance.update_score(correct=False)                
                return input_processing.answer_processing(num1, num2, ans, self.op,'I')

        except ValueError:

            print("\n\nPlease enter integer values only!")
        
        return self.get_usr_answer(num1, num2, ans)
