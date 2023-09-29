##Shepurd Clair Route##
init python:
    def ClairHasUnseenScene():
        if (GetCharValue("Clair") >= 5 and GetRelationship("Clair") != "Rascal" and personalstats["Courage"] >= 3 and personalstats["Charm"] >= 3):
            return "ShepClair_1"
        return False

label ShepClair_1:

default shepclair_motivation = ""

scene stadium_empty
with Dissolve(2.0)
queue music "Audio/Music/shepclair_pilgrimage.mp3"

show screen songsplash("Pilgrimage", "Takeru Kanazaki")

red @thinking "...What is she even doing?"

show clair

narrator "You watch as Instructor Clair stands before a Dragonair and Gyarados."

clair thinkingbrow "..."

pause 1.0

clair @talkingmouth "Gyarados, Earthquake."

narrator "The Gyadaros doesn't even hesitate, rattling the very ground of the arena. However, the Dragonair remains standing."

pause 2.0

clair angrybrow "{i}Sigh...{/i}"

clair "Dee-Dee, Dragon Pulse."

narrator "The Dragonair sends out a beam of pure energy; the Gyarados takes the full force of it; while she doesn't faint, the Gyarados seems to be on her last legs."

narrator "Clair tosses out a PokéBall. The Gyarados is returned, leaving only Clair and the Dragonair."

show clair thinking

narrator "Clair stands for a moment, rubbing her chin deep in thought."

red @happy "{b}Dee-Dee{/b}?"

clair @blush surprised "What?"
pause 1.0
show clair angry with dis

narrator "Clair tosses a second PokéBall out, retrieving 'Dee-Dee'."

clair angry "Must you stalk in the shadows? A true trainer wouldn't behave in such a manner."

if (classstats["Poison"] >= 1):
    clair @thinking "It must be that coward Koga's influence."

red @angry "If you invited me here for another lecture, I think I'll pass."

clair sad "No, I recognize I do that far too often in class anyways."

pause 0.5

clair neutralbrow neutralmouth "Your standoff with Lance is legendary in the teacher's lounge."

red @surprised "Huh?"

clair @angry "When you were there for Janine's fight. He approached you, and tried to talk you down about your treatment of your Pikachu."

clair @thinking "Anyone else would've fallen apart in front of him and his imposing presence, but not you."

red @sad "That's because Silver stood up fo-{w=0.2}{nw}"

clair "Not immediately. Before that happened, you faced him down. A champion in this league, and you a pipsqueak."

clair angry "You understand that he is absolute power, something you cannot hope to defeat?"

pause 1.0

narrator "It seems this was for once not a rhetorical question."

red @angry "You're a teacher, so I don't really think we should be having this conversation."

clair "Right now, I am a fellow trainer. You will treat me as such."

red @angry "Then, you should know that your attitude is complete crap."

show clair surprised

extend @angry ".. and so is Lance's whole philosophy."

red @thinking "Pokémon aren't just weapons. They're living creatures, and ignoring that makes you a weaker trainer."

if (classstats["Dark"] >= 1):
    clair @thinking "I see you have been taking Karen's lessons to heart."

    clair @sad "Hmph. She never stops believing in her Pokémon..."

    clair "Even still..."

clair angry "Lance has a proven track record. Uses the strongest Pokémon, with the most intense battle tactics, and he wins time and time again."

##This section will need touchups to account for QQs, and potentially other big win moments in the game. ATM, I'm 2 lazy OMEGALUL

clair "You, on the other hand, have what? A few intramural wins at best?"

clair @sad "Every duelist starts out believing what you do. Then they lose their first {b}real{/b} match, and they begin to understand the way the world works."

clair "There's no room for hesitation, no room for affe-{w=0.2}{nw}"

red @angry "Booooooring."

show clair surprised

red @surprised "Sorry, we're talking candidly, right?"

clair "R-Right."

red @happy "Not gonna let you lecture me, then."

### Edits for big wins/having had a {b}real{/b} lost should go here.

red @thinking "I will prove Lance wrong."

red neutral "[pika_name] and I will beat him."

pause 1.0

clair thinkingbrow smilemouth "You really believe that, don't you?"

if (WonBattle("Instructor Clair3")):
    clair happy "You have consistently bested my class challenges, so I suppose there might be some truth to what you say..."

elif (WonBattle("Instructor Clair2")):
    clair neutral "You have shown some skill in class so far..."

clair angry "Prove it."

red @surprised "W-what? Here? Now?"

clair @thinking "We may be speaking as fellow trainers, but I am still a teacher here."

clair "I will not be made a fool of."

red @neutral "Aren't your Pokémon injured from when you were playing chess with them?"

clair @thinking "..."

extend @smilemouth "I have others."

clair @happy "Show me you have what it takes!"

$ trainer1 = Trainer("red", TrainerType.Player, [Pokemon(610, level=22, moves=[GetMove("Legacy"), GetMove("Dragon Dance"), GetMove("Bite"), GetMove("Taunt")])])
$ trainer2 = Trainer("clair", TrainerType.Enemy, [
    Pokemon(610, level=22, moves=[GetMove("Legacy"), GetMove("Dragon Dance"), GetMove("Bite"), GetMove("Taunt")])
])

call Battle([trainer1, trainer2], reanchor=[False, False], uniforms=[True, False]) from _shep_call_Battle_1 ##Gotta call my own battles
$ gymbattles["ShepClair_1"]  = _return
    
show clair with dis

if (WonBattle("ShepClair_1")):
    clair @happy "..."

    clair neutral "We should see to your Pokémon."

    pause 1.0
    $ HealParty()

    $ ValueChange("Instructor Clair", 1, -0.5)

    clair "I see now you can put your Pokémon where your mouth is."

    clair thinking "Hmm..."

else:
    show clair surprised

    redmind @angry "...Damn it."

    clair thinking "...We should see to your Pokémon."

    pause 1.0
    $ HealParty()

    $ shepclair_motivation == "Stubborn"
        
    red @sad "Look, this wasn't a great showing for me, but if you just hear me out..."

    clair angry "Stubborn."

    clair "That is what motivates you. Not genuine faith, not actual skill, but unrelenting stubbornness."

    clair thinkingbrow @angrymouth "In the face of reality, you continue to push against it."

    clair @sadmouth "How I envy that."

    extend @angrymouth "... and how incredibly pedestrian."
        
    redmind @thinking "..."
    clair neutral "We are done here."
        
    red @angry "So that's it? You're giving up again?"

    show clair surprised

    clair angry "...{i}{b}Again?{/b}{/i}"

    red @thinking "There has to be some reason you're so keen on Lance's interactions with me."

    red @neutral "Then you're talking about what motivates me to stand up to him."

    red @angry "You were in my shoes once, weren't you?"

    clair thinking "...{i}Unbelievable{/i}."

    pause 1.0

    $ ValueChange("Instructor Clair", 1, -0.5)

clair "Lance is my cousin. We grew up together in Blackthorn City."

pause 0.5

clair thinkingbrow sadmouth "You and your Pikachu, you feel like you've known them forever, right?"

red @thinking "Yes."

clair @sadbrow "That's how I felt with my first Dratini."

clair @smilebrow "She used to wrap herself around my neck like a scarf, and we'd go on little adventures."

red @surprised "A Dratini as a scarf? Those things are like 6 feet long!"

clair angry "It was a baby, not important."

clair @sadbrow "We were inseparable. I'd earn her by passing the Dragon's Den test, which was all about loving your Pokémon and treating them with kindness."

red @neutral "I'm surprised Lance was able to pass that test too."

##ALERT ALERT WARNING NON-CANON LORE AHEAD, PROCEED WITH CAUTION##

clair thinking "{w=0.2}.{w=0.2}.{w=0.2}."

pause 1.0

clair "He didn't."

clair "He refused to accept their teachings. He believed that only strength made a trainer unbeatable. He never bothered with the quiz. Instead, he got an old fishing rod and started hunting for a Dratini of his own."

clair "Once he did, he then proceeded to use that Dratini to build a team of his own."

clair angry "Eventually he wound up back at the Dragon's Den, there to prove them wrong. Not for a reward, but for purely validation. To his credit, he won."

clair "Every single disciple was no match for him. He was intelligent, quick, and extremely capable."

clair @sad "...seeing Dee-Dee unconscious on the floor for the first time..."

clair "When something like that happens... when everything you've ever believed in is absolutely and utterly crushed in front of your very eyes..."

clair sad "How can you not doubt your convictions?"

narrator "Her eyes start to water, but with what can only be sheer willpower they dry up before you can even be certain it was happening."

if (shepclair_motivation == "Stubborn"):
    clair sadbrow smilemouth "{b}Stubbornness{/b}. That's how you do it, right? Even when there's nothing left but pieces, you will yourself and pick them up and start putting things back together."

    red @sad "You keep calling it being stubborn, but I see it as more like simply not giving up."

    red @neutral "[pika_name] might not be the strongest Electric-type. They might not even be a very strong Pokémon."

    red @happy "But they're my friend. I won't start doubting [pika_name], just like I wouldn't doubt any of the other Pokémon I have."

    red @thinking "It may take a hundred tries. It may take my whole life... but I won't stop trying."

else:
    menu:
        "{color=#ff8412}Because I can't slow down and let it get to me.":
            $ shepclair_motivation == "Instinctive"
            show clair surprised

            red @happy "I was incredibly lucky to be able to attend this school. So far, I think I'm doing alright."

            red @thinking "If I let myself get clouded by doubt over some egotistical champion's belief that I'd fail, I would be throwing away everything I've worked for."

            clair @blush -sadbrow happymouth "Heh... why am I not surprised?"

            clair thinkingbrow @happymouth "It's because it's {b}instinctive{/b} for you."

            clair "You could be staring death in the face and you wouldn't crack, because that's how it is."

            clair "No room for doubt because doubt is..."

            red @happy "A waste of time."

            clair @happy "Right. A waste of time."
            
        "{color=#e226a6}Because I know that I'm doing the right thing.":
            $ shepclair_motivation == "Trusting"
            show clair surprised

            red @neutral "I may suffer a few defeats in battles, but I haven't really lost anything."

            red @thinking "I gained valuable experience, perhaps a new rival, and almost certainly a new goal to reach."

            red @thinking "None of that changes who I am and what I believe unless I let it."

            red @neutral "At the end of the day, why should anyone but me decide who I am?"

            clair @blush -happybrow "It's {b}trust{/b} then. Trust in your Pokémon, trust in your skills..."

            red @happy "Trust in myself."

show clair thinking

red @sad "Saying it out loud, it kind of sounds a little like how Lance used to be when he was younger..."

clair @angry "No. Lance was fueled by arrogance. That is what he drew from. You, on the other hand, draw it from something else."

if (IsBefore(30, 4, 2024)):
    redmind @thinking "Maybe it has something to do with Frienergy? Not that she would know about that."

else:
    clair @angrybrow talking2mouth "Perhaps it comes from that... ability of yours."

pause 0.5 

clair thinkingbrow "There's only two other people I've truly been this honest with before..."

clair @happymouth "...Interesting."

pause 0.5

clair @angry "Let me make one thing abundantly clear: my class time will continue to be where you learn."

clair "Don't think me opening up to you is your ticket out of assignments or responsibilities."

red @surprised "I wouldn't even consider it that way."

clair @thinkingbrow talkingmouth "Good."

show clair sadbrow happymouth

clair "Even if I don't fully believe you will win, it is almost too fascinating to look away from."

clair @thinkingbrow "It would seem that I have things to learn from you, [first_name]."

red neutral "Happy to have helped, Instructor."

clair "I would like to hear more about how you and [pika_name] spend time together."

red @happy "Only if I get to hear more about Lil' Cee-Cee and Dee-Dee's Adventures."

clair @surprised "'{i}Cee-Cee{/i}'?"

extend @blush ".{w=0.2}.{w=0.2}.{w=0.2}"

extend @happy "Fine, you {color=#0EFFFF}rascal{/color}."

$ persondex["Instructor Clair"]["Relationship"] = "Rascal"
$ persondex["Instructor Clair"]["RelationshipRank"] = 1

$ renpy.music.set_volume(0.1, delay=0.0, channel="music")
play sound "audio/sav.wav"
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

narrator "Your heart shifts as you feel your relationship with Clair evolve from '{color=#0EFFFF}Student{/color}' to '{color=#0EFFFF}Rascal{/color}'!"

return