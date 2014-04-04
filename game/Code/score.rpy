init -1 python:
    import urllib2
    from urllib import urlencode # new module and function
    if not persistent.user_name:
        persistent.user_name = False
    
screen hiscore:
    tag menu
    python:
        url = "http://vntycoon.vnovel.com/extra/score.php"
        if persistent.user_name:
            data = {'user':persistent.user_name, 'score':str(inventory.money)}
            encoded_data = urlencode(data) # remember that this is from that imported module, normally you'd use this: urllib.urlencode(data) if you used a normal import.
            website = urllib2.urlopen(url, encoded_data)
        else:
            website = urllib2.urlopen(url)
        data = website.read()
        #y = data.count("<br>") - 1
        
    use navigation
    add "hiscore_title" xpos 152 ypos 20
    
    $ dat = data.split('<br>')
    vbox xpos 220 ypos 100:
        for da in dat:
            #text da color "000"
            $ d = da.split('***')
            #hbox:
            window xsize 550 ysize 50 background None:
                $ i = 0
                for dd in d:
                    if i==0:
                        text dd color "000" xalign 0.0 size 40 ypos 0 font "Assets/gui/animeace.ttf"
                    else:
                        $ score = "$"+str(int(float(dd)))
                        text score color "000" xalign 1.0 size 40 ypos 0 font "Assets/gui/animeace.ttf"
                    $ i += 1
            #    text dd color "000"# xpos 100
    textbutton ("Enable submiting of my score to the internet") action ui.callsinnewcontext("submit_score") ypos 600 xpos 100
    
label submit_score:
    call screen submit_score
    $ persistent.user_name = _return.lower()
    return

screen submit_score:
    add "#000"
    window:
        has vbox
        text "Enter your name:"
        if persistent.user_name:
            input default persistent.user_name
        else:
            input