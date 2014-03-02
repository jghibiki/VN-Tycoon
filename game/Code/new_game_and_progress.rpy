screen game_button:
    textbutton "Make a game!" action Show("new_game")

screen new_game:
    add "#000"
    textbutton "Cancel" action Return()

screen game_progress:
    add "#000"
    textbutton "Cancel" action Return()