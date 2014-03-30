init python:
    descInputOption = {
                                "skill" : [
                                            "Hey all! \(~o~)/ Looking to hire someone to do some <*input*> for a project of mine. I need about <*inputQuantity*> <*input*> actually.",
                                            "I need someone to help me with <*input*> for this game. Specifically I'll be needing <*inputQuantity*> <*input*>. I'd really appreciate the help. :)",
                                            
                                            "Hello! I have an idea for a visual novel and am looking for someone that would be interested in doing the <*input*> for me. I estimate that aproximately <*inputQuantity*> <*input*> will be needed.",
                                            "Hey all, <*user*> here. The goal of my project is to create a visual novel intended for commercial release on a BMTMezzo managed site and on Vapor.\n\nOpen Positions:\n<*job_in*> 1,\n<*job_in*> 2,\nVoice actor\n\nI need <*inputQuantity*> <*input*>.\n\n",
                                            "Looking for <*job_in*>, willing to lend a hand with some <*input*> (about <*inputQuantity*> will be required).",
                                            "My studio is looking for <*job_in*> to help with some of our projects! You'll be working on some high quality commercial works. We are only looking for developers with experience and who are able to work on a deadline and meet them. We require <*inputQuantity*> <*input*> for now (more work may be available later if this goes well).",
                                          ],
                                "non-skill": [
                                                "I'm looking to sell some work of mine for $<*inputQuantity*>.",
                                                "I'm an expert VN dev looking to work on <*output*>. My price is $<*inputQuantity*>.",
                                                "I've been putting this off for a while but I think it's time I took <*output*> commissions. I'm very versatile with the styles I use. My price is only <*inputQuantity*> USD. I accept PayFiend as a method of payment.",
                                                "Starving <*job_out*> looking for work! (T_T) My price is $<*inputQuantity*>. You can pay me with PayFiend or CompliantArt points.",
                                                "Hello, thank you for your interest! I am a high school student looking to make money for allowance and school supplies through working on <*output*> and voice acting. My <*output*> is only $<*inputQuantity*>.",
                                             ]
                              }

    descOutputOption = {
                         "skill" : [
                                        "I'd be willing to trade for <*outputQuantity*> <*output*>. If you are interested let me know.",
                                        
                                        "I'd like to trade that for <*outputQuantity*> <*output*>. Note that I have an unusual <*output*> style with a dreamy and whimsical kind of touch. I can do other styles too of course, but this kind of <*output*> is the type of <*output*> I'm most comfortable working on. XD",
                                        "I'm offering <*outputQuantity*> <*output*>. If anyone is interested, please contact me!! Thanks so much!",
                                        "I'm new here, but I'm interested in helping out. I can offer <*outputQuantity*> <*output*>. Thank you for reading! :3",
                                        "I'll give you <*outputQuantity*> <*output*>. No 18+ stuff please. :(",
                                        "I'm offering my <*output*> services to anyone who needs them. I'll do <*outputQuantity*> <*output*>. However, I'll only accept projects that don't have strict deadlines. I'm really terrible with deadlines orz.",
                                        "I can offer you <*outputQuantity*> <*output*> for that. Please contact me via PM to apply, comment if you have any questions.\n\n<*user*>"
                                   ],
                         "non-skill": [
                                        "I'd be willing to pay $<*outputQuantity*>. PM me if interested. 8)",
                                        "I can only pay you $<*outputQuantity*>.",
                                        "I'll pay $<*outputQuantity*>! (^_^)/",
                                        
                                      ]
                        }
                        
    
                        
                        
    msgReminderOptions = {
                            "skill" : [
                                        "Thanks for messaging me, as a reminder, it's <*inputQuantity*> <*input*> for <*outputQuantity*> <*output*>. Just message me again when you're done.",
                                        
                                        "Great to have you on the team! Please message me again as soon as you have for me <*inputQuantity*> <*input*> and I'll send you <*outputQuantity*> <*output*>.",
                                        
                                        "Hey!\n\nGood to hear you're interested. You're a real life saver, since my <*input*> looks uh... let's just say I could pass it around kindergarten and parents'd wonder whose kid made it.\n\nAnyway, I sent you an invite for my project storage folder. Add me for easy chatting later, okay? Once you have made <*inputQuantity*> <*input*> PM me again and I'll send you <*outputQuantity*> <*output*> as agreed.",
                                        
                                      ],
                            "non-skill" : {
                                            "in" : [
                                                     "So that will be $<*inputQuantity*> for <*outputQuantity*> <*output*>. Just send me a messege when you're ready to transfer the funds. <3",
                                                     "Please send me another PM once you transfered $<*inputQuantity*> to my PayFiend account. I'll send you <*outputQuantity*> <*output*> as soon as I see the money.",
                                                   ],
                                            "out" : [
                                                     "Just message me when you're ready with account info, and I'll send you $<*outputQuantity*> for the agreed upon <*inputQuantity*> <*input*>.",
                                                     "Once you have <*inputQuantity*> <*input*> ready for me, message me again and I'll send you $<*outputQuantity*> to your PayFiend account.",
                                                    ]
                                          }
                         }

    msgResponseOptions = [
                            "Nice doing business with you!",
                            "Nice working with you!",
                            "Great. Thanks.",
                            "Awesome! :3"
                         ]

    threadTitlesInput = ["Looking for <*job*>",
                         "Looking for <*job*>, please!",
                         "Recruiting <*job*>",
                         "<*job*> is needed",
                         "<*job*> Wanted",
                         "Hiring <*job*>",
                         "Looking for visual novel <*job*>",
                        ]
    threadTitlesOutput = ["<*job*> for hire",
                          "<*job*> Looking for Work",
                          "<*user*>'s <*output*> services",
                          "Need a <*job*>?",
                          "<*job*> Available",
                          "<*job*> Here",
                          "<*job*> looking for projects",
                          "<*job*> open for commissions",
                          "<*job*> for your <*output*> needs",
                          "Experienced <*job*> for Hire",
                          "<*job*> willing to work",
                          "Need a professional <*job*>?",
                         ]
    threadTitlesOutputExtras = ["","","","",
                                "!","!",
                                " - High Quality",
                                " - Fast Delivery",
                                " - Affordable!",
                                " {{OPEN}",
                                " [OPEN]"," [OPEN]",
                                "[open]",
    ]
    
    threadTitlesInputExtras = ["","","","",
                                "!","!",
                                " {{OPEN}",
                                " [OPEN]"," [OPEN]",
                                " [open]",
                                
    ]
    
                         