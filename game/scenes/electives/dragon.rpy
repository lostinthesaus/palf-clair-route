label dragonelective:

$ renpy.transition(dissolve)
show screen currentdate

scene map
show blank2:
    alpha 0.8

show classroom with dis:
    alpha 1.0
show dragontype:
    alpha 0.0 xalign 0.5 yalign 1.0
    ease 0.5 alpha 1.0
show dragclass:
    alpha 0.5 xalign 0.5 yalign 1.0
    block:
        ease 2.0 alpha 1.0
        ease 2.0 alpha 0.5
        repeat
show classlights:
    alpha 0.0 xalign 0.5 yalign 1.0
    ease 0.5 alpha 0.5
show dragglow:
    alpha 0.75 xalign 0.5 yalign 1.0
    block:
        ease 2.25 alpha 0.5
        ease 1.8 alpha 0.75
        repeat

$ location = "dragon"
$ passedclass = False

############################################################################################################################################################################################################################
#### 13. DRAGON      #######################################################################################################################################################################################################
############################################################################################################################################################################################################################
$ renpy.pause(1.0, hard=True)

call dawnevent from _call_dawnevent
call ethanevent from _call_ethanevent_2
call tiaevent from _call_tiaevent

label afterdragonsetup:

if (2.1 in persondex["Instructor Clair"]["ClassesKnown"]):
    menu:
        "{b}>General Studies{/b}":
            pass

        ">Ask for move tutoring":
            jump movetutordragon

        ">Craft items" if (3.1 in persondex["Instructor Clair"]["ClassesKnown"]):
            jump itemcraftdragon

if (persondex["Instructor Clair"]["ClassesKnown"] == []): #first class
    $ persondex["Instructor Clair"]["ClassesKnown"].append(1)
    $ renpy.pause(1.0, hard=True)

    red uniform thinking "Of all the people to be here..."

    show blue uniform with dis

    blue "That look on your face is {i}priceless.{/i}"
    blue talkingmouth "Sad you're never gonna be the best as long as I'm here, right?"
    blue @angrybrow "There are plenty of other schools you can transfer to."
    blue happy "It's not too late to save yourself from being number two for another year!"

    red -thinking @frownmouth "Yeah, right. I'm not coming all this way just to quit."

    blue angry "Ha! We'll just see about that!"
    
    hide blue with dis

    pause 0.75
    
    hide blue2

    show clair with dis

    clair @angry "Take your seats. Quickly now!{w=0.5} Class started a while ago."

    ethan uniform surprised "Dude! Look at what she's wearing!"
    red "I'm a bit more focused on what she {i}isn't{/i} wearing."


    if (calDate.month == 4 and calDate.day == 5):
        clair @closedbrow talking2mouth "Good day, class. Welcome to your first {color=#0048ff}Dragon-type class{/color} of the year."
    else:
        clair  @closedbrow talking2mouth "I see we have some new students. Welcome to your first {color=#0048ff}Dragon-type class{/color}."

    $ BecomeNamed("Instructor Clair")
    clair @talking2mouth "I'm Clair, your teacher for this year."
    $ ValueChange("Instructor Clair", 1, -0.5)

    hide clair with dis

    pause 0.5
    
    show clairbg with dis

    clair @angry "First off, let me say this..."
    clair @closedbrow talking2mouth "This class will be unlike anything you have taken before."
    clair @angry "That is because Dragon Pokémon are unlike any Pokémon in the world."
    clair @talking2mouth "If you are in this class simply because you've heard that Dragon Pokémon are the strongest Pokémon known to mankind, then you might as well drop out now."
    clair @angry "Dragon Pokémon are strong not only in body, but in mind!"
    clair @closedbrow talking2mouth "As the apex species of Pokémon, they will not obey humans so easily."
    clair @surprised "Many careless Dragon Trainers in the past have lost their lives attempting to tame them."
    clair @angrybrow talking2mouth"To properly instruct you all on how to train and care for your Dragon Pokémon, I will not tolerate laziness or misconduct in this classroom!"
    clair @talking2mouth "If I see or hear anything out of you that goes against the school's policies or my own, I'll personally sign your expulsion papers from this school!"

    ethan @thinking "Geez. Despite how hot she is, this lady is really putting on the hard-ass pants."
    red @happy "What pants?"

    clair @talkingmouth "It is no coincidence that Dragon Pokémon are present on the majority of Champion teams.{w=0.5} They are superior to all other Pokémon in both offense and defense."
    clair @closedbrow happymouth "There is nothing a Dragon Pokémon can't do that other Pokémon can!"

    show dawn sadbrow uniform at leftside with dis

    pause 1.5

    clair @angry "You! You look doubtful!"

    dawn surprised "Uh? N-no, Miss! Not me! I totally respect Dragon-types! Yep!"

    show leaf uniform at rightside with dis

    leaf "Okay, I gotta hear this. What's your story, pinky?"

    dawn sad "N-nothing! Other p-pinky. Or... like, light Magenta-ie? I'm sorry, I don't know what color that is on your hat, but I started talking and now it's too late to stop and--"

    show classroom with vpunch

    show dawn surprised with dis
    clair @angry "Silence! You're making a mockery of the proud name of Dragon-types! With such {i}disrespect{/i}, you can {i}never{/i} hope to stand in the presence of a--"

    show dawn -surprised with dis
    leaf angrybrow angrysmilemouth "Yo. I {i}have{/i} a Dratini."

    clair surprisedbrow "...W-what?"

    leaf happy "Yeah. Cute little guy. Likes to ride in my hoodies."

    clair "..."

    show classroom with vpunch

    clair @closedbrow talkingmouth "WELL!{w=0.5} It's only natural that a not-fully-evolved Pokémon would be easier to get along with, and have mercy on your--"

    dawn happy "Oh, I have an Altaria! And, um, she can Mega Evolve! And she does it sometimes so that I can rest in her fluff!"

    pause 1.0

    redmind @thinking "Mega Evolution, huh?"

    dawn surprised "Um, I'm sorry! I didn't mean to interrupt! I'm sure my Altaria is just a very special case!" 
    dawn sad "And, I mean, I raised her from a Swablu, which is really kind of cheating, right? I'm sorry!"
    dawn surprised "You're right about Dragon-types, and I'm wrong! About everything!"

    show dawn:
        xpos 0.25
        ease 0.2 xpos -0.5

    pause 0.5

    show leaf happy with dis

    hide leaf at rightside with dis

    pause 1.0

    show classroom with vpunch

    hide blue

    clair -surprisedbrow @closedbrow talkingmouth"WELL!{w=0.5} Clearly, you girls are very skilled and talented trainers. As is befitting a student of Kobukan Academy. But anyone else who attempted to treat their Dragon-types with such {i}reckless{/i} disregard--!"

    show blue uniform happy at rightside with dis

    blue "That's not what you said before."

    clair @angry "Who said that?!"
        
    blue surprisedbrow "Uh, me.{w=0.5} I'm just pointing out the contradiction in what you said and--"
        
    show classroom:
        parallel:
            xalign 0.0
            ease 0.03 xpos -15
            ease 0.03 xpos 15
            ease 0.03 xpos 0
            repeat 3
        parallel:
            yalign 0.0
            ease 0.03 ypos -30
            ease 0.03 ypos 30
            ease 0.03 ypos 0
            repeat 3
    
    show dragontype:
        parallel:
            xalign 0.0
            ease 0.03 xpos -15
            ease 0.03 xpos 15
            ease 0.03 xpos 0
            repeat 3
        parallel:
            yalign 0.0
            ease 0.03 ypos -30
            ease 0.03 ypos 30
            ease 0.03 ypos 0
            repeat 3


    show blue surprised with dis
    clair @angry "SILENCE! I hear one more word out of you and I'll toss you out of this school myself!"
    
    blue surprised "Urp!"

    hide blue at rightside with dis

    redmind @happy "Wow, she managed to scare [blue_name].{w=0.5} That's not something many people are able to pull off."

    pause 2.0

    clair @sad "We've wasted far too much time today..."
    clair @closedbrow talking2mouth "The point is, if you want to survive training a Dragon Pokémon, there are strict guidelines and rules that you must adhere to before even attempting to approach one, let alone trying to catch one!"
    clair @talking2mouth "Dragon Pokémon are in many ways superior beings to humans, so you will treat them as such."
    clair @closedbrow talking2mouth "Anything less, and you might find yourself with your life on the line."

    ethan "If this lady is trying to scare me from ever partnering with a Dragon Pokémon, it's working."
    red "We can't give up now.{w=0.5} It's way too early in the game for us to call it quits just yet."

    hide clair
elif (2.1 not in persondex["Instructor Clair"]["ClassesKnown"] and classstats["Dragon"] >= 10):#Legacy
    show clair with dis
    if (2 not in persondex["Instructor Clair"]["ClassesKnown"]):
        $ renpy.pause(1.0, hard=True)

        narrator "The class is reading about the influence of Dragon-type Pokémon in human history, when suddenly..."

        clair @angry "[first_name]! Look at me."

        red uniform @surprised "Ulp. Yes, Ma'am!"

        clair @closedbrow talkingmouth "You seem as though you're close to grasping a fragment of the Dragon Type's majesty!" 
        clair @talking2mouth "You'll take the advancement exam, after you answer one question!"

        red @thinking "Uh, okay..."

        clair @surprisedbrow talking2mouth "What is the downfall of every other type as compared to the Dragon type?"

        red @surprised "Um... well, you've told us a lot about why dragons are the best, but I don't think you've mentioned the other types as much..."

        clair @closedbrow talking2mouth "I ask because I want to hear {i}your{/i} opinion. Quickly, now!"

        red @thinking "Okay, well... no other type has as good a balance of offense and defense."

        clair @talking2mouth "No."

        red @sad "Hey, I thought this was an opinion question..."

        clair @angry "Your opinion is wrong. It's {i}reputation!{/i} It's {i}legacy{/i}!"

        red @thinking "...Um. What does that mean?"

        clair @closedbrow talkingmouth "What do you think when you hear a dragon is coming for you?"

        red @happy "Well, I think I'd better run. Or maybe hide...? Or cower?"

        clair @closedbrow talking2mouth "Exactly! Now, what do you think when I say a 'grass' is coming for you? Or a 'psychic' is coming for you?"
        clair @angry "Or, as Instructor {i}Valerie{/i} would point out, a 'fairy' is coming for you?"

        red @surprised "Huh. That's... actually, I see what you mean. That's not nearly as scary."

        clair @happy "Exactly! The legend of dragons affects the battle before it even begins!"
        clair @talkingmouth "A key part of mastering your usage of dragons is {i}wielding{/i} that legacy."
        clair @talking2mouth "I challenge you to a one-on-one Pokémon battle."
        clair @closedbrow talkingmouth "Prove to me your worthiness, and I will bestow upon you a powerful Dragon-type move, honed and perfected across hundreds of generations of dragon tamers--{i}Legacy!{/i}"

        red @thinking "Doesn't ring a bell."

        clair @closedbrow talkingmouth "It will cause your opponent to become paralyzed with fear, and flinch at your wrath, as soon as your dragons enter the battlefield."

        red @happy "...Does it work after that?"

        pause 2.0

        clair @sad "...No."

        pause 1.0

        clair @angry "But who would need that?"

        $ persondex["Instructor Clair"]["ClassesKnown"].append(2)
    else:
        red uniform @talking2mouth "Clair, I've studied since the last time we fought--and now I'm more than ready to beat you."

    clair @talking2mouth "Enough talk! Face me! We'll see if you are truly worthy to wield the power of legends! {color=#0048ff}I will be using a noble Dragon Pokémon{/color}--choose accordingly!"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    clair @happy "Behold, students! The dance of dragons begins now!"
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("clair", TrainerType.Enemy, [
        Pokemon(704, level=11, moves=[GetMove("Tackle"), GetMove("Absorb"), GetMove("Water Gun"), GetMove("Dragon Breath")], ability="Sap Sipper")
    ])

    call Battle([trainer1, trainer2], reanchor=[False, False], uniforms=[True, False]) from _call_Battle_26
    $ gymbattles["Instructor Clair1"]  = _return

    show clair with dis

    if (WonBattle("Instructor Clair1")):
        $ persondex["Instructor Clair"]["ClassesKnown"].append(2.1)

        red uniform @confusedeyebrows talking2mouth "Huh. With the way you were talking up your Pokémon, I kinda figured you'd use something more powerful than a Goomy."

        clair @closedbrow talking2mouth "I do not want you to {i}fail{/i} this class. Obviously, I am holding back against a student such as yourself." 
        clair @talkingmouth "More challenges await on the long road to walking the path of a dragon tamer!"

        $ passedclass = True
        jump aftertutorintrodragon
    
    else:
        clair @angry "Disappointing! You besmirch the noble name of dragons by putting up such a weak showing!"
        clair @closedbrow talkingmouth "Train hard and return."

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide clair with dis
elif (3.1 not in persondex["Instructor Clair"]["ClassesKnown"] and classstats["Dragon"] >= 20):#Dragon Fang
    show clair with dis
    if (3 not in persondex["Instructor Clair"]["ClassesKnown"]):
        $ renpy.pause(1.0, hard=True)

        clair @talking2mouth "[first_name]! I have need of your attention!"

        red uniform @talkingmouth "Yes, Instructor Clair?"

        clair @talkingmouth "I would ask you a question. When interacting with dragons, what is the most important thing to remember?"

        red @thinking "Hm... that they're superior creatures, in every way, shape, and form?"

        if (GetRelationshipRank("Instructor Clair") >= 1):

            clair @happy "Good! You've been listening to my lectures. Now, what is the most important thing to remember when interacting with any Pokémon, of any type?"

            red @confused "Oh? I'm not sure I know that one, Ma'am."

            clair @angry "Foolishness! I know you do--I've seen it in how you interact with your Pokémon. You must remember to make them feel appreciated! And loved!"

            redmind uniform @surprised "...Huh."

            red uniform @neutral "Yeah, that's what I told you."

            pause 0.25

            clair surprised "...So it is."

            pause 0.5

            clair angry "I misspoke."

            red uniform @happy "I don't think so."

            clair @sadbrow -happymouth "{size=30}Inconcievably frustrating...{/size}"

            clair angry @talking2mouth "Regardless of that, it's doubly important for interacting with the truly awe-inspiring Dragon-types!"

        else:
            
            clair @happy "Good! You've been listening to my lectures. Now, what is the most important thing to remember when interacting with any Dragon?"

            red @confused "Oh? I'm not sure I know that one, Ma'am."

            clair @angry "Fool! Is it not obvious? You must fully respect the immense power that they wield! They must feel appreciated! And lov-"

            clair @surprised "A-and "

            extend @angry "respected!"

            redmind uniform @thinking "She's not wrong..."

            red @surprised "But shouldn't you do that for any Pokémon, even other types?"

            clair @surprised "U-uh..."

            clair @thinkingbrow "Hmph! Perhaps, but is it not natural that the most superior of Pokémon should be the most appreciated and loved?"
            
            redmind @thinking "And {i}there{/i} it is."

        clair @closedbrow talking2mouth "You must compliment your dragons! You must praise them! And if they deign to accept your appreciation, they may bestow upon you a gift from their mighty hoard!"

        red @confused "Oh, yeah? How does that work?"

        clair @happy "Behold!"

        show clair:
            ease 0.5 xpos 0.25

        $ dragonairnum = pokedexlookupname("Dragonair", DexMacros.Id)

        $ sidemonnum = dragonairnum

        $ PlaySound("Pokemon/ball sound.ogg")
        $ PlaySound("Pokemon/cries/{}.wav".format(dragonairnum))

        show sideportraitfull at pokeball, dormdesk

        if (GetRelationshipRank("Instructor Clair") >= 1):
            "{color=#0000ff}Dee-Dee{/color}" "Dra..."

            red uniform @happy "Well hey there, you must be Dee-Dee!"

            clair @angry "I- ...[first_name]!"

            red uniform @talkingmouth "You are just adorable. I bet she used to wear you like a lil' scarf when you were both little, right?"

            "{color=#0000ff}Dee-Dee{/color}" "Dra!"

            clair @blush -surprisedbrow -angrymouth "Dee-Dee!"

            red uniform @happy "I think that's a yes, Instructor."

            clair @blush -sad "...I have made a grave mistake."

            red uniform @happy "Well Dee-Dee, I think you're a real strong Pokémon, aren't you? I've bet you've won plenty of battles."

        else:
            "{color=#0000ff}Dragonair{/color}" "Dra..."
            
            pause 2.0
            
            red @talkingmouth "Okay. I'm beholding. Now what?"
            
            clair @talkingmouth "Compliment her."
            
            pause 1.0
            
            red @confused "You're serious?"
            
            clair @closedbrow talking2mouth "Unless you can swallow your pride and accept the superiority of another, you will never make a good Dragon-type trainer! I'm entirely serious, [first_name] [last_name]."
            
            pause 1.0
            
            red @confused "Okay."
            
            pause 0.5
            
            red @talkingmouth "Hey, Dragonair. You've got some really sweet wings. And that pearl on your chest? Beautiful."

        $ PlaySound("Pokemon/cries/{}.wav".format(dragonairnum))

        show sideportraitfull:
            easein 0.5 ypos 0.88
            easeout 0.5 ypos 0.78

        pause 2.0

        if (GetRelationshipRank("Instructor Clair") >= 1):
            
            narrator "Dee-Dee seems extraordinarily pleased, and bows her head at you. Instructor Clair's brow could not be more furrowed."

            clair @thinking "...At least it worked, I suppose."

            clair @angry "Must you do so in such an... embarassing way?"

            clair @surprised "Still, how quickly you got Dee-Dee's respect..."

            red uniform @confused "So... besides messing with you, what was the point of this?"

            clair @thinking -talkingmouth "A chance to speak with an actually strong Pokémon."

            pause 0.5

            clair @thinking "... and to see how easily you connect with Pokémon."

            red uniform @thinking "Yeah, well, I think Dee-Dee is more then strong."

            extend @happy "She's also a really cute Pokémon!"

            clair @angry "She is not-"

        else:
            
            narrator "The Dragonair seems pleased, and bows its head at you. Instructor Clair is notably impressed."

            clair @surprised "...So much respect! {size=30}In so little time... hm.{/size}"
            
            red @confused "What was I supposed to get out of this?"
            
            clair @talkingmouth "The experience of communing with a higher life form!"
            
            red @talkingmouth "Right. Well, this was fun. Um..."
            
        $ PlaySound("Pokemon/cries/{}.wav".format(dragonairnum))

        narrator "Suddenly, the Dragonair places a small, pointed tooth in your hand."

        $ PlaySound("Pokemon/ball sound.ogg")

        show sideportraitfull at backinpokeball

        show clair:
            xpos 0.25
            pause 2.0
            ease 0.5 xpos 0.5

        clair @surprised "Hah! That's a Dragon Fang. Dragons will only grant those to the trainers they think are truly worthy! They give Dragon-type moves a 10%% boost to their power!" 
        clair @surprised "This must mean my Dragonair thinks you are ready to take the advancement exam!"

        redmind @confused "Who's the instructor here, you or the Dragonair?"

        $ persondex["Instructor Clair"]["ClassesKnown"].append(3)
    else:
        red uniform @talking2mouth "Instructor Clair, my Pokémon and I have trained, and are ready to take the advancement exam again."

    clair @angry "The time for righteous battle is now! {color=#0048ff}I'll be using a noble Dragon-type.{/color} Surely only another Dragon-type could beat me!"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    clair @happy "Let us bear witness to the majestic dance of dragons!"
    
    $ trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $ trainer2 = Trainer("clair", TrainerType.Enemy, [
        Pokemon("Drampa", level=21, moves=[GetMove("Dragon Rage"), GetMove("Light Screen"), GetMove("Glare"), GetMove("Protect")], ability="Sap Sipper", item="Oran Berry")
    ])

    call Battle([trainer1, trainer2], reanchor=[False, False], uniforms=[True, False]) from _call_Battle_78
    $ gymbattles["Instructor Clair2"]  = _return

    show clair with dis

    if (WonBattle("Instructor Clair2")):
        $ persondex["Instructor Clair"]["ClassesKnown"].append(3.1)

        clair @happy "Hm! It seems you are worthy of this Dragon Fang, after all!"

        if (GetRelationshipRank("Instructor Clair") >= 1):
            red uniform @happy "Didn't Dee-Dee already give it to me, though? Are you second-guessing her?"

            clair @blush -surprised "Wh--"

            pause 0.5

            clair @blush -angry "Imbecile."

            clair @blush thinking "You will erase that name from your memory."

            red uniform @happy "Seeing how flustered you get, I don't think I can."

            clair @sad "{i}Sigh{/i}..." 

        
        else:
            red uniform @happy "Didn't your Dragonair already give it to me, though? Are you second-guessing her?"
            
            clair @surprised "Wh-- No! I would never! Don't try to get smart with me, [last_name]! My cousin's told me about you."
            
            redmind @thinking "Your cousin? Wait... Lance. Of course."

        $ GetItem("Dragon Fang", 1, "You gained a Dragon Fang! It's still a bit wet.")

        jump aftertutoring
    
    else:
        clair @closedbrow talking2mouth "Shameful. This dragon classroom rarely bears witness to fights such as that. I'd ask you to see to it that it does not see another!"

        hide clair with dis

        redmind uniform @thinking "Oof... that was an embarrassing loss. Still, at least I learned something..."

    hide clair with dis
elif (4.1 not in persondex["Instructor Clair"]["ClassesKnown"] and classstats["Dragon"] >= 30):#Dragon Breath
    show clair with dis
    if (4 not in persondex["Instructor Clair"]["ClassesKnown"]):
        $ renpy.pause(1.0, hard=True)

        clair @talkingmouth "[first_name] [last_name]! What is a dragon's most powerful weapon?"

        red uniform @confused "Their... legacy?"

        clair @closedbrow talking2mouth "I'm not speaking metaphorically. What do dragons use to inflict the most damage on their foes?"

        red @talkingmouth "Well... it depends on if they're a special or a physical attacker... but the classic 'draconic weapon' is their breath."

        clair @happy "This is correct!"

        red @thinking "Not all dragons know Dragon Breath, though."

        clair @talking2mouth "This is also correct. But a dragon's breath can take many forms. Even the same dragon might have multiple breaths. Flamethrower, Dragon Pulse, Thunderbolt, Ice Beam..."
        clair @talkingmouth "All breaths of the noble dragon!"

        red @confused "I guess it's true that a lot of dragons emit their energy attacks from their mouths. They aren't actually, like, 'breathing' the element, though, are they?"

        clair @closedbrow talkingmouth "In technical, scientific, terms, no. Rather, they're generating energy that resembles that element from an organ in their mouth and expelling it."
        clair @talking2mouth "But to the scientists of the Sinnoh region who first made a dedicated catalog of this behavior, it appeared as though the dragons were, indeed, breathing these powers."
        clair @closedbrow talkingmouth "And even before that first Pokédex, it was a commonly understood medieval belief that dragons could, truly, 'breathe' their attacks."

        pause 0.5

        clair @angry "At this point, claiming that dragons do not 'breathe' fire, or ice, or whatever else they please, is naught but an exercise in pedantry."

        red @confused "And far be it from me to engage in such foibles."

        pause 0.5

        clair @talking2mouth "Indeed."

        pause 0.5

        clair @closedbrow talkingmouth "I was not sure about you at first, [first_name]. My cousin's reports on your character were frequent, and uncomplimentary."
        
        if (GetRelationshipRank("Instructor Clair") >= 1):

            clair @thinkingbrow happymouth "But, we've already discussed our intentions about that."

            red uniform @thinking "Yes, and how I'm going to prove you both wrong."

            clair @thinking "Hmph."

            extend sad ".."

            pause 0.5

            clair neutral "In any case, I believe you are ready to advance to the next level of my class."

            red uniform @happy "Great! What's that mean exactly?"

            clair talkingmouth "It means you will be tested accordingly, and as a reward I will impart my knowledge of the move Dragon Breath."

            red uniform @surprised "Uh... I don't know if I'm ready to face down another one of your Pokémon..."

            clair @thinkingbrow -angrymouth "Pfft. That was a special test, this one will follow the rubric outlined."

            if (WonBattle("ShepClair_1")):
                
                clair @happy "As I recall, you actually won there, anyways. This should be no struggle for you."

            clair @talking2mouth "If you defeat me, the move Dragon Breath can be taught to any Dragon Pokémon powerful enough to harness it."

            clair @sad "...a-and a few other Pokémon are strong enough to wield it too."

        else:
            
            clair @talkingmouth "But he, not being a dragon, is capable of lapses in judgment. It seems that you are, at the very least, as respectful of the majesty of dragons as you should be."
            
            pause 0.5
            
            clair @sadbrow talking2mouth "Though still wholly ignorant of how glorious they truly are, of course."
            
            red @happy "Well, you're doing a brilliant job of educating me on that matter."
            
            clair @closedbrow talkingmouth "Hmph. Your flattery is appreciated. I think you are ready to advance to the next level of this class."
            
            red @surprised "Oh, really? Fantastic! What does that mean?"
            
            clair @closedbrow talkingmouth "It means that I will teach your Pokémon the move Dragon Breath if you pass the advancement exam."
            
            clair @talking2mouth "There are even some non-Dragon-types that are capable of learning the move. Reluctantly, I will impart the move unto them, as well."
            
        red @talkingmouth "Alright. I'm ready to take the exam now, then."

        $ persondex["Instructor Clair"]["ClassesKnown"].append(4)
    else:
        red uniform @talking2mouth "Instructor Clair, I've studied since the last time we fought--and now I'm more than ready to beat you."

    clair @closedbrow talkingmouth "Hm! Can you ever truly be ready to [bluecolor]face down a dragon?{/color} Pick a Pokémon, then, to behold my power!"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    clair @happy "Let us bear witness to the majesty of dragons!"

    $ hidebattleui=False
    $ mustswitch = False
    $ trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $ trainer2 = Trainer("clair", TrainerType.Enemy, [
        Pokemon("Cyclizar", level=31, moves=[GetMove("U-Turn"), GetMove("Bite"), GetMove("Quick Attack"), GetMove("Breaking Swipe")], ability="Shed Skin", item="Sitrus Berry")
    ])

    call Battle([trainer1, trainer2], uniforms=[True, False], reanchor=[False, False]) from _call_Battle_79
    $ gymbattles["Instructor Clair3"]  = _return

    show clair with dis

    if (WonBattle("Instructor Clair3")):
        $ persondex["Instructor Clair"]["ClassesKnown"].append(4.1)

        clair @talkingmouth "Well done. You have managed to beat three powerful Dragons. In future fights, I will be using three Pokémon. I will expect you to bring three of your own."

        pause 0.5

        red uniform @confused "Uh, sorry, one question. Are you {i}only{/i} going to use Dragon-types?"

        pause 0.5

        if (GetRelationshipRank("Instructor Clair") >= 1):
            clair @thinking "...Maybe, maybe not. You'll have to wait and see."
        else:
            clair @talking2mouth "Don't ask foolish questions."

        $ passedclass = True

        jump aftertutorintrodragon
    
    else:
        clair @closedbrow talking2mouth "Disappointing! You besmirch the noble name of dragons by putting up such a weak showing!"
        clair @talking2mouth "Train hard and return."

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide clair with dis

else:#generic scene
    show clair with dis
    clair @closedbrow talkingmouth "Sit down, students, and get out your notebooks. I want you to take very careful notes on what I am about to tell you."
    hide clair with dis
    show clairbg with dis
    
    if (GetRelationshipRank("Instructor Clair") >= 1):

        clair "Dragon-types are a very powerful typing of Pokémon. It requires an incredibly strong trainer to wield them at full strength."

        clair "...but a strong trainer must also recognize certain weaknesses that Dragon-types can struggle from."
    
    else:
        clair "Dragon-types have a long and storied history in the mythology of almost every region. Perhaps someone could explain why they are so superior? Yes, you."
        
    narrator "Class proceeds without incident."
    if (IsBefore(7, 4, 2004)):
        pass

    elif (GetCharValue("Instructor Clair") < 10):
        narrator "You notice Instructor Clair seems to eye you with some suspicion."
        $ ValueChange("Instructor Clair", 1, -0.5)
        
        if (GetCharValue("Instructor Clair") == 10):
            clair "[first_name]! A word, if you will."

            show clair:
                xpos 0.25
                pause 2.0
                ease 0.5 xpos 0.5

            redmind @surprised "Uh oh, what will the lecture be now?"
            clair "The next time you have free time, you will meet me at the Battle Hall. Understood?"
            red @surprised "W-what? Any reason?"
            clair closedbrow angrymouth ".{w=0.2}.{w=0.2}.{w=0.2}"
            clair @angrybrow "Be there, [first_name]."
        
            hide clair with dis

            redmind @surprised "What could this possibly be about? Haven't had any other teachers demand to see me outside of class time..."
            redmind @thinking "She has been judging me ever since that public confrontation with Lance... maybe it has something to do with that?"
            redmind @angry "Knowing her, I should expect a lecture. I better be {color=#e226a6}patient{/color} enough to sit through another one."
            redmind @neutral "..."
            extend @surprised " yeah, better make sure I have the {color=#ff8412}courage{/color} to do this too. She's likely to yell my ear off or {b}challenge me to a battle{/b}."

    elif (GetCharValue("Instructor Clair") > 10 and GetRelationshipRank("Instructor Clair") >= 1):
        narrator "Instructor Clair constantly gives you a side-eye, a judging look in it."
        $ ValueChange("Instructor Clair", 1, -0.5)

return

label movetutordragon:
show clair with dis
clair @surprised "You wish to dip into the hoard of Dragon-type moves that Dragon tamers jealously covet? Very well!"
clair @talking2mouth "I can teach Legacy, a move of unparalleled speed that will paralyze your foe and cause them to flinch the first turn a dragon is sent into combat."
if (4.1 in persondex["Instructor Clair"]["ClassesKnown"]):
    clair @talkingmouth "If that is not enough, I can also teach Dragon Breath! This move hits with such force it can paralyze the foe, {i}and{/i} do damage!"

label aftertutorintrodragon:
$ taughtmove = None

menu:
    ">Learn Legacy":
        $ taughtmove = "Legacy"
    ">Learn Dragon Breath" if (4.1 in persondex["Instructor Clair"]["ClassesKnown"]):
        $ taughtmove = "Dragon Breath"
    "Nevermind":
        clair @angry "Turning down a dragon's power? Foolish!"

        if (passedclass):
            jump aftertutoring
        else:
            jump afterdragonsetup
python:
    hidebattleui = True
    renpy.transition(dissolve)
    newindex = renpy.call_screen("switch", MakeRed())
    if (newindex != "back"):
        newmon = playerparty[newindex]
    hidebattleui=False
if (newindex == "back"):
    clair @angry "Turning down a dragon's power? Foolish!"
elif (MonCanLearn(newmon, taughtmove)):
    $ playerparty[newindex].LearnNewMove([(1, taughtmove)])
    if (taughtmove in newmon.GetMoveNames()):
        jump endclass
else:
    clair @closedbrow talking2mouth "I very much doubt {i}that{/i} Pokémon could ever learn such a powerful draconic technique!"
    
jump aftertutorintrodragon

label itemcraftdragon:
show clair with dis

clair @closedbrow talkingmouth "A dragon's hoard is overflowing with powerful items that boost their strength tremendously!"
clair @talking2mouth "A patient dragon may lend you the use of a discarded Dragon Fang. Even a trinket like that can boost the power of your Dragon-type moves by 10%%!"

menu:    
    ">Obtain Dragon Fang" if (3.1 in persondex["Instructor Clair"]["ClassesKnown"]):
        $ GetItem("Dragon Fang", 1, "You patiently compliment Instructor Clair's Dragonair until it deigns to give you one of its fangs.")
        jump endclasscraft
    "Nevermind":
        clair @surprised "Tut! Perhaps you don't know what you'd do with such a powerful item?"
        jump afterdragonsetup