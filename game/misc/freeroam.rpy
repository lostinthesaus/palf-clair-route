init python:
    def GetSmilePortrait(charname, transforms = None):
        charname = charname.lower()
        actualname = charname.replace(" uniform", "")
        if (transforms == None):
            transforms = []
        renpy.transition(dissolve)
        if (actualname not in ["hilbert", "sabrina", "silver", "tia"]):
            renpy.show(charname + " happy", transforms)
        elif (actualname == "sabrina"):
            renpy.show(charname + " happymouth", transforms)
        elif (actualname in ["hilbert", "silver"]):
            renpy.show(charname + " smilemouth", transforms)
        elif (actualname == "tia"):
            if (not IsBefore(17, 4, 2004)):
                renpy.show(charname + " happy hat", transforms)
            else:
                renpy.show(charname + " happy", transforms)

label freeroam:

python:
    if (pikachuobj not in playerparty):
        AddPikachu()

    HealParty() 

label beforemusic:

stop music fadeout 2.5
$ renpy.music.queue("audio/music/GSCBike_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
$ renpy.music.queue("audio/music/GSCBike_Loop.ogg", channel='music', loop=True)

label aftersetup:

$ freeroaming = True

scene map with splitfade
show blank2 as blackground behind map
show screen currentdate 
call screen map_UI(_with_none=False)
hide blackground
with dissolve
$ trainer1 = Trainer("red", TrainerType.Ally, playerparty)

$ interaction = _return
$ interactionsprite = interaction.lower()
if (interaction == "Professor Cherry"):
    $ interactionsprite = "kris"
if (interaction == "Tia" and not IsBefore(17, 4, 2004)):
    $ interactionsprite = "tia hat"
if (interaction == "Instructor Clair"):
    $ interactionsprite = "clair"

if (interaction == "Study"):
    redmind @thinking "Now, which type should I focus on...?"

    show blank2 with dis:
        alpha 0.8

    $ lastclass = ""

    call screen studyfocus
    $ selectedtype = _return 

    hide blank2 with dis

    if (selectedtype == "Back"):
        jump aftersetup

    if (excusesecondelective or excusesecondhomeroom):
        redmind uniform @thinking "Almost everyone else is in class right now, so I'll have to study alone. It won't be as effective as studying with someone."

        menu:
            "That's fine.":
                $ IncreaseProficiency(selectedtype, 0.25)

            "Nevermind":
                jump aftersetup
    else:
        $ randomstudent = RandomChoice(list(GetStudents(selectedtype)), True)

        $ pronoun = ("him" if persondex[randomstudent]["Sex"] == Genders.Male else "her")

        label afterlibraryseed:

        redmind @thinking "It looks like [randomstudent] is in the library right now. Should I study with [pronoun]?"

        menu: 
            "Yeah, sure.":
                show library with Dissolve(1.0)
                $ renpy.show(randomstudent.lower(), [dissolvein])

                pause 1.0

                narrator "You spent some time studying [selectedtype]-type Pokémon with [randomstudent]."

                $ GetSmilePortrait(randomstudent)
                if (randomstudent in ["Jasmine", "Grusha"]):
                    $ ValueChange(randomstudent, 4, 0.5)
                else:
                    $ ValueChange(randomstudent, 2, 0.5)
                    
                $ IncreaseProficiency(selectedtype, 0.5)

                $ renpy.transition(dis)
                $ renpy.hide(randomstudent.lower())

            "No, contact someone else.":
                redmind @thinking "Right... let's see if anyone would be interested in studying this with me."
                redmind @thinking "They'll need to be taking the [selectedtype] Elective as well, of course."

                show phone_B 
                show phone_A
                with fadeinbottom

                hide blank2 with dis

                call screen phoneinterface(selectedtype, _with_none=False)
                with dissolve
                $ contact = _return

                if (contact == "Back"):
                    hide phone_B 
                    hide phone_A
                    with fadeoutbottom
                    jump afterlibraryseed
                elif (contact != "Sabrina"):
                    $ pronoun = ("he" if persondex[contact]["Sex"] == Genders.Male else "she")
                    redmind @thinking "Alright, I'll text [contact] and see if [pronoun] can show up."
                else:
                    hide phone_B 
                    hide phone_A
                    with fadeoutbottom
                    redmind @thinking "Alright, I'll think hard at Sabrina and see if she can show up."

                show library with Dissolve(1.0)

                hide phone_B 
                hide phone_A
                with fadeoutbottom

                $ renpy.show(contact.lower(), [dissolvein])

                pause 1.0

                narrator "You spent some time studying [selectedtype]-type Pokémon with [contact]."

                $ renpy.transition(dis)
                $ GetSmilePortrait(contact.lower())
                $ ValueChange(contact, 1, 0.5)
                $ IncreaseProficiency(selectedtype, 0.5)

                $ renpy.transition(dis)
                $ renpy.hide(contact.lower())
            
            "Nevermind, I don't want to study.":
                jump aftersetup

elif (interaction == "Town"):
    if (IsBefore(17, 4, 2004)):
        redmind @thinking "I should probably get a bit more used to the campus before I head out alone."
        jump aftersetup

    elif (trainer1.HasMons()):
        menu:
            "Go to the city.":
                call city from _call_city

            "Nevermind.":
                jump aftersetup
    else:
        redmind @thinking "I shouldn't leave campus with a party this tired-out."
        jump aftersetup

elif (interaction == "Fields"):
    if (IsBefore(13, 4, 2004)):
        redmind @thinking "I should probably get a bit more used to the campus before I head out alone."
        jump aftersetup
    elif (trainer1.HasMons()):
        call wildarea("fields") from _call_wildarea
    else:
        redmind @thinking "I shouldn't leave campus with a party this tired-out."
        jump aftersetup 

elif (interaction == "Business"):
    show baseball
    show gardenia 
    with dis
    gardenia @happy "Heya! You're looking good. Ready to talk business?"
    label beginbusiness:
    menu:
        ">Manage Investments":
            if (investment != 0):
                $ investmentmin = 1000 + math.floor(investment * .1)
                gardenia @talkingmouth "Your total investments come out to $[investment]. For an increase in your basic investment, I'll take anything north of $[investmentmin]."
                python:
                    nextgains = 1
                    for gainthreshold in shopitems.keys():
                        if (gains < gainthreshold):
                            nextgains = gainthreshold - gains
                            break
                $ investmenttime = math.ceil(nextgains / (investment * .05))
                $ investmentportion = math.floor(investment * 0.05)
                gardenia @talking2mouth "Oh, and the stores say they'll be stocking some new materials when your investment has returned... about... $[nextgains] more."
                if (investmenttime == 1):
                    gardenia @talkingmouth "At your current rate of $[investmentportion] per day, you'll make that by the next school day."
                else:
                    gardenia @talkingmouth "At your current rate of $[investmentportion] per day, you'll make that in [investmenttime] school days."
                gardenia @angrybrow happymouth "Hey, you can always speed that up by increasing your investment. What'd ya say?"
            else:
                $ investmentmin = 1000
                gardenia @talkingmouth "If you want to get started, all I need is a little investment of $1,000." 
                gardenia @happy "Or more. I'd take more."
            menu:
                ">Increase Investment":
                    gardenia @happy "Nice! How much?"
                    $ newinvestment = int(renpy.input("How much would you like to invest?", default=investmentmin, length=7, allow="1234567890"))
                    if (newinvestment < investmentmin):
                        gardenia @sad "Sorry! I can't take investments under [investmentmin]. I don't trade in penny stocks, y'know."
                    else:
                        $ InvestmentChange(newinvestment)
                        gardenia @happy "Pleasure doing business with you."

                "Nevermind":
                    jump beginbusiness

        ">Sell Items" if (persondex["Gardenia"]["Contact"]):
            gardenia @happy "Sure, I'll buy something off of you. What're ya sellin'?"

            label selling:

            $ item = renpy.call_screen("fieldinventory", True)
            if (item == "back"):
                gardenia @angrybrow happymouth "Ah, boo!"
                jump beginbusiness
            else:
                $ itemvalue = GetItemSellValue(item)
                $ itemvalueformat = "{:,}".format(itemvalue)
                gardenia @talkingmouth "Hm... not a lot of demand for that item. Best I can do is $[itemvalueformat]."

                $ itemcount = GetItemCount(item)
                $ halfitem = math.floor(itemcount / 2.0)

                menu:
                    ">Sell One":
                        $ money += itemvalue
                        $ LoseItem(item)
                        gardenia @happy "Pleasure doing business with ya!"

                    ">Sell Half ([halfitem])" if (itemcount >= 3):
                        $ money += itemvalue * halfitem
                        $ LoseItem(item, halfitem)
                        gardenia @happy "Pleasure doing business with ya!"

                    ">Sell All ([itemcount])" if (itemcount > 1):
                        $ money += itemvalue * itemcount
                        $ LoseItem(item, itemcount)
                        gardenia @happy "Pleasure doing business with ya!"

                    "Nevermind.":
                        pass

                jump selling

        "Nevermind.":
            gardenia @angrybrow happymouth "Ah, boo!"
            pass

    hide baseball
    hide gardenia 
    with dis
    jump aftersetup

elif (interaction == "LevelCheck"):
    show stadium_empty
    show janine 
    with dis
    $ levelaim = AimLevel()
    $ highestlevel = GetHighestLevel()
    janine @surprised "Hm?"
    janine @closedbrow talkingmouth "Oh, you want a check-in, huh? You should have a team of level [levelaim] Pokémon."
    janine @talkingmouth "Your highest-leveled Pokémon is level [highestlevel]. {nw}"
    if (highestlevel >= levelaim):
        extend @happymouth "You're good."
        if (highestlevel > levelaim + 5):
            janine @surprised "Maybe a bit too good. You've spending a lot of time training, huh? Don't neglect your other responsibilities."
    elif (highestlevel < levelaim):
        extend @sadbrow talkingmouth "Fix that."
        if (highestlevel < levelaim - 5):
            janine @sad "Soon. This is a dangerous situation to be in."

    red @talkingmouth "Thanks for the advice."

    jump aftersetup

elif (interaction == "CriticalCheck"):
    show clouds
    show garden:
        zoom 0.625
    show kris
    with dis
    $ critrate = GetAverageProficiency()
    kris @happy "Hello, [first_name]."
    kris @talkingmouth "Have you been keeping up on your capturing? [bluecolor]Given your current proficiencies, you should expect to be able to land critical captures [critrate]%% of the time."

    red @talkingmouth "Understood. Thanks, Doctor."

    jump aftersetup

elif (interaction == "Back"):
    jump aftersetup

elif (len(getscenes([interaction])) == 1 and getscenes([interaction])[0][1]):#character scenes
    $ renpy.hide(interactionsprite)
    $ renpy.show(interactionsprite, [farleftside, dissolvein])
    narrator "You want to find [interaction]?"

    menu:
        "Yes, go looking for [interaction].":
            stop music fadeout 2.0
            $ renpy.hide(interactionsprite)
            $ renpy.call(getscenes([interaction])[0][1])

            if (GetRelationshipRank(interaction) == 1):
                if (interaction in classdex.keys()):
                    python:
                        classessstring = ""
                        classes = classdex[interaction]
                        for i, classname in enumerate(classes):
                            classessstring += (" and " if i == len(classes) - 1 else " ") + classname + ("," if i < len(classes) - 1 and len(classes) != 2 else "")

                    narrator "Hanging out with [interaction] will now convey a tiny amount of EXP to[classessstring] Pokémon in your party."

                elif (interaction == "Janine"):
                    narrator "Your Pokémon have resolved to work even harder to protect you from the scary woman!"
                    narrator "(They don't quite get the social dynamics going on here...)"

                    python:
                        for mon in playerparty:
                            mon.GainExperience(math.floor(pow(AimLevel(), 3) / 25 / 2))

            jump afterfreetime

        "Nevermind.":
            python:
                renpy.hide(interactionsprite)
                renpy.jump("freeroam")

else:
    if (interaction in ["Sabrina", "Blue", "Janine", "Misty", "Dawn", "Hilbert", "Professor Cherry"] and GetRelationshipRank(interaction) == 0):
        narrator "You suspect that you are not close enough to [interaction] to hang out one-on-one..."
        jump aftersetup
    elif (interaction == "Janine"):
        if (janinedomming):
            narrator "You know better than to bother Janine while she's busy. The possible consequences scare and thrill you... but should be left for another time."
        else:
            narrator "You shouldn't bother Janine while she's busy."
        jump aftersetup
    else:
        if (not IsBefore(17, 4, 2004)):
            if ("tia" in interactionsprite):
                $ interactionsprite += " hat"
        $ renpy.hide(interactionsprite)
        $ renpy.show(interactionsprite, [farleftside, dissolvein])
        narrator "You want to find [interaction]?"

        menu:
            ">Yes, hang out":
                python:
                    GetSmilePortrait(interactionsprite)
                    valuetochange = 3
                    if (interaction in ["Jasmine", "Grusha"]):
                        valuetochange = 6
                    ValueChange(interaction, valuetochange, 0.12)

                narrator "You spend some one-on-one time with [interaction]."
                python:
                    if (GetRelationshipRank(interaction) == 1):
                        partyset = set()
                        if (interaction in classdex.keys()):
                            for mon in playerparty:
                                for typename in classdex[interaction]:
                                    if mon.HasType(typename):
                                        partyset.add(mon)
                        for mon in partyset:
                            mon.GainExperience(math.floor(pow(AimLevel(), 3) / 25 * (GetRelationshipRank(interaction) / 5)))

                    renpy.hide(interactionsprite)
                jump afterfreetime

            ">Give a gift" if (interaction not in GiftsGiven and persondex["Gardenia"]["Contact"]):
                $ item = renpy.call_screen("fieldinventory", True)
                if (item == "back"):
                    $ renpy.hide(interactionsprite)
                    $ renpy.jump("freeroam")
                else:
                    menu:
                        ">Give [interaction] the [item]":
                            python:
                                presentvalue = GetGiftValue(interaction, item)
                                GetSmilePortrait(interactionsprite)
                                if (presentvalue == 1):
                                    renpy.say(None, "{} seems confused, but politely accepts the {}.".format(interaction, item))
                                elif (presentvalue == 2):
                                    renpy.say(None, "{} accepts the {}.".format(interaction, item))
                                elif (presentvalue == 3):
                                    renpy.say(None, "{} happily accepts the {}.".format(interaction, item))
                                elif (presentvalue == 4):
                                    renpy.say(None, "{} joyfully accepts the {}.".format(interaction, item))
                                elif (presentvalue >= 5):
                                    renpy.say(None, "{} ecstatically accepts the {}!".format(interaction, item))
                                if (interaction in ["Jasmine", "Grusha"]):
                                    presentvalue *= 2
                                GiftsGiven.append(interaction)
                                ValueChange(interaction, presentvalue, 0.12)
                                LoseItem(item)

                        "Nevermind":
                            pass

                    $ renpy.hide(interactionsprite)
                    $ renpy.jump("freeroam")

            "Nevermind":
                python:
                    renpy.hide(interactionsprite)
                    renpy.jump("freeroam")

$ freeroaming = False

label afterfreetime:
call clearscreens from _call_clearscreens_18

hide blank2
show blank2 with Dissolve(1.0)

pause 1.0

if (timeOfDay == "Morning"):
    $ timeOfDay = "Noon"
elif (timeOfDay == "Noon" or timeOfDay == "Afternoon"):
    $ timeOfDay = "Evening"
elif (timeOfDay == "Evening" or timeOfDay == "After School"):
    if (excusesecondhomeroom):
        $ jumpto = "aftersecondhomeroom"
        $ jumptoyear = "01"
        $ jumptomonth = ("0" if calDate.month < 10 else "") + str(calDate.month)
        $ jumptodate = ("0" if calDate.day < 10 else "") + str(calDate.day)
        $ renpy.jump(jumpto + jumptoyear + jumptomonth + jumptodate)
    else:
        $ timeOfDay = "Night"

hide noon
hide evening
hide night

if (timeOfDay == "Noon"):
    show noon at vspaz
elif (timeOfDay == "Evening"):
    show evening at vspaz
    if (not excusesecondhomeroom and getRWDay(0) not in ["Saturday", "Sunday"]):
        pause 3.0

        $ jumpto = "secondhomeroom"
        $ jumptoyear = "01"
        $ jumptomonth = ("0" if calDate.month < 10 else "") + str(calDate.month)
        $ jumptodate = ("0" if calDate.day < 10 else "") + str(calDate.day)
        $ renpy.jump(jumpto + jumptoyear + jumptomonth + jumptodate)

elif (timeOfDay == "Night"):
    show night at vspaz

    pause 3.0

    show screen currentdate with dis

    return

pause 3.0

jump beforemusic
