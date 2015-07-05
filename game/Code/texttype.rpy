init -1 python:
    job = None
    def make_posts_list():
        random_username = make_user()
        posts_list = [
            "yay for a GXB game ^^ there is just not enough GxB games around here",
            "If you need help with the title for your VN I can help.",
            "Is this project dead?",
            "Ahahaha. No.", 
            "While 640x480 worked perfectly during it's time, it is no longer sufficient for larger screens. We all know that the future belongs to 800x600.",
            "Yes, I agree with " + random_username + "."
        ]
        if not job == "writer":
            posts_list.append("I don't care how good the story is, your art looks like crap and I wouldn't play it.")
        if job == "composer":
            posts_list.append("Do you even [[s]lift[[/s] know how much all this equipment and software costs?")

        return posts_list

    
transform textPause(showTime, start_curx, start_cury, end_curx, end_cury):
    xpos start_curx
    ypos start_cury
    on show:
        time showTime
        linear 1.0 xpos end_curx ypos end_cury

screen autoPost(x, y, curx, cury, bg, autoText, typeSpeed = 40, moveCursor=False, textSize=12, wait=False, dont_hide=False):
    zorder 20
    add bg
    default showTime = len(autoText) / typeSpeed
    $ start_curx = x+50
    $ start_cury = y+50
    if moveCursor:
        add "Assets/gui/cursor.png" at textPause(showTime, start_curx, start_cury, curx, cury)
    add Text(autoText, slow = True, slow_speed = typeSpeed, slow_abortable = True, color="#000", size=textSize) xpos x ypos y
    if not wait:
        $ wait_to_hide = showTime + 1.5
        timer wait_to_hide action [Hide("autoPost"), Return()]
        
        
screen autoPostFixed(x, y, bg, autoText, textSize=12):
    zorder 20
    add bg
    add Text(autoText, color="#000", size=textSize) xpos x ypos y

