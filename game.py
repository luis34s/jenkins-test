def game(player1,player2):

    if (player1 == 'rock' and player2 == 'paper') or (player1 == 'paper' and player2 == 'scissors') or (player1 == 'scissors' and player2 == 'rock'):
            return 'player 2 wins'
            
    elif (player1 == 'rock' and player2 == 'scissors') or (player1 == 'paper' and player2 == 'rock') or (player1 == 'scissors' and player2 == 'paper'):
            return 'player 1 wins'
            
    elif  player1 == player2 :
            return 'nobody win'            
    else:
            return 'Try again'
        

    




    
  
