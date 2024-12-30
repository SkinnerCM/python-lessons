def calculate_answer(num1, num2, op):

        if op == 'add':
            ans = num1+num2

        elif op == 'sub':
            ans = num1-num2

        elif op == 'mult':
            ans = num1*num2

        return ans
   


def answer_processing(num1, num2, ans, op, flag):
    
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