import op_menu

class MainMenu:

    def __init__(self):

        pass

    def mathblitz(self, game_instance):

        
        sp = 50*' '

        print('\n\n\n')
        print(sp+"           __            |                         ")
        print(sp+"          |  |           |                         ")
        print(sp+"          |  |           |                         ")
        print(sp+"     _____|  |_____      |      ______________     ")
        print(sp+"    |              |     |     |              |    ")
        print(sp+"     ‾‾‾‾‾|  |‾‾‾‾‾      |      ‾‾‾‾‾‾‾‾‾‾‾‾‾‾     ")
        print(sp+"          |  |           |                         ")
        print(sp+"          |  |           |                         ")
        print(sp+"           ‾‾            |                         ")
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


            print(f'Score: {game_instance.score}')


            op = input(sp+"Which arithmetic operation would you like to practice? " 
                    "(Enter 'Q' to quit) ")

            if op.lower() == 'q':
                
                main_loop = False

            elif op in ['1','2','3','4']:

                operation = ['add', 'sub', 'mult', 'div'][int(op)-1]
                
                OpMenu = op_menu.OpMenu(game_instance,operation)
                OpMenu.op_menu()
                
            else:            
                print('\n'+sp+"Please enter a digit 1-4 or 'Q' to quit! ")

        return False


