init python:
    userNames = []
    def make_user():
        import random   
        users1 = ["hard", "black", "angry", "happy", "tricky", "silly", "solid", "liquid", "friendly", "tsundere", "silver", "morpheus", "cool", "fatal", "evil", "kitty", "moe", "moemoe", "bara", "bishie", "ecchi", "gei", "loli", "shota", "mecha", "baka", "hime", "kami", "kawaii"]
        users2 = ["guard", "reset", "white", "darkness", "rabbit", "panda", "dragon", "snake", "fool", "sake", "wolf", "kid", "Z", "unicorn", "pcguy", "kitty", "cat", "fish", "catgirl", "dere", "guro", "chan", "kokoro", "oni"]
        users3 = ["tsundere", "morpheus", "kitty", "moemoe", "bishie", "shota", "reset", "panda", "dragon", "snake", "wolf", "unicorn", "pcguy", "catgirl", "kokoro", "akuma", "uragirimono", "2freenscr", "ChikkWriter", "DubyaMarsBillion", "MediumGhoul", "SizzlinFix", "slypedump", "vengeance", "coolediate", "EarSnoopy", "EasyPeasyLemonSqueezy", "Fantasymark"]
        
        if random.randint(1,4)==1:
            num_words = 1
        else:
            num_words = 2
        user2 = ""
        sep = ""
        
        user1 = random.choice (users1)
        if num_words==1:
            user1 = random.choice (users3)
         
        if random.choice (["cap", "no cap"]) == "cap":
            user1 = user1.title()

        if num_words>1:
            user2 = random.choice (users2)
            if random.choice (["cap", "no cap"]) == "cap":
                user2 = user2.title()
            else:
                sep = random.choice (["", " ", "_"])
                if random.randint(1,10)==5:
                    sep = random.choice (["And", "x", "The"])
                    user1 = user1.title()
                    user2 = user2.title()

        username=user1+sep+user2
        if username in userNames:
            username += random.choice (["007", "3000", "2000", "1", "42"])
        while username in userNames:
            username += str(random.randint(1,100))
        userNames.append(username)
        return username
    