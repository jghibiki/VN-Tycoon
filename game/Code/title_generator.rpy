

init python:
    def nameGen():
        first_title_type = random.choice(["noun", "adjective"])
        if first_title_type == "noun":
            #nouns:
            if mygame.genre=="mystery":
                title1 = random.choice(["The Butler", "Labyrinth", "Secret", "Killing", "Invisibility"])
            if mygame.genre=="comedy":
                title1 = random.choice(["The Cake", "Hitler", "Panda", "Uncle", "The Toilet"])
            if mygame.genre=="horror":    
                title1 = random.choice(["Danger", "Silent", "Bat", "A Devil", "The Blade"])
            if mygame.genre=="sci-fi":    
                title1 = random.choice(["Scientist", "Planet", "The Robot", "The Alien", "The Power"])
            if mygame.genre=="romance":
                title1 = random.choice(["The Lip", "The Kiss", "Touch", "Dreamer", "Mist"])
            if mygame.genre=="fantasy":    
                title1 = random.choice(["Fellowship", "The Prince", "The Caesar", "Sorcery", "Big Guard"])
            if mygame.genre=="slice":    
                title1 = random.choice(["Nobody", "Boy", "People", "Second Brother", "Someone"])
        else:#adjectives
            if mygame.genre=="mystery":
                title1 = random.choice(["Misty", "Misterious", "The Missing", "The Sleeping", "The Invisible"])
            if mygame.genre=="comedy":
                title1 = random.choice(["Delicious", "The Laughing", "The Smelly", "Pink", "The Laughing"])
            if mygame.genre=="horror":
                title1 = random.choice(["Silent", "The Zombified", "Burning", "The Bloody", "The Corrupt"])
            if mygame.genre=="sci-fi":    
                title1 = random.choice(["Interstellar", "Infinite", "Mutated", "The Extraordinary", "The 10th"])
            if mygame.genre=="romance":
                title1 = random.choice(["Wet", "Pervy", "The Wild", "Lonely", "The Hot"])
            if mygame.genre=="fantasy":    
                title1 = random.choice(["The Witches's", "Magical", "Immortal", "Undead", "Brave"])
            if mygame.genre=="slice":    
                title1 = random.choice(["Magnificent ", "Dying", "Blue", "Naked", "The Boring"])

        if first_title_type == "noun":
            if mygame.relationship=="bxg":
                title2 = random.choice(["of Truth", "of the Fire", "is a Lie!", "in Tears", "Beyond Imaginary"])
            if mygame.relationship=="bxb":
                title2 = random.choice(["of the Black Vampiric Pets", "and the Tentacle Monster", "and the Suicide", "is Supreme", "Departed"])
            if mygame.relationship=="gxb":
                title2 = random.choice(["in the World", "of Secret", "of Supreme Future", "On My Bed", "With Savage Mask"])
            if mygame.relationship=="gxg":
                title2 = random.choice(["in the Death", "of the River", "Cold Casket", "of Circus", "in the Bus"])
            if mygame.relationship=="none":
                title2 = random.choice(["about the Dracula", "of Grace", "with the Obsession", "and the Dragon", "of the Woman"])
        else:
            if mygame.relationship=="bxg":
                title2 = random.choice(["Night", "Someone", "Nobody", "Slave", "Husband"])
            if mygame.relationship=="bxb":
                title2 = random.choice(["Boyfriend", "Servant", "Stones", "Illusion", "Petals"])
            if mygame.relationship=="gxb":
                title2 = random.choice(["Healer", "Abyss", "Visions", "Alien", "Lover"])
            if mygame.relationship=="gxg":
                title2 = random.choice(["Past", "Tears", "Dragon", "Bride", "Twins"])
            if mygame.relationship=="none":
                title2 = random.choice(["Sword", "Wings", "Spirits", "Petals", "Rainbow"])

        # if mygame.gameplay=="vn":
            # title3 = random.choice(["", "", "", "", ""])
        # if mygame.gameplay=="kn":
            # title3 = random.choice(["", "", "", "", ""])
        # if mygame.gameplay=="rpg":
            # title3 = random.choice(["", "", "", "", ""])
        # if mygame.gameplay=="sim":
            # title3 = random.choice(["", "", "", "", ""])
            
        mygame.title = title1 + " " + title2
        return
