label coder_event8:
    $ config.rollback_enabled = True
    $ renpy.block_rollback()
    scene black
        
    #after hiring a writer
    t neutral_2 "I finally broke down today and accepted that I need a writer. When I forwarded my script to Mark, he fell over laughing for nearly ten minutes. I would have burned the script, but burning silicon releases toxic fumes."
    t "I personally thought that the adventures of Captain Squiqqlywall and his stalwart crew as they fight the dreaded Bibbles was a totally awesome idea. Turns out that it wasn't even fit for a low budget kids show."
    t "Talk with the writer gave me some hope in my project though. It took a while, a carton of chocolate milk, and some compromises on my part, but I think we finally have an outline that won't torpedo this project."
    t scared "She was a bit gruff with me though. I thought I was living out a horror story for a while. Even with the barrier of the internet between us, it was kind of scaring me."
    t neutral "Still... As the saying goes, it takes all kinds to make the world go around. Maybe all writers are like that. I wonder if I have time to do a study on that..."
        
    $ coder_event8 = True
    jump sim