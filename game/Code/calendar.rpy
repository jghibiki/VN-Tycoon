init python:
    clock = False#make false to hide the clock
#calendar stuff:
    minutes = 750#must be initially defined.
    theweekday = 18#tuesday, the number of the weekday, this automatically changes but must be initially assigned
    themonth = 9#september, the number of the month, this automatically changes but must be initially assigned
    theday = 21#this automatically changes but must be initially assigned
    theyear = 2013#this automatically changes but must be initially assigned
    dayofyear = 264#you must calculate this properly, this automatically changes
    yearlim = 365#initially define it as 365 or 366, whichever is correct, this gets changed automatically later
    daylim = 30#initially define it as 28, 29, 30, or 31, whichever is correct, this gets changed automatically later
    stringweekday = "Wednesday"#3, the string of the weekday, this automatically changes but must be initially assigned
    stringmonth = "September"#9, the string of the month, this automatically changes but must be initially assigned



    def time_callback():#constantly calculate the time
        if (hasattr(store, 'minutes')):
            if (store.minutes > 1440):
                store.minutes = store.minutes - 1440
                store.theweekday = store.theweekday + 1
                store.theday = store.theday + 1
                store.dayofyear = dayofyear + 1
                
        if (hasattr(store, 'theweekday')):#setweekday
            if store.theweekday > 7:
                store.theweekday = store.theweekday - 7
            if store.theweekday == 1:
                store.stringweekday = "Sunday"
            elif store.theweekday == 2:
                store.stringweekday = "Monday"
            elif store.theweekday == 3:
                store.stringweekday = "Tuesday"
            elif store.theweekday == 4:
                store.stringweekday = "Wednesday"
            elif store.theweekday == 5:
                store.stringweekday = "Thursday"
            elif store.theweekday == 6:
                store.stringweekday = "Friday"
            elif store.theweekday == 7:
                store.stringweekday = "Saturday"
            else:
                store.stringweekday = "Error"
                
        if (hasattr(store, 'theday')):#monthlim
            if store.theday > store.daylim:
                store.theday = store.theday - store.daylim
                
        if (hasattr(store, 'themonth')):#setmonth
            if store.themonth == 1:
                store.stringmonth = "January"
                store.daylim = 31
            if store.themonth == 2:
                store.stringmonth = "February"
                if ((((int(store.theyear) / 4)*4) - store.theyear) == 0):
                    store.daylim = 29
                else:
                    store.daylim = 28
            if store.themonth == 3:
                store.stringmonth = "March"
                store.daylim = 31
            if store.themonth == 4:
                store.stringmonth = "April"
                store.daylim = 30
            if store.themonth == 5:
                store.stringmonth = "May"
                store.daylim = 31
            if store.themonth == 6:
                store.stringmonth = "June"
                store.daylim = 30
            if store.themonth == 7:
                store.stringmonth = "July"
                store.daylim = 31
            if store.themonth == 8:
                store.stringmonth = "August"
                store.daylim = 31
            if store.themonth == 9:
               store.stringmonth = "September"
               store.daylim = 30
            if store.themonth == 10:
               store.stringmonth = "October"
               store.daylim = 31
            if store.themonth == 11:
               store.stringmonth = "November"
               store.daylim = 30
            if store.themonth == 12:
               store.stringmonth = "December"
               store.daylim = 31
            
            if (hasattr(store, 'dayofyear') and hasattr(store, 'yearlim')):#yearstuff
               if store.dayofyear > store.yearlim:
                   store.dayofyear = store.dayofyear - store.yearlim
                   store.theyear = store.theyear + 1
               if ((((int(store.theyear) / 4)*4) - store.theyear) == 0):
                   store.yearlim = 366
               else:
                   store.yearlim = 365
    config.python_callbacks.append(time_callback)
    
    def Calendar(x=0, y=0, size=14):
        ui.frame(xfill=False, xminimum = 400, yminimum=None, xpos=x, ypos=y, background=None) #, xalign=1.0, yalign = 0.805)
        ui.vbox()
        ui.text("(%s) - %s %d %d" % (stringweekday, stringmonth, theday, theyear), xalign=1.0, size=size, color = "bccacc")
        ui.close()
        
    def Clocks(x=0, y=0, size=14):
        ui.frame(xfill=False, xminimum = 110, yminimum=None, xpos=x, ypos=y, background=None)
        ui.vbox()
        if (minutes > 719):
            if ((minutes - (int(minutes/60))*60) < 10):
                if((int(minutes/60)) == 12):
                    ui.text("12:0%d PM" % ((minutes - (int(minutes/60))*60)), xalign=1.0, size=size, color = "bccacc")
                else:
                    ui.text("%d:0%d PM" % ((int(minutes/60)-12), (minutes - (int(minutes/60))*60)), xalign=1.0, size=size, color = "bccacc")
            else:
                if((int(minutes/60)) == 12):
                    ui.text("12:%d PM" % ((minutes - (int(minutes/60))*60)), xalign=1.0, size=size, color = "bccacc")
                else:
                    ui.text("%d:%d PM" % ((int(minutes/60)-12), (minutes - (int(minutes/60))*60)), xalign=1.0, size=size, color = "bccacc")
        else:
            if ((minutes - (int(minutes/60))*60) < 10):
                if((int(minutes/60)) == 0):
                    ui.text("12:0%d AM" % ((minutes - (int(minutes/60))*60)), xalign=1.0, size=size, color = "bccacc")
                else:
                    ui.text("%d:0%d AM" % ((int(minutes/60)), (minutes - (int(minutes/60))*60)), xalign=1.0, size=size, color = "bccacc")
            else:
                if((int(minutes/60)) == 0):
                    ui.text("12:%d AM" % ((minutes - (int(minutes/60))*60)), xalign=1.0, size=size, color = "bccacc")
                else:
                    ui.text("%d:%d AM" % ((int(minutes/60)), (minutes - (int(minutes/60))*60)), xalign=1.0, size=size, color = "bccacc")
        ui.close()
        
        
        
init python:
    renpy.image("clock", "Assets/gui/clock.png") # Short Clockhand
    renpy.image("clock_1", "Assets/gui/clock_1.png") # Long Clockhand
    renpy.image("clock_2", "Assets/gui/clock_2.png") # Clockface
    minutes = 540
    
    def AClocks(x=.5, y=.5):
#        if clock: # if False - clock is hide
            ui.at(Position(xpos=x, ypos=y, xanchor="center", yanchor="center"))
            ui.add("clock_2")
            # xalign and yalign can be replaced by xpos and ypos - position where the center of the clock should be
            # this segment is the one responsible for the clockface
           
            ui.at(Position(xpos=x, ypos=y, xanchor="center", yanchor="center"))
            ui.at(RotoZoom((minutes*6), (minutes*6), 5.0, 1, 1, 1, rot_bounce= False, rot_anim_timebase=False, opaque=False), )
            ui.add("clock")
            # this segment is the one responsible for the short clock hand.

            ui.at(Position(xpos=x, ypos=y, xanchor="center", yanchor="center"))
            ui.at(RotoZoom ((minutes*0.5), (minutes*0.5), 5.0, 1, 1, 1, rot_bounce= False, rot_anim_timebase=False, opaque=False))
            ui.add("clock_1")
            # this segment is the one responsible for the long clock hand.

    #config.overlay_functions.append(AClocks)
