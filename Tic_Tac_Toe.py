
# coding: utf-8

# In[ ]:



print ("WELCOME TO TIC TAC TOE\n\nBy default 'Player 1' plays with 'X' and 'Player 2' plays with 'O'\n\nGood luck!")



while True:
    board = [1,2,3,4,5,6,7,8,9]
    def print_board():
        print ('\n')
        print (board[6],board[7],board[8])
        print (board[3],board[4],board[5])
        print (board[0],board[1],board[2])
        
    print_board()


    def win_search():
        
        if ((board[0] == 'x' or board[0] == 'o')  and 
            (board[1] == 'x' or board[1] == 'o')  and 
            (board[2] == 'x' or board[2] == 'o')  and 
            (board[3] == 'x' or board[3] == 'o')  and 
            (board[4] == 'x' or board[4] == 'o')  and 
            (board[5] == 'x' or board[5] == 'o')  and 
            (board[6] == 'x' or board[6] == 'o')  and 
            (board[7] == 'x' or board[7] == 'o')  and 
            (board[8] == 'x' or board[8] == 'o')): 
            print ("\nCAT'S GAME!")
            return True
        
        elif (board[6] == board[7] == board[8] == 'x' or 
            board[3] == board[4] == board[5] == 'x' or 
            board[0] == board[1] == board[2] == 'x' or  
            board[8] == board[5] == board[2] == 'x' or  
            board[6] == board[3] == board[0] == 'x' or
            board[7] == board[4] == board[1] == 'x' or
            board[6] == board[4] == board[2] == 'x' or
            board[8] == board[4] == board[0] == 'x'): 
            print ('\nGame Over! Player 1 WINS!') 
            return True

        elif (board[6] == board[7] == board[8] == 'o' or 
            board[3] == board[4] == board[5] == 'o' or 
            board[0] == board[1] == board[2] == 'o' or  
            board[8] == board[5] == board[2] == 'o' or  
            board[6] == board[3] == board[0] == 'o' or
            board[7] == board[4] == board[1] == 'o' or
            board[6] == board[4] == board[2] == 'o' or
            board[8] == board[4] == board[0] == 'o'): 
            print ('\nGame Over! Player 2 WINS!') 
            return True
        

    while True:
        if win_search() ==True:
            break

        def player_1():
            while True:
                inp = input ('\nPlayer 1, please enter a number for the board position choice: ')
                try: 
                    inp == int(inp)
                    if int(inp) in range(1,10):
                        if board [int(inp)-1] == 'x' or board [int(inp)-1] == 'o': 
                            print ('\nChoose another position on the board!')
                        else:
                            break
                    else: 
                        print ('\nHas to be a number from 1 to 9!')
                except:
                    print ('\nHas to be a number!')
            #for i in board:
            board[int(inp)-1]= 'x'
            print_board()
        player_1()

        if win_search() == True:
            break

        def player_2():
            while True:
                inp = input ('\nPlayer 2, please enter a number for the board position choice: ')
                try: 
                    inp == int(inp)
                    if int(inp) in range(1,10):
                        if board [int(inp)-1] == 'x' or board [int(inp)-1] == 'o': 
                            print ('\nChoose another position on the board!')
                        else:
                            break       
                    else: 
                        print ('\nHas to be a number from 1 to 9!')
                except:
                    print ('\nHas to be a number!')


            board[int(inp)-1]= 'o'
            print_board()
        player_2()
   
    
    play_again = input ('\nWould you like to play again? (Y/N): ')
    if play_again == 'Y' or play_again =='y': continue 
    else:
        break


