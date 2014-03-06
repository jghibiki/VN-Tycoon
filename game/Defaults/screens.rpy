# This file is in the public domain.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:
    # Defaults for side_image and two_window
    default side_image = None
    default two_window = False
    # Decide if we want to use the one-window or two-window varaint.
    if not two_window:
        # The one window variant.        
        window:
            id "window"
            has vbox:
                style "say_vbox"
            if who:
                text who id "who"
            text what id "what"
    else:
        # The two window variant.
        vbox:
            style "say_two_window_vbox"
            if who:            
                window:
                    style "say_who_window"
                    text who:
                        id "who"
            window:
                id "window"

                has vbox:
                    style "say_vbox"
                text what id "what"
                
    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0
    # Use the quick menu.
    use quick_menu

init -1 python:
    style.say_dialogue.color = "000"
    style.say_thought.color = "000"
    
    
    style.say_window.background = Frame("Assets/gui/textbox1.png", 25, 25)
    style.say_window.left_padding=100
    style.say_window.right_padding=100
    style.say_window.bottom_padding=67
    style.say_window.top_padding=25
    
    style.say_window.yminimum = 169
    
    style.say_who_window.background = Frame("Assets/gui/namebox1.png", 15, 15)
    style.say_who_window.left_margin = 66
    style.say_who_window.bottom_margin = 10
    style.say_label.xalign = 0.5
    
    #style.say_window.bottom_padding=100
##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:
    window: 
        style "menu_window"        
        xalign 0.5
        yalign 0.5
        vbox:
            style "menu"
            spacing 2
            for caption, action, chosen in items:
                if action:  
                    button:
                        action action
                        style "menu_choice_button"                        
                        text caption style "menu_choice"
                else:
                    text caption style "menu_caption"

init -2 python:
    config.narrator_menu = True
    
    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.75)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:
    window style "input_window":
        has vbox
        text prompt style "input_prompt"
        input id "input" style "input_text"
    use quick_menu
        
##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:
    window:
        style "nvl_window"
        has vbox:
            style "nvl_vbox"
        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id
                has hbox:
                    spacing 10
                if who is not None:
                    text who id who_id
                text what id what_id
        # Display a menu, if given.
        if items:
            vbox:
                id "menu"
                for caption, action, chosen in items:
                    if action:
                        button:
                            style "nvl_menu_choice_button"
                            action action
                            text caption style "nvl_menu_choice"
                    else:
                        text caption style "nvl_dialogue"
    add SideImage() xalign 0.0 yalign 1.0
    use quick_menu
        
        
        
screen help_screen:
    tag menu
    use navigation
    vbox ypos .026 xmaximum 1020:
        add "help_title" xpos .02
        hbox:
            frame:
                xmaximum 940
                ymaximum 555
                left_padding 20
                right_padding 20
                ypadding 20
                #xmargin 60
                left_margin 60
                right_margin 20
                top_margin 80
                #bottom_margin 165
                viewport id "vp":
                    style_group "help_bar"
                    draggable True
                    mousewheel True
                    vbox:
                        style_group "help"
                        use help
            vbar value YScrollValue("vp") ymaximum 480 ypos 80 # top_margin 80 bottom_margin 165# yalign 1.0

init python:
    style.help_text.size=38
 
#    style.help_bar_vbar.top_bar  = "Assets/gui/config_bar_full.png"
    #style.help_bar_vbar.right_bar = "Assets/gui/config_bar_empty.png"
    # style.help_bar.ymaximum = 30    
    # style.help_bar.xmaximum = 192
    # style.help_bar.xalign = .5


 
##############################################################################
# Main Menu 
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

init:
    $ menu_actions = {"return": Return(), "config": ShowMenu("preferences"), "save": ShowMenu("save"), "load": ShowMenu("load"), "main": MainMenu(), "help": ShowMenu("help_screen"), "quit": Quit(), "start": Start(), "extras": ShowMenu("extras_blank"), "cg_gallery": ShowMenu("cg_gallery"), "ch_gallery": ShowMenu("ch_gallery"), "bg_gallery": ShowMenu("bg_gallery"), "music_room": ShowMenu("music_room"), "dev_gallery": ShowMenu("dev_gallery")}
    
    $ button_text = "Start"
    image m_button_start = At(LiveComposite ((312, 80), (0,0), "Assets/gui/main_button.png", (8, 6), Text(button_text, style="main_butt")), main_eff)
    image m_button_start_hover = At(LiveComposite ((312, 80), (0,0), "Assets/gui/main_button.png", (3, 1), Text(button_text, style="main_butt_hover")), main_eff)

    $ button_text = "Load"
    image m_button_load = At(LiveComposite ((312, 80), (0,0), "Assets/gui/main_button.png", (8, 6), Text(button_text, style="main_butt")), main_eff)
    image m_button_load_hover = At(LiveComposite ((312, 80), (0,0), "Assets/gui/main_button.png", (3, 1), Text(button_text, style="main_butt_hover")), main_eff)

    $ button_text = "Config"
    image m_button_config = At(LiveComposite ((312, 80), (0,0), "Assets/gui/main_button.png", (8, 6), Text(button_text, style="main_butt")), main_eff)
    image m_button_config_hover = At(LiveComposite ((312, 80), (0,0), "Assets/gui/main_button.png", (3, 1), Text(button_text, style="main_butt_hover")), main_eff)

    $ button_text = "Extras"
    image m_button_extras = At(LiveComposite ((312, 80), (0,0), "Assets/gui/main_button.png", (8, 6), Text(button_text, style="main_butt")), main_eff)
    image m_button_extras_hover = At(LiveComposite ((312, 80), (0,0), "Assets/gui/main_button.png", (3, 1), Text(button_text, style="main_butt_hover")), main_eff)

    $ button_text = "Help"
    image m_button_help = At(LiveComposite ((312, 80), (0,0), "Assets/gui/main_button.png", (8, 6), Text(button_text, style="main_butt")), main_eff)
    image m_button_help_hover = At(LiveComposite ((312, 80), (0,0), "Assets/gui/main_button.png", (3, 1), Text(button_text, style="main_butt_hover")), main_eff)

    $ button_text = "Quit"
    image m_button_quit = At(LiveComposite ((312, 80), (0,0), "Assets/gui/main_button.png", (8, 6), Text(button_text, style="main_butt")), main_eff)
    image m_button_quit_hover = At(LiveComposite ((312, 80), (0,0), "Assets/gui/main_button.png", (3, 1), Text(button_text, style="main_butt_hover")), main_eff)
    
# screen snow:
    # zorder -1
    # window:
        # background SnowBlossom(Animation("Assets/gui/frame.png", 0.15, "Assets/gui/frame.png", 0.15))
# init:
    # $ style.button.hover_sound = CLICK
        
screen main_menu:
    tag menu
    add "main_menu_cg"
    add "Assets/gui/main_menu_ground.png"
    add "Assets/gui/main_menu_title.png"
    $ main_menu_items = ["start", "load", "config", "extras", "help", "quit"]
    $ y = 129
    vbox xalign .5 yalign .5:
        for item in main_menu_items:
            $ button_name = "m_button_" + item
            $ button_name_hover = button_name + "_hover"
            $ tip_name = "tooltip_" + item
            $ my_action = menu_actions[item]
            button background None focus_mask True action [Hide("gui_tooltip"), my_action] hovered [ Play ("sound", "Assets/sfx/click.ogg"), Show("gui_tooltip", my_picture=tip_name) ] unhovered [Hide("gui_tooltip")]:
                add button_name
                hover_child button_name_hover
    
init -2:
    transform main_eff:
        xalign .5
        yalign .5
        zoom 0.5
        easein 1.0 zoom 1.0

##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation


init:
    # image button_ch_gallery = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button.png",(19, 19), "Assets/gui/icon_ch_gallery.png",  (77, 18), Text("Char. Art", style="side_butt")), side_eff)
    $ x = 50
    $ button_text = "Return"
    image button_return = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button.png", (x, 18), Text(button_text, style="side_butt")), side_eff)
    image button_return_selected_idle = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button_selected.png", (x, 18), Text(button_text, style="side_butt")), side_eff_selected_idle)
    image button_return_selected_hover = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button_selected.png", (x, 18), Text(button_text, style="side_butt")), side_eff_selected_hover)

    $ button_text = "Config"
    image button_config = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button.png", (x, 18), Text(button_text, style="side_butt")), side_eff)
    image button_config_selected_idle = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button_selected.png", (x, 18), Text(button_text, style="side_butt")), side_eff_selected_idle)
    image button_config_selected_hover = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button_selected.png", (x, 18), Text(button_text, style="side_butt")), side_eff_selected_hover)
    
    $ button_text = "Save Game"
    image button_save = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button.png", (x, 18), Text(button_text, style="side_butt")), side_eff)
    image button_save_selected_idle = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button_selected.png", (x, 18), Text(button_text, style="side_butt")), side_eff_selected_idle)
    image button_save_selected_hover = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button_selected.png", (x, 18), Text(button_text, style="side_butt")), side_eff_selected_hover)
    image button_save_insensitive = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button.png", (x, 18), Text(button_text, style="side_butt_insensitive")), side_eff_insensitive)

    $ button_text = "Load Game"
    image button_load = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button.png", (x, 18), Text(button_text, style="side_butt")), side_eff)
    image button_load_selected_idle = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button_selected.png", (x, 18), Text(button_text, style="side_butt")), side_eff_selected_idle)
    image button_load_selected_hover = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button_selected.png", (x, 18), Text(button_text, style="side_butt")), side_eff_selected_hover)

    $ button_text = "Main Menu"
    image button_main = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button.png", (x, 18), Text(button_text, style="side_butt")), side_eff)
    image button_main_selected_idle = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button_selected.png", (x, 18), Text(button_text, style="side_butt")), side_eff_selected_idle)
    image button_main_selected_hover = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button_selected.png", (x, 18), Text(button_text, style="side_butt")), side_eff_selected_hover)
    image button_main_insensitive = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button.png", (x, 18), Text(button_text, style="side_butt_insensitive")), side_eff_insensitive)

    $ button_text = "Help"
    image button_help = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button.png", (x, 18), Text(button_text, style="side_butt")), side_eff)
    image button_help_selected_idle = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button_selected.png", (x, 18), Text(button_text, style="side_butt")), side_eff_selected_idle)
    image button_help_selected_hover = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button_selected.png", (x, 18), Text(button_text, style="side_butt")), side_eff_selected_hover)
    
    $ button_text = "Quit"
    image button_quit = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button.png", (x, 18), Text(button_text, style="side_butt")), side_eff)
    image button_quit_selected_idle = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button_selected.png", (x, 18), Text(button_text, style="side_butt")), side_eff_selected_idle)
    image button_quit_selected_hover = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button_selected.png", (x, 18), Text(button_text, style="side_butt")), side_eff_selected_hover)
    
init -1:
    transform side_eff:
        on idle:
            alpha .8
            easein 0.5 xpos 0
        on hover:
            alpha 1.0
            easein 0.3 xpos 20
            easein 0.3 xpos -20
    transform side_eff_selected_idle:
        alpha .8
        easein 0.5 xpos 0
    transform side_eff_selected_hover:
        alpha 1.0
    transform side_eff_insensitive:
        alpha .4
        xpos 0
    
init:
    transform trans30:
        alpha 0.3
    image main_menu_cg="Assets/bg/bedroom.jpg"
    image main_menu_cg_foggy=LiveComposite((1366,768), (0,0), Solid("#fff"), (0,0), At(ImageReference("main_menu_cg"), trans30))

screen navigation:
    add "main_menu_cg_foggy"
    add "Assets/gui/main_menu_ground.png"
    add "Assets/gui/game_menu_ground.png"

    $ game_menu_items = ["return", "config", "save", "load", "main", "quit"]
    
    $ y = 129
    vbox xpos 1060 ypos 129 spacing 9:
        for item in game_menu_items:
            $ button_name = "button_" + item
            $ button_name_selected_idle = button_name + "_selected_idle"
            $ button_name_selected_hover = button_name + "_selected_hover"
            $ button_name_insensitive = button_name + "_insensitive"
            $ tip_name = "tooltip_" + item
            $ my_action = menu_actions[item]
            button background None focus_mask True action my_action hovered [ Play ("sound", "Assets/sfx/click.ogg"), Show("gui_tooltip", my_picture=tip_name) ] unhovered [Hide("gui_tooltip")]:
                add button_name
                selected_idle_child button_name_selected_idle
                #selected_hover_child button_name_selected_hover
                insensitive_child button_name_insensitive
                
screen gui_tooltip (my_picture="", my_tt_xpos=58, my_tt_ypos=683):
    add my_picture xpos my_tt_xpos ypos my_tt_ypos

init -1 python:
    style.button.background=Frame("Assets/gui/frame.png",25,25)
    style.button.yminimum=52
    style.button.xminimum=52
    style.button_text.color="000000DD"
    style.button_text.selected_color="4abff2"
    style.button_text.insensitive_color="fff"
    style.button_text.outlines=[(2, "00000000", 0, 0)]
    style.button_text.hover_outlines=[(2, "ffffff", 0, 0)]
    style.button_text.insensitive_outlines=[(2, "00000000", 0, 0)]
    style.button_text.selected_outlines=[(2, "00000040", 0, 0)]
    style.button_text.selected_hover_outlines=[(2, "ffffffa0", 0, 0)]
    
    if renpy.variant("touch"):
        style.button.yminimum=52*2
        style.button.xminimum=52*2
        style.button_text.size=32
    
    
    #Screen titles:
    style.title = Style(style.default)
    style.title.size=32
    style.title.bold=True
    style.title.font="Assets/gui/animeace2_reg.ttf"
    style.title.outlines=[(3, "4abff2", 0, 0)]
    style.title.color="fff"

    style.main_butt = Style(style.title)
    style.main_butt.size=50
    style.main_butt.outlines=[(2, "05b1e6", 0, 0)]
    style.main_butt.kerning = -2
    style.main_butt.min_width=312
    style.main_butt.text_align=.5
    
    style.main_butt_hover = Style(style.main_butt)
    style.main_butt_hover.outlines=[(2, "05b1e6", 0, 0), (0, "05b1e6", 5, 5)]
    
    
    style.side_butt = Style(style.title)
    style.side_butt.size=28
    style.side_butt.bold=False
    style.side_butt.outlines=[(2, "4abff2", 0, 0), (0, "4abff2", 3, 3), (0, "4abff2", 4, 4)]
    
    
    style.side_butt_insensitive = Style(style.side_butt)
    style.side_butt_insensitive.outlines=[]
    
    
    #Tooltips:
    style.tips_top = Style(style.default)
    #style.title.font="Assets/gui/arial.ttf"
    style.tips_top.size=14
    style.tips_top.color="fff"
    style.tips_top.outlines=[(3, "6b7eef", 0,0)]
    style.tips_top.kerning = 5

    style.tips_bottom = Style(style.tips_top)
    style.tips_top.size=20
    style.tips_bottom.outlines=[(0, "6b7eef", 1, 1), (0, "6b7eef", 2, 2)]
    style.tips_bottom.kerning = 2
    
init:
    #Screen titles:
    image extras_title=Text("extras", style="title")
    image cg_gallery_title=Text("CG gallery", style="title")
    image character_gallery_title=Text("character gallery", style="title")
    image bg_gallery_title=Text("BG gallery", style="title")
    image concept_gallery_title=Text("concept gallery", style="title")
    image music_room_title=Text("music room", style="title")

    image title_configuration=Text("Configuration", style="title")
    image title_save_game=Text("Save Game", style="title")
    image title_load_game=Text("Load Game", style="title")
    image help_title=Text("Help", style="title")

    image information = Text("INFORMATION", style="tips_top")
    #Tooltips - game menu:    
    image tooltip_save=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Save a game in progress", style="tips_bottom"))
    image tooltip_load=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Load a game in progress", style="tips_bottom"))
    image tooltip_config=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Configure the game settings", style="tips_bottom"))
    image tooltip_main=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Return to main menu", style="tips_bottom"))
    image tooltip_quit=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Quit the game :(", style="tips_bottom"))
    image tooltip_return=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Return to the previous screen", style="tips_bottom"))

    #Tooltips - main menu
    image tooltip_start=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Start a new game", style="tips_bottom"))
    image tooltip_extras=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("View the additional unlockable\ncontent", style="tips_bottom"))
    # tooltip_load, tooltip_config and tooltip_quit are already defined above
    image tooltip_help=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("View the game help.", style="tips_bottom"))


    image tooltip_cg_gallery=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("View the event CG Gallery", style="tips_bottom"))
    image tooltip_ch_gallery=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("View the characters Gallery", style="tips_bottom"))
    image tooltip_bg_gallery=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("View the backgrounds Gallery", style="tips_bottom"))
    image tooltip_music_room=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Listen to the music", style="tips_bottom"))
    image tooltip_dev_gallery=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("View the concepts and sketches", style="tips_bottom"))    
    # tooltip_return already defined above
    
    #Tooltips - options:
    image tooltip_config_windowed=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Toggle windowed mode", style="tips_bottom"))
    image tooltip_config_fullscreen=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Toggle fullscreen mode", style="tips_bottom"))
    image tooltip_config_enable_transition=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Enable in-game transitions", style="tips_bottom"))
    image tooltip_config_enable_transition=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Disble in-game transitions", style="tips_bottom"))
    image tooltip_config_stop_skip=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Stop fast skipping after a choice", style="tips_bottom"))
    image tooltip_config_go_skip=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Resume fast skipping after a choice", style="tips_bottom"))
    image tooltip_config_seen=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Fast skip text that has already been seen", style="tips_bottom"))
    image tooltip_config_all=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Fast skip all text regardless of whether\nit has already been seen or not", style="tips_bottom"))
    image tooltip_config_skipping=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Turn on game skipping", style="tips_bottom"))    
    
    
    
# EXTRAS:
init:
    $ x = 50
    $ button_text = "CG Gallery"
    image button_cg_gallery = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button.png", (x, 18), Text(button_text, style="side_butt")), side_eff)
    image button_cg_gallery_selected_idle = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button_selected.png", (x, 18), Text(button_text, style="side_butt")), side_eff_selected_idle)
    image button_cg_gallery_selected_hover = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button_selected.png", (x, 18), Text(button_text, style="side_butt")), side_eff_selected_hover)

    $ button_text = "Characters"
    image button_ch_gallery = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button.png", (x, 18), Text(button_text, style="side_butt")), side_eff)
    image button_ch_gallery_selected_idle = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button_selected.png", (x, 18), Text(button_text, style="side_butt")), side_eff_selected_idle)
    image button_ch_gallery_selected_hover = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button_selected.png", (x, 18), Text(button_text, style="side_butt")), side_eff_selected_hover)

    $ button_text = "BG Gallery"
    image button_bg_gallery = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button.png", (x, 18), Text(button_text, style="side_butt")), side_eff)
    image button_bg_gallery_selected_idle = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button_selected.png", (x, 18), Text(button_text, style="side_butt")), side_eff_selected_idle)
    image button_bg_gallery_selected_hover = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button_selected.png", (x, 18), Text(button_text, style="side_butt")), side_eff_selected_hover)

    $ button_text = "Music Room"
    image button_music_room = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button.png", (x, 18), Text(button_text, style="side_butt")), side_eff)
    image button_music_room_selected_idle = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button_selected.png", (x, 18), Text(button_text, style="side_butt")), side_eff_selected_idle)
    image button_music_room_selected_hover = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button_selected.png", (x, 18), Text(button_text, style="side_butt")), side_eff_selected_hover)

    $ button_text = "Concept Art"
    image button_dev_gallery = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button.png", (x, 18), Text(button_text, style="side_butt")), side_eff)
    image button_dev_gallery_selected_idle = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button_selected.png", (x, 18), Text(button_text, style="side_butt")), side_eff_selected_idle)
    image button_dev_gallery_selected_hover = At(LiveComposite ((335, 74), (0,0), "Assets/gui/side_button_selected.png", (x, 18), Text(button_text, style="side_butt")), side_eff_selected_hover)
    
screen extras:
    add "main_menu_cg_foggy"
    add "Assets/gui/main_menu_ground.png"
    add "Assets/gui/game_menu_ground.png"
    $ extras_items = ["cg_gallery", "ch_gallery", "bg_gallery", "music_room", "dev_gallery", "return"]
    $ y = 129
    vbox xpos 1060 ypos 129 spacing 9:
        for item in extras_items:
            $ button_name = "button_" + item
            $ button_name_selected_idle = button_name + "_selected_idle"
            $ button_name_selected_hover = button_name + "_selected_hover"
            $ button_name_insensitive = button_name + "_insensitive"
            $ tip_name = "tooltip_" + item
            $ my_action = menu_actions[item]
            button background None focus_mask True action my_action hovered [ Play ("sound", "Assets/sfx/click.ogg"), Show("gui_tooltip", my_picture=tip_name) ] unhovered [Hide("gui_tooltip")]:
                add button_name
                selected_idle_child button_name_selected_idle
                #selected_hover_child button_name_selected_hover
                insensitive_child button_name_insensitive

screen extras_blank:
    tag menu # This ensures that any other menu screen is replaced.
    use extras # We include the extras navigation screen
    add "extras_title" xpos 152 ypos 20

##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.
    
screen file_picker:

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"
            
            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)
                    
            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5
                
        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"
            
            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)
                    
                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)
                    
                    
screen save:
    tag menu
    use navigation
    vbox ypos .026 xmaximum 950:
        add "title_save_game" xpos .02
        use file_picker

screen load:
    tag menu
    use navigation
    vbox ypos .026 xmaximum 950:
        add "title_load_game" xpos .02
        use file_picker

init -2 python:
    style.file_picker_frame = Style(style.menu_frame)
    style.file_picker_nav_button = Style(style.small_button)
    style.file_picker_nav_button_text = Style(style.small_button_text)
    style.file_picker_button = Style(style.large_button)
    style.file_picker_text = Style(style.large_button_text)

##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces
    
screen preferences:
    tag menu
    use navigation
    vbox ypos .026 xmaximum 950:
        add "title_configuration" xpos .02
        # Put the navigation columns in a three-wide grid.
        grid 3 1 ypos .05 xpos 20 spacing 20:
            style_group "prefs"
            xfill True

            # The left column.
            vbox:
                frame:
                    style_group "pref"
                    has vbox
                    text _("Display")
                    null height 10
                    null
                    textbutton _("Window") action Preference("display", "window")
                    textbutton _("Fullscreen") action Preference("display", "fullscreen")

                frame:
                    style_group "pref"
                    has vbox
                    text _("Transitions")
                    null height 10
                    textbutton _("All") action Preference("transitions", "all")
                    textbutton _("None") action Preference("transitions", "none")

                frame:
                    style_group "pref"
                    has vbox
                    text _("Text Speed")
                    null height 10
                    bar value Preference("text speed")

                # frame:
                    # style_group "pref"
                    # has vbox
                    # textbutton _("Joystick...") action Preference("joystick")

            vbox:
                frame:
                    style_group "pref"
                    has vbox
                    text _("Skip")
                    null height 10
                    textbutton _("Seen Messages") action Preference("skip", "seen")
                    textbutton _("All Messages") action Preference("skip", "all")

                # frame:
                    # style_group "pref"
                    # has vbox
                    # textbutton _("Begin Skipping") action Skip()

                frame:
                    style_group "pref"
                    has vbox
                    text _("After Choices")
                    null height 10
                    textbutton _("Stop Skipping") action Preference("after choices", "stop")
                    textbutton _("Keep Skipping") action Preference("after choices", "skip")

                frame:
                    style_group "pref"
                    has vbox
                    text _("Auto-Forward Time")
                    null height 10
                    bar value Preference("auto-forward time")
            use sound_options
            
screen sound_options:
    vbox:
        frame:
            style_group "pref"
            has vbox
            text _("Music Volume")
            null height 10
            bar value Preference("music volume")

        frame:
            style_group "pref"
            has vbox
            text _("Sound Volume")
            null height 10
            bar value Preference("sound volume")
            if config.sample_sound:
                textbutton _("Test"):
                    action Play("sound", config.sample_sound)
                    style "soundtest_button"

        if config.has_voice:
            frame:
                style_group "pref"
                has vbox
                text _("Voice Volume")
                null height 10
                bar value Preference("voice volume")
                if config.sample_voice:
                    textbutton "Test":
                        action Play("voice", config.sample_voice)
                        style "soundtest_button"

init -2 python:
    style.pref_frame.background=None
    style.pref_text.color = "000"
    style.pref_text.font = "Assets/gui/animeace2_reg.ttf"
    style.pref_text.xalign = .5
    style.pref_label.xalign = .5
    
    style.pref_frame.xfill = True
    style.pref_frame.xmargin = 5
    style.pref_frame.top_margin = 50

    style.pref_vbox.xfill = True

    style.pref_button.size_group = "pref"
    style.pref_button.xalign = .5

    
    style.pref_slider.left_bar = "Assets/gui/config_bar_full.png"
    style.pref_slider.right_bar = "Assets/gui/config_bar_empty.png"
    #style.pref_slider.thumb = None
    #style.pref_slider.xmaximum = 290
    style.pref_slider.ymaximum = 30
    #style.pref_slider.ymaximum = 44   
    #style.pref_slider.left_gutter = 0
    #style.pref_slider.right_gutter = 0

    
    style.pref_slider.xmaximum = 192
    style.pref_slider.xalign = .5

    style.soundtest_button.xalign = 1.0



##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt
    
screen yesno_prompt:

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05
        
        has vbox:
            xalign .5
            yalign .5
            spacing 30
            
        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100
            
            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action


init -2 python:    
    style.yesno_button.size_group = "yesno"
    style.yesno_label_text.text_align = 0.5


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu:

    # Add an in-game quick menu.
    hbox:
        style_group "quick"
    
        xalign 1.0
        yalign 1.0

        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Skip") action Skip()
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')
        
init -2 python:
    style.quick_button.set_parent('default')
    style.quick_button.background = None
    style.quick_button.xpadding = 5

    style.quick_button_text.set_parent('default')
    style.quick_button_text.size = 12
    style.quick_button_text.idle_color = "#8888"
    style.quick_button_text.hover_color = "#ccc"
    style.quick_button_text.selected_idle_color = "#cc08"
    style.quick_button_text.selected_hover_color = "#cc0"
    style.quick_button_text.insensitive_color = "#4448"
    
    # Set a default value for the auto-forward time, and note that AFM is
    # turned off by default.
    config.default_afm_time = 10
    config.default_afm_enable = False
    
    
