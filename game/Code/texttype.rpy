init -1 python:
    job = None
    def make_posts_list():
        random_username = make_user()
        posts_list = [
            "yay for a GXB game ^^ there is just not enough GxB games around here",
            "If you need help with the title for your VN I can help.",
            "Is this project dead?",
            "Ahahaha. No.", 
            "While 640x480 worked perfectly during it's time, it is no longer sufficient for larger screens. We all know that the future belongs to 800x600."
            "Yes, I agree with " + random_username + "."
        ]
        if not job == "writer":
            posts_list.append("I don't care how good the story is, your art looks like crap and I wouldn't play it.")
            
        return posts_list

    
transform textPause(showImage, start_curx, start_cury, end_curx, end_cury):
    # xalign -0.1
    # yalign -0.1
    xpos start_curx
    ypos start_cury
    on show:
        time showImage
        linear 1.0 xpos end_curx ypos end_cury

screen autoPost(x, y, curx, cury, bg, autoText, typeSpeed = 40):
    add bg
    default showImage = len(autoText) / typeSpeed
    $ start_curx = x+50
    $ start_cury = y+50
    add "Assets/gui/cursor.png" at textPause(showImage, start_curx, start_cury, curx, cury)
    add Text(autoText, slow = True, slow_speed = typeSpeed, slow_abortable = True, color="#000", size=12) xpos x ypos y
    $ wait_to_hide = showImage+1.5
    timer wait_to_hide action [Hide("autoPost"), Return()]