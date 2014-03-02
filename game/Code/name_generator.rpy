label name_gen:
    python:
        import random
        if mygame.genre=="mystery":
            title1 = random.choice(["The Butler", "Labyrinth", "Secret", "Killing", "The Invisible"])
        if mygame.genre=="comedy":
            title1 = random.choice(["Delicious", "Hitler", "Wild", "The Stolen", "The Sleeping"])
        if mygame.genre=="horror":    
            title1 = random.choice(["Danger", "Silent", "Bat", "A Devil", "The Corrupt"])
        if mygame.genre=="sci-fi":    
            title1 = random.choice(["Scientist", "Snake", "The Robot", "The Alien", "Nobody"])
        if mygame.genre=="romance":    
            title1 = random.choice(["The Lip", "Teacher", "Touch", "Dreamer", "Mist"])
        if mygame.genre=="fantasy":    
            title1 = random.choice(["The Ultimate", "The Prince", "The Caesar Without", "Sorcery", "Big Guard"])
        if mygame.genre=="drama":    
            title1 = random.choice(["The Weeping", "Boy", "People", "Second Brother", "Dream"])

        if mygame.relationship=="bxg":
            title2 = random.choice(["of Truth", "of the Fire", "Someone", "Dusk", "Beyond Imaginary"])
        if mygame.relationship=="bxb":
            title2 = random.choice(["of the Black Vampiric Pets", "Night", "and the Suicide", "is Supreme", "Departed"])
        if mygame.relationship=="gxb":
            title2 = random.choice(["Silence", "of Secret", "of Supreme Future", "On My Bed", "With Savage Mask"])
        if mygame.relationship=="gxg":
            title2 = random.choice(["in the Death", "of River", "Cold Casket", "of Circus", "the Bus"])
        if mygame.relationship=="none":
            title2 = random.choice(["Dracula", "of Grace", "Obsession", "Dragon", "of the Woman"])

        if mygame.gameplay=="vn":
            title3 = random.choice(["", "", "", "", ""])
        if mygame.gameplay=="kn":
            title3 = random.choice(["", "", "", "", ""])
        if mygame.gameplay=="rpg":
            title3 = random.choice(["", "", "", "", ""])
        if mygame.gameplay=="sim":
            title3 = random.choice(["", "", "", "", ""])
            
        mygame.title = title1 + " " + title2 + title3
    return