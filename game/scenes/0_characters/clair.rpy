##Shepurd Clair Route##
init python:
    def ClairHasUnseenScene():
        if (GetCharValue("Instructor Clair") >= 10 and personalstats["Courage"] >= 3 and personalstats["Charm"] >= 3 and GetRelationship("Instructor Clair") != "Frustration"):
            return "ShepClair_1"
        return False

label ShepClair_1:

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

$ PlaySound("pokemon/ball sound.ogg")
narrator "Clair tosses out a Poké Ball. The Gyarados is returned, leaving only Clair and the Dragonair."

show clair thinking

narrator "Clair stands for a moment, rubbing her chin deep in thought."

red @happy "Dee-Dee?"

clair @blush surprised "What?"
pause 1.0
show clair angry with dis

$ PlaySound("pokemon/ball sound.ogg")
narrator "Clair tosses a second Poké Ball out, retrieving 'Dee-Dee'."

clair angry "Must you stalk in the shadows? A true trainer wouldn't behave in such a manner."

if (classstats["Poison"] >= 1):
    clair @thinking "It must be that coward Koga's influence."

clair angry "Battles are meant to be face to face; you must see the white in the eyes of your opponent if you are to get the proper measure of them."
clair happy "And what better place to be then atop of a mighty Dragon Pokémon?"

red @surprised "Uh, probably not in immediate dang-{w=0.2}{nw}"

clair angry "Nowhere. The only way to reach the heights of Pokémon Champion is atop the strongest of them all. {nw}"
clair happy "The greatness of the Dragon-type Pokémons can't be understated, after all they have all the advantages of -{nw}"

hide clair with dis

pause 1.0
clair "Hey!"

show clair surprised with dis

clair surprised "Where do you think you're going?"

red @angry "Sorry, figured I could catch the rest of this at next class."

clair thinking "..."
clair sad "I apologize. This is not why I asked you out here."

red @angry "Then what {i}is{/i} the reason I'm here right now?"

clair thinking "...Your standoff against Lance is legendary in the teacher's lounge."
clair neutral "It's not every day a student who has no real battle experience stands up to him."

red @sad "That's because Silver stood up fo-{w=0.2}{nw}"

clair "Not immediately. Before that happened, you faced him down. A champion in this league, and you a pipsqueak."

clair angry "My cousin is the pinnacle of what Kobukan Academy can make. He consistently wins, has an incredible tactical sense, and an actual champion."

clair thinkingbrow talkingmouth "You have what, exactly? A few intramural wins?"

clair neutral "You're not the first trainer to believe they can break the mold."

extend @sad "..and you'll either end up a nobody, or recognize the flaws in your logic."

red @thinking "Starting to sound like a lecture again..."

clair angry "I say all this only to offer you a warning, [first_name]. If you persist with your foolish notion of 'friendship', you will only find the road a painful one."
clair thinking @talkingmouth "You clearly have some talent. It would be a shame if it was wasted, you understand?"

red @thinking "..."
redmind @surprised "Huh, that wasn't a rhetorical question for once."
red @angry "...Nope."

clair thinking "Good, I would therefore like-{w=0.4}{nw}"
clair surprised "Huh?"

red @neutral "Respectfully, Instructor Clair, I don't think you're right."

red @thinking "Pokémon battles aren't just about who or what is the strongest. They're living creatures, and ignoring that makes you a weaker trainer."

if (classstats["Dark"] >= 1):
    clair @thinking "I see you have been taking Karen's lessons to heart."

    clair @sad "Hmph. She never stops believing in her Pokémon..."

clair sad "A naive perspective. Expected of a new student, but not one that hopes to win any titles."

red @angry "Why do you care?"

clair angry "Because I-"

show clair surprised
pause 0.5
show clair angry

clair thinking "I am your teacher. Am I not supposed to be concerned with the success of my students?"

red @angry "Not like this. Clearly something else is going on here."

pause 0.5

red @thinking "Look, I'm not taking your classes because I believe in Dragon-type supremacy or whatever. I'm taking them because I have a need to train Dragon-type Pokémon."

red @neutral "Honestly, if it wasn't for that, I'd be taking another elective."

show clair sad

red @angry "All day, every day, it's the same lecture. Dragons aren't the end all be all. They have weaknesses, just like any other type."

show clair surprised

red @happy "That's the beauty of Pokémon, right? It's all about forming bonds, accounting for weaknesses, and doing the best that you can."

clair @blush "I..."

pause 0.2

extend -thinkingbrow angrymouth " cannot believe you will continue this irrational behavior."

red @angry "Fine, let me prove it."

clair thinking "..."

clair @happymouth "It's good to know you express the values of a Dragon-type."

red neutral "Yeah yeah, you got any Pokémon not badly wounded?"

clair angrybrow talkingmouth "Yes, I might have one available."

if (WonBattle("Instructor Clair2")):
    clair thinking "We've battled a few times in class, and you've done well there..."

elif (WonBattle("Instructor Clair1")):
    clair neutral "You may have faced a test of mine before, but..."

clair angrybrow happymouth "Let's see how your ideals stand up to me truly!"

$ trainer1 = Trainer("red", TrainerType.Player, playerparty)
$ trainer2 = Trainer("clair", TrainerType.Enemy, [
    Pokemon(230, level=50, moves=[GetMove("Rain Dance"), GetMove("Draco Meteor"), GetMove("Surf"), GetMove("Ice Beam")], ability="Swift Swim", intelligence=2)
])

call Battle([trainer1, trainer2], reanchor=[False, False], uniforms=[True, False]) from _shep_call_Battle_1 ##Gotta call my own battles
$ gymbattles["ShepClair_1"]  = _return
    
show clair with dis
queue music "Audio/Music/shepclair_pilgrimage.mp3"

if (WonBattle("ShepClair_1")):
    clair surprised "I..."

    pause 0.3

    clair thinkingbrow @talkingmouth "...Interesting."

    clair neutral "We should see to your Pokémon."

    pause 1.0
    $ HealParty()

    $ ValueChange("Instructor Clair", 1, 0.55)

    clair "I see now you can put your Pokémon where your mouth is."

    red "You starting to believe me now?"

    clair neutralbrow happymouth "I am not a Champion. This doesn't truly prove anything."

    red @thinking "No, but that's what this is about, isn't it?"

    clair surprised "What?"

    red @thinking "You mentioned before that Lance is your cousin. You grew up with him, didn't you?"

    clair thinking ".{w=0.2}.{w=0.2}.{w=0.2}"

    clair "Yes."

    red @thinking "I grew up with Blue. You could say we have a rivalry that has come from that time."

    red @angry "He put me in a really crap spot back in the day, and it's taken me a long time to forgive him for it."

    red @thinking "Lance... he's a rival to you too, isn't he?"

    show clair sad

    pause 0.35

    show clair thinking

    clair thinking "...Hmm."

else:
    show clair sad

    redmind @angry "...Damn it."

    clair thinking "...We should see to your Pokémon."

    pause 1.0
    $ HealParty()
        
    red @sad "Look, this wasn't a great showing for me, but if you just hear me out..."

    clair angry "{b}Stubborn{/b}."

    red @surprised "What?"

    clair "That is what drives you and your foolish ideals. Not actual skill, but unrelenting stubbornness."

    clair thinkingbrow @angrymouth "In the face of reality, you wage an unwinnable war against it."

    clair @sadmouth "How I envy that.{w=0.2}"

    extend @angrymouth ".. and how incredibly pedestrian."
        
    redmind @thinking "..."
    clair neutral "We are done here."
        
    red @angry "So that's it? You're giving up again?"

    show clair surprised

    clair angry "...{i}{b}Again?{/b}{/i}"

    red @thinking "There has to be some reason you're so invested in Lance's interactions with me."

    red @neutral -angrymouth "Then you're talking about what motivates me to follow my ideals."

    red @angry "You were in my shoes once, weren't you?"

    clair thinking @talking2mouth "...Unbelievable."

    pause 1.0

    $ ValueChange("Instructor Clair", 1, 0.55)

    pause 0.25

clair neutral "I asked you out here to do one thing. To warn you about the path you are on."

clair thinking "It seems I have failed."

clair @talking2mouth "You have disregarded my warning, and tried to interrogate me on my past."

if (not IsBefore(30, 4, 2024)):
    clair "Your 'ability' might help you to do so with your classmates, but it will not work with me."

red @surprised "I'm just trying to figure out why it matters to you!"

clair angry "Let us not forget you sullied Dragon-types with your rhetoric as well!"

redmind @sad "Man, we almost made it without any more of that..."

clair @thinkingbrow "You are immensely {color=#5a94c6}frustrating{/color}! If you are going to have {i}any{/i} hope of beating Lance, we are going to need to work on a great many things."

clair thinking "We simply will not have enough time in class to do so."

clair neutral "You will find time to meet with me outside of it."

red @surprised "Hold up, we're going to train? What if I refuse?"

clair surprised "I am offering you an opportunity to learn one on one from the former eighth gym leader of Johto."

redmind @thinking "It is a rather good deal..."

pause 0.5

red @thinking "...One condition. You leave the long lecturing for class. Outside? I have a little more respect for my time than to keep going through this."

show clair thinking

pause 0.25

clair neutral "Only if you assure me you will not let my leniency outside permit you to shirk your duties for my class."

red @neutral "Deal."

clair thinking "..."
extend neutral " Deal."

clair "Unfortunately, I have a few matters to attend to now. This will be our meeting spot for the time being."

if (WonBattle("ShepClair_1")):
    clair thinking talkingmouth "{i}Maybe it is possible...{/i}"
else:
    clair thinking talkingmouth "{i}Their stubbornness will at least prove entertaining, if nothing else...{/i}
    "
hide clair with dis

pause 2.0

redmind @surprised "...What have I just signed myself up for?"

$ renpy.music.set_volume(0.1, delay=0.0, channel="music")
pause 0.2
play sound "audio/sav.wav"
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

$ persondex["Instructor Clair"]["Relationship"] = "Frustration"
$ persondex["Instructor Clair"]["RelationshipRank"] = 1

narrator "Your heart shifts as you feel your relationship with Clair evolve from '{color=#5a94c6}Student{/color}' to ...'{color=#5a94c6}Frustration{/color}'?"

redmind @thinking "{w=0.2}.{w=0.2}.{w=0.2}."
red @happy "Heh, 'Dee-Dee'."

return