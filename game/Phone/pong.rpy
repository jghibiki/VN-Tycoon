init:

    image bg pong field:
        "phone/pong_field.png"
        xanchor 0.5
        yanchor 0.5
        rotate_pad True
        rotate -90.0#270.0
        xanchor 0.0
        yanchor 0.0
        xpos 0
        ypos -150
    python:

        class PongDisplayable(renpy.Displayable):

            def __init__(self):

                renpy.Displayable.__init__(self)
                
                # Some displayables we use.
                self.paddle = Image("phone/pong.png")
                self.ball = Image("phone/pong_ball.png")
                self.player = Text(_("Player"), size=14, color="FFF")
                self.eileen = Text(_("Oponent"), size=14, color="FFF")
                self.ctb = Text(_("Click to Begin"), size=14, color="FFF")
                
                # The sizes of some of the images.
                self.PADDLE_WIDTH = 6
                self.PADDLE_HEIGHT = 60
                # self.PADDLE_WIDTH = 8
                # self.PADDLE_HEIGHT = 79
                self.BALL_WIDTH = 11
                self.BALL_HEIGHT = 11
                # self.BALL_WIDTH = 15
                # self.BALL_HEIGHT = 15
                self.COURT_TOP = 75
#                self.COURT_BOTTOM = 543
                self.COURT_BOTTOM = 300
                self.WIDTH=config.screen_width
                self.HEIGHT=config.screen_height

                self.COURT_LEFT=125
                
                # If the ball is stuck to the paddle.
                self.stuck = True
                
                # The positions of the two paddles.
                self.playery = (self.COURT_BOTTOM - self.COURT_TOP) / 2
                self.computery = self.playery

                # The speed of the computer.
                #self.computerspeed = 350.0
                self.computerspeed = 250.0

                # The position, dental-position, and the speed of the
                # ball.
                #self.bx = 88
                self.bx = self.COURT_LEFT+88
                self.by = self.playery
                self.bdx = .5
                self.bdy = .5
                self.bspeed = 300.0

                # The time of the past render-frame.
                self.oldst = None

                # The winner.
                self.winner = None

            def visit(self):
                return [ self.paddle, self.ball, self.player, self.eileen, self.ctb ]
                
            # Recomputes the position of the ball, handles bounces, and
            # draws the screen.
            def render(self, width, height, st, at):
                
                # The Render object we'll be drawing into.
                r = renpy.Render(width, height)
                
                # Figure out the time elapsed since the previous frame.
                if self.oldst is None:
                    self.oldst = st
                    
                dtime = st - self.oldst
                self.oldst = st

                # Figure out where we want to move the ball to.
                speed = dtime * self.bspeed
                oldbx = self.bx

                if self.stuck:
                    self.by = self.playery
                else:                    
                    self.bx += self.bdx * speed
                    self.by += self.bdy * speed

                # Move the computer's paddle. It wants to go to self.by, but
                # may be limited by it's speed limit.
                cspeed = self.computerspeed * dtime
                if abs(self.by - self.computery) <= cspeed:
                    self.computery = self.by
                else:
                    self.computery += cspeed * (self.by - self.computery) / abs(self.by - self.computery)

                y = self.computery
                y = max(y, self.COURT_TOP+15)
                y = min(y, self.COURT_BOTTOM-15)
                self.computery = y
                
                # Handle bounces.
                
                # Bounce off of top.
                ball_top = self.COURT_TOP + self.BALL_HEIGHT / 2                
                if self.by < ball_top:
                    self.by = ball_top + (ball_top - self.by)
                    self.bdy = -self.bdy
                    renpy.sound.play("phone/pong_beep.wav", channel=0)
                    
                # Bounce off bottom.
                ball_bot = self.COURT_BOTTOM - self.BALL_HEIGHT / 2
                if self.by > ball_bot:
                    self.by = ball_bot - (self.by - ball_bot)
                    self.bdy = -self.bdy
                    renpy.sound.play("phone/pong_beep.wav", channel=0)

                # This draws a paddle, and checks for bounces.                       
                def paddle(px, py, hotside):

                    # Render the paddle image. We give it an 800x600 area
                    # to render into, knowing that images will render smaller.
                    # (This isn't the case with all displayables. Solid, Frame,
                    # and Fixed will expand to fill the space allotted.)
                    # We also pass in st and at.
                    pi = renpy.render(self.paddle, self.WIDTH, self.HEIGHT, st, at)

                    # renpy.render returns a Render object, which we can
                    # blit to the Render we're making.
                    r.blit(pi, (int(px), int(py - self.PADDLE_HEIGHT / 2)))

                    if py - self.PADDLE_HEIGHT / 2 <= self.by <= py + self.PADDLE_HEIGHT / 2:

                        hit = False
                        
                        if oldbx >= hotside >= self.bx:
                            self.bx = hotside + (hotside - self.bx)
                            self.bdx = -self.bdx
                            hit = True
                            
                        elif oldbx <= hotside <= self.bx:
                            self.bx = hotside - (self.bx - hotside)
                            self.bdx = -self.bdx
                            hit = True
                            
                        if hit:
                            renpy.sound.play("phone/pong_boop.wav", channel=1)
                            self.bspeed *= 1.10
                            
                # Draw the two paddles.
                #paddle(68, self.playery, 68 + self.PADDLE_WIDTH)
                #paddle(724, self.computery, 724)
                paddle(self.COURT_LEFT+68, self.playery, self.COURT_LEFT+68 + self.PADDLE_WIDTH)
                paddle(484, self.computery, 484)

                # Draw the ball.
                ball = renpy.render(self.ball, self.WIDTH, self.HEIGHT, st, at)
                r.blit(ball, (int(self.bx - self.BALL_WIDTH / 2),
                              int(self.by - self.BALL_HEIGHT / 2)))

                # Show the player names.                
                player = renpy.render(self.player, self.WIDTH, self.HEIGHT, st, at)
                #r.blit(player, (20, 25))
                r.blit(player, (175, 60))

                # Show Eileen's name.
                eileen = renpy.render(self.eileen, self.WIDTH, self.HEIGHT, st, at)
                ew, eh = eileen.get_size()
                #r.blit(eileen, (790 - ew, 25))
                r.blit(eileen, (510 - ew, 60))
                
                oponentscore = renpy.render(Text(str(pong_oponent), size=14, color="FFF"), self.WIDTH, self.HEIGHT, st, at)
                r.blit(oponentscore, (490 - ew, 60))
                playerscore = renpy.render(Text(str(pong_player), size=14, color="FFF"), self.WIDTH, self.HEIGHT, st, at)
                r.blit(playerscore, (230, 60))
                
                # Show the "Click to Begin" label.
                if self.stuck:
                    ctb = renpy.render(self.ctb, self.WIDTH, self.HEIGHT, st, at)
                    cw, ch = ctb.get_size()
                    #r.blit(ctb, (400 - cw / 2, 30)) 
                    r.blit(ctb, (345 - cw / 2, 60)) 
                    
                
                # Check for a winner.
                if self.bx < 150:
                #if self.bx < -200:
                    self.winner = "oponent"
                    # Needed to ensure that event is called, noticing
                    # the winner.
                    renpy.timeout(0)

                #elif self.bx > 1000:
                elif self.bx > 505:
                    self.winner = "player"
                    renpy.timeout(0)

                # Ask that we be re-rendered ASAP, so we can show the next frame.
                renpy.redraw(self, 0)
                
                # Return the Render object.
                return r
                
            # Handles events.
            def event(self, ev, x, y, st):
                import pygame
                # Mousebutton down == start the game by setting stuck to false.
                if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                    self.stuck = False
                # Set the position of the player's paddle.
                y = max(y, self.COURT_TOP+15)
                y = min(y, self.COURT_BOTTOM-15)
                self.playery = y
                # If we have a winner, return him or her. Otherwise, ignore the current event.
                if self.winner:
                    return self.winner
                else:
                    raise renpy.IgnoreEvent()
