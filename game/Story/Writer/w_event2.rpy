# Event 2:
# Being stuck on writing.
# Summary:
# Joan Gold has a writer's block and tries to fix that situation by researching online.
# Scene:
label writer_event2:
    $ post = "Close to the village street stood the one-story house in which Luella Miller, who had an evil\nname in the village, had dwelt. She had been dead for years, yet there were those in the village\nwho, in spite of the clearer light which comes on a vantage-point from a long-past danger, half\nbelieved in the tale which they had heard from their childhood. In their hearts, although they\nscarcely would have owned it, was a survival of the wild horror and frenzied fear of their\nancestors who had dwelt in the same age with Luella Miller. Young people even would stare with\na shudder at the old house as they passed, and children never played around it as was their wont\naround an untenanted building. Not a window in the old Miller house was broken: the panes\nreflected the morning sunlight in patches of emerald and blue, and the latch of the sagging front\ndoor was never lifted, although no bolt secured it. Since Luella Miller had been carried out of it,\nthe house had had no tenant except one friendless old soul who had no choice between that and\nthe far-off shelter of the open sky."
    
    show screen sentence (showOptions=False)
    with dissolve
#    show screen window_frame("Sentence", "icon16_sentence", None)
#    show "Assets/gui/sentence.png"
    show screen autoPostFixed(278, 302, "#00000000", post, textSize=16)
    $ days_word = numToWords(day)
    $ words = mygame.writing_done
    $ words = str(int(words)) + ",000"

    Joan neutral "Ugh. Just staring at this .doc makes me suicidal. How did I not get past [words] words after [days_word] days? I said I was a writer, dammit, so why am I not writing? This is a cardinal rule of the damn universe: An artist makes art, a programmer programs, composers compose and writers... write, dammit!"
    Joan despair "Bah, it's just not coming to me. Screw it, I give up. This isn't working out. They say to 'just write', but how the hell am I supposed to 'just write' if I can't figure out where to even start? Like, whoever thought of the entire 'just write': I want to punch you in the balls."
    Joan neutral "I'm not even joking. I will find out where you live. I will come down to your house and punch you in the friggin' balls. And then punch your wife in the tits. And your dog on the snout."
    Joan scowl_closed "Wait, scratch that, the poor dog's done nothing wrong. I can't punch an innocent bystander, that'd be inhumane."
    Joan scowl_open "But I'll still punch YOU, your wife, and probably your children too; they deserve it. Or will deserve it. I'm pretty sure there's not a kid in the world that hasn't deserved a beating at some point. Multiple points."
    Joan laugh_big "Wait, that's it! Brilliant! Way to go, Joan. That's how we'll proceed from here. Hahaha! I'm a genius. God, quick, I have to write this down."
    
    Joan scowl_closed "... And it's gone."
    Joan scowl_open "GOD. DAMMIT."
    
    #hide screen computer
    #hide screen window_frame
    #hide screen autoPostFixed
    hide screen autoPostFixed
    hide screen sentence
    with dissolve
    $ writer_event2 = True
    
    

init python:
    def numToWords(num,join=True):
        '''words = {} convert an integer number into words'''
        units = ['','one','two','three','four','five','six','seven','eight','nine']
        teens = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen', \
                 'seventeen','eighteen','nineteen']
        tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy', \
                'eighty','ninety']
        thousands = ['','thousand','million','billion','trillion','quadrillion', \
                     'quintillion','sextillion','septillion','octillion', \
                     'nonillion','decillion','undecillion','duodecillion', \
                     'tredecillion','quattuordecillion','sexdecillion', \
                     'septendecillion','octodecillion','novemdecillion', \
                     'vigintillion']
        words = []
        if num==0: words.append('zero')
        else:
            numStr = '%d'%num
            numStrLen = len(numStr)
            groups = (numStrLen+2)/3
            numStr = numStr.zfill(groups*3)
            for i in range(0,groups*3,3):
                h,t,u = int(numStr[i]),int(numStr[i+1]),int(numStr[i+2])
                g = groups-(i/3+1)
                if h>=1:
                    words.append(units[h])
                    words.append('hundred')
                if t>1:
                    words.append(tens[t])
                    if u>=1: words.append(units[u])
                elif t==1:
                    if u>=1: words.append(teens[u])
                    else: words.append(tens[t])
                else:
                    if u>=1: words.append(units[u])
                if (g>=1) and ((h+t+u)>0): words.append(thousands[g]+',')
        if join: return ' '.join(words)
        return words