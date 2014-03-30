init python:
    descInputOption = {
                                "skill" : [
                                            "Hey all! looking to hire someone to do some <*input*> for a project of mine. I need about <*inputQuantity*> <*input*> actually."
                                          ],
                                "non-skill": [
                                                "I'm looking to sell some work of mine for $<*inputQuantity*>."
                                             ]
                              }

    descOutputOption = {
                         "skill" : [
                                        "I'd be willing to trade for <*outputQuantity*> <*output*>. If you are intrested let me know.",
                                   ],
                         "non-skill": [
                                        "I'd be willing to pay $<*outputQuantity*>. PM me if interested. 8)"
                                      ]
                        }

    msgReminderOptions = {
                            "skill" : [
                                        "Thanks for messaging me, as a reminder, it's <*inputQuantity*> <*input*> for <*outputQuantity*> <*output*>. Just message me again when you're done.",
                                      ],
                            "non-skill" : {
                                            "in" : [
                                                     "So that will be $<*inputQuantity*> for <*outputQuantity*> <*output*>. Just send me a messege when you're ready to transfer the funds."
                                                   ],
                                            "out" : [
                                                     "Just message me when your ready with account info, and I'll send you $<*outputQuantity*> for the agreed upon <*inputQuantity*> <*input*>."
                                                    ]
                                          }
                         }

    msgResponseOptions = [
                            "Nice doing business with you!",
                            "Nice working with you!"
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
                          "Need a professional <*job*>",
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
    
                         