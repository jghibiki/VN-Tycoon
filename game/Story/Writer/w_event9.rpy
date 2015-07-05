# Event 9:
# Earning money through odd jobs.
# Summary:
# Joan goes out to work, but she hasn't had stable employment in a while. She earns money in a different way instead: Odd jobs.
# Scene:
label writer_event9:
    $ config.rollback_enabled = True
    $ renpy.block_rollback()
    scene black
    Joan scowl_open "Maaaan, how can people stand doing this kind of work? The smell of pizzas all day long just makes me wanna chow down. Just look at you! Perfection incarnate! Salami, cheese, all these... green stuff. Veggies? Paprika? Whatever man! You're delicious, I wanna eat you."
    Joan "But then I can't. Because, you know. The worst decision in the world is to be a deliveryman. Or woman. Or girl. Person. Smelling these things all day... Ugh, I should've just gone with washing the windows again. It's been a while since I cleaned over at Moonbux..."
    Joan despair "AAAAH! What am I, retarded?! Oh... oh damn, you were just too delicious. I'm sorry, Mr Pizza, but I couldn't resist. I know you were meant for that blind bat. But you were too good. Too delicious. You had to be eaten."
    Joan scowl_closed "... My pay is getting docked so hard. Wait, no, I can deal. Maybe I can convince her this is the new way to go."
    Joan "And then never apply for this job again. Ever."
    Joan "Or uh, I can... apologise? Honesty's always the best policy, right? ... Right?"
    Joan "Yeah, I need to get back on the ghost writing gig."
    $ writer_event9 = True
    jump sim
    