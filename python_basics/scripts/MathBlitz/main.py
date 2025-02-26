#!/usr/bin/env python3


"""
-----------------------------------------------------------------------------------------------------------------------------------
 Author: Colin M. Skinner
 Date Created: 2024-08-02
 Last Modified: 2024-11-21
 Description:   MathBlitz is an interactive math practice game that helps users improve their arithmetic skills. 
                The game offers four types of operations: Addition, Subtraction, Multiplication, and Division. 
                Users can select an operation and choose the difficulty level (by specifying the number of digits). 
                For each operation, a random math problem is generated, and the user must provide the correct answer. 
                The user's score is updated based on their performance, and they can choose to continue or exit at any point.

                The game includes the following features:
                - Score tracking: Users earn or lose points for correct or incorrect answers.
                - Difficulty adjustment: Users can adjust the number of digits involved in the math problems.
                - Repeated practice: After answering, users are given the option to try another problem or return to the main menu.

 Dependencies:  
 Usage: 


 Notes: 
 ------------------------------------------------------------------------------------------------------------------------------------
"""
import main_menu

 
class MathBlitz:


    def __init__(self):

        self.score = 0 
        self.op_dict = {'add': ['Addition', 'adding', '+'],
                        'sub': ['Subtraction', 'subtracting', '-'],
                        'mult': ['Multiplication', 'multiplying', '\u00D7'],
                        'div': ['Division', 'dividing', '\u00F7']
                        }


    def update_score(self, correct=True):

        if correct:
            self.score+=100
        else:
            self.score-=100

        print('\nScore: '+ str(self.score))

    def run(self):
            
        menu = main_menu.MainMenu()

        while menu.mathblitz(self):
            pass


if __name__ == "__main__":
    
    game = MathBlitz()
    game.run()
