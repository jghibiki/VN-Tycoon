init:
    image mystery1 = "Assets/covers/mystery1.jpg"
    image mystery2 = "Assets/covers/mystery2.jpg"
    image comedy1 = "Assets/covers/comedy1.jpg"
    image comedy2 = "Assets/covers/comedy2.jpg"
    image horror1 = "Assets/covers/horror1.jpg"
    image horror2 = "Assets/covers/horror2.jpg"
    image scifi1 = "Assets/covers/scifi1.jpg"
    image scifi2 = "Assets/covers/scifi2.jpg"
    image romance1 = "Assets/covers/romance1.jpg"
    image romance2 = "Assets/covers/romance2.jpg"
    image fantasy1 = "Assets/covers/fantasy1.jpg"
    image fantasy2 = "Assets/covers/fantasy2.jpg"
    image slice1 = "Assets/covers/slice1.jpg"
    image slice2 = "Assets/covers/slice2.jpg"
    
    ###
    image azura angry smile large = "Assets/covers/azura angry smile large.png"
    image lee = "Assets/covers/lee-novelty-set-700.png"
    
init python:
    for expression in ["smile1", "smile2", "smile3", "smile4"]:
        for hair in ["black", "blue"]:
            for clothes in ["clothes1", "clothes2", "clothes3", "clothes4", "clothes5", "clothes6"]:
                for knife in ["knife", "noknife"]:
                    renpy.image("edgy_tan " + expression + " " + hair + " " + clothes + " " + knife, im.Composite (None, 
                        (0,0), "Assets/covers/edgytan_base.png",
                        (0,0), "Assets/covers/edgytan_" + clothes + ".png",
                        (0,0), "Assets/covers/edgytan_hair_" + hair + ".png",
                        (0,0), "Assets/covers/edgytan_mouth_" + expression + ".png",
                        (0,0), "Assets/covers/edgytan_" + knife + ".png",
                    ))
    
    for expression in ["wide", "frown", "small", "smile"]:
        for eyes in ["blink", "open", "wink", "closed"]:
            for clothes in ["uniform", "shirt", "jumper", "none"]:
                for eyebrows in ["happy", "normal", "frown"]:
                    for blush in ["blush", "none"]:
                        renpy.image("lee " + expression + " " + eyes + " " + clothes + " " + eyebrows + " " + blush, im.Composite (None, 
                            (0,0), "Assets/covers/lee_base.png",
                            (0,0), "Assets/covers/lee_" + clothes + ".png",
                            (0,0), "Assets/covers/lee_" + eyes + ".png",
                            (0,0), "Assets/covers/lee_" + expression + ".png",
                            (0,0), "Assets/covers/lee_eyebrows_" + eyebrows + ".png",
                            (0,0), "Assets/covers/lee_" + blush + ".png",
                        ))
    
    for expression in ["wide", "frown", "small", "smile"]:
        for eyes in ["eyes1", "eyes2", "eyes3", "eyes4"]:
            for clothes in ["uniform", "shirt", "none"]:
                for eyebrows in ["angry", "e1", "e2"]:
                    for blush in ["blush", "none"]:
                        renpy.image("aiden " + expression + " " + eyes + " " + clothes + " " + eyebrows + " " + blush, im.Composite (None, 
                            (0,0), "Assets/covers/aiden_base.png",
                            (0,0), "Assets/covers/aiden_" + clothes + ".png",
                            (0,0), "Assets/covers/aiden_" + eyes + ".png",
                            (0,0), "Assets/covers/aiden_" + expression + ".png",
                            (0,0), "Assets/covers/aiden_eyebrows_" + eyebrows + ".png",
                            (0,0), "Assets/covers/aiden_" + blush + ".png",
                        ))
    
    for expression in ["pout", "frown", "smile", "smile2"]:
        for eyes in ["closed", "blink", "half", "large"]:
            for clothes in ["jacket", "uniform", "shirt", "singlet", "shirt2", "none"]:
                for eyebrows in ["arched", "angry"]:
                    for blush in ["blush", "none"]:
                        renpy.image("azura " + expression + " " + eyes + " " + clothes + " " + eyebrows + " " + blush, im.Composite (None, 
                            (0,0), "Assets/covers/azura_base.png",
                            (0,0), "Assets/covers/azura_" + clothes + ".png",
                            (0,0), "Assets/covers/azura_" + eyes + ".png",
                            (0,0), "Assets/covers/azura_" + expression + ".png",
                            (0,0), "Assets/covers/azura_eyebrows_" + eyebrows + ".png",
                            (0,0), "Assets/covers/azura_" + blush + ".png",
                        ))

    for expression in ["open", "mouth2", "smile"]:
        for eyes in ["closed", "normal", "half"]:
            for clothes in ["dress", "uniform", "shirt", "shorts", "shirt2", "none"]:
                for eyebrows in ["normal", "worried", "arched", "linework"]:
                    for blush in ["blush", "none"]:
                        renpy.image("kyria " + expression + " " + eyes + " " + clothes + " " + eyebrows + " " + blush, im.Composite (None, 
                            (0,0), "Assets/covers/kyria_base.png",
                            (0,0), "Assets/covers/kyria_" + clothes + ".png",
                            (0,0), "Assets/covers/kyria_" + eyes + ".png",
                            (0,0), "Assets/covers/kyria_" + expression + ".png",
                            (0,0), "Assets/covers/kyria_eyebrows_" + eyebrows + ".png",
                            (0,0), "Assets/covers/kyria_" + blush + ".png",
                        ))


    for expression in ["mouth1", "mouth2", "mouth3", "mouth4", "mouth5", "mouth6", "mouth7", "mouth8", "mouth9"]:
        for eyes in ["eyes1", "eyes2", "eyes3", "eyes4", "eyes5", "eyes6"]:
            for clothes in ["dress", "none"]:
                for hair in ["hair1", "hair2", "hair3", "hair4", "hair5"]:
                    for glasses in ["glasses", "none"]:
                        for detail in ["angry", "sweat", "none"]:
                            for blush in ["blush", "none"]:
                                renpy.image("eileen " + expression + " " + eyes + " " + clothes + " " + hair + " " + glasses + " " + detail + " " + blush, im.Composite (None, 
                                    (0,0), "Assets/covers/eileen_base.png",
                                    (0,0), "Assets/covers/eileen_" + clothes + ".png",
                                    (0,0), "Assets/covers/eileen_" + eyes + ".png",
                                    (0,0), "Assets/covers/eileen_" + expression + ".png",
                                    (0,0), "Assets/covers/eileen_" + hair + ".png",
                                    (0,0), "Assets/covers/eileen_" + glasses + ".png",
                                    (0,0), "Assets/covers/eileen_" + detail + ".png",
                                    (0,0), "Assets/covers/eileen_" + blush + ".png",
                                ))

                        
    
    
            #, "mystery")
            #"comedy")
            # "horror")
            # "sci-fi")
            #, "romance")
            # "fantasy")
            #"slice")



init python:
    def make_cover(game):
        if game.genre == "mystery":
            game.bg = random.choice(["mystery1", "mystery2"])
            coverfont = "Assets/covers/MysteryForest.ttf"
        elif game.genre == "comedy":
            game.bg = random.choice(["comedy1", "comedy2"])
            coverfont = "Assets/covers/FunnyKid.ttf"
        elif game.genre == "horror":
            game.bg = random.choice(["horror1", "horror2"])
            coverfont = "Assets/covers/OhTheHorror.ttf"
        elif game.genre == "sci-fi":
            game.bg = random.choice(["scifi1", "scifi2"])
            coverfont = "Assets/covers/scifie.ttf"
        elif game.genre == "romance":
            game.bg = random.choice(["romance1", "romance2"])
            coverfont = "Assets/covers/EasyRomance.ttf"
        elif game.genre == "fantasy":
            game.bg = random.choice(["fantasy1", "fantasy2"])
            coverfont = "Assets/covers/PERRYGOT.TTF"
        else: # game.genre == "slice":
            game.bg = random.choice(["slice1", "slice2"])
            coverfont = "Assets/covers/RajaDrama.ttf"

        sp2 = None
        boys = ["lee", "aiden", "azura"]
        girls = ["edgy_tan", "eileen", "kyria"]
        if game.relationship == "bxg":
            sp1 = random.choice(boys)
            sp2 = random.choice(girls)
        elif game.relationship == "bxb":
            sp1 = random.choice(boys)
            boys.remove(sp1)
            sp2 = random.choice(boys)
        elif game.relationship == "gxg":
            sp1 = random.choice(girls)
            girls.remove(sp1)
            sp2 = random.choice(girls)
        elif game.relationship == "gxb":
            sp1 = random.choice(girls)
            sp2 = random.choice(boys)
        else:
            boys_or_girls = random.choice([boys, girls])
            sp1 = random.choice(boys_or_girls)
            
        
        #if 1==1:
        #if game.genre == "horror" and game.relationship == "bxg":
        
            #$ game.sp1 = random.choice(["azura angry smile large", "lee"])
            
            #$ sp2 = random.choice(["edgy_tan"])
            #$ sp2 = random.choice(["lee"])
            #$ sp2 = random.choice(["aiden"])
    #        $ sp2 = random.choice(["azura"])
            #$ sp2 = random.choice(["kyria"])       
            
            
        for i in range(1,3):
            if i==1:
                sp=sp1
            if i==2:
                sp=sp2
            if sp=="edgy_tan":
                sp = sp + " " + random.choice(["smile1", "smile2", "smile3", "smile4"]) + " " + random.choice(["black", "blue"])  + " " + random.choice(["clothes1", "clothes2", "clothes3", "clothes4", "clothes5", "clothes6"])  + " " + random.choice(["knife", "noknife"])
            if sp=="lee":
                sp = sp + " " + random.choice(["wide", "frown", "small", "smile"]) + " " + random.choice(["blink", "open", "wink", "closed"])  + " " + random.choice(["uniform", "shirt", "jumper", "none"]) + " " + random.choice(["happy", "normal", "frown"]) + " " + random.choice(["blush", "none"])
            if sp=="aiden":
                sp = sp + " " + random.choice(["wide", "frown", "small", "smile"]) + " " + random.choice(["eyes1", "eyes2", "eyes3", "eyes4"])  + " " + random.choice(["uniform", "shirt", "none"]) + " " + random.choice(["angry", "e1", "e2"]) + " " + random.choice(["blush", "none"])
            if sp=="azura":
                sp = sp + " " + random.choice(["pout", "frown", "smile", "smile2"]) + " " + random.choice(["closed", "blink", "half", "large"])  + " " + random.choice(["jacket", "uniform", "shirt", "singlet", "shirt2", "none"]) + " " + random.choice(["arched", "angry"]) + " " + random.choice(["blush", "none"])
            if sp=="kyria":
                sp = sp + " " + random.choice(["open", "mouth2", "smile"]) + " " + random.choice(["closed", "normal", "half"])  + " " + random.choice(["dress", "uniform", "shirt", "shorts", "shirt2", "none"]) + " " + random.choice(["normal", "worried", "arched", "linework"]) + " " + random.choice(["blush", "none"])
            if sp=="eileen":
                sp = sp + " " + random.choice(["mouth1", "mouth2", "mouth3", "mouth4", "mouth5", "mouth6", "mouth7", "mouth8", "mouth9"]) + " " + random.choice(["eyes1", "eyes2", "eyes3", "eyes4", "eyes5", "eyes6"])  + " " + random.choice(["dress", "dress", "dress", "none"]) + " " + random.choice(["hair1", "hair2", "hair3", "hair4", "hair5"]) + " " + random.choice(["glasses", "none"]) + " " + random.choice(["angry", "sweat", "none"]) + " " + random.choice(["blush", "none"])        
            if i==1:
                game.sp1 = sp
            if i==2:
                game.sp2 = sp
        return "1"+game.genre
        
screen show_cover(game=mygame):
    add game.bg
    add game.sp1 xalign 0.1
    
    if game.sp2:
        add game.sp2 xalign 0.7
    python:
        title = game.title
        if game.genre == "mystery":
            coverfont = "Assets/covers/MysteryForest.ttf"
        elif game.genre == "comedy":
            coverfont = "Assets/covers/FunnyKid.ttf"
        elif game.genre == "horror":
            coverfont = "Assets/covers/OhTheHorror.ttf"
        elif game.genre == "sci-fi":
            coverfont = "Assets/covers/scifie.ttf"
        elif game.genre == "romance":
            coverfont = "Assets/covers/EasyRomance.ttf"
        elif game.genre == "fantasy":
            coverfont = "Assets/covers/PERRYGOT.TTF"
        else: # game.genre == "slice":
            coverfont = "Assets/covers/RajaDrama.ttf"
    
    text title xalign .5 yalign .8 size 60 outlines [(2, "000000", 0, 0)] font coverfont
        
    textbutton "Return" ypos 700 action Hide("show_cover")#Return()