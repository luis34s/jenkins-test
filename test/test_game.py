from game import game

def test_game_01():
    assert game('rock','scissors') == 'player 1 wins', 'Unespected result'
    assert game('scissors','rock') == 'player 2 wins', 'Unespected result'
    assert game('scissors','paper') == 'player 1 wins', 'Unespected result'


