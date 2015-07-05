label writer_event11:
    $ config.rollback_enabled = True
    $ renpy.block_rollback()
    scene black
# Event 11:
# You're such a badass, you finished the game successfully!
# Summary:
# You finished a game that has 100,000 words and over 50,000 downloads within 60 days. 
# Scene:
    Joan laugh_big "Ahaha... hahaha... AHAHAHA! I DID IT! I DID IIIT!"
    Joan "Hah! Look at that, you pompous ass! I did it! Fifty kay! That's a lot. That's like, a success, man! Each download being equal to at least two words means I'm doing prrrretty great."
    Joan laugh_med "Pfft, now who was bragging about being a great VN writer? Who was saying it's difficult to release this shit and make it quality? Because I just did it."
    Joan "You can take your damn arrogance and shove it up yours! Ahahaha! I did it! I'm a VN novelist!"
    Joan laugh_big "... I'm a VN novelist."
    Joan despair "Oh god. I just spent all that time... writing a VN... when I could have been working to pay the rent... and get a decent job..."
    Joan "I'm screwed."
    Joan "I'm so damn screwed."
    Joan scowl_open "Aaaaaaaaaaaaaagghhhhh! I'll just have to write an even BETTER Visual Novel and rake in the big money! You can do it, Joan!"
    Joan scowl_closed "... Really, you can! ... Please can... please..."
    $ writer_event11 = True
    call the_end
    jump sim