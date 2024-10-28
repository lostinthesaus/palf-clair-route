################################################################################
## Initialization
################################################################################

init offset = -1

init python:
    gui.button_image_extension = ".webp"

################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.webp", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.webp", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.webp", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.webp", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.webp", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.webp"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.webp", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.webp"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.webp", gui.frame_borders, tile=gui.frame_tile)

style buttonhover:
    color "#000000"
    hover_color "#f0f0f0"
    font "fonts/pkmndp.ttf"


################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    $ si = SideImage()
    if (si != Null and who not in [pokedexlookup(sidemonnum, DexMacros.Name), starter_name] and not renpy.variant("small") and not hideside and (not showredonly or who == first_name)):
        add si

    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    if (si != Null and who in [pokedexlookup(sidemonnum, DexMacros.Name), starter_name] and not renpy.variant("small") and not hideside and (not showredonly or who == first_name)):
        add si

## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.webp", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.webp", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    line_spacing 12

    adjust_spacing True

style say_portrait_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    line_spacing 12

    adjust_spacing True

## Input screen ################################################################
##
## This screen is used to display !. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    modal True
    use currentdate()

    style_prefix "input"

    window:
        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    viewport id "choices":
        at choicefade
        style "menu_window"
        xalign 0.5
        yalign 0.45
        if len(items) >= 12:
            scrollbars "vertical"
            arrowkeys True
            pagekeys True
            mousewheel True
            vscrollbar_base_bar "#fff"
            vscrollbar_thumb "#363436"
            vscrollbar_top_bar "#e7e6e7"
            vscrollbar_bottom_bar "#e7e6e7"

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.80)
        xmaximum int(config.screen_width * 1.00)
        yminimum int(config.screen_height * 0.80)
        ymaximum int(config.screen_height * 1.00)

## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():
    if (not testbattle):
        ## Ensure this appears on top of other screens.
        zorder 100

        #add "gui/dialogue_frame.webp" zoom 0.12 ypos 0.99 yanchor 0.5 xalign 0.5

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            if (_rollback):
                textbutton _("Back") action Rollback() text_font "fonts/pkmndp.ttf" background Frame("gui/dialogue_frame.webp") keyboard_focus False
            if (_skipping):
                textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True) text_font "fonts/pkmndp.ttf" background Frame("gui/dialogue_frame.webp") keyboard_focus False
            textbutton _("Menu") action ShowMenu() text_font "fonts/pkmndp.ttf" background Frame("gui/dialogue_frame.webp") keyboard_focus False

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():
    
    modal True

    # The various buttons.
    imagemap:
        ground "imagemaps/Nav_Menu_Ground.webp"
        idle "imagemaps/Nav_Menu_Idle.webp"
        hover "imagemaps/Nav_Menu_Hover.webp"
        selected_idle "imagemaps/Nav_Menu_Selected.webp"
        selected_hover "imagemaps/Nav_Menu_Selected.webp"
        
        hotspot (30, 240, 93, 25) action Preference("display", "any window")
        hotspot (162, 240, 115, 25) action Preference("display", "fullscreen")
        
        hotspot (28, 386, 50, 25) action Preference("text speed", 30)
        hotspot (112, 386, 72, 25) action Preference("text speed", 60)
        hotspot (222, 386, 50, 25) action Preference("text speed", 90)
        
        hotspot (28, 527, 50, 25) action SetField(config,"skip_delay",500)
        hotspot (112, 527, 72, 25) action SetField(config,"skip_delay",100)
        hotspot (222, 527, 50, 25) action SetField(config,"skip_delay",10)
        
        hotspot (101, 1018, 86, 31) action Hide("navigation", transition=dissolve)

        bar pos (141, 720) value Preference("music volume") style "pref_slider"
        bar pos (141, 808) value Preference("sound volume") style "pref_slider"
    
    vbox:
        xpos 25
        yanchor 0.5
        ypos 620
        textbutton "{b}Profanity: " + ("On" if profanity else "Off") + "{/b}" action ToggleVariable("profanity") text_font "fonts/pkmndp.ttf" text_color "#000" text_hover_color "#ff0000"
        textbutton "{b}Skip: " + ("All" if preferences.skip_unseen else "Seen") + "{/b}" action ToggleVariable("preferences.skip_unseen") text_font "fonts/pkmndp.ttf" text_color "#000" text_hover_color "#ff0000"
    
init -2 python:
    style.pref_slider.left_bar = "GUI/bar_full.webp"
    style.pref_slider.right_bar = "GUI/bar_empty.webp"
    style.pref_slider.ymaximum = 6
    style.pref_slider.xmaximum = 110
    style.pref_slider.thumb = None
    style.pref_slider.thumb_offset = 5
    style.pref_slider.thumb_shadow = None

    def SortDatabase():
        if (socialsort == None):
            return persondex.keys()
        elif (socialsort == "abc"):
            return sorted(persondex.keys(), key=(lambda entry : entry))
        elif (socialsort == "lv"):
            return sorted(persondex.keys(), key=(lambda entry : persondex[entry]["Value"]), reverse=True)
        elif (socialsort == "mood"):
            return sorted(persondex.keys(), key=(lambda entry : GetMood(entry) + (-9999 if GetNature(entry) == TrainerNature.Special else 0)), reverse=True)

screen blackscreen:
    add "BG/Blank2.webp"

init -2 python:
    social_page_char_shown = ""

init python:
    def GetChibi(char):
        if (char == "Professor Cherry"):
            char = "kris"
        elif (char == "Instructor Clair"):
            char = "clair"
        elif ((playercharacter != None or InDungeon()) and char == first_name or char == "Red"):
            char = "red"
        charname = char.lower()
        pathstr = "images/chibis/" + char.lower() + ".webp"
        if (renpy.exists(pathstr)):
            return pathstr
        else:
            return "images/chibis/quest.webp"

screen olddatabasedata(char):
    imagebutton idle Transform("images/GUI/readback.webp", zoom=0.5) ypos 0.98 yanchor 1.0 xalign 0.5
    add GetChibi(char) xpos 0.6 ypos 0.98 yanchor 1.0 zoom 0.6
    grid 1 10:
        ypos 0.745 xpos 0.37
        #xalign 0.5 yalign 0.5
        $ chartuple = GetScenes([char])[0]
        $ charname = chartuple[0]
        $ hasscene = chartuple[1]
        $ posttext = ""
        if (playercharacter == None):
            if (not hasscene):
                $ posttext = PrintSceneConditions(GetNextScene(charname))
            else:
                $ posttext = "{gradient2=3-#f00-#0f0-33-#0f0-#00f-33-#00f-#f00-33}{b}{size=30}Ready!{/size}{/b}{/gradient2}"
            if (posttext != ""):
                text "{b}Next Scene:{/b} " + posttext color "#000" size 30            

        if (usingmoods and GetNature(char) != TrainerNature.Special):
            $ mood = GetMood(char)
            $ nature = GetNature(char)
            $ bondchange = mooddict[max(min(10, mood), -10)][nature][0]
            $ moodchange = mooddict[max(min(10, mood), -10)][nature][1]
            text "{b}Current Mood:{/b} " + moodtoword(mood) + " (" + str(mood) + ")" color "#000" size 30
            if (bondchange == 0 and moodchange == 0):
                text "{b}Next Day:{/b} No Change" color "#000" size 30 
            else:
                text "{b}Next Day:{/b} " + ("+" if bondchange > -1 else "" ) + str(bondchange) + " Bond, " + ("+" if moodchange > -1 else "" ) + str(moodchange) + " Mood" color "#000" size 30 
            text "{b}Nature:{/b} " + str(GetNature(char)) color "#000" size 30 
        $ rank = GetRelationshipRank(char)
        text "{b}Relationship:{/b} " + GetRelationship(char) + ("" if rank == 0 else ", Rank " + str(rank)) color "#000" size 30
        text "{b}Contact Info:{/b} " + ("Acquired" if persondex[char]["Contact"] else "Unacquired") color "#000" size 30

        $ classstring = "None"
        if (char != "Yellow"):
            for i, classtype in enumerate(GetCharTypes(char)):
                if (classstring == "None"):
                    $ classstring = ""
                if (i != 0):
                    $ classstring += ", "
                $ classstring += classtype

        text "{b}Known Classes:{/b} " + classstring color "#000" size 30

        if (persondex["Gardenia"]["Contact"] and playercharacter == None):
            if (not (char in ["Sabrina", "Blue", "Janine", "Misty", "Dawn", "Hilbert", "Professor Cherry"] and GetRelationshipRank(char) == 0) and not char in ["Janine", "Yellow"]):
                if (char not in GiftsGiven):
                    text "{b}Gifting:{/b} Can gift" color "#000" size 30
                else:
                    text "{b}Gifting:{/b} Gifted this week" color "#000" size 30
            else:
                text "{b}Gifting:{/b} Cannot gift" color "#000" size 30


screen database(calling=False, limittype=None):
    $ yvalue = 0
    $ xvalue = 0
    add "BG/Blank2.webp" alpha 0.6

    if (newdatabase):
        $ chars_shown = 0
        $ valid_chars_pixels = ValidCharacterNum() * 135
        default adj = ui.adjustment(value=0, range=valid_chars_pixels)
        add "gui/bg_tiles/bg_tile_none_full.webp" zoom 1 xpos 0
        viewport id "example":
            scrollbars "vertical"
            arrowkeys True
            pagekeys True
            mousewheel True
            vscrollbar_base_bar "#fff"
            vscrollbar_thumb "#363436"
            vscrollbar_top_bar "#e7e6e7"
            vscrollbar_bottom_bar "#e7e6e7"
            
            area(260,0,917,1080)
            child_size (900, valid_chars_pixels)
            yadjustment adj
            $ yval = 0
            for char in SortDatabase():
                $ person = persondex[char]
                $ pointvalue = person["Value"]
                if (person["Named"] and (calling and person["Contact"] or (pointvalue != 0 or GetMood(char) != 0)) and (not calling or person["Contact"]) and (limittype == None or limittype in GetCharTypes(char))):
                    $ chartuple = GetScenes([char])[0]
                    $ charname = chartuple[0]
                    $ hasscene = chartuple[1]
                    $ chars_shown += 1

                    $ tooltip = GetTooltip()
                    if social_page_char_shown is char:
                        imagebutton idle "social_frame_hover" hover "social_frame_hover" xalign 0 ypos yval xpos 0 action (NullAction() if not calling else [Return(char), Hide("databasechar")]) hovered [SetVariable("social_page_char_shown", char), Show("databasechar", None, char)]
                    else:
                        imagebutton idle "social_frame" hover "social_frame_hover" xalign 0 ypos yval xpos 0 action (NullAction() if not calling else [Return(char), Hide("databasechar")]) hovered [SetVariable("social_page_char_shown", char), Show("databasechar", None, char)]

                    # Show name and relationship.
                    $ char_name = char
                    if char == "Professor Cherry":
                        $ char_name = "Prof. Cherry"
                    elif (char == "Nate" and HasEvent("Nate", "Blake")):
                        $ char_name = "\"Nate\""
                    text "{size=50}{color=#ffffff}" + char_name + "{/color}{/size}" pos (10, 10 + yval) outlines [ (absolute(4), "#000", absolute(0), absolute(0)) ]
                    if char == "Tia" and playercharacter == None:
                        textbutton "{size=30}{color=#000000}{font=fonts/pkmndp.ttf}" + GetRelationship(char) + "{/color}{/size}" pos (10, 95 + yval) text_outlines [ (absolute(2), "#fff", absolute(0), absolute(0)) ] tooltip "This indicates your current relationship\nwith the character." action NullAction()
                    else:
                        textbutton "{size=36}{color=#ffffff}{font=fonts/pkmndp.ttf}" + GetRelationship(char) + "{/color}{/size}" pos (4, 89 + yval) text_outlines [ (absolute(4), "#000", absolute(0), absolute(0)) ] tooltip "This indicates your current relationship\nwith the character." action NullAction()

                    # EXP bar.
                    $ barcolor = GetCharColor(char)
                    bar range GetEXPRequiredForLevel(char) value pointvalue pos (165, 65 + yval) xmaximum 200 right_bar "#808080" left_bar (barcolor if pointvalue > 0 else "#808080") 
                    text ("EXP: " + str(pointvalue) + ("/" + str(GetEXPRequiredForLevel(char)) if pointvalue > 0 else "")) color "#fff" pos (175, 65 + yval) outlines [ (absolute(5), "#000", absolute(0), absolute(0)) ]

                    # Mood and Nature information.
                    if (usingmoods):
                        $ mood = GetMood(char)
                        $ nature = GetNature(char)
                        text "{size=20}{color=#ffffff}Mood:{/color}{/size}" pos (375, 7 + yval) outlines [ (absolute(4), "#000", absolute(0), absolute(0)) ]
                        
                        if nature == "Special":
                            textbutton "{font=fonts/pkmndp.ttf}{size=30}{color=#ffffff}Stable{/color}{/size}" pos (369, 26 + yval) text_outlines [ (absolute(4), "#000", absolute(0), absolute(0)) ] tooltip "The Mood of this character does not change." action NullAction()
                        else:
                            textbutton "{font=fonts/pkmndp.ttf}{size=30}{color=#ffffff}" + moodtoword(mood) + (" ({color=00ff00}" if mood > -1 else " ({color=ee4b2b}") + str(mood) + "{/color}{color=#ffffff})" + "{/color}{/size}" pos (369, 26 + yval) text_outlines [ (absolute(4), "#000", absolute(0), absolute(0)) ] tooltip "The Mood of a character is a view of their current feelings,\nand determines their Bond gain/loss over time." action NullAction()
                        text "{size=20}{color=#ffffff}Nature:{/color}{/size}" pos (375, 75 + yval) outlines [ (absolute(4), "#000", absolute(0), absolute(0)) ]
                        
                        $ nature_tip = "This should not be seen."
                        if nature == "Special":
                            $ nature_tip = "This character's Bond is not affected by their Mood."
                        elif nature == "Devoted":
                            $ nature_tip = "Devoted characters are staunch allies,\nwhose Bond will never decrease, even if in a bad Mood."
                        elif nature == "Neutral":
                            $ nature_tip = "Neutral characters are neutral towards you. Piss them off,\nBond will decrease, make them happy, it will increase in same quantities."
                        elif nature == "Distant":
                            $ nature_tip = "Distant characters have a Mood that decays rapidly, if positive.\nIf in a bad Mood, watch out, as their Bond will decrease quickly."
                        elif nature == "Friendly":
                            $ nature_tip = "Friendly characters will increase Bond quickly if in a positive Mood.\nBut if they are pushed far enough in a negative direction... Bond will nosedive."
                        elif nature == "Moody":
                            $ nature_tip = "Moody characters are erratic, making great gains in Bond if in a good Mood,\nbut massive losses if unhappy."
                        textbutton "{font=fonts/pkmndp.ttf}{size=30}{color=#ffffff}" + nature + "{/color}{/size}" pos (369, 94 + yval) text_outlines [ (absolute(4), "#000", absolute(0), absolute(0)) ] tooltip nature_tip action NullAction()
                

                    # Next Day info.
                    if (usingmoods and GetNature(char) != TrainerNature.Special):
                        $ bondchange = mooddict[max(min(10, GetMood(char)), -10)][GetNature(char)][0]
                        $ moodchange = mooddict[max(min(10, GetMood(char)), -10)][GetNature(char)][1]
                        text "{size=30}{color=#ffffff}Next Day:{/color}{/size}" pos (575, 7 + yval) outlines [ (absolute(4), "#000", absolute(0), absolute(0)) ]
                        textbutton "{font=fonts/pkmndp.ttf}{size=30}{color=#ffffff}" + "Bond: " + ("{color=00ff00}+" if bondchange > -1 else "{color=ff0000}" ) + str(bondchange) + "{/color}{/size}" pos (569, 41 + yval) text_outlines [ (absolute(4), "#000", absolute(0), absolute(0)) ] tooltip "This is the amount the Bond will change overnight. Bond is also known as EXP.\nA high Mood will lead to increases, but negative {i}may{/i} cause decreases." action NullAction()
                        textbutton "{font=fonts/pkmndp.ttf}{size=30}{color=#ffffff}" + "Mood: " + ("{color=00ff00}+" if moodchange > -1 else "{color=ff0000}" ) + str(moodchange) + "{/color}{/size}" pos (569, 81 + yval) text_outlines [ (absolute(4), "#000", absolute(0), absolute(0)) ] tooltip "This is how the Mood of this character will change overnight.\nOver time without interference, Mood will move to 0." action NullAction()

                    $ chartuple = GetScenes([char])[0]
                    $ charname = chartuple[0]
                    $ hasscene = chartuple[1]
                    $ posttext = ""
                    if (playercharacter == None):
                        if (not hasscene):
                            $ posttext = PrintSceneConditions(GetNextScene(charname))
                        else:
                            $ posttext = "{gradient2=3-#f00-#0f0-33-#0f0-#00f-33-#00f-#f00-33}{b}{size=30}Ready!{/size}{/b}{/gradient2}"

                        if ("Ready!" in posttext):
                            textbutton "{size=30}{color=#ffffff}{font=fonts/pkmndp.ttf}" + "Scene {i}{size=25}    i{/size}{/i}{size=30}\n" + posttext pos (725, 60 + yval) text_outlines [ (absolute(4), "#000", absolute(0), absolute(0)) ] tooltip PrintSceneConditions(GetNextScene(charname)) action NullAction() 
                        elif (posttext != ""):
                            textbutton "{size=30}{color=#ffffff}{font=fonts/pkmndp.ttf}" + "Scene {i}{size=25}    i{/size}{/i}{size=30}\nConditions: " pos (725, 60 + yval) text_outlines [ (absolute(4), "#000", absolute(0), absolute(0)) ] tooltip posttext action NullAction()

                    # Phone icon.
                    if persondex[char]["Contact"]:
                        imagebutton idle "gui/phone_green.webp" pos (725, 4 + yval) xanchor 0 tooltip "You have their contact." action NullAction()
                    else:
                        imagebutton idle "gui/phone_red.webp" pos (725, 4 + yval) xanchor 0 tooltip "You don't have their contact." action NullAction()

                    # Gift info.
                    if (persondex["Gardenia"]["Contact"] and playercharacter == None):
                        if (not (char in ["Sabrina", "Blue", "Janine", "Misty", "Dawn", "Hilbert", "Professor Cherry"] and GetRelationshipRank(char) == 0) and not char in ["Janine", "Yellow"]):
                            if (char not in GiftsGiven):
                                imagebutton idle "gui/gift_red.webp" pos (790, 4 + yval) xanchor 0 tooltip "You can give a gift to this character, this week." action NullAction()
                            else:
                                imagebutton idle "gui/gift_green.webp" pos (790, 4 + yval) xanchor 0 tooltip "You've given them a gift this week." action NullAction()

                    $ gendersymbol = ""
                    if ("Sex" in person.keys()):
                        if (person["Sex"] == Genders.Male):
                            $ gendersymbol = "{font=fonts/pkmndp.ttf}{color=#4287f5}♂{/font}"
                        else:
                            $ gendersymbol = "{font=fonts/pkmndp.ttf}{color=#ff00b7}♀{/font}"
                    
                    $ valueceil = GetCharacterLevel(char)
                    text gendersymbol + "{color=#ffffff}Lv." + str(valueceil) pos (280, 30 + yval) xanchor 0 outlines [ (absolute(4), "#000", absolute(0), absolute(0)) ]
                                        
                    $ yval += 135

        vbox:
            textbutton "{b}Back{/b}" action [Return("Back"), Hide("databasechar")] xminimum 250 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
            null height 50
            textbutton "Lv. Sort" action SetVariable("socialsort", "lv") xminimum 250 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
            if (usingmoods):
                textbutton "Mood Sort" action SetVariable("socialsort", "mood") xminimum 250 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
            textbutton "ABC Sort" action SetVariable("socialsort", "abc") xminimum 250 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
            textbutton "Met Sort" action SetVariable("socialsort", None) xminimum 250 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
            null height 50
            textbutton "Page Up" action Function(adj.change, adj.value - 1080), renpy.restart_interaction xminimum 250 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"    
            textbutton "Page Down" action Function(adj.change, adj.value + 1080), renpy.restart_interaction xminimum 250 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
            null height 50
            textbutton "Swap Style" action [ToggleVariable("newdatabase"), Hide("databasechar")] xminimum 250 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
    
    else:
        $ yvalue = 0
        $ xvalue = 0
        $ xzoomvalue = 0.7
        add "BG/Blank2.webp" alpha 0.6
        for char in SortDatabase():
            $ person = persondex[char]
            $ pointvalue = person["Value"]
            if (person["Named"] and (calling and person["Contact"] or (pointvalue != 0 or GetMood(char) != 0)) and (not calling or person["Contact"]) and (limittype == None or limittype in GetCharTypes(char))):
                $ xvalue = yvalue % 6
                $ ybuffer = math.floor(yvalue / 6) * 105
                $ xbuffer = 280 + math.floor(xvalue * 365 * xzoomvalue)
                $ chartuple = GetScenes([char])[0]
                $ charname = chartuple[0]
                $ hasscene = chartuple[1]
        
                imagebutton idle Transform("GUI/frame_battlestat.webp", xzoom=xzoomvalue) hover Transform("GUI/frame_sbattlestat.webp", xzoom=xzoomvalue) action (NullAction() if not calling else [Return(char), Hide("olddatabasedata")]) hovered Show("olddatabasedata", Dissolve(0.5), char) unhovered Hide("olddatabasedata", Dissolve(0.5)) ypos ybuffer xpos xbuffer at [Transform(yzoom=0.8), (tintstrobe if hasscene else Transform(matrixcolor=TintMatrix("#fff")))]
                
                $ charformatname = char
                if (charformatname == "Professor Cherry"):
                    $ charformatname = "P. Cherry"
                elif (char == "Nate" and HasEvent("Nate", "Blake")):
                    $ charformatname = "\"Nate\""
                text charformatname pos (xbuffer + 10, 28 + ybuffer)
                $ gendersymbol = ""

                if ("Sex" in person.keys()):
                    if (person["Sex"] == Genders.Male):
                        $ gendersymbol = "{color=#2b00ff}{font=fonts/pkmndp.ttf}♂{/font}"
                    else:
                        $ gendersymbol = "{color=#ff00b7}{font=fonts/pkmndp.ttf}♀{/font}"
                    
                $ valueceil = GetCharacterLevel(char)
                text gendersymbol + "{color=#000000}Lv." + str(valueceil) pos (xbuffer + math.floor(365 * xzoomvalue) - 10, 30 + ybuffer) xanchor 1.0

                $ barcolor = GetCharColor(char)

                bar range GetEXPRequiredForLevel(char) value pointvalue pos (xbuffer + 10, 65 + ybuffer) xmaximum math.floor(335 * xzoomvalue) right_bar "#fff" left_bar (barcolor if pointvalue > 0 else "#fff")
                text ("EXP: " + str(pointvalue) + ("/" + str(GetEXPRequiredForLevel(char)) if pointvalue > 0 else "")) color "#fff" pos (xbuffer + 20, 65 + ybuffer) outlines [ (absolute(5), "#000", absolute(0), absolute(0)) ]
                $ yvalue += 1

        vbox:
            textbutton "{b}Back{/b}" action Return("Back") xminimum 250 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
            null height 50
            textbutton "Lv. Sort" action SetVariable("socialsort", "lv") xminimum 250 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
            if (usingmoods):
                textbutton "Mood Sort" action SetVariable("socialsort", "mood") xminimum 250 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
            textbutton "ABC Sort" action SetVariable("socialsort", "abc") xminimum 250 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
            textbutton "Met Sort" action SetVariable("socialsort", None) xminimum 250 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
            null height 50
            textbutton "Swap Style" action [ToggleVariable("newdatabase"), Hide("databasechar")] xminimum 250 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"

screen databasechar(char):
    $ charcolor = GetCharColor(char)
    $ finalmatrix = TintMatrix(charcolor) * BrightnessMatrix(1.0) * ContrastMatrix(0.0)
    $ value = persondex[char]["Value"]
    $ valueceil = GetCharacterLevel(char)
    $ charimage = GetCharacterSprite(char)

    $ num_classes = len(GetCharTypes(char))
    $ class1 = ""
    $ class2 = ""
    $ class3 = ""
    $ class4 = ""
    $ invalid_check = True
    if char == "Instructor Clair":
        $ char_name = "Clair"
        $ num_classes == 1
        $ class1 == "Dragon"
    if ((char == "Ethan" and playercharacter == None) or (char == first_name and playercharacter == "Ethan")):
        $ class_sort = sorted(classstats.items(), key=lambda x:x[1], reverse=True)
        if (class_sort[0][1] > 0):
            $ class1 = class_sort[0][0].lower()
            $ num_classes = 1
        if (class_sort[1][1] > 0):
            $ class2 = class_sort[1][0].lower()
            $ num_classes = 2
            if (class_sort[2][1] / class_sort[1][1] >= 0.5): # Need to make sure class #2 is at least 1, don't want to divide by zero!
                $ class3 = class_sort[2][0].lower()
                $ num_classes += 1
    
    # Code for displaying type backgrounds.
    if num_classes == 0 or invalid_check == False:
        add "gui/bg_tiles/bg_tile_unknown_full.webp" zoom 1 xpos 1177 crop (1177,0,743,1080)
    elif num_classes == 1:
        if (class1 == ""):
            $ class1 = GetCharTypes(char)[0].lower()
        add "gui/bg_tiles/bg_tile_" + class1 + "_full.webp" zoom 1 xpos 1177 crop (1177,0,743,1080)
    elif num_classes == 2:
        if (class2 == ""):
            $ class1 = GetCharTypes(char)[0].lower()
            $ class2 = GetCharTypes(char)[1].lower()
        add "gui/bg_tiles/bg_tile_" + class1 + "_full.webp" zoom 1 xpos 1177 crop (1177,0,372,1080)
        add "gui/bg_tiles/bg_tile_" + class2 + "_full.webp" zoom 1 xpos 1549 crop (1549,0,371,1080)
    elif num_classes == 3:
        if (class3 == ""):
            $ class1 = GetCharTypes(char)[0].lower()
            $ class2 = GetCharTypes(char)[1].lower()
            $ class3 = GetCharTypes(char)[2].lower()
        
        add "gui/bg_tiles/bg_tile_" + class1 + "_full.webp" zoom 1 xpos 1177 crop (1177,0,743,360)
        add "gui/bg_tiles/bg_tile_" + class2 + "_full.webp" zoom 1 xpos 1177 ypos 360 crop (1177,360,743,360)
        add "gui/bg_tiles/bg_tile_" + class3 + "_full.webp" zoom 1 xpos 1177 ypos 720 crop (1177,720,743,360)
        
    $ finalmatrix = BrightnessMatrix(0.0) * ContrastMatrix(0.0)

    add charimage xpos .7805 zoom 1.27 matrixcolor TintMatrix("#000")
    add charimage xpos .8005 zoom 1.2
    
    $ char_name = char
    if char == "Professor Cherry":
        $ char_name = "Prof. Cherry"
    $ font_size = 80
    if len(char_name) > 12: # This code exists just in case a character has a MASSIVE name. Or if the player names their Red something long.
        $ font_size = 960 // len(char_name)
    text "{size=" + str(font_size) + "}{color=" + charcolor + "}" + char_name.replace("\n", "").replace("\t","") outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] vertical True xalign .98 yalign .5 kerning 30
    
    $ tooltip = GetTooltip()
    if tooltip:
            nearrect:
                focus "tooltip"
                prefer_top True

                frame:
                    xanchor 0.0
                    xpos 1.0
                    text "{size=25}" + tooltip

init python:
    def moodtoword(points):
        if (points <= -10):
            return "Desolate"
        elif (points == -9):
            return "Heartbroken"
        elif (points == -8):
            return "Devastated"
        elif (points == -7):
            return "Sorrowful"
        elif (points == -6):
            return "Downtrodden"
        elif (points == -5):
            return "Depressed"
        elif (points == -4):
            return "Unhappy"
        elif (points == -3):
            return "Saddened"
        elif (points == -2):
            return "Irritated"
        elif (points == -1):
            return "Discontent"
        elif (points == 0):
            return "Mellow"
        elif (points == 1):
            return "Content"
        elif (points == 2):
            return "Serene"
        elif (points == 3):
            return "Happy"
        elif (points == 4):
            return "Joyful"
        elif (points == 5):
            return "Ecstatic"
        elif (points == 6):
            return "Exuberant"
        elif (points == 7):
            return "Jubilant"
        elif (points == 8):
            return "Delighted"
        elif (points == 9):
            return "Euphoric"
        elif (points >= 10):
            return "Blissful"

screen traits():
    if (playercharacter == None):
        add "red happy" xpos 0.65 ypos 1.5
    elif (playercharacter == "Ethan"):
        add "ethan closedbrow talking2mouth" xpos 0.65 ypos 1.5
    elif (playercharacter == "Blue"):
        add "blue" xpos 0.65 ypos 1.5
    elif (playercharacter == "Leaf"):
        add "leaf flirt" xpos 0.65 ypos 1.4
    elif (playercharacter == "Bea"):
        add "bea" xpos 0.65 ypos 1.4
    elif (playercharacter == "Lisia"):
        add "lisia" xpos 0.65 ypos 1.4
    elif (playercharacter == "Cheren"):
        add "cheren sad2brow shadow smilemouth" xpos 0.65 ypos 1.4
    else:
        add playercharacter.lower() xpos 0.65 ypos 1.4
        
    add "BG/Blank2.webp" alpha 0.6
    $ plot_values = (personalstats["Charm"] + 15, personalstats["Knowledge"] + 15, personalstats["Courage"] + 15, personalstats["Wit"] + 15, personalstats["Patience"] + 15)
    add RadarChart(
        size=800,
        values=plot_values,
        max_value=75,
        labels=[Text("{color=#b7669e}Charm\nLv. " + str(plot_values[0] - 15), outlines=[ (absolute(10), "#000", absolute(0), absolute(0)) ]), 
            Text("{color=#66b77d}Knowledge\nLv. " + str(plot_values[1] - 15), outlines=[ (absolute(10), "#000", absolute(0), absolute(0)) ]), 
            Text("{color=#ff8412}Courage\nLv. " + str(plot_values[2] - 15), outlines=[ (absolute(10), "#000", absolute(0), absolute(0)) ]), 
            Text("{color=#60c2f8}Wit\nLv. " + str(plot_values[3] - 15), outlines=[ (absolute(10), "#000", absolute(0), absolute(0)) ]), 
            Text("{color=#e226a6}Patience\nLv. " + str(plot_values[4] - 15), outlines=[ (absolute(10), "#000", absolute(0), absolute(0)) ])],
        lines={"webs": [2, 4, 6, 8]},
        data_colour=(255, 0, 0, 255),
        line_colour=(153, 153, 153, 255),
        background_colour=(255, 255, 255, 255)) align (0.17, 0.55)

    text "TRAITS" color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] size 80 xpos .24 ypos .85
    text "PROFICIENCIES" color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] size 80 xalign .98 ypos .1

    grid 2 9:
        xalign 0.98
        yalign 0.5
        spacing 20
        for classtype in altclassdex.keys():     
            text classtype + ": " + FormatNum(classstats[classtype]) size 30 color ("#f00" if classstats[GetStatRank(0)] == classstats[classtype] else "#fff") outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]

    if (playercharacter == "Lisia"):
        text "Coordinator Knowledge: 11,212,014" color "#FF69B4" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] size 40 align (1.0, 1.0)
    if (playercharacter == None and coordinating):
        text "Coordinator Knowledge: " + str(coordinatingknowledge) color "#FF69B4" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] size 40 align (1.0, 1.0)

    textbutton "Back" action Return() xminimum 200 text_xalign .5 xalign 0.0 yalign 1.0 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"

init python:
    def SwapPositions(pos1, pos2):
        global pkmnlocked
        try:
            playerparty[pos1], playerparty[pos2] = playerparty[pos2], playerparty[pos1]
            pkmnlocked = pos2
            renpy.show_screen("partyviewerpopup", pkmnlocked)
        except:
            pkmnlocked = -1
    
    def SwitchItems(pos1, pos2):
        global pkmnlocked
        try:
            playerparty[pos1].Item, playerparty[pos2].Item = playerparty[pos2].Item, playerparty[pos1].Item
        except:
            pkmnlocked = -1

screen partyviewerpopup(index):
    $ temp_ypos = 50 + 100 * index
    zorder 10
    viewport id "party_viewer_popup":
        area(1685,temp_ypos - 10,120,120)
        if pkmnlocked != -1:
            textbutton "{color=#000000}Hide" text_xalign 0.5 xalign 0.0 pos(0,0) action [Hide("mondata"), Hide("nonbattlemoves"), Hide("movedata"), Hide("partyviewerpopup"), SetVariable("pkmnlocked", -1), SetVariable("pkmnlockedmove", -1)] text_font "fonts/pkmndp.ttf" style "menu_choice_button" maximum (120,45) minimum (120,45)
        if index < len(playerparty) and len(playerparty) > 1 and pkmnswapitem == -1 and playerparty[index].GetItem() != None:
            textbutton "{color=#000000}Switch Item" text_xalign 0.5 xalign 0.0 pos(0,45) action SetVariable("pkmnswapitem", 1) text_font "fonts/pkmndp.ttf" style "menu_choice_button" maximum (120,75) minimum (120,75)
        elif (pkmnswapitem != -1):
            textbutton "{color=#000000}End Swap" text_xalign 0.5 xalign 0.0 pos(0,45) action SetVariable("pkmnswapitem", -1) text_font "fonts/pkmndp.ttf" style "menu_choice_button" maximum (120,75) minimum (120,75)

screen partyviewer():
    if partyviewer:
        for i, pkmn in enumerate(playerparty):
            if (not InDungeon() or (InDungeon() and i == 0)):
                textbutton "" xalign 1.0 ypos 50 + 100 * i xminimum 115 yminimum 100 background Color("#d200ab" if i == pkmnlocked else "#d200ac00")
                imagebutton: 
                    idle "GUI/stats_frame.webp" 
                    hover "GUI/stats_frame_hover.webp" 
                    action ([SetVariable("pkmnlocked", (-1 if pkmnlocked != -1 else i)), SetVariable("pkmnlockedmove", -1), (Show("partyviewerpopup", index=i) if pkmnlocked == -1 else Hide("partyviewerpopup"))] if pkmnlocked == -1 or pkmnlocked == i else Function(SwapPositions, pkmnlocked, i) if pkmnswapitem == -1 else Function(SwitchItems, pkmnlocked, i))
                    xalign 1.0 
                    keyboard_focus False
                    ypos 50 + 100 * i 
                    hovered ([Show("mondata", None, pkmn), Show("nonbattlemoves", None, pkmn)] if pkmnlocked == -1 else NullAction()) 
                    unhovered ([Hide("mondata"), Hide("nonbattlemoves"), Hide("movedata")] if pkmnlocked == -1 else Hide("movedata"))
                add "GUI/pokeballicon.webp" xanchor 1.0 xpos 1900 ypos 60 + 100 * i
                if (pkmn.Id == 25.2):
                    add pkmn.GetImage() zoom 0.2 ypos 45 + 100 * i xanchor 1.0 xpos 1925 at (monochrome if max(pkmn.GetHealth(), pkmn.GetCaught()) <= 0 else None)
                else:
                    add pkmn.GetImage() zoom 0.2 ypos 60 + 100 * i xanchor 1.0 xpos 1900 at (monochrome if max(pkmn.GetHealth(), pkmn.GetCaught()) <= 0 else None)
                if (pkmn.GetItem() != None):
                    add "GFX/item.webp" zoom 0.3 ypos 55 + 100 * i xanchor 1.0 xpos 1915
                if (pkmn.GetForeverals() != []):
                    add "GFX/foreveral.webp" zoom 0.3 ypos 100 + 100 * i xanchor 1.0 xpos 1915
                if (pkmn.GetHealthPercentage() < 1):
                    $ maxhealth = pkmn.GetStat(Stats.Health, triggerAbilities=False)
                    $ health = max(pkmn.GetHealth(), pkmn.GetCaught())
                    $ barcolor = "#00b612"
                    if (health / maxhealth <= 0.25):
                        $ barcolor = "#ff0000"
                    elif (health / maxhealth <= 0.5):
                        $ barcolor = "#fff700"
                    bar range maxhealth value health pos (1910, 135 + 100 * i) xanchor 1.0 xmaximum 100 ymaximum 10 yminimum 10 right_bar "#000" left_bar barcolor
        
        if (len(playerparty) > 0 and not InDungeon()):
            textbutton "{color=#000000}Collapse" xalign 1.0 text_xalign 0.5 ypos 50 + 100 * len(playerparty) xminimum 115 yminimum 50 ymaximum 50 action [SetVariable("partyviewer", False)] text_font "fonts/pkmndp.ttf" style "menu_choice_button" keyboard_focus False
    elif (len(playerparty) > 0 and not InDungeon()):
        textbutton "{color=#000000}Expand" xalign 1.0 text_xalign 0.5 ypos 50 xminimum 115 yminimum 50 ymaximum 50 action [SetVariable("partyviewer", True)] text_font "fonts/pkmndp.ttf" style "menu_choice_button" keyboard_focus False

screen wallet():
    if (money > 0):
        frame:
            ypadding 10
            xpadding 15
            background Frame("GFX/DateTimeBanner.webp") at Transform(xzoom=-1)
            text "$" + str('{:,}'.format(money)) size 28 color "#1c1c1c" at Transform(xzoom=-1) alt ""

screen inventorywidget():
    if (len(inventory) > 1 and not disableinventory):
        imagebutton: 
            idle "GUI/stats_frame.webp" 
            hover "GUI/stats_frame_hover.webp"
            keyboard_focus False 
            action [Function(renpy.retain_after_load), SetVariable("activemon", None), SetVariable("activeitem", None), SetVariable("invoverwrite", None), ShowTransient("fieldinventory"), SetVariable("pkmnlocked", -1), SetVariable("pkmnlockedmove", -1), Hide("foreveralinventory"), Hide("partyviewerpopup"), Hide("partyviewer"), Hide("mondata"), Hide("nonbattlemoves")]
            align (1.0, 1.0)
        add "GUI/backpack.webp" align (0.99, 0.99) 

screen foreveralwidget():
    if (len(foreveralinv) > 1 and not disableinventory):
        imagebutton: 
            idle "GUI/stats_frame.webp" 
            hover "GUI/stats_frame_hover.webp" 
            keyboard_focus False
            action ([Function(renpy.retain_after_load), ShowTransient("modalinteractivescreen", screenname="foreveralinventory"), SetVariable("pkmnlocked", -1), SetVariable("pkmnlockedmove", -1), Hide("fieldinventory"), Hide("partyviewerpopup"), Hide("partyviewer"), Hide("mondata"), Hide("nonbattlemoves")] if not InDungeon() else Call("BlockDungeonForeverals"))
            align (1.0, 0.9)
        add "GUI/foreveralsicon.webp" align (0.99, 0.89)

label BlockDungeonForeverals:
if (indungeontutorial):
    return
$ indungeontutorial = True
"The Mysteriosity is too powerful here... your Foreverals are highly unstable."
"Better leave 'em alone!"
$ indungeontutorial = False
return

init python:
    def GetForeveralMonname(foreveralname, changenidoran = True):
        monname = foreveralname[:foreveralname.index(" ")]
        if ("Mime Jr." in foreveralname):
            monname = "Mime Jr."
        elif ("Mr. Mime" in foreveralname):
            monname = "Mr. Mime"
        elif (monname == "Nidoran-X" and changenidoran):
            monname = "Nidoran♀"
        elif (monname == "Nidorin-X" and changenidoran):
            monname = "Nidorina"
        elif (monname == "X-sire" and changenidoran):
            monname = "Quagsire"
        return monname

    def GetPlayerpartyForeverals():
        partyforeverals = []
        for mon in playerparty:
            if mon.GetForeverals() != []:
                partyforeverals.append(mon.GetForeverals())
        return partyforeverals

    def SortedForeverals():
        global foreveraldex
        removethese = []
        for fvl in foreveraldex:
            if (fvl[FVLMacros.FVLLevel] > 10):
                removethese.append(fvl)
        foreveraldexcopy = [fvl for fvl in foreveraldex if fvl not in removethese]
        if (foreveralsort == "National Dex"):
            foreveraldexcopy.sort(reverse = foreveralsortinverse, key=(lambda entry : pokedexlookupname(GetForeveralMonname(entry[0], True), DexMacros.Id)))
        elif (foreveralsort == "Obtained"):
            foreveraldexcopy.sort(reverse = foreveralsortinverse, key=(lambda entry : (1000000 if entry[0] not in claimedforeverals else claimedforeverals.index(entry[0]))))
        elif (foreveralsort == "Type"):
            foreveraldexcopy.sort(reverse = foreveralsortinverse, key=(lambda entry : pokedexlookupname(GetForeveralMonname(entry[0], True), DexMacros.Type1)))
        elif (foreveralsort == "Category"):
            foreveraldexcopy.sort(reverse = foreveralsortinverse, key=(lambda entry : entry[0].replace(GetForeveralMonname(entry[0], False), "")))
        elif (foreveralsort == "Alphabetical"):
            foreveraldexcopy.sort(reverse = foreveralsortinverse, key=(lambda entry : entry[0]))

        return foreveraldexcopy[foreveralpage * 20:foreveralpage * 20 + 20]

    def AllMoves():
        movedex = set()
        finallist = []
        for fvl in claimedforeverals:
            for move in lookupforeveraldata(fvl, FVLMacros.FVLMoves):
                if (move not in movedex):
                    movedex |= { move }
                    finallist.append((move, fvl))
        return finallist

    def SortedMoves():
        finallist = AllMoves()

        if (foreveralsort == "Type"):
            finallist.sort(reverse = foreveralsortinverse, key=(lambda entry : GetMove(entry[0]).Type))
        elif (foreveralsort == "Category"):
            finallist.sort(reverse = foreveralsortinverse, key=(lambda entry : GetMove(entry[0]).Category))
        elif (foreveralsort == "Alphabetical"):
            finallist.sort(reverse = foreveralsortinverse, key=(lambda entry : GetMove(entry[0]).Name))
        elif (foreveralsort == "Limit"):
            finallist.sort(reverse = foreveralsortinverse, key=(lambda entry : -GetCalculatedMovePower(entry[0])))

        return finallist[foreveralpage * 30:foreveralpage * 30 + 30]

    def SortedForms():
        finallist = []
        for fvl in claimedforeverals:
            if ("Megaveral" in fvl or "Diveral" in fvl or "Gigaveral" in fvl):
                for mon in lookupforeveraldata(fvl, FVLMacros.FVLTypeData):
                    if (not isinstance(mon, str)):
                        finallist.append((mon, fvl))

        if (foreveralsort == "Type"):
            finallist.sort(reverse = foreveralsortinverse, key=(lambda entry : pokedexlookup(entry[0], DexMacros.Type1)))
        elif (foreveralsort == "National Dex"):
            finallist.sort(reverse = foreveralsortinverse, key=(lambda entry : entry[0]))
        elif (foreveralsort == "Category"):
            finallist.sort(reverse = foreveralsortinverse, key=(lambda entry : (3 if "Diveral" in entry[1] else (2 if "Gigaveral" in entry[1] else 1))))
        elif (foreveralsort == "Alphabetical"):
            finallist.sort(reverse = foreveralsortinverse, key=(lambda entry : pokedexlookup(entry[0], DexMacros.Name)))
        elif (foreveralsort == "Limit"):
            finallist.sort(reverse = foreveralsortinverse, key=(lambda entry : -pokedexlookup(entry[0], DexMacros.Total)))

        return finallist[foreveralpage * 20:foreveralpage * 20 + 20]

label trainingdata(mon, inbattle = False):
    if (inbattle):
        show screen battleui
    $ explainingf = True
    
    narrator "This Pokémon's behavior is different! It must be specially trained!"
        
    $ explainingf = False
    return

screen foreveralinfo(foreveral):
    modal True
    zorder 13

    $ entry = [ent for ent in foreveraldex if ent[FVLMacros.FVLName] == foreveral][0]
    default fvlmontypes = [pokedexlookupname(GetForeveralMonname(foreveral), DexMacros.Type1), pokedexlookupname(GetForeveralMonname(foreveral), DexMacros.Type2)]
    $ entryid = pokedexlookupname(GetForeveralMonname(foreveral), DexMacros.Id)
    $ hasfvl = foreveral in claimedforeverals
    default chosenmember = None
    $ eligiblemons = [pikachuobj] if pikachuobj in playerparty else [] # Pika can be chosen if he's in the party

    default loadoutdic = {"moves":[], "fvls":[], "forme":None}
    default toggledholdingfvl = False

    $ showid = entryid
    if entry[FVLMacros.FVLType] == ForeveralTypes.FormSwap:
        if "forme" in loadoutdic and loadoutdic["forme"] in entry[FVLMacros.FVLTypeData]:
            $ showid = loadoutdic["forme"]
    
    $ formtypeoverride = [pokedexlookup(showid, DexMacros.Type1), pokedexlookup(showid, DexMacros.Type2)]
    
    # These only apply if pika is a thing and is chosen.
    $ liberationlimit = GetLiberationLimitFromLoadout(loadoutdic) if chosenmember == pikachuobj else (0, []) # Automatically-updating LL from current loadout, only if Pika is chosen.
    $ eligibleformids = [frm[0] for frm in LoadoutDiveralForms(loadoutdic, False, True)] if chosenmember == pikachuobj else []

    for mon in playerparty:
        if mon != pikachuobj and (math.floor(mon.GetId()) == math.floor(entryid) or (entry[FVLMacros.FVLType] == ForeveralTypes.FormSwap and mon.GetId() in entry[FVLMacros.FVLTypeData])):
            $ eligiblemons.append(mon)

    $ canteditreason = ""

    if not hasfvl:
        $ canteditreason = "You do not have this foreveral."
    elif inbattle:
        $ canteditreason = "Can't edit Pokémon moves or foreveral during combat."
    elif foreveral in WhoHasFVLs(True) and not WhoHasFVLs(True)[foreveral][1]:
        $ canteditreason = "This foreveral is held by {} in the PC.".format(WhoHasFVLs(True)[foreveral][0].GetNickname())
    
    $ LLmsg = ""

    if liberationlimit:
        $ LLmsg = "Liberation Limit breakdown:\n"
        for category, specific, increase in liberationlimit[1]:
            if (not isinstance(specific, str)):
                $ specific = pokedexlookup(specific, DexMacros.Name)
            $ LLmsg += specific + ": " + str(math.floor(increase)) + "\n"
        $ LLmsg += "Total: " + str(liberationlimit[0]) + "/" + str(maxliberationlimit)
    elif not loadoutdic["moves"]: # No moves
        $ LLmsg = "Please choose at least one move."
    
    $ whoholdsfvlinparty = None
    if foreveral in WhoHasFVLs(True) and WhoHasFVLs(True)[foreveral][1]:
        $ whoholdsfvlinparty = WhoHasFVLs(True)[foreveral][0]
    
    # Above this is just data setup. Now actual screen data begins.
    if inbattle: # Show dummy frame while in battle to make it flush nicely
        frame:
            xpos 0.209
            yanchor 0.0
            ypos 0.124
            xysize (1118, 545)
            background "images/GUI/readback.webp"
    
    frame:
        xpos position(6, 0.209)
        yanchor 0.0
        ypos position(6, 0.124)
        xysize (1106, 533)
        if (fvlmontypes if formtypeoverride == [] else formtypeoverride)[1]:
            background Composite((1106, 533),
                                (0, 0), Crop((0, 0, 553, 533), "GUI/bg_tiles/bg_tile_" + (fvlmontypes if formtypeoverride == [] else formtypeoverride)[0].lower() + "_full.webp"),
                                (553, 0), Crop((13, 0, 1106-553, 533), "GUI/bg_tiles/bg_tile_" + (fvlmontypes if formtypeoverride == [] else formtypeoverride)[1].lower() + "_full.webp"),
                                (0, 0), "#ffffffa0")
        else:
            background Composite((1106, 533),
                                (0, 0), Crop((0, 0, 1106, 533), "GUI/bg_tiles/bg_tile_" + (fvlmontypes if formtypeoverride == [] else formtypeoverride)[0].lower() + "_full.webp"),
                                (0, 0), "#ffffffa0")
        padding (0, 0)

        viewport: # This viewport is purely for cropping purposes.
            pos (500, 0)
            xysize (606, 483)
            yinitial 0.3
            add "Pokemon/{}.webp".format(showid):
                xysize (750, 750)
                alpha 0.4

        vbox:
            text foreveral ypos 0 size 60 xalign .5

            frame:
                background None
                xysize (1106, 423)
                
                if entry[FVLMacros.FVLLevel] < 11:
                    $ fvlreqstr = "Reach a bond level of {} and rank {} with{}".format(entry[FVLMacros.FVLLevel], (entry[FVLMacros.FVLLevel]-1) // 2, "..." if entry[FVLMacros.FVLTrainer] in persondex.keys() and persondex[entry[FVLMacros.FVLTrainer]]["Named"] else " a certain trainer.")

                    text fvlreqstr:
                        ypos position(-230, 1.0) # This ensures this text is always just over the chibi.
                        yanchor 1.0
                        xmaximum 400
                        yfill False
                        size 25
                        color "#000"
                        font "fonts/pkmndp.ttf"

                    add (GetChibi(entry[FVLMacros.FVLTrainer]) if entry[FVLMacros.FVLTrainer] in persondex.keys() and persondex[entry[FVLMacros.FVLTrainer]]["Named"] else "images/chibis/quest.webp"):
                        yalign 1.0
                        xysize (250, 250)
                
                vbox:
                    pos(0, 0)
                    xmaximum 535

                    text "Description:":
                        bold True
                        font "fonts/pkmndp.ttf"
                        size 35
                    
                    text "{}.".format(entry[FVLMacros.FVLDescription]):
                        font "fonts/pkmndp.ttf"
                        size 25
                
                if chosenmember == pikachuobj:
                        textbutton str(liberationlimit[0]) + "/" + str(maxliberationlimit):
                            tooltip LLmsg
                            text_font "fonts/pkmndp.ttf"
                            text_color "#000000fe"
                            ypos 0 xalign .5
                            padding (0, 0)
                            action NullAction()
                
                # HOLD FVL SECTION
                vbox:
                    xsize 400
                    xalign 1.0
               
                    if chosenmember == pikachuobj:
                        $ pika_fvl_actions = []
                        $ addingfvl = False
                        if "fvls" not in loadoutdic or not loadoutdic["fvls"]: # No FVLs
                            $ pika_fvl_actions = [SetDict(loadoutdic, "fvls", [foreveral])]
                            $ addingfvl = True
                        elif foreveral in loadoutdic["fvls"]: # FVL is equipped by Pika
                            $ pika_fvl_actions = [RemoveFromSet(loadoutdic["fvls"], foreveral)]
                            if "fvls" in GenerateCurrPikachuLoadout() and set(loadoutdic["fvls"]) - set([foreveral]) != set(GenerateCurrPikachuLoadout()["fvls"]) and foreveral not in GenerateCurrPikachuLoadout()["fvls"]: # If we changed stuff...
                                $ pika_fvl_actions.append(SetDict(loadoutdic, "fvls", GenerateCurrPikachuLoadout()["fvls"])) # ...restore the original.
                        elif len(loadoutdic["fvls"]) == GetMaxForeveralCount(): # Want to equip FVL when at cap
                            $ pika_fvl_actions = [RemoveFromSet(loadoutdic["fvls"], loadoutdic["fvls"][0]), AddToSet(loadoutdic["fvls"], foreveral)]
                            $ addingfvl = True
                        else: # Can just add normally
                            $ pika_fvl_actions = [AddToSet(loadoutdic["fvls"], foreveral)]
                            $ addingfvl = True
                        
                        if addingfvl and "forme" in loadoutdic and loadoutdic["forme"]: # If a forme is already set while we wanna hold a FVL...
                            if entry[FVLMacros.FVLType] != ForeveralTypes.FormSwap or loadoutdic["forme"] not in entry[FVLMacros.FVLTypeData]: # ...and if our FVL doesn't support the current form (either by not being a diveral or just not being the correct one)...
                                $ pika_fvl_actions.append(SetDict(loadoutdic, "forme", None)) # ...unset the forme!
                        elif not addingfvl: # And if we're un-holding a FVL...
                            $ pika_fvl_actions += [SetDict(loadoutdic, "forme", None if "forme" not in GenerateCurrPikachuLoadout() else GenerateCurrPikachuLoadout()["forme"]) if "forme" not in GenerateCurrPikachuLoadout() else None] # ...restore the existing one (and remove background overriding).
                        
                    $ toggleaction = None
                    if "fvls" in loadoutdic and foreveral in loadoutdic["fvls"]:
                        $ toggleaction = ToggleSetMembership(loadoutdic["fvls"], foreveral)
                    else:
                        $ toggleaction = SetDict(loadoutdic, "fvls", [foreveral])
                    
                    hbox:
                        imagebutton:
                            if ("fvls" in loadoutdic and foreveral in loadoutdic["fvls"]) or (whoholdsfvlinparty and not chosenmember): # If you don't have a mon selected, color FVL if anyone in party holds FVL. Otherwise, color if current mon is set to hold it.
                                idle Transform("GFX/foreveral.webp", xysize=(50, 50), matrixcolor=IdentityMatrix())
                                hover Transform("GFX/foreveral.webp", xysize=(50, 50), matrixcolor=BrightnessMatrix(0.1))
                            else:
                                idle Transform("GFX/foreveral.webp", xysize=(50, 50), matrixcolor=SaturationMatrix(0))
                                hover Transform("GFX/foreveral.webp", xysize=(50, 50), matrixcolor=SaturationMatrix(0)*BrightnessMatrix(0.1))
                            if whoholdsfvlinparty and chosenmember and whoholdsfvlinparty != chosenmember:
                                tooltip "This foreveral is held by {}. Applying will move it to {}.".format(whoholdsfvlinparty.GetNickname(), chosenmember.GetNickname())
                            if chosenmember != pikachuobj:
                                action [toggleaction, SetScreenVariable("toggledholdingfvl", True)]
                            else:
                                action [toggleaction, SetScreenVariable("toggledholdingfvl", True)] + pika_fvl_actions
                            sensitive bool(chosenmember)
                        
                        null width 5
                        
                        textbutton ("Foreveral {} held{}.".format(("is" if ("fvls" in loadoutdic and foreveral in loadoutdic["fvls"]) or (whoholdsfvlinparty and not chosenmember) else "isn't") if not toggledholdingfvl else ("will be" if ("fvls" in loadoutdic and foreveral in loadoutdic["fvls"]) or (whoholdsfvlinparty and not chosenmember) else "won't be"), " by this Pokémon" if chosenmember else "") if hasfvl else "You don't own this foreveral."):
                            text_size 20
                            text_font "fonts/pkmndp.ttf"
                            style "menu_choice_button"
                            yalign 0.5
                            xysize (345, 50)
                            text_color ("#000000fe" if chosenmember else "#888888fe")
                            if chosenmember:
                                text_hover_color "#ff00fffe"
                            if whoholdsfvlinparty and chosenmember and whoholdsfvlinparty != chosenmember:
                                tooltip "This foreveral is held by {}. Applying will move it to {}.".format(whoholdsfvlinparty.GetNickname(), chosenmember.GetNickname())
                            if chosenmember != pikachuobj:
                                action [toggleaction, SetScreenVariable("toggledholdingfvl", True)]
                            else:
                                action [toggleaction, SetScreenVariable("toggledholdingfvl", True)] + pika_fvl_actions
                            sensitive bool(chosenmember)
                    
                    # DIVERAL FORMS DROPDOWN
                    if entry[FVLMacros.FVLType] == ForeveralTypes.FormSwap:
                        textbutton "{} diveral forms:".format("Choose" if chosenmember else "Preview"):
                            text_font "fonts/pkmndp.ttf"
                            style "menu_choice_button"
                            xysize (400, 50)
                            text_color "#000000fe"
                            text_hover_color "#ff00fffe"
                            text_size 30
                            action CaptureFocus("form_drop")
                
                # FOREVERAL MOVES SECTION
                vbox:
                    xsize 300 + 18 * (len(entry[FVLMacros.FVLMoves]) > 4)
                    anchor (1.0, 1.0)
                    xpos position(-350, 1.0)
                    ypos position(-30, 1.0)

                    text "Foreveral moves:" font "fonts/pkmndp.ttf"
                    
                    frame:
                        ymaximum 200
                        background None
                        padding (0, 0)

                        has viewport:
                            if len(entry[FVLMacros.FVLMoves]) > 4: # Add a scrollbar for FVLs that give more than 2 moves (hi Blue)
                                scrollbars "vertical"
                                arrowkeys True
                                pagekeys True
                                mousewheel True
                                vscrollbar_base_bar "#fff"
                                vscrollbar_thumb "#363436"
                                vscrollbar_top_bar "#e7e6e7"
                                vscrollbar_bottom_bar "#e7e6e7"
                            
                            has vbox:
                                for move in entry[FVLMacros.FVLMoves]:
                                    textbutton "{size=25}" + GetTypeEssentiarum(GetMove(move).Type) + "{/size} " + move:
                                        text_font "fonts/pkmndp.ttf"
                                        style "menu_choice_button"
                                        xysize (300, 50)
                                        text_color ("#000000fe" if chosenmember and len(loadoutdic["moves"]) < 4 and move not in loadoutdic["moves"] else "#888888fe")
                                        if chosenmember:
                                            text_hover_color "#ff00fffe"
                                        text_size 30
                                        if chosenmember != pikachuobj:
                                            action AddToSet(loadoutdic["moves"], move)
                                        else:
                                            action [AddToSet(loadoutdic["moves"], move)]
                                        sensitive bool(chosenmember) and len(loadoutdic["moves"]) < 4 and move not in loadoutdic["moves"]
                
                # ELIGIBLE MEMBER AND MOVESET VIEW
                vbox:
                    xsize 300 + 18 * (len(eligiblemons) > 3)
                    align (1.0, 1.0)
                    yfit False

                    if not chosenmember and not canteditreason: # Default state, party member not chosen
                        if len(eligiblemons):
                            frame:
                                ysize 125
                                background None
                                padding (0, 0)

                                text "Please choose a party member:" font "fonts/pkmndp.ttf" size 30 yalign 1.0

                            frame:
                                ymaximum 150
                                background None
                                padding (0, 0)

                                has viewport:
                                    if len(eligiblemons) > 3: # Ensure scrolling only when needed (i.e. too many eligible mons)
                                        scrollbars "vertical"
                                        arrowkeys True
                                        pagekeys True
                                        mousewheel True
                                        vscrollbar_base_bar "#fff"
                                        vscrollbar_thumb "#363436"
                                        vscrollbar_top_bar "#e7e6e7"
                                        vscrollbar_bottom_bar "#e7e6e7"
                                    
                                    has vbox:
                                        for mon in eligiblemons:
                                            
                                            textbutton mon.GetNickname():
                                                text_font "fonts/pkmndp.ttf"
                                                style "menu_choice_button"
                                                xysize (300, 50)
                                                text_color "#000000fe"
                                                text_hover_color "#ff00fffe"
                                                text_size 30
                                                if mon != pikachuobj:
                                                    action [SetScreenVariable("chosenmember", mon), SetScreenVariable("loadoutdic", GenerateCurrPokemonLoadout(mon))]
                                                else:
                                                    action [SetScreenVariable("chosenmember", mon), SetScreenVariable("loadoutdic", GenerateCurrPikachuLoadout())]
                        else: # No eligible mons
                            frame:
                                ysize 275
                                background None
                                padding (0, 0)

                                text "You don't have any eligible Pokémon in your party." font "fonts/pkmndp.ttf" yalign 1.0
                    
                    elif not canteditreason: # Shows up when mon is chosen
                        null height 20

                        hbox:
                            textbutton "Go back":
                                text_font "fonts/pkmndp.ttf"
                                style "menu_choice_button"
                                xysize (150, 50)
                                text_color "#000000fe"
                                text_hover_color "#ff00fffe"
                                text_size 30
                                action [SetScreenVariable("chosenmember", None), SetScreenVariable("toggledholdingfvl", False), SetScreenVariable("loadoutdic", {"moves":[], "fvls":[], "forme":None})]
                            textbutton "Reset":
                                text_font "fonts/pkmndp.ttf"
                                style "menu_choice_button"
                                xysize (150, 50)
                                text_color "#000000fe"
                                text_hover_color "#ff00fffe"
                                text_size 30
                                if chosenmember != pikachuobj:
                                    action [SetDict(loadoutdic, "moves", chosenmember.GetMoveNames())]
                                else:
                                    action [SetDict(loadoutdic, "moves", chosenmember.GetMoveNames())]
                        
                        null height 5

                        for i in range(4):
                            if i < len(loadoutdic["moves"]):
                                textbutton GetTypeEssentiarum(GetMove(loadoutdic["moves"][i]).Type)  + " " + loadoutdic["moves"][i]:
                                    text_font "fonts/pkmndp.ttf"
                                    style "menu_choice_button"
                                    xysize (300, 50)
                                    text_color "#000000fe"
                                    text_hover_color "#ff00fffe"
                                    text_size 30
                                    if chosenmember != pikachuobj:
                                        action RemoveFromSet(loadoutdic["moves"], loadoutdic["moves"][i]) 
                                    else:
                                        action RemoveFromSet(loadoutdic["moves"], loadoutdic["moves"][i]) 
                            else:
                                null height 50
                    else: 
                        null height 275 # Make sure height is idential to not shift top stuff


            hbox xalign 0.5:
                textbutton "Back":
                    text_font "fonts/pkmndp.ttf"
                    style "menu_choice_button"
                    xysize (553, 50)
                    text_color "#000000fe"
                    text_hover_color "#ff00fffe"
                    text_size 25
                    text_xalign .5
                    action [Hide(transition=dissolve), SetVariable("explainingf", False)]
                textbutton "Apply":
                    text_font "fonts/pkmndp.ttf"
                    style "menu_choice_button"
                    xysize (553, 50)
                    text_color ("#000000fe" if chosenmember and loadoutdic["moves"] and (int(liberationlimit[0]) <= maxliberationlimit if chosenmember == pikachuobj else True) else "#888888fe")
                    text_size 25
                    text_xalign .5
                    if chosenmember:
                        if chosenmember != pikachuobj:
                            if not loadoutdic["moves"]:
                                action NullAction()
                                tooltip "Please choose at least one move."
                            else:
                                action [Function(ApplyForeveralLoadout, chosenmember, loadoutdic), Hide(transition=dissolve), SetVariable("explainingf", False)]
                        elif int(liberationlimit[0]) > maxliberationlimit or not loadoutdic["moves"]: # If LL is too high or there are no moves selected, disable button.
                            action NullAction()
                        else:
                            text_hover_color "#ff00fffe"
                            action [Function(ApplyNamelessPikachuLoadout, loadoutdic), Hide(transition=dissolve), SetVariable("explainingf", False)]
                            
                    else:
                        action NullAction()
                        tooltip (canteditreason if canteditreason else "Please choose a Pokémon to edit." if eligiblemons else None)
    
    if GetTooltip():
        nearrect:
            focus "tooltip"
            prefer_top True

            frame:
                xanchor 0.0
                xpos .5

                if isinstance(GetTooltip(), str): # If text-based tooltip
                    text GetTooltip() size 30 color "#000" font "fonts/pkmndp.ttf"
    
    if GetFocusRect("form_drop"): # Form dropdown
        dismiss action ClearFocus("form_drop")

        nearrect:
            focus "form_drop"
            
            frame:
                ymaximum 250
                xsize 400
                background None
                padding (0, 0)

                has viewport:
                    if len(entry[FVLMacros.FVLTypeData]) > 10 - (chosenmember == pikachuobj): # Ensure scrolling only when needed (i.e. too many eligible forms)
                        scrollbars "vertical"
                        arrowkeys True
                        pagekeys True
                        mousewheel True
                        vscrollbar_base_bar "#fff"
                        vscrollbar_thumb "#363436"
                        vscrollbar_top_bar "#e7e6e7"
                        vscrollbar_bottom_bar "#e7e6e7"
                    
                    has vbox:
                        if chosenmember == pikachuobj:
                            $ pikaswapformextra = []
                            $ pikaremoveformextra = SetDict(loadoutdic, "fvls", [] if "fvls" not in GenerateCurrPikachuLoadout() else GenerateCurrPikachuLoadout()["fvls"]) if not toggledholdingfvl else None # If you unselect a form, restore FVLs if you're not holding it already
                            if not set(entry[FVLMacros.FVLTypeData]) & set(eligibleformids): # If the forms offered aren't available on equipped diverals...
                                $ pikaswapformextra.append(SetDict(loadoutdic, "fvls", [])) # ...remove all FVLs if you select one!
                        
                        if chosenmember == pikachuobj and "forme" in loadoutdic and loadoutdic["forme"] in entry[FVLMacros.FVLTypeData]:
                            textbutton "Remove form":
                                text_font "fonts/pkmndp.ttf"
                                style "menu_choice_button"
                                xysize (400, 50)
                                text_color "#000000fe"
                                text_hover_color "#ff00fffe"
                                text_size 30
                                action [SetDict(loadoutdic, "forme", None), SetScreenVariable("showid", entryid), pikaremoveformextra, ClearFocus("form_drop")]
                        for form in entry[FVLMacros.FVLTypeData]:
                            textbutton pokedexlookup(form, DexMacros.Forme):
                                text_font "fonts/pkmndp.ttf"
                                style "menu_choice_button"
                                xysize (400, 50)
                                text_color "#000000fe"
                                text_hover_color "#ff00fffe"
                                text_size 30
                                if chosenmember != pikachuobj:
                                    action [SetDict(loadoutdic, "forme", form), ClearFocus("form_drop")]
                                else:
                                    action [SetDict(loadoutdic, "forme", form), pikaswapformextra, ClearFocus("form_drop")]

screen modalinteractivescreen(screenname):
    modal True
    zorder 12
    $ tagname = "interactive_" + screenname
    tag tagname
     
    use expression screenname pass (True)

screen decorativescreen(screenname):
    use expression screenname pass (False)
    $ tagname = "decorative_" + screenname
    tag tagname

screen foreveralinventory(interact = True):
    on "show" action If("pika_loadouts" not in globals(), SetVariable("pika_loadouts", {}), NullAction()) # To ensure save compatibility, we create the loadout dict on the first time this is shown.
    hbox:
        align (0.5, 0.05)
        if (foreveralinvsubmenu == "Loadouts"): # Adding all top buttons manually, as they're functionally different for the loadouts. 
            default currloadout = {"moves":[]}

            textbutton "Loadouts" action [SetVariable("foreveralpage", 0), SetVariable("loadoutscreen", "Loadouts")] xmaximum 224 text_size 40 text_xalign 0.5 text_color ("#000" if loadoutscreen != "Loadouts" else "#ff0000") text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" sensitive interact
            textbutton "Moves" action [SetVariable("foreveralpage", 0), SetVariable("loadoutscreen", "Moves")] xmaximum 224 text_size 40 text_xalign 0.5 text_color ("#000" if loadoutscreen != "Moves" else "#ff0000") text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" sensitive interact
            textbutton "Foreverals" action [SetVariable("foreveralpage", 0), SetVariable("loadoutscreen", "Foreverals")] xmaximum 224 text_size 40 text_xalign 0.5 text_color ("#000" if loadoutscreen != "Foreverals" else "#ff0000") text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" sensitive interact
            textbutton "Forms":
                style "menu_choice_button" text_font "fonts/pkmndp.ttf"
                xmaximum 224 text_size 40 text_xalign 0.5
                sensitive interact
                if LoadoutDiveralForms(currloadout, False):
                    action [SetVariable("foreveralpage", 0), SetVariable("loadoutscreen", "Forms")]
                    text_color ("#000" if loadoutscreen != "Forms" else "#ff0000")
                    text_hover_color "#f0f"
                else:
                    action NullAction()
                    text_color "#888888fe"
            textbutton "Sort by":
                action If(loadoutscreen != "Loadouts", CaptureFocus("loadouts_sortdrop"), NullAction()) # Useless when on the overview
                xmaximum 224 text_size 40 text_xalign 0.5
                text_color If(loadoutscreen != "Loadouts", "#000", "#888888fe")
                sensitive interact
                if loadoutscreen != "Loadouts":
                    text_hover_color "#f0f"
                style "menu_choice_button" text_font "fonts/pkmndp.ttf"
        if (foreveralinvsubmenu in ["Foreverals", "Forms"] and foreveralinvsubmenu != "Loadouts"):
            textbutton "National Dex" action SetVariable("foreveralsort", "National Dex") xmaximum 224 text_size 40 text_xalign 0.5 text_color ("#000" if foreveralsort != "National Dex" else "#ff0000") text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" sensitive interact
        if (foreveralinvsubmenu == "Foreverals" and foreveralinvsubmenu != "Loadouts"):
            textbutton "Obtained" action SetVariable("foreveralsort", "Obtained") xmaximum 224 text_size 40 text_xalign 0.5 text_color ("#000" if foreveralsort != "Obtained" else "#ff0000") text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" sensitive interact
        if (foreveralinvsubmenu != "Foreverals" and foreveralinvsubmenu != "Loadouts"):
            textbutton "Limit" action SetVariable("foreveralsort", "Limit") xmaximum 224 text_size 40 text_xalign 0.5 text_color ("#000" if foreveralsort != "Limit" else "#ff0000") text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" sensitive interact
        if (foreveralinvsubmenu != "Loadouts"):
            textbutton "Type" action SetVariable("foreveralsort", "Type") xmaximum 224 text_size 40 text_xalign 0.5 text_color ("#000" if foreveralsort != "Type" else "#ff0000") text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" sensitive interact
            textbutton "Category" action SetVariable("foreveralsort", "Category") xmaximum 223 text_size 40 text_xalign 0.5 text_color ("#000" if foreveralsort != "Category" else "#ff0000") text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" sensitive interact
            textbutton "Alphabetical" action SetVariable("foreveralsort", "Alphabetical") xmaximum 223 text_size 40 text_xalign 0.5 text_color ("#000" if foreveralsort != "Alphabetical" else "#ff0000") text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" sensitive interact
    
    if (usingliberationlimit):
        #left side
        textbutton ("{b}Foreverals{/b}" if foreveralinvsubmenu == "Foreverals" else "Foreverals") xmaximum 250 xpos 0.151 ypos .2 text_size 40 text_xalign 0.5 text_color "#000" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action [SetVariable("foreveralpage", 0), SetVariable("foreveralinvsubmenu", "Foreverals")] text_hover_color "#f0f" sensitive interact
        textbutton ("{b}Moves{/b}" if foreveralinvsubmenu == "Moves" else "Moves") xmaximum 250 xpos 0.151 ypos .275 text_size 40 text_xalign 0.5 text_color "#000" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action [SetVariable("foreveralpage", 0), SetVariable("foreveralinvsubmenu", "Moves")] text_hover_color "#f0f" sensitive interact
        textbutton ("{b}Forms{/b}" if foreveralinvsubmenu == "Forms" else "Forms") xmaximum 250 xpos 0.151 ypos .35 text_size 40 text_xalign 0.5 text_color "#000" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action [SetVariable("foreveralpage", 0), SetVariable("foreveralinvsubmenu", "Forms")] text_hover_color "#f0f" sensitive interact
        textbutton ("{b}Loadouts{/b}" if foreveralinvsubmenu == "Loadouts" else "Loadouts") xmaximum 250 xpos 0.151 ypos .425 text_size 40 text_xalign 0.5 text_color "#000" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action [SetVariable("foreveralpage", 0), SetVariable("foreveralinvsubmenu", "Loadouts")] text_hover_color "#f0f" sensitive interact
        #right side
        $ ll = GetLiberationLimit()
        frame:
            xpadding 5
            xsize 250 
            xpos .856 
            ypos .125
            style "menu_choice_button"
            vbox:
                text "Liberation Limit" size 40 xalign 0.5 color "#000" font "fonts/pkmndp.ttf"
                text str(ll[0]) + "/" + str(maxliberationlimit) size 40 xalign 0.5 color "#000" font "fonts/pkmndp.ttf"
                for category, specific, increase in ll[1]:
                    if (not isinstance(specific, str)):
                        $ specific = pokedexlookup(specific, DexMacros.Name)
                    text specific.replace("♂", "{font=fonts/pkmndp.ttf}♂{/font}").replace("♀", "{font=fonts/pkmndp.ttf}♀{/font}") + ": " + str(math.floor(increase)) size 30 color "#000" font "fonts/pkmndp.ttf"
    
    if (foreveralinvsubmenu == "Foreverals"):
        textbutton "Page " + str(foreveralpage + 1) + "/" + str(math.ceil(len(foreveraldex) / 20)) xmaximum 250 xpos 0.151 ypos .125 text_size 40 text_xalign 0.5 text_color "#000" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
        frame:
            xpos 0.209
            yanchor 0.0
            ypos 0.124
            xysize (1118, 545)
            background "images/GUI/readback.webp"
            $ foreveralcount = 0
            grid 2 10:
                xfill True
                transpose True
                for foreveral in SortedForeverals():
                    $ foreveralcount += 1
                    textbutton GetTypeEssentiarum(pokedexlookupname(GetForeveralMonname(foreveral[0], True), DexMacros.Type1)) + foreveral[0]:
                        text_size 30
                        text_color ("#000000fe" if foreveral[0] in claimedforeverals else "#717171fe") 
                        action [Show("foreveralinfo", foreveral=foreveral[0], transition=dissolve), SetVariable("explainingf", True)]
                        text_hover_color "#ff00fffe"
                        sensitive interact
                for x in range(20 - foreveralcount):
                    null
    elif (foreveralinvsubmenu == "Moves"):
        $ moveslist = SortedMoves()
        textbutton "Page " + str(foreveralpage + 1) + "/" + str(math.ceil(len(AllMoves()) / 30)) xmaximum 250 xpos 0.151 ypos .125 text_size 40 text_xalign 0.5 text_color "#000" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
        frame:
            xpos 0.209
            yanchor 0.0
            ypos 0.124
            xysize (1118, 545)
            background "images/GUI/readback.webp"
            $ foreveralcount = 0
            grid 3 10:
                transpose True
                for move, fvl in moveslist:
                    $ foreveralcount += 1
                    textbutton GetTypeEssentiarum(GetMove(move).Type) + move + " (" + str(GetCalculatedMovePower(move)) + ")":
                        text_color "#000000fe"
                        text_hover_color "#ff00fffe"
                        text_size 30
                        action [Show("foreveralinfo", foreveral=fvl, transition=dissolve), SetVariable("explainingf", True)]
                        sensitive interact
                for x in range(30 - foreveralcount):
                    null
    elif (foreveralinvsubmenu == "Forms"):
        $ formslist = SortedForms()
        textbutton "Page " + str(foreveralpage + 1) + "/" + str(math.ceil(len(formslist) / 20)) xmaximum 250 xpos 0.151 ypos .125 text_size 40 text_xalign 0.5 text_color "#000" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
        frame:
            xpos 0.209
            yanchor 0.0
            ypos 0.124
            xysize (1118, 545)
            background "images/GUI/readback.webp"
            $ foreveralcount = 0
            grid 2 10:
                transpose True
                for mon, fvl in formslist:
                    $ foreveralcount += 1
                    textbutton GetTypeEssentiarum(pokedexlookup(mon, DexMacros.Type1)) + pokedexlookup(mon, DexMacros.Forme).replace(" Form", "").replace("♂", "{font=fonts/DejaVuSans.ttf}♂{/font}").replace("♀", "{font=fonts/DejaVuSans.ttf}♀{/font}") + " (" + str(math.floor(pokedexlookup(mon, DexMacros.Total) / 5)) + ")":
                        text_color "#000000fe"
                        text_hover_color "#ff00fffe"
                        text_size 30
                        action [Show("foreveralinfo", foreveral=fvl, transition=dissolve), SetVariable("explainingf", True)]
                        sensitive interact
                for x in range(20 - foreveralcount):
                    null
    elif (foreveralinvsubmenu == "Loadouts"):
        if loadoutscreen == "Moves":
            $ loadoutmoveslist = SortedLoadoutMoves()
            textbutton "Page " + str(foreveralpage + 1) + "/" + str(math.ceil(len(AllMoves()) / 30)) xmaximum 250 xpos 0.151 ypos .125 text_size 40 text_xalign 0.5 text_color "#000" style "menu_choice_button" text_font "fonts/pkmndp.ttf" sensitive interact
        if loadoutscreen == "Foreverals":
            textbutton "Page " + str(foreveralpage + 1) + "/" + str(math.ceil(len(claimedforeverals) / 20)) xmaximum 250 xpos 0.151 ypos .125 text_size 40 text_xalign 0.5 text_color "#000" style "menu_choice_button" text_font "fonts/pkmndp.ttf" sensitive interact
        if loadoutscreen == "Forms":
            $ loadoutformslist = LoadoutDiveralForms(currloadout)
            textbutton "Page " + str(foreveralpage + 1) + "/" + str(math.ceil(len(loadoutformslist) / 20)) xmaximum 250 xpos 0.151 ypos .125 text_size 40 text_xalign 0.5 text_color "#000" style "menu_choice_button" text_font "fonts/pkmndp.ttf" sensitive interact
        frame:
            xpos 0.209
            yanchor 0.0
            ypos 0.124
            xysize (1118, 545)
            background "images/GUI/readback.webp"
            $ foreveralcount = 0
            $ currpika = GenerateCurrPikachuLoadout()
            
            default chosen_loadout = None
            $ curr_libcost = GetLiberationLimitFromLoadout(currloadout)
            $ wherefvls = LoadoutWhoHasFVLs(currloadout)
            $ whereallfvls = WhoHasFVLs()
            $ anyboxedfvls = bool(sum([not mon[1] for heldfvl, mon in wherefvls.items()])) # This will be True if at least one FVL is held by a PC'd mon.

            if loadoutscreen == "Loadouts": # Show main loadout screen
                vbox:
                    hbox xalign 0.5:
                        textbutton "Loadouts:":
                            text_font "fonts/pkmndp.ttf"
                            style "menu_choice_button"
                            xysize (277, 50)
                            sensitive interact
                            if pika_loadouts:
                                text_color "#000000fe"
                                text_hover_color "#ff00fffe"
                                action CaptureFocus("loadouts_drop")
                            else:
                                text_color "#888888fe"
                                action NullAction()
                            text_size 30
                            text_xalign .5
                        textbutton "Clear loadout":
                            text_font "fonts/pkmndp.ttf"
                            style "menu_choice_button"
                            xysize (277, 50)
                            text_color "#000000fe"
                            text_hover_color "#ff00fffe"
                            text_size 30
                            text_xalign .5
                            action [SetLocalVariable("currloadout", {"moves":[]}), SetLocalVariable("chosen_loadout", None)]
                            sensitive interact
                        
                        if chosen_loadout:
                            textbutton "Rename loadout":
                                text_font "fonts/pkmndp.ttf"
                                style "menu_choice_button"
                                xysize (277, 50)
                                text_color "#000000fe"
                                text_hover_color "#ff00fffe"
                                text_size 30
                                text_xalign .5
                                action CaptureFocus("rename_loadout")
                                sensitive interact
                            textbutton "Delete loadout":
                                text_font "fonts/pkmndp.ttf"
                                style "menu_choice_button"
                                xysize (277, 50)
                                text_color "#000000fe"
                                text_hover_color "#ff00fffe"
                                text_size 30
                                text_xalign .5
                                action CaptureFocus("del_loadout")
                                sensitive interact
                        else:
                            frame background None xysize (277, 50) padding (0, 0)
                            frame background None xysize (277, 50) padding (0, 0)
                    hbox:
                        frame:
                            background None
                            xysize (550, 435)

                            text If(chosen_loadout, chosen_loadout, "New loadout") ypos 0 size 60 xalign .5
                            if currloadout != {"moves":[]}:
                                textbutton str(curr_libcost[0]) + "/" + str(maxliberationlimit):
                                    tooltip curr_libcost[1]
                                    text_font "fonts/pkmndp.ttf"
                                    text_color "#000000fe"
                                    ypos 60 xalign .5
                                    padding (0, 0)
                                    action NullAction()
                                    sensitive interact

                            vbox pos(10, 100):
                                hbox:
                                    text "Foreveral:" yalign .5
                                    if "fvls" in currloadout.keys() and len(currloadout["fvls"]) > 0:
                                        textbutton ",".join(currloadout["fvls"]):
                                            text_font "fonts/pkmndp.ttf"
                                            style "menu_choice_button"
                                            xysize (300, 50)
                                            yalign .5
                                            text_color "#000000fe"
                                            text_hover_color "#ff00fffe"
                                            text_size 30
                                            action SetDict(currloadout, "fvls", [])
                                            sensitive interact
                                    else:
                                        text "None"
                                
                                hbox:
                                    text "Form:" yalign .5
                                    
                                    if "forme" in currloadout.keys() and currloadout["forme"]:
                                        textbutton pokedexlookup(currloadout["forme"], DexMacros.Forme).replace(" Form", ""):
                                            text_font "fonts/pkmndp.ttf"
                                            style "menu_choice_button"
                                            xysize (300, 50)
                                            yalign .5
                                            text_color "#000000fe"
                                            text_hover_color "#ff00fffe"
                                            text_size 30
                                            action SetDict(currloadout, "forme", None)
                                            sensitive interact
                                    else:
                                        text "None"
                            
                            vbox pos(.5, 250) xalign .5:
                                text "Moveset:" align (.5, .5)

                                grid 2 2 yalign .5:
                                    for i in range(4):
                                        if i < len(currloadout["moves"]):
                                            textbutton GetTypeEssentiarum(GetMove(currloadout["moves"][i]).Type) + currloadout["moves"][i]:
                                                text_font "fonts/pkmndp.ttf"
                                                style "menu_choice_button"
                                                xysize (250, 50)
                                                text_color "#000000fe"
                                                text_hover_color "#ff00fffe"
                                                text_size 30
                                                action RemoveFromSet(currloadout["moves"], currloadout["moves"][i])
                                                sensitive interact
                                        else:
                                            null
                        frame:
                            background "#333"
                            xysize (5, 435)
                            xalign .5
                        frame:
                            background None
                            xysize (550, 435)

                            text "Current loadout" ypos 0 size 60 xalign .5
                            vbox pos(10, 100):
                                hbox:
                                    text "Foreveral:" yalign .5
                                    if "fvls" in currpika.keys():
                                        text ",".join(currpika["fvls"]):
                                            font "fonts/pkmndp.ttf"
                                            style "menu_choice_button"
                                    else:
                                        text "None"
                                
                                hbox:
                                    text "Form:" yalign .5
                                    
                                    if "forme" in currpika.keys():
                                        text pokedexlookup(currpika["forme"], DexMacros.Forme).replace(" Form", ""):
                                            font "fonts/pkmndp.ttf"
                                    else:
                                        text "None"
                            
                            vbox pos(.5, 250) xalign .5:
                                text "Moveset:" align (.5, .5)

                                grid 2 2 yspacing 5 yalign .5:
                                    for i in range(4):
                                        if i < len(currpika["moves"]):
                                            text GetTypeEssentiarum(GetMove(currpika["moves"][i]).Type) + currpika["moves"][i]:
                                                font "fonts/pkmndp.ttf"
                                                size 30
                                        else:
                                            null

                    hbox xalign 0.5:
                        textbutton "<- Edit Pikachu's loadout":
                            text_font "fonts/pkmndp.ttf"
                            style "menu_choice_button"
                            xysize (300, 50)
                            text_color "#000000fe"
                            text_hover_color "#ff00fffe"
                            text_size 25
                            text_xalign .5
                            action [SetLocalVariable("currloadout", copy.deepcopy(currpika)), SetLocalVariable("chosen_loadout", None)]
                            sensitive interact

                        textbutton "Save loadout":
                            text_font "fonts/pkmndp.ttf"
                            style "menu_choice_button"
                            xysize (300, 50)
                            text_color If(curr_libcost[0] <= maxliberationlimit and len(currloadout["moves"]) > 0, "#000000fe", "#888888fe")
                            sensitive interact
                            if curr_libcost[0] <= maxliberationlimit and len(currloadout["moves"]) > 0:
                                text_hover_color "#ff00fffe"
                            else:
                                tooltip "Cannot save - loadout exceeds Liberation Limit or has no moves!"
                            text_size 40
                            text_xalign .5
                            action If(curr_libcost[0] <= maxliberationlimit and len(currloadout["moves"]) > 0, CaptureFocus("loadouts_save"), NullAction())

                        textbutton "Apply loadout to Pikachu ->":
                            text_font "fonts/pkmndp.ttf"
                            style "menu_choice_button"
                            xysize (300, 50)
                            text_color If(curr_libcost[0] <= maxliberationlimit and len(currloadout["moves"]) > 0 and not anyboxedfvls, "#000000fe", "#888888fe")
                            sensitive interact
                            if curr_libcost[0] <= maxliberationlimit and len(currloadout["moves"]) > 0 and not anyboxedfvls:
                                text_hover_color "#ff00fffe"
                            elif anyboxedfvls:
                                tooltip wherefvls
                            else:
                                tooltip "Cannot apply - loadout exceeds Liberation Limit or has no moves!"
                            text_size 25
                            text_xalign .5
                            action If(curr_libcost[0] <= maxliberationlimit and len(currloadout["moves"]) > 0 and not anyboxedfvls, Function(ApplyNamelessPikachuLoadout, currloadout), NullAction())
            elif loadoutscreen == "Moves": # Handle move selection
                $ foreveralcount = 0
                grid 3 10:
                    transpose True
                    for move, fvl in loadoutmoveslist:
                        $ foreveralcount += 1
                        textbutton GetTypeEssentiarum(GetMove(move).Type) + If(move in currloadout["moves"], "{color=#22bb33fe}" + move + "{/color}", move) + " (" + str(GetCalculatedMovePower(move)) + ")":
                            text_color "#000000fe"
                            text_hover_color "#ff00fffe"
                            text_size 30
                            sensitive interact
                            if move in currloadout["moves"]:
                                action RemoveFromSet(currloadout["moves"], move)
                            elif len(currloadout["moves"]) < 4:
                                action AddToSet(currloadout["moves"], move)
                            else:
                                action [AddToSet(currloadout["moves"], move), RemoveFromSet(currloadout["moves"], currloadout["moves"][0])]
                    for x in range(30 - foreveralcount):
                        null
            elif loadoutscreen == "Foreverals": # Handle foreveral selection - filter ONLY obtained, sort with "Sort by"
                $ foreveralcount = 0
                grid 2 10:
                    xfill True
                    transpose True
                    for foreveral in LoadoutFVLWithForm(currloadout):
                        $ foreveralcount += 1
                        $ fvltext = foreveral
                        $ heldtooltip = ""
                        if "fvls" in currloadout and foreveral in currloadout["fvls"]:
                            $ fvltext = "{color=#22bb33fe}" + foreveral + "{/color}"
                        elif foreveral in whereallfvls:
                            if whereallfvls[foreveral][1]:
                                $ fvltext = "{color=#d5af2afe}" + foreveral + "{/color}"
                                $ heldtooltip = "This foreveral is currently held by " + whereallfvls[foreveral][0].GetNickname() + ".\nApplying this loadout will remove it."
                            else:
                                $ fvltext = "{color=#d4351efe}" + foreveral + "{/color}"
                                $ heldtooltip = "This foreveral is currently held by " + whereallfvls[foreveral][0].GetNickname() + " in the PC.\nYou will not be able to apply a loadout with this foreveral while " + whereallfvls[foreveral][0].GetNickname() + " is there."

                        textbutton GetTypeEssentiarum(pokedexlookupname(GetForeveralMonname(foreveral, True), DexMacros.Type1)) + fvltext:
                            text_size 30
                            text_color "#000000fe"
                            text_hover_color "#ff00fffe"
                            sensitive interact
                            if "fvls" not in currloadout: # If FVLs are added for the first time, create the key for them
                                action SetDict(currloadout, "fvls", [foreveral])
                            elif foreveral in currloadout["fvls"]:
                                action RemoveFromSet(currloadout["fvls"], foreveral)
                            elif len(currloadout["fvls"]) < GetMaxForeveralCount():
                                action AddToSet(currloadout["fvls"], foreveral)
                            else:
                                action [AddToSet(currloadout["fvls"], foreveral), RemoveFromSet(currloadout["fvls"], currloadout["fvls"][0])]
                            if heldtooltip:
                                tooltip heldtooltip
            elif loadoutscreen == "Forms": # Handle form selection - should be unlocked only after at least one diveral or no FVLs are selected, and show the appropriate diverals
                grid 2 10:
                    transpose True
                    for mon, fvl in loadoutformslist:
                        $ foreveralcount += 1
                        textbutton GetTypeEssentiarum(pokedexlookup(mon, DexMacros.Type1)) + If("forme" in currloadout and mon == currloadout["forme"], "{color=#22bb33fe}" + pokedexlookup(mon, DexMacros.Forme).replace(" Form", "") + "{/color}" , pokedexlookup(mon, DexMacros.Forme).replace(" Form", "")) + " (" + str(math.floor(pokedexlookup(mon, DexMacros.Total) / 5)) + ")":
                            text_color "#000000fe"
                            text_hover_color "#ff00fffe"
                            text_size 30
                            sensitive interact
                            if "forme" not in currloadout:
                                action SetDict(currloadout, "forme", mon)
                            elif mon == currloadout["forme"]:
                                action SetDict(currloadout, "forme", None)
                            else:
                                action SetDict(currloadout, "forme", mon)
                    for x in range(20 - foreveralcount):
                        null
    if (not renpy.get_screen("foreveralinfo")):
        hbox:
            xalign .5 yalign 0.68
            textbutton "<-" action Function(ForeveralPageIncrement, -1) xminimum 200 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" sensitive interact
            textbutton "Back" action Hide() xminimum 200 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" sensitive interact
            textbutton "->" action Function(ForeveralPageIncrement, 1) xminimum 200 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" sensitive interact
    
    if GetFocusRect("loadouts_drop"): # Handle dropdown for FVL loadouts. This should be last to ensure proper layering. Tooltips right under.
        dismiss action ClearFocus("loadouts_drop")

        nearrect:
            focus "loadouts_drop"
            
            frame:
                xsize 277 + 18 * (len(pika_loadouts) > 10)
                ymaximum 50 * min(len(pika_loadouts), 10)
                modal True
                background None
                padding (0, 0)

                has viewport:
                    if len(pika_loadouts) > 10: # Ensure scrolling only when needed (i.e. too many loadouts)
                        scrollbars "vertical"
                        arrowkeys True
                        pagekeys True
                        mousewheel True
                        vscrollbar_base_bar "#fff"
                        vscrollbar_thumb "#363436"
                        vscrollbar_top_bar "#e7e6e7"
                        vscrollbar_bottom_bar "#e7e6e7"
                    
                    has vbox:
                        for ky in pika_loadouts.keys():
                            textbutton ky:
                                text_font "fonts/pkmndp.ttf"
                                style "menu_choice_button"
                                xysize (277, 50)
                                text_color "#000000fe"
                                text_hover_color "#ff00fffe"
                                text_size 30
                                text_xalign .5
                                action [SetLocalVariable("chosen_loadout", ky), SetLocalVariable("currloadout", copy.deepcopy(pika_loadouts[ky])), ClearFocus("loadouts_drop")]

    if GetFocusRect("loadouts_sortdrop"): # Sorting the selection lists
        dismiss action ClearFocus("loadouts_sortdrop")

        nearrect:
            focus "loadouts_sortdrop"
            
            frame:
                xsize 224
                ymaximum 50 * min(len(loadoutsortdict[loadoutscreen]), 10)
                modal True
                background None
                padding (0, 0)

                has viewport:
                    if len(loadoutsortdict[loadoutscreen]) > 10: # Ensure scrolling only when needed (i.e. too many loadouts) - this will never be necessary
                        scrollbars "vertical"
                        arrowkeys True
                        pagekeys True
                        mousewheel True
                        vscrollbar_base_bar "#fff"
                        vscrollbar_thumb "#363436"
                        vscrollbar_top_bar "#e7e6e7"
                        vscrollbar_bottom_bar "#e7e6e7"
                    
                    has vbox:
                        for ky in loadoutsortdict[loadoutscreen]:
                            textbutton ky:
                                text_font "fonts/pkmndp.ttf"
                                style "menu_choice_button"
                                xysize (224, 50)
                                text_color "#000000fe"
                                text_hover_color "#ff00fffe"
                                text_size 30
                                text_xalign .5
                                action [SetVariable("loadoutsort", ky), ClearFocus("loadouts_sortdrop")]

    if GetFocusRect("rename_loadout"): # Renaming interface
        dismiss action [ClearFocus("rename_loadout"), SetLocalVariable("renameconfirm", False), SetLocalVariable("newrename", "")] # In addition to clearing the focus, reset popup-specific variables to their initial values

        nearrect:
            focus "rename_loadout"

            frame:
                xsize 277
                yfill False
                modal True

                default renameconfirm = False

                vbox:
                    if not renameconfirm:
                        text "Are you sure you want to rename this loadout?" yalign .5
                        
                        hbox:
                            textbutton "Yes":
                                text_font "fonts/pkmndp.ttf"
                                style "menu_choice_button"
                                xysize (132, 50) # Normalized for size, rounded down
                                text_color "#000000fe"
                                text_hover_color "#ff00fffe"
                                text_size 30
                                text_xalign .5
                                action SetLocalVariable("renameconfirm", True)
                            textbutton "No":
                                text_font "fonts/pkmndp.ttf"
                                style "menu_choice_button"
                                xysize (132, 50)
                                text_color "#000000fe"
                                text_hover_color "#ff00fffe"
                                text_size 30
                                text_xalign .5
                                action ClearFocus("rename_loadout")
                            
                    else:
                        key "input_enter" action NullAction() # This is to ensure the input can't close the rect prematurely by pressing enter.

                        text "Please type a new name below:" yalign .5

                        default newrename = ""

                        input:
                            exclude "{}[[]%<>"
                            length 12
                            value LocalVariableInputValue("newrename")

                        textbutton "Confirm":
                            text_font "fonts/pkmndp.ttf"
                            style "menu_choice_button"
                            xysize (265, 50) # 12px less than width for margins
                            text_color If(newrename and newrename not in pika_loadouts, "#000000fe", "#888888fe")
                            if newrename and newrename not in pika_loadouts: # Make button visibly non-interactive if newrename is already a loadout name. Clicking away achieves the same practical result as renaming the loadout to itself.
                                text_hover_color "#ff00fffe"
                            text_size 30
                            text_xalign .5
                            action If(newrename and newrename not in pika_loadouts, [Function(RenamePikachuLoadout, chosen_loadout, newrename), SetLocalVariable("chosen_loadout", newrename), SetLocalVariable("newrename", ""), ClearFocus("rename_loadout")], NullAction())

    if GetFocusRect("del_loadout"): # Deleting interface
        dismiss action ClearFocus("del_loadout")

        nearrect:
            focus "del_loadout"

            frame:
                xsize 277
                yfill False
                modal True

                vbox:
                    text "Are you sure you want to delete this loadout?" yalign .5
                    
                    hbox:
                        textbutton "Yes":
                            text_font "fonts/pkmndp.ttf"
                            style "menu_choice_button"
                            xysize (132, 50) # Normalized for size, rounded down
                            text_color "#000000fe"
                            text_hover_color "#ff00fffe"
                            text_size 30
                            text_xalign .5
                            action [Function(DeletePikachuLoadout, chosen_loadout), SetLocalVariable("chosen_loadout", None), SetLocalVariable("currloadout", {"moves":[]}), ClearFocus("del_loadout")]
                        textbutton "No":
                            text_font "fonts/pkmndp.ttf"
                            style "menu_choice_button"
                            xysize (132, 50)
                            text_color "#000000fe"
                            text_hover_color "#ff00fffe"
                            text_size 30
                            text_xalign .5
                            action ClearFocus("del_loadout")
    
    if GetFocusRect("loadouts_save"): # Saving interface
        dismiss action [ClearFocus("loadouts_save"), SetLocalVariable("saveas", False), SetLocalVariable("newname", "")] # In addition to clearing the focus, reset popup-specific variables to their initial values

        nearrect:
            focus "loadouts_save"
            prefer_top True

            frame:
                xsize 300
                yfill False
                modal True

                default saveas = False

                vbox:
                    if chosen_loadout and not saveas: # Only show this if editing an existing loadout, before deciding to save to a new name. Otherwise show the input.
                        text "Save to {b}current{/b} loadout or as a {b}new{/b} loadout?" yalign .5
                        
                        hbox:
                            textbutton "New":
                                text_font "fonts/pkmndp.ttf"
                                style "menu_choice_button"
                                xysize (144, 50) # Normalized for size, rounded down
                                text_color "#000000fe"
                                text_hover_color "#ff00fffe"
                                text_size 30
                                text_xalign .5
                                action SetLocalVariable("saveas", True)
                            textbutton "Current":
                                text_font "fonts/pkmndp.ttf"
                                style "menu_choice_button"
                                xysize (144, 50)
                                text_color "#000000fe"
                                text_hover_color "#ff00fffe"
                                text_size 30
                                text_xalign .5
                                action [Function(SavePikachuLoadout, chosen_loadout, currloadout), SetLocalVariable("saveas", False), SetLocalVariable("newname", ""), ClearFocus("loadouts_save")]
                    
                    else:
                        key "input_enter" action NullAction() # This is to ensure the input can't close the rect prematurely by pressing enter.

                        text "Please type a name below:" yalign .5

                        default newname = ""

                        input:
                            exclude "{}[[]%<>"
                            length 12
                            value LocalVariableInputValue("newname")

                        textbutton If(newname not in pika_loadouts, "Confirm", "Overwrite?"): # The button text serves as a warning if you're about to overwrite a loadout
                            text_font "fonts/pkmndp.ttf"
                            style "menu_choice_button"
                            xysize (288, 50) # 12px less than frame width to account for margins and symmetry, 6px on each side
                            text_color If(newname, "#000000fe", "#888888fe")
                            if newname: # Make button visibly non-interactive if newname is empty. Clicking away does nothing, as one might expect.
                                text_hover_color "#ff00fffe"
                            text_size 30
                            text_xalign .5
                            action If(newname, [Function(SavePikachuLoadout, newname, currloadout), SetLocalVariable("chosen_loadout", newname), SetLocalVariable("saveas", False), SetLocalVariable("newname", ""), ClearFocus("loadouts_save")], NullAction())

    if GetTooltip():
        nearrect:
            focus "tooltip"
            prefer_top True

            frame:
                xanchor 0.0
                xpos .5

                if isinstance(GetTooltip(), (list, tuple)): # If this is a LL tooltip
                    vbox:
                        for category, specific, increase in GetTooltip():
                            if (not isinstance(specific, str)):
                                $ specific = pokedexlookup(specific, DexMacros.Name)
                            text specific + ": " + str(math.floor(increase)) size 30 color "#000" font "fonts/pkmndp.ttf"
                elif isinstance(GetTooltip(), str): # If text-based tooltip
                    text GetTooltip() size 30 color "#000" font "fonts/pkmndp.ttf"
                elif isinstance(GetTooltip(), dict): # FVLs equipped on boxed mons
                    vbox:
                        text "Cannot apply loadout."
                        for heldfvl, mon in GetTooltip().items():
                            if not mon[1]:
                                text "The {b}" + heldfvl + "{/b} is currently held by " + mon[0].GetNickname() + " in the PC."

init python:
    def ForeveralPageIncrement(value):
        global foreveralpage
        if (foreveralinvsubmenu == "Foreverals"):
            if (value == -1):
                if (foreveralpage > 0):
                    foreveralpage -= 1
                else:
                    foreveralpage = math.ceil(len(foreveraldex) / 20 - 1)
            else:
                if (foreveralpage < math.ceil(len(foreveraldex) / 20) - 1):
                    foreveralpage += 1
                else: 
                    foreveralpage = 0
        elif (foreveralinvsubmenu == "Moves"):
            if (value == -1):
                if (foreveralpage > 0):
                    foreveralpage -= 1
                else:
                    foreveralpage = math.ceil(len(AllMoves()) / 30 - 1)
            else:
                if (foreveralpage < math.ceil(len(AllMoves()) / 30) - 1):
                    foreveralpage += 1
                else:
                    foreveralpage = 0
        elif (foreveralinvsubmenu == "Forms"):
            if (value == -1):
                if (foreveralpage > 0):
                    foreveralpage -= 1
                else:
                    foreveralpage = math.ceil(len(SortedForms()) / 20 - 1)
            else:
                if (foreveralpage < math.ceil(len(SortedForms()) / 20) - 1):
                    foreveralpage += 1
                else:
                    foreveralpage = 0
        elif (foreveralinvsubmenu == "Loadouts"): # Loadout stuff needs separate handling per each case.
            if (loadoutscreen == "Foreverals"):
                if (value == -1):
                    if (foreveralpage > 0):
                        foreveralpage -= 1
                    else:
                        foreveralpage = math.ceil(len(claimedforeverals) / 20 - 1)
                else:
                    if (foreveralpage < math.ceil(len(claimedforeverals) / 20) - 1):
                        foreveralpage += 1
                    else:
                        foreveralpage = 0
            elif (loadoutscreen == "Moves"):
                if (value == -1):
                    if (foreveralpage > 0):
                        foreveralpage -= 1
                    else:
                        foreveralpage = math.ceil(len(AllMoves()) / 30 - 1)
                else:
                    if (foreveralpage < math.ceil(len(AllMoves()) / 30) - 1):
                        foreveralpage += 1
                    else:
                        foreveralpage = 0
            elif (loadoutscreen == "Forms"):
                if (value == -1):
                    if (foreveralpage > 0):
                        foreveralpage -= 1
                    else:
                        foreveralpage = math.ceil(len(SortedLoadoutForms()) / 20 - 1)
                else:
                    if (foreveralpage < math.ceil(len(SortedLoadoutForms()) / 20) - 1):
                        foreveralpage += 1
                    else:
                        foreveralpage = 0

init python:
    def InvokeUseItem(partymon = None):
        renpy.invoke_in_new_context(UseItem, partymon)

screen fieldinventory(pickitem = False):
    zorder 10
    modal True
    hbox:
        align (0.5, 0.05)
        textbutton "Healing" action SetVariable("invpage", "Healing") xmaximum 224 text_size 40 text_xalign 0.5 text_color ("#000" if invpage != "Healing" else "#ff0000") text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
        textbutton "Evo Items" action SetVariable("invpage", "Evo Items") xmaximum 224 text_size 40 text_xalign 0.5 text_color ("#000" if invpage != "Evo Items" else "#ff0000") text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
        textbutton "Poké Balls" action SetVariable("invpage", "Poké Balls") xmaximum 224 text_size 40 text_xalign 0.5 text_color ("#000" if invpage != "Poké Balls" else "#ff0000") text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
        textbutton "Battle Items" action SetVariable("invpage", "Battle Items") xmaximum 223 text_size 40 text_xalign 0.5 text_color ("#000" if invpage != "Battle Items" else "#ff0000") text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
        textbutton "Misc." action SetVariable("invpage", "Misc.") xmaximum 223 text_size 40 text_xalign 0.5 text_color ("#000" if invpage != "Misc." else "#ff0000") text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
    frame:
        xpos 0.209
        yanchor 0.0
        ypos 0.124
        xysize (1118, 545)
        background "images/GUI/readback.webp"
        if (invoverwrite == None):
            $ itemcount = 0
            grid 4 10:
                transpose True
                for item in inventory.keys():
                    if (invpage == InventoryCategory(item)):
                        $ itemcount += 1
                        textbutton ("" if inventory[item] == 1 else str(inventory[item]) + "x ") + item text_color "#2b2b2b" action ([SetVariable("activeitem", item), SetVariable("invoverwrite", "What would you like to do with the {}?".format(item))] if not pickitem else Return(item)) text_hover_color "#fff"
                for x in range(40 - itemcount):
                    null
        elif (invoverwrite[:4] == "What"):
            vbox:
                xfill True
                spacing 30
                null
                text invoverwrite color "#000000" size 40 xalign 0.5
                if (not TrainerItem(activeitem)):
                    textbutton ">Give to a Pokémon." action SetVariable("invoverwrite", "Which Pokémon do you want to give the {} to?".format(activeitem)) xsize 250 text_xalign .5 text_size 30 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"        
                    textbutton ">Use on a Pokémon." action SetVariable("invoverwrite", "Which Pokémon do you want to use the {} on?".format(activeitem)) xsize 250 text_xalign .5 text_size 30 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"        
                else:
                    textbutton ">Use the item." action Function(InvokeUseItem) xsize 250 text_xalign .5 text_size 30 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
                textbutton "Nevermind." action [SetVariable("activeitem", None), SetVariable("invoverwrite", None)] xsize 250 xfill True text_xalign .5 text_size 30 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"        
        elif (invoverwrite[:5] == "Which"):
            vbox:
                xfill True
                spacing 30
                null
                text invoverwrite color "#000000" size 40 xalign 0.5
                null
                grid 3 2:
                    spacing 20
                    xalign 0.5
                    for partymon in playerparty:
                        textbutton partymon.GetNickname() action (Function(InvokeUseItem, partymon) if "use" in invoverwrite else Function(GiveItem, partymon)) xsize 200 text_xalign .5 text_size 30 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"        
                    for x in range(6 - len(playerparty)):
                        null
                textbutton "Nevermind." action [SetVariable("activeitem", None), SetVariable("invoverwrite", None)] xsize 250 xfill True text_xalign .5 text_size 30 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"        
        
        elif ("is already holding" in invoverwrite):
            vbox:
                xfill True
                spacing 30
                null
                text invoverwrite color "#000000" size 40 xalign 0.5
                null
                textbutton "Yes, swap items." action Function(SwapItems) xsize 250 text_xalign .5 text_size 30 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"        
                textbutton "Nevermind." action [SetVariable("activeitem", None), SetVariable("invoverwrite", None)] xsize 250 xfill True text_xalign .5 text_size 30 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
        else:
            vbox:
                xfill True
                spacing 30
                null
                text invoverwrite color "#000000" size 40 xalign 0.5
                null
                textbutton "Confirm" action [SetVariable("activemon", None), SetVariable("activeitem", None), SetVariable("invoverwrite", None)] xsize 250 text_xalign .5 text_size 30 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"        

    textbutton "Back" action ([SetVariable("activemon", None), SetVariable("activeitem", None), SetVariable("invoverwrite", None), (Hide("fieldinventory") if not pickitem else Return("back"))]) xminimum 200 text_xalign .5 xalign .5 yalign 0.68 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"

screen mondata(pkmn, showtip = True):
    zorder 10
    add "gui/button/choice_idle_background.webp" xalign .5 xzoom 1.5 yzoom 15
    $ gendersymbol = ""
    if (pkmn.GetGender() == Genders.Male):
        $ gendersymbol = "{font=fonts/pkmndp.ttf}{color=#2b00ff}♂{/font}"
    elif (pkmn.GetGender() == Genders.Female):
        $ gendersymbol = "{font=fonts/pkmndp.ttf}{color=#ff00b7}♀{/font}"
    add pkmn.GetImage() yalign 0.25 xalign 0.5 alpha 0.2
    $ nick = pkmn.GetNickname()
    text nick + " " + gendersymbol + ("" if nick == pokedexlookup(pkmn.GetId(), DexMacros.Name) else "\n{size=30}{color=#000}(" + pokedexlookup(pkmn.GetId(), DexMacros.Name) + "){/size}") xminimum 550 xpos .1 yalign .05 size (70 if len(nick) < 10 else 50)
    text "Lv. " + str(pkmn.GetLevel()) xminimum 550 xalign .5 ypos .03 size 50
    if (pkmn in playerparty + box):
        text "(Level Cap: " + str(math.floor(pkmn.GetLevelCap())) + ", Exp for Lv: " + str(pkmn.GetMaxLevel()) + ")" xalign .5 ypos .09 size 40
    
    $ typestring = ""
    for element in pkmn.GetTypes():
        if (typestring != ""):
            $ typestring += "{color=#fff}/{/color}"
        $ typestring += "{color=" + GetTypeColor(element) + "}" + element + "{/color}"

    text typestring yalign .07 size 70 xanchor 1.0 xpos 0.9 outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]
    
    $ showll = usingliberationlimit and pkmn.Id == 25.2

    hbox:
        xalign .5
        ypos .15
        if (showll):
            vbox:
                $ ll = GetLiberationLimit()
                text "{b}Liberation Limit" xminimum 300 xalign .5 size 40
                for category, specific, increase in ll[1]:
                    if (not isinstance(specific, str)):
                        $ specific = pokedexlookup(specific, DexMacros.Name)
                    if (specific not in category):
                        text category + " (" + specific.replace("♂", "{font=fonts/pkmndp.ttf}♂{/font}").replace("♀", "{font=fonts/pkmndp.ttf}♀{/font}") +"): " + str(math.floor(increase)) xminimum 300 size 40
                    else:
                        text category + ": " +  str(math.floor(increase)) xminimum 300 size 40
                text "{b}Total:{/b} " + str(math.floor(ll[0])) + "/" + str(math.floor(maxliberationlimit))
            null width 50

        grid 4 7:
            text "{b}Stat" xminimum 300 size 40
            text "{b}Value" xminimum 300 xalign .5 size 40
            text "{b}EVs" xminimum 300 xalign .5 size 40
            text "{b}IVs" xminimum 300 xalign .5 size 40
            text "HP" xminimum 300 size 40
            text str(max(pkmn.GetHealth(), pkmn.GetCaught())) + "/" + str(pkmn.GetStat(Stats.Health)) xminimum 300 xalign .5 size 40
            text str(pkmn.GetEV(Stats.Health)) + "/255" xminimum 300 xalign .5 size 40
            text str(pkmn.GetIV(Stats.Health)) + "/31" xminimum 300 xalign .5 size 40
            $ attackbonus = NatureToBonus(pkmn.GetNature(), Stats.Attack)
            text "Attack" xminimum 300 size 40 color ("#000" if attackbonus == 1 else ("#ff0000" if attackbonus == 1.1 else "#0000ff"))
            text str(pkmn.GetStat(Stats.Attack, triggerAbilities=False, absolute=True)) xminimum 300 xalign .5 size 40
            text str(pkmn.GetEV(Stats.Attack)) + "/255" xminimum 300 xalign .5 size 40
            text str(pkmn.GetIV(Stats.Attack)) + "/31" xminimum 300 xalign .5 size 40
            $ defensebonus = NatureToBonus(pkmn.GetNature(), Stats.Defense)
            text "Defense" xminimum 300 size 40 color ("#000" if defensebonus == 1 else ("#ff0000" if defensebonus == 1.1 else "#0000ff"))
            text str(pkmn.GetStat(Stats.Defense, triggerAbilities=False, absolute=True)) xminimum 300 xalign .5 size 40
            text str(pkmn.GetEV(Stats.Defense)) + "/255" xminimum 300 xalign .5 size 40
            text str(pkmn.GetIV(Stats.Defense)) + "/31" xminimum 300 xalign .5 size 40
            $ specialattackbonus = NatureToBonus(pkmn.GetNature(), Stats.SpecialAttack)
            text "Special Attack" xminimum 300 size 40 color ("#000" if specialattackbonus == 1 else ("#ff0000" if specialattackbonus == 1.1 else "#0000ff"))
            text str(pkmn.GetStat(Stats.SpecialAttack, triggerAbilities=False, absolute=True)) xminimum 300 xalign .5 size 40
            text str(pkmn.GetEV(Stats.SpecialAttack)) + "/255" xminimum 300 xalign .5 size 40
            text str(pkmn.GetIV(Stats.SpecialAttack)) + "/31" xminimum 300 xalign .5 size 40
            $ specialdefensebonus = NatureToBonus(pkmn.GetNature(), Stats.SpecialDefense)
            text "Special Defense" xminimum 300 size 40 color ("#000" if specialdefensebonus == 1 else ("#ff0000" if specialdefensebonus == 1.1 else "#0000ff"))
            text str(pkmn.GetStat(Stats.SpecialDefense, triggerAbilities=False, absolute=True)) xminimum 300 xalign .5 size 40
            text str(pkmn.GetEV(Stats.SpecialDefense)) + "/255" xminimum 300 xalign .5 size 40
            text str(pkmn.GetIV(Stats.SpecialDefense)) + "/31" xminimum 300 xalign .5 size 40
            $ speedbonus = NatureToBonus(pkmn.GetNature(), Stats.Speed)
            text "Speed" xminimum 300 size 40 color ("#000" if speedbonus == 1 else ("#ff0000" if speedbonus == 1.1 else "#0000ff"))
            text str(pkmn.GetStat(Stats.Speed, triggerAbilities=False, absolute=True)) xminimum 300 xalign .5 size 40
            text str(pkmn.GetEV(Stats.Speed)) + "/255" xminimum 300 xalign .5 size 40
            text str(pkmn.GetIV(Stats.Speed)) + "/31" xminimum 300 xalign .5 size 40

    if (pkmn in playerparty + box):
        text "EXP: " + str(math.floor(pkmn.GetExperience())) + ", To Next Level: " + str(math.floor(pkmn.CalculateAllExperienceNeededForLevel(pkmn.GetMaxLevel() + 1) - pkmn.GetExperience()) + 1) size 40 yalign .43 xalign 0.5

    $ status = "None"
    if (pkmn.GetHealthPercentage() <= 0.0 and pkmn.GetCaught() <= 0):
        $ status = "Fainted"
    else:
        for statustype in nonvolatiles:
            if (pkmn.HasStatus(statustype)):
                $ status = statustype
    
    hbox:
        yalign .48
        xalign .5
        spacing 30
        text "Status: " + status.title() xminimum 300 size 40 yalign .5
        if (pkmn.GetItem() == None):
            text "Item: None" xminimum 300 size 40 yalign .5
        else:
            textbutton "Item: " + pkmn.GetItem():
                xminimum 300 text_xalign .5
                ymaximum 60 text_size 40 text_color "#000" text_hover_color "#f0f" 
                style "menu_choice_button" text_font "fonts/pkmndp.ttf" 
                action [Function(RemoveItem, pkmn)]

        text "Nature: " + NatureToString(pkmn.GetNature()) xminimum 300 size 40 yalign .5
        $ fvlability = False
        for fvl in pkmn.GetForeverals():
            if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.AddAbility):
                $ fvlability = True
        if (not fvlability):
            text "Ability: " + pkmn.GetAbility() xminimum 300 size 40 yalign .5
        else:
            hbox:
                text "Ability: " xminimum 300 size 40 yalign .5
                vbox:
                    text pkmn.GetAbility() xminimum 300 size 40 yalign .5
                    for fvl in pkmn.GetForeverals():
                        if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.AddAbility):
                            for ability in lookupforeveraldata(fvl, FVLMacros.FVLTypeData):
                                text "(" + ability + ")" xminimum 300 size 40 yalign .5
        if (usingforeverals):
            if (pkmn.GetForeverals() == []):
                text "Foreveral: None" xminimum 300 size 40 yalign .5
            else:
                textbutton "Foreveral: " + pkmn.GetForeverals()[0]:
                    xminimum 300 text_xalign .5
                    ymaximum 60 text_size 40 text_color "#000" text_hover_color "#f0f" 
                    style "menu_choice_button" text_font "fonts/pkmndp.ttf" 
                    action [Function(RemoveForeverals, pkmn)]

    if (showtip):
        text ("(Click on {} to lock screen and switch Pokémon.)" if pkmnlocked == -1 else "{{u}}(Click on {} to unlock screen, or click on another Pokémon to switch positions.){{/u}}").format(pkmn.GetNickname()) xminimum 300 xalign .5 yalign .55 size 40

init python:
    def SwapMovePositions(pkmn, pos1, pos2):
        global pkmnlockedmove
        try:
            pkmn.Moves[pos1], pkmn.Moves[pos2] = pkmn.Moves[pos2], pkmn.Moves[pos1]
            pkmnlockedmove = pos2
        except:
            pkmnlockedmove = -1

screen nonbattlemoves(pkmn, newmove=False, tooltips = True):
    zorder 11
    grid len(pkmn.GetMoves()) 1:
        xalign .5
        yalign (.65 if tooltips else .55)

        $ move_index = 0
        for move in pkmn.Moves:
            textbutton move.Name: 
                action ([Hide("movedata", Dissolve(0.5)), Hide("nonbattlemoves", Dissolve(0.5)), Return(move)] if newmove else [(SetVariable("pkmnlockedmove", (-1 if pkmnlockedmove != -1 else move_index)) if pkmnlockedmove == -1 or pkmnlockedmove == move_index else Function(SwapMovePositions, pkmn, pkmnlockedmove, move_index), renpy.restart_interaction)]) 
                xminimum 350 text_xalign .5 text_size 60 
                text_color ("#FF0000" if move_index == pkmnlockedmove else "#000")
                text_hover_color ("#FF9900" if move_index == pkmnlockedmove else "#f0f")
                style "menu_choice_button" 
                text_font "fonts/pkmndp.ttf"
                hovered ([Show("movedata", Dissolve(0.5), move), Hide("mondata", Dissolve(0.5))] if tooltips else NullAction())
                unhovered ([Hide("movedata", Dissolve(0.5)), Show("mondata", Dissolve(0.5), pkmn)] if tooltips else NullAction())
            $ move_index += 1

## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

init:
    image clouds: #daytime
        "BG/sky_base.webp"
        subpixel True
        block:
            xalign 0.0
            linear 60.0 xpos -1.0
            repeat
                
    python:
        style.mm_root.background = "clouds"

screen main_menu():
    
    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"
        
    # The main menu buttons.
    
    imagemap:
        ground "imagemaps/Title_Still_Ground.webp"
        idle "imagemaps/Title_Still_Idle.webp"
        hover "imagemaps/Title_Still_Hover.webp"
        
        hotspot (41, 455, 192, 55) action Start()
        hotspot (41, 391, 203, 55) action Show("load", transition=dissolve)
        hotspot (41, 588, 174, 52) action Show("navigation", transition=dissolve)
        hotspot (41, 647, 203, 52) action Show("help", transition=dissolve)
        hotspot (41, 711, 102, 52) action Quit(confirm=False)
        hotspot (41, 991, 173, 44) action Jump("credits")

    text "Version " + config.version xalign 1.0 yalign 1.01 color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]

screen abortbattletester:
    textbutton "Leave Battle Tester" text_xalign 0.5 align (0.5, 1.0) action MainMenu(confirm=False) text_font "fonts/pkmndp.ttf" style "menu_choice_button" xmaximum 300

## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu():
    
    modal True
    
    imagemap:
        ground "imagemaps/Menu_Ground.webp"
        idle "imagemaps/Menu_Idle.webp"
        hover "imagemaps/Menu_Hover.webp"
        
        hotspot (26, 194, 146, 40) action [Hide("game_menu", transition=dissolve), SetVariable("yvalue", 1.0), ShowMenu("text_history", transition=dissolve)]
        
        hotspot (25, 306, 169, 50) action Show("navigation", transition=dissolve)
        hotspot (25, 368, 101, 50) action Show("save", transition=dissolve)
        hotspot (25, 427, 101, 50) action Show("load", transition=dissolve)
        
        hotspot (25, 607, 147, 50) action [Hide("game_menu", transition=dissolve), Show("traits", transition=dissolve), Hide("database", transition=dissolve)]
        hotspot (25, 545, 148, 50) action [Hide("game_menu", transition=dissolve), Hide("traits", transition=dissolve), Show("database", transition=dissolve)]
        hotspot (24, 782, 223, 43) action MainMenu()
        
        hotspot (101, 1018, 86, 31) action [Hide("game_menu", transition=dissolve), Return()]

## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

init python:
    def CanSave():
        return not inbattle and not InDungeon()

    def RenameFile(slot):
        global save_name
        if (inbattle):
            renpy.invoke_in_new_context(renpy.say, None, "You cannot save in the middle of a battle!")
            return
        elif (InDungeon()):
            renpy.invoke_in_new_context(renpy.say, None, "You cannot save in a dungeon!")
            return
        else:
            savename = FileSaveName(slot)
            if ("{size=30}" in savename and "{/size}" in savename 
            and "Afternoon" not in savename
            and "Early Morning" not in savename
            and "Morning" not in savename
            and "Evening" not in savename
            and "Noon" not in savename
            and "Night" not in savename
            and "Midnight" not in savename):
                savename = savename[savename.index("{size=30}") + len("{size=30}"):savename.index("{/size}")]
            else:
                savename = timeOfDay

            save_name = renpy.invoke_in_new_context(renpy.input, "Type a name for the save.", default=savename, length=16, exclude="{}[[]%<>",)
            if (save_name.strip() == ""):
                save_name = timeOfDay
            hours = math.floor(int(renpy.get_game_runtime()) / 3600)
            minutes = math.floor((int(renpy.get_game_runtime()) / 60) % 60)
            if (minutes < 10):
                minutes = "0" + str(minutes)
            save_name = "{}, {} {}\n{}\n{}".format(getRWDay(0), str(calendar.month_name[calDate.month]), getRDay(0), "{size=30}" + save_name + "{/size}", "Playtime: " + str(hours) + ":" + str(minutes))

screen save():
    modal True
    imagemap:
        ground "imagemaps/Save_Load_Ground.webp"
        idle "imagemaps/Save_Load_Idle.webp"
        hover "imagemaps/Save_Load_Hover.webp"
        selected_idle "imagemaps/Save_Load_Selected.webp"
        selected_hover "imagemaps/Save_Load_Hover.webp"
        hotspot (6, 997, 38, 38) clicked If(int(persistent._file_page) > 1, SetVariable("persistent._file_page", str(max(1, int(persistent._file_page) - 5))))
        
        hotspot (53, 997, 38, 38) clicked If(int(persistent._file_page) > 1, SetVariable("persistent._file_page", str(int(persistent._file_page) - 1)))
        # hotspot (33, 953, 38, 38) clicked FilePage(1)
        # hotspot (82, 953, 38, 38) clicked FilePage(2)
        # hotspot (132, 953, 38, 38) clicked FilePage(3)
        # hotspot (181, 953, 38, 38) clicked FilePage(4)
        # hotspot (230, 953, 38, 38) clicked FilePage(5)
        hotspot (207, 997, 38, 38) clicked FilePage(int(persistent._file_page) + 1), SetVariable("persistent._file_page", str(int(persistent._file_page) + 1))
        hotspot (254, 997, 38, 38) clicked FilePage(int(persistent._file_page) + 5), SetVariable("persistent._file_page", str(int(persistent._file_page) + 5))

        hotspot (20, 84, 261, 150) clicked ([Function(RenameFile, 1), FileSave(1)] if CanSave() else Function(RenameFile, 1)):
            use load_save_slot(number=1)
        hotspot (20, 255, 261, 150) clicked ([Function(RenameFile, 2), FileSave(2)] if CanSave() else Function(RenameFile, 2)):
            use load_save_slot(number=2)
        hotspot (20, 435, 261, 150) clicked ([Function(RenameFile, 3), FileSave(3)] if CanSave() else Function(RenameFile, 3)):
            use load_save_slot(number=3)
        hotspot (20, 615, 261, 150) clicked ([Function(RenameFile, 4), FileSave(4)] if CanSave() else Function(RenameFile, 4)):
            use load_save_slot(number=4)
        hotspot (20, 794, 261, 150) clicked ([Function(RenameFile, 5), FileSave(5)] if CanSave() else Function(RenameFile, 5)):
            use load_save_slot(number=5)

        hotspot (101, 1018, 86, 31) action Hide("save", transition=dissolve), Hide("extra_load")
        $ str_page = "Pg. " + persistent._file_page
        text str_page xpos 200 ypos 1042

        hotspot (33, 1040, 40, 40) action ToggleScreen("extra_load")

    imagebutton:
        idle "GUI/SavePage_Idle.webp"
        hover "GUI/SavePage_Hover.webp"
        selected_idle "GUI/SavePage_Hover.webp"
        action FilePage(max(1, int(persistent._file_page) - 2))
        xpos 33
        ypos 953
    text ("{font=fonts/pkmndp.ttf}{size=25}{color=#000}" + str(max(1, int(persistent._file_page) - 2)) + "{/color}{/size}{/font}") xpos 33+20 ypos 953+22 xalign 0.5 yalign 0.5 xanchor 0.5 yanchor 0.5

    imagebutton:
        idle "GUI/SavePage_Idle.webp"
        hover "GUI/SavePage_Hover.webp"
        selected_idle "GUI/SavePage_Hover.webp"
        action FilePage(max(2, int(persistent._file_page) - 1))
        xpos 82
        ypos 953
    text ("{font=fonts/pkmndp.ttf}{size=25}{color=#000}" + str(max(2, int(persistent._file_page) - 1)) + "{/color}{/size}{/font}") xpos 82+20 ypos 953+22 xalign 0.5 yalign 0.5 xanchor 0.5 yanchor 0.5

    imagebutton:
        idle "GUI/SavePage_Idle.webp"
        hover "GUI/SavePage_Hover.webp"
        selected_idle "GUI/SavePage_Hover.webp"
        action FilePage(max(3, int(persistent._file_page)))
        xpos 132
        ypos 953
    text ("{font=fonts/pkmndp.ttf}{size=25}{color=#000}" + str(max(3, int(persistent._file_page))) + "{/color}{/size}{/font}") xpos 132+20 ypos 953+22 xalign 0.5 yalign 0.5 xanchor 0.5 yanchor 0.5

    imagebutton:
        idle "GUI/SavePage_Idle.webp"
        hover "GUI/SavePage_Hover.webp"
        action FilePage(max(4, int(persistent._file_page) + 1))
        xpos 181
        ypos 953
    text ("{font=fonts/pkmndp.ttf}{size=25}{color=#000}" + str(max(4, int(persistent._file_page) + 1)) + "{/color}{/size}{/font}") xpos 181+20 ypos 953+22 xalign 0.5 yalign 0.5 xanchor 0.5 yanchor 0.5

    imagebutton:
        idle "GUI/SavePage_Idle.webp"
        hover "GUI/SavePage_Hover.webp"
        action FilePage(max(5, int(persistent._file_page) + 2))
        xpos 230
        ypos 953
    text ("{font=fonts/pkmndp.ttf}{size=25}{color=#000}" + str(max(5, int(persistent._file_page) + 2)) + "{/color}{/size}{/font}") xpos 230+20 ypos 953+22 xalign 0.5 yalign 0.5 xanchor 0.5 yanchor 0.5

screen load():
    
    modal True

    #This ensures that any other menu screen is replaced.
    #tag menu

    imagemap:
        ground "imagemaps/Save_Load_Ground.webp"
        idle "imagemaps/Save_Load_Idle.webp"
        hover "imagemaps/Save_Load_Hover.webp"
        selected_idle "imagemaps/Save_Load_Selected.webp"
        selected_hover "imagemaps/Save_Load_Hover.webp"
        cache False
        hotspot (6, 997, 38, 38) clicked If(int(persistent._file_page) > 1, SetVariable("persistent._file_page", str(max(1, int(persistent._file_page) - 5))))
        
        hotspot (53, 997, 38, 38) clicked If(int(persistent._file_page) > 1, SetVariable("persistent._file_page", str(int(persistent._file_page) - 1)))
        # hotspot (33, 953, 38, 38) clicked FilePage(1)
        # hotspot (82, 953, 38, 38) clicked FilePage(2)
        # hotspot (132, 953, 38, 38) clicked FilePage(3)
        # hotspot (181, 953, 38, 38) clicked FilePage(4)
        # hotspot (230, 953, 38, 38) clicked FilePage(5)
        hotspot (207, 997, 38, 38) clicked FilePage(int(persistent._file_page) + 1), SetVariable("persistent._file_page", str(int(persistent._file_page) + 1))
        hotspot (254, 997, 38, 38) clicked FilePage(int(persistent._file_page) + 5), SetVariable("persistent._file_page", str(int(persistent._file_page) + 5))

        hotspot (20, 84, 261, 150) clicked FileLoad(1):
            use load_save_slot(number=1)
        hotspot (20, 255, 261, 150) clicked FileLoad(2):
            use load_save_slot(number=2)
        hotspot (20, 435, 261, 150) clicked FileLoad(3):
            use load_save_slot(number=3)
        hotspot (20, 615, 261, 150) clicked FileLoad(4):
            use load_save_slot(number=4)
        hotspot (20, 794, 261, 150) clicked FileLoad(5):
            use load_save_slot(number=5)
            
        hotspot (101, 1018, 86, 31) action Hide("load", transition=dissolve), Hide("extra_load")
        $ str_page = "Pg. " + persistent._file_page
        text str_page xpos 200 ypos 1042

        hotspot (33, 1040, 40, 40) action ToggleScreen("extra_load")

    imagebutton:
        idle "GUI/SavePage_Idle.webp"
        hover "GUI/SavePage_Hover.webp"
        selected_idle "GUI/SavePage_Hover.webp"
        action FilePage(max(1, int(persistent._file_page) - 2))
        xpos 33
        ypos 953
    text ("{font=fonts/pkmndp.ttf}{size=25}{color=#000}" + str(max(1, int(persistent._file_page) - 2)) + "{/color}{/size}{/font}") xpos 33+20 ypos 953+22 xalign 0.5 yalign 0.5 xanchor 0.5 yanchor 0.5

    imagebutton:
        idle "GUI/SavePage_Idle.webp"
        hover "GUI/SavePage_Hover.webp"
        selected_idle "GUI/SavePage_Hover.webp"
        action FilePage(max(2, int(persistent._file_page) - 1))
        xpos 82
        ypos 953
    text ("{font=fonts/pkmndp.ttf}{size=25}{color=#000}" + str(max(2, int(persistent._file_page) - 1)) + "{/color}{/size}{/font}") xpos 82+20 ypos 953+22 xalign 0.5 yalign 0.5 xanchor 0.5 yanchor 0.5

    imagebutton:
        idle "GUI/SavePage_Idle.webp"
        hover "GUI/SavePage_Hover.webp"
        selected_idle "GUI/SavePage_Hover.webp"
        action FilePage(max(3, int(persistent._file_page)))
        xpos 132
        ypos 953
    text ("{font=fonts/pkmndp.ttf}{size=25}{color=#000}" + str(max(3, int(persistent._file_page))) + "{/color}{/size}{/font}") xpos 132+20 ypos 953+22 xalign 0.5 yalign 0.5 xanchor 0.5 yanchor 0.5

    imagebutton:
        idle "GUI/SavePage_Idle.webp"
        hover "GUI/SavePage_Hover.webp"
        action FilePage(max(4, int(persistent._file_page) + 1))
        xpos 181
        ypos 953
    text ("{font=fonts/pkmndp.ttf}{size=25}{color=#000}" + str(max(4, int(persistent._file_page) + 1)) + "{/color}{/size}{/font}") xpos 181+20 ypos 953+22 xalign 0.5 yalign 0.5 xanchor 0.5 yanchor 0.5

    imagebutton:
        idle "GUI/SavePage_Idle.webp"
        hover "GUI/SavePage_Hover.webp"
        action FilePage(max(5, int(persistent._file_page) + 2))
        xpos 230
        ypos 953
    text ("{font=fonts/pkmndp.ttf}{size=25}{color=#000}" + str(max(5, int(persistent._file_page) + 2)) + "{/color}{/size}{/font}") xpos 230+20 ypos 953+22 xalign 0.5 yalign 0.5 xanchor 0.5 yanchor 0.5


screen extra_load:
    frame:
        #xysize (300,200) 
        style "menu_choice_button"
        xpos 0.38
        ypos 0.9
        #xmaximum .4
        vbox:
            hbox:
                text " {size=+2}Travel to page:"
                button:
                    id "input_1"
                    xysize (250,25)
                    action NullAction()
                    add Input(hover_color="#f0f0f0",size=40, color="#000", default=int(persistent._file_page), changed=file_page_func, length=10, button=renpy.get_widget("extra_load","input_1")) yalign 0 
            hbox:
                textbutton " {b}Enter{/b}" style "buttonhover" action Hide("extra_load")

init python:
    def file_page_func(newstring):
        if newstring.isdigit() and int(newstring) > 0:
            persistent._file_page = newstring

screen load_save_slot:
    if (len(FileSaveName(number)) < 11):
        $ file_text = "{color=#ffffff}{font=fonts/pkmndp.ttf}{size=22}%s\n\n\n%s{/size}{/font}{/color}" % (FileSaveName(number),
                            FileTime(number, format='%m/%d/%Y - %H:%M', empty=_("Empty Slot"))) 
    else:
        $ file_text = "{color=#ffffff}{font=fonts/pkmndp.ttf}{size=22}%s\n\n%s{/size}{/font}{/color}" % (FileSaveName(number),
                            FileTime(number, format='%m/%d/%Y - %H:%M', empty=_("Empty Slot"))) 

    add FileScreenshot(number) xpos 1 ypos 2 zoom 0.7
    text file_text xpos 10 ypos 10 outlines [ (3, "#000") ] line_spacing 0.75 line_leading 1.0 kerning 2.0
    
    key "save_delete" action FileDelete(number)

##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu

    # Include the navigation.
    use navigation

## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help: 
    
    modal True
    
    imagemap:
        ground "GFX/Help1.webp"        
        hotspot (0, 0, 1920, 1080) action Hide("help", transition=dissolve)

################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    modal True

    if message == layout.QUIT:
        $ pkmnlocked = -1
        $ pkmnlockedmove = -1
        $ renpy.hide_screen("foreveralinventory")
        $ renpy.hide_screen("fieldinventory")
        $ renpy.hide_screen("partyviewerpopup")

        $ renpy.hide_screen("partyviewer")
        $ renpy.hide_screen("mondata")
        $ renpy.hide_screen("nonbattlemoves")

        imagemap:
            ground 'GUI/Quit_Idle.webp'
            hover 'GUI/Quit_Hover.webp'
       
            hotspot (834, 510, 130, 76) action yes_action
            hotspot (978, 510, 130, 76) action no_action
            
    elif message == layout.OVERWRITE_SAVE:
        imagemap:
            ground 'GUI/Overwrite_Idle.webp'
            hover 'GUI/Overwrite_Hover.webp'
       
            hotspot (834, 510, 130, 76) action yes_action
            hotspot (978, 510, 130, 76) action no_action
    
    elif message == layout.DELETE_SAVE:
        imagemap:
            ground 'GUI/Delete_Save_Idle.webp'
            hover 'GUI/Delete_Save_Hover.webp'
       
            hotspot (834, 510, 130, 76) action yes_action
            hotspot (978, 510, 130, 76) action no_action
        
    elif message == layout.LOADING:
        imagemap:
            ground 'GUI/Load_Idle.webp'
            hover 'GUI/Load_Hover.webp'
       
            hotspot (834, 510, 130, 76) action yes_action
            hotspot (978, 510, 130, 76) action no_action
        
    elif message == layout.MAIN_MENU:
        imagemap:
            ground 'GUI/Return_Menu_Idle.webp'
            hover 'GUI/Return_Menu_Hover.webp'
       
            hotspot (834, 510, 130, 76) action yes_action
            hotspot (978, 510, 130, 76) action no_action

    else:
        window:
            style "gm_root"

        frame:
            style_prefix "confirm"

            xfill True
            xmargin 50
            ypadding 25
            yalign .25

            vbox:
                xfill True
                spacing 25

                text _(message):
                    xalign 0.5

                hbox:
                    spacing 100
                    xalign .5
                    textbutton _("Yes") action yes_action
                    textbutton _("No") action no_action


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.webp", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "fonts/DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.webp", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.webp"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.webp"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.webp"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.webp"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.webp"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.webp"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.webp"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.webp", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.webp", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.webp", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.webp", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.webp", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.webp"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.webp", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.webp"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900

##USER-CREATED SCREENS

init python:
    def ForeveralDataNewContext(foreveral, inbattle):
        renpy.call_in_new_context("foreveraldata", foreveral, inbattle)

    def TrainingDataNewContext(mon, inbattle):
        renpy.call_in_new_context("trainingdata", mon, inbattle)

screen battleui():
    if (not hidebattleui):
        for i, playermon in enumerate(FriendlyBattlers()):
            $ originali = i
            $ i = len(FriendlyBattlers()) - i - 1
            $ isprojecting = playermon.GetFormeOverride() != None and playermon.Id == 25.2 and playermon.GetId() != 25.2

            if (playermon.Id != 25.2):
                add playermon.GetImage() at (hovering if originali == BattlerIndex and len(FriendlyBattlers()) > 1 else None) xpos 250 * i + 200 * (len(FriendlyBattlers()) == 1) + 100 * (len(FriendlyBattlers()) == 2) * i + 50 * (len(FriendlyBattlers()) == 2) yanchor 1.0 ypos 1.0 - .15 * i xzoom -1.0 / (i * 0.25 + 1) yzoom 1.0 / (i * 0.25 + 1) zoom (0.8 if isprojecting else 1.0)
            else:
                $ xposition = (-75 if FriendlyBattlers().index(playermon) == 0 else 0) + (75 if isprojecting else 0) + 250 * i + 200 * (len(FriendlyBattlers()) == 1) + 100 * (len(FriendlyBattlers()) == 2) * i + 50 * (len(FriendlyBattlers()) == 2)
                add "Pokemon/25.2-4.webp" at (hovering if originali == BattlerIndex and len(FriendlyBattlers()) > 1 else None) xpos xposition yanchor 1.0 ypos 1.0 - .15 * i xzoom -1.0 / (i * 0.25 + 1) yzoom 1.0 / (i * 0.25 + 1) zoom (0.8 if isprojecting else 1.0) 
                add "Pokemon/25.2-1.webp" at (hovering if originali == BattlerIndex and len(FriendlyBattlers()) > 1 else None) matrixcolor TintMatrix(GetLiberaColor()) xpos xposition yanchor 1.0 ypos 1.0 - .15 * i xzoom -1.0 / (i * 0.25 + 1) yzoom 1.0 / (i * 0.25 + 1) zoom (0.8 if isprojecting else 1.0)

                if (isprojecting):
                    add "Pokemon/{}.webp".format(playermon.GetId()) at (hoverfloat) matrixcolor SaturationMatrix(2.0) alpha 0.8 xpos xposition - 150 ypos -0.05 + 1.0 - .15 * i xzoom -1.0 / (i * 0.25 + 1) yzoom 1.0 / (i * 0.25 + 1)

                add "Pokemon/25.2-3.webp" at (hovering if originali == BattlerIndex and len(FriendlyBattlers()) > 1 else None) xpos xposition yanchor 1.0 ypos 1.0 - .15 * i xzoom -1.0 / (i * 0.25 + 1) yzoom 1.0 / (i * 0.25 + 1) zoom (0.8 if isprojecting else 1.0)
                add "Pokemon/25.2-5.webp" at (hovering if originali == BattlerIndex and len(FriendlyBattlers()) > 1 else None) matrixcolor TintMatrix(GetLiberaColor()) xpos xposition yanchor 1.0 ypos 1.0 - .15 * i xzoom -1.0 / (i * 0.25 + 1) yzoom 1.0 / (i * 0.25 + 1) zoom (0.8 if isprojecting else 1.0)
                add "Pokemon/25.2-2.webp" at (hovering if originali == BattlerIndex and len(FriendlyBattlers()) > 1 else None) matrixcolor TintMatrix(GetLiberaColor(False)) xpos xposition yanchor 1.0 ypos 1.0 - .15 * i xzoom -1.0 / (i * 0.25 + 1) yzoom 1.0 / (i * 0.25 + 1) zoom (0.8 if isprojecting else 1.0)

        for i, enemymon in enumerate(EnemyBattlers()):
            $ i = len(EnemyBattlers()) - i - 1
            add enemymon.GetImage() xanchor 1.0 xpos 1920 - (250 * i + 200 * (len(EnemyBattlers()) == 1) + 100 * (len(EnemyBattlers()) == 2) * i + 50 * (len(EnemyBattlers()) == 2)) yanchor 1.0 ypos 1.0 - .15 * i zoom 1.0 / (i * 0.25 + 1)

        for i, trainer in enumerate(FriendlyTrainers()):
            if (trainer.HasMons() and not trainer.GetIsPokemon()):
                for j, mon in enumerate(trainer.GetTeam()):
                    add "GUI/pixelpokeball_indicator.webp" xpos 380 + j * 40 ypos 20 + 40 * i matrixcolor SaturationMatrix(mon.GetHealth() > 0)

        for i, trainer in enumerate(EnemyTrainers()):
            if (trainer.HasMons() and not trainer.GetIsPokemon()):
                for j, mon in enumerate(trainer.GetTeam()):
                    add "GUI/pixelpokeball_indicator.webp" xpos 1920 - 420 - j * 40 xzoom -1 ypos 20 + 40 * i matrixcolor SaturationMatrix(mon.GetHealth() > 0)

        $ ylevels = 0
        if (CurrentWeather != None):
            add "GUI/frame_pbattlestat.webp" ypos 8 + 40 * ylevels at Transform(yzoom=0.3) xalign 0.5
            text CurrentWeather[0].title() ypos 18 + 40 * ylevels xalign 0.5
            $ ylevels = 1

        for effect in BattlefieldEffects:
            add "GUI/frame_pbattlestat.webp" ypos 8 + 40 * ylevels at Transform(yzoom=0.3) xalign 0.5
            text effect ypos 18 + 40 * ylevels xalign 0.5
            $ ylevels += 1

        #left side, your stuff
        $ ylevels = 0
        for i, mon in enumerate(FriendlyBattlers()):
            $ health = mon.GetHealth()
            $ maxhealth = mon.GetStat(Stats.Health)
            $ ybuffer = i * 106 + ylevels * 35
            add "GUI/frame_pbattlestat.webp" ypos ybuffer yzoom .8 xanchor .03

            text mon.GetNickname() pos (17, 30 + ybuffer) size 35 - (1.5 * max(0, (count_non_brace_chars(mon.GetNickname()) - 10)))

            hbox:
                xanchor 1.0 pos (350, 30 + ybuffer)
                ypos ybuffer + 30
                #xpos 0.115

                if (mon.GetForeverals() != []):
                    imagebutton:
                        idle Transform("gfx/foreveralpixel.webp", matrixcolor=InvertMatrix(0), zoom=1)
                        hover Transform("gfx/foreveralpixel.webp", matrixcolor=InvertMatrix(), zoom=1)
                        action (Hide("stats"), Show("foreveralinfo", foreveral=mon.GetForeverals()[0], transition=dissolve) if not explainingf else NullAction())

                if (mon.GetTrained() != []):
                    imagebutton:
                        idle Transform("gfx/trainedlogo.webp", matrixcolor=InvertMatrix(0), zoom=0.75)
                        hover Transform("gfx/trainedlogo.webp", matrixcolor=InvertMatrix(), zoom=0.75)
                        action (Hide("stats"), Function(TrainingDataNewContext, mon, True) if not explainingf else NullAction())

                $ gendersymbol = ""
                if (mon.GetGender() == Genders.Male):
                    $ gendersymbol = "{font=fonts/pkmndp.ttf}{color=#2b00ff}♂{/font}"
                elif (mon.GetGender() == Genders.Female):
                    $ gendersymbol = "{font=fonts/pkmndp.ttf}{color=#ff00b7}♀{/font}"
                text " " + gendersymbol + "{color=#000000}Lv." + str(mon.GetLevel()) 

            $ barcolor = "#00b612"
            if (health / maxhealth <= 0.25):
                $ barcolor = "#ff0000"
            elif (health / maxhealth <= 0.5):
                $ barcolor = "#fff700"

            bar range maxhealth value health pos (12, 65 + ybuffer) xmaximum 335 right_bar "#fff" left_bar barcolor
            text (str(health) + "/" + str(maxhealth)) color "#fff" pos (17, 65 + ybuffer) outlines [ (absolute(5), "#000", absolute(0), absolute(0)) ]

            if (mon.IsTerad()):
                add "GUI/frame_pbattlestat.webp" xanchor .1 ypos (i + 1) * 105 + 10 + ylevels * 35 at Transform(yzoom=0.3)
                text "{gradient2=3-#f00-#0f0-11-#0f0-#00f-11-#00f-#f00-11}Terastallized {/gradient2}" + mon.GetTeraType() xpos 15 ypos (i + 1) * 105 + 10 + ylevels * 35 + 8
                $ ylevels += 1

            for status in mon.GetStatusKeys():
                if (status[0] != "."):
                    add "GUI/frame_pbattlestat.webp" xanchor .1 ypos (i + 1) * 105 + 10 + ylevels * 35 at Transform(yzoom=0.3)
                    if (status in ["diveralized", "mega evolved", "minigigamaxed"]):
                        text "{gradient2=3-#f00-#0f0-11-#0f0-#00f-11-#00f-#f00-11}" + status.title() + "{/gradient2}" xpos 15 ypos (i + 1) * 105 + 10 + ylevels * 35 + 8
                    else:
                        text status.title() xpos 15 ypos (i + 1) * 105 + 10 + ylevels * 35 + 8
                    $ ylevels += 1

            for change in mon.GetAllStatChanges().keys():
                add "GUI/frame_pbattlestat.webp" xanchor .1 ypos (i + 1) * 105 + 10 + ylevels * 35 at Transform(yzoom=0.3)
                text StatToString(change) xpos 15 ypos (i + 1) * 105 + 10 + ylevels * 35 + 8
                text ("+" if mon.GetStatChanges(change) > 0 else "" ) + str(mon.GetStatChanges(change)) xpos 325 xanchor 1.0 ypos (i + 1) * 105 + 10 + ylevels * 35 + 8
                $ ylevels += 1
        
        for effect in FriendlyEffects:
            $ yceiling = len(FriendlyBattlers()) * 105 + 10 + ylevels * 35
            add "GUI/frame_pbattlestat.webp" xanchor .03 ypos yceiling at Transform(yzoom=0.3)
            text effect.title() xpos 15 ypos yceiling + 8
            $ ylevels += 1

        #right side, their stuff
        if (uifuckery) < 2:
            $ ylevels = 0
            for i, mon in enumerate(EnemyBattlers()):
                $ health = mon.GetHealth()
                $ maxhealth = mon.GetStat(Stats.Health)
                $ ybuffer = i * 106 + ylevels * 35
                add "GUI/frame_pbattlestat.webp" ypos ybuffer yzoom .8 xanchor .97 xpos 1.0
                text mon.GetNickname() pos (1920-345, 30 + ybuffer) size 35 - (1.5 * max(0, (count_non_brace_chars(mon.GetNickname()) - 10)))
                
                hbox:
                    xanchor 1.0 pos (1920-10, 30 + ybuffer)

                    if (mon.GetForeverals() != []):
                        imagebutton:
                            idle Transform("gfx/foreveralpixel.webp", matrixcolor=InvertMatrix(0), zoom=1)
                            hover Transform("gfx/foreveralpixel.webp", matrixcolor=InvertMatrix(), zoom=1)
                            action (Hide("stats"), Show("foreveralinfo", foreveral=mon.GetForeverals()[0], transition=dissolve) if not explainingf else NullAction())

                    if (mon.GetTrained() != []):
                        imagebutton:
                            idle Transform("gfx/trainedlogo.webp", matrixcolor=InvertMatrix(0), zoom=0.75)
                            hover Transform("gfx/trainedlogo.webp", matrixcolor=InvertMatrix(), zoom=0.75)
                            action (Hide("stats"), Function(TrainingDataNewContext, mon, True) if not explainingf else NullAction())

                    $ gendersymbol = ""
                    if (mon.GetGender() == Genders.Male):
                        $ gendersymbol = "{font=fonts/pkmndp.ttf}{color=#2b00ff}♂{/font}"
                    elif (mon.GetGender() == Genders.Female):
                        $ gendersymbol = "{font=fonts/pkmndp.ttf}{color=#ff00b7}♀{/font}"
                    text " " + gendersymbol + "{color=#000000}Lv." + str(mon.GetLevel())

                $ barcolor = "#00b612"
                if (health / maxhealth <= 0.25):
                    $ barcolor = "#ff0000"
                elif (health / maxhealth <= 0.5):
                    $ barcolor = "#fff700"

                bar range maxhealth value health pos (1920-12, 65 + ybuffer) xmaximum 335 right_bar barcolor left_bar "#fff" bar_invert True xanchor 1.0
                #text (str(health) + "/" + str(maxhealth)) color "#fff" pos (1920-17, 65 + ybuffer) outlines [ (absolute(5), "#000", absolute(0), absolute(0)) ] xanchor 1.0

                if (mon.IsTerad()):
                    add "GUI/frame_pbattlestat.webp" xanchor .9 xpos 1.0 ypos (i + 1) * 105 + 10 + ylevels * 35 at Transform(yzoom=0.3)
                    text "{gradient2=3-#f00-#0f0-11-#0f0-#00f-11-#00f-#f00-11}Terastallized {/gradient2}" + mon.GetTeraType() xpos 1920-15 xanchor 1.0 ypos (i + 1) * 105 + 10 + ylevels * 35 + 8
                    $ ylevels += 1

                for status in mon.GetStatusKeys():
                    if (status[0] != "."):
                        add "GUI/frame_pbattlestat.webp" xanchor .9 xpos 1.0 ypos (i + 1) * 105 + 10 + ylevels * 35 at Transform(yzoom=0.3)
                        if (status in ["diveralized", "mega evolved", "minigigamaxed"]):
                            text "{gradient2=3-#f00-#0f0-11-#0f0-#00f-11-#00f-#f00-11}" + status.title() + "{/gradient2}" xpos 1920-15 xanchor 1.0 ypos (i + 1) * 105 + 10 + ylevels * 35 + 8
                        else:
                            text status.title() xpos 1920-15 xanchor 1.0 ypos (i + 1) * 105 + 10 + ylevels * 35 + 8
                        $ ylevels += 1

                for change in mon.GetAllStatChanges().keys():
                    add "GUI/frame_pbattlestat.webp" xanchor .9 xpos 1.0 ypos (i + 1) * 105 + 10 + ylevels * 35 at Transform(yzoom=0.3)
                    text StatToString(change) xpos 1920-325 ypos (i + 1) * 105 + 10 + ylevels * 35 + 8
                    text ("+" if mon.GetStatChanges(change) > 0 else "" ) + str(mon.GetStatChanges(change)) xpos 1920-15 xanchor 1.0 ypos (i + 1) * 105 + 10 + ylevels * 35 + 8
                    $ ylevels += 1
            
            for effect in EnemyEffects:
                $ yceiling = len(EnemyBattlers()) * 105 + 10 + ylevels * 35
                add "GUI/frame_pbattlestat.webp" xanchor .97 xpos 1.0 ypos yceiling at Transform(yzoom=0.3)
                text effect.title() xpos 1920-15 xanchor 1.0 ypos yceiling + 8
                $ ylevels += 1

define longtext = "{gradient2=3-#f00-#0f0-11-#0f0-#00f-11-#00f-#f00-11}{size=60} Terastallize! {/size}{/gradient2}"
define shorttext = "Terastallize"
define longlibtext = "{gradient2=3-#f00-#0f0-11-#0f0-#00f-11-#00f-#f00-11}{size=60} Liberize! {/size}{/gradient2}"
define longdivtext = "{gradient2=3-#f00-#0f0-11-#0f0-#00f-11-#00f-#f00-11}{size=60} Diveralize! {/size}{/gradient2}"
define longmegatext = "{gradient2=3-#f00-#0f0-11-#0f0-#00f-11-#00f-#f00-11}{size=60} Mega Evolve! {/size}{/gradient2}"
define longminigigatext = "{gradient2=3-#f00-#0f0-11-#0f0-#00f-11-#00f-#f00-11}{size=60} Minigigamax! {/size}{/gradient2}"

screen battle(currentMon=None):
    if (not renpy.get_screen("battleui")):
        use battleui()

    $ showteraoption = False
    if (currentMon != None and "Tera Orb" in inventory.keys()):
        $ showteraoption = True
        for allymon in currentMon.GetTrainer().GetTeam():
            if (allymon.IsTerad() and (allymon != currentMon or allymon == currentMon and allymon.GetTerastallized() != Turn)):
                $ showteraoption = False

    $ hasdiveral = False
    if (currentMon != None):
        for fvl in currentMon.GetForeverals():
            if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.FormSwap):
                $ hasdiveral = True

    vbox:
        xalign .5
        yalign .5
        if (currentMon != None):
            if (showteraoption):
                textbutton "[terabuttontext]" action Return(value='tera') text_font "fonts/pkmndp.ttf" xmaximum 360 text_xalign .5 text_size 60 text_color "#4b4b4b" top_padding 17 style "menu_choice_button" hovered SetVariable('terabuttontext', (longtext if not currentMon.IsTerad() else shorttext)) unhovered SetVariable('terabuttontext', (shorttext if not currentMon.IsTerad() else longtext))
            if (movesdodged.count("Dragon Pulse") >= 4 and dawnbattle):
                textbutton "[longlibtext]" action Return(value='lib') text_font "fonts/pkmndp.ttf" xmaximum 360 text_xalign .5 text_size 60 text_color "#4b4b4b" top_padding 17 style "menu_choice_button"
            if (hasdiveral and GimmickCost > 0):
                textbutton "[longdivtext]" action Return(value='div') text_font "fonts/pkmndp.ttf" xmaximum 360 text_xalign .5 text_size 60 text_color "#4b4b4b" top_padding 17 style "menu_choice_button"
            if (currentMon.GetItem() != None and currentMon.GetItem()[-3:] == "ite" and (correctmegaitems[currentMon.GetItem()] == pokedexlookup(currentMon.Id, DexMacros.Name) or currentMon.Id == 25.2) and GimmickCost > 0):
                textbutton "[longmegatext]" action Return(value='mega') text_font "fonts/pkmndp.ttf" xmaximum 360 text_xalign .5 text_size 60 text_color "#4b4b4b" top_padding 17 style "menu_choice_button"
            if (currentMon.GetItem() != None and "Minigiga" in currentMon.GetItem() and (correctmegaitems[currentMon.GetItem()] == pokedexlookup(currentMon.Id, DexMacros.Name) or currentMon.Id == 25.2) and GimmickCost > 0):
                textbutton "[longminigigatext]" action Return(value='giga') text_font "fonts/pkmndp.ttf" xmaximum 360 text_xalign .5 text_size 60 text_color "#4b4b4b" top_padding 17 style "menu_choice_button"
        textbutton " Fight " action Return(value='fight') text_font "fonts/pkmndp.ttf" xmaximum 270 text_xalign .5 text_size 60 text_color "#9b5151" text_hover_color "#d03b3d" style "menu_choice_button"
        textbutton "  Bag  " action Return(value='bag') text_font "fonts/pkmndp.ttf" xmaximum 270 text_xalign .5 text_size 60 text_color "#826926" text_hover_color "#c98022" style "menu_choice_button"
        textbutton "Pokémon" action Return(value='pokemon') text_font "fonts/pkmndp.ttf" xmaximum 270 text_xalign .5 text_size 60 text_color "#437128" text_hover_color "#459426" style "menu_choice_button"
        textbutton "  Run  " action Return(value='run') text_font "fonts/pkmndp.ttf" xmaximum 270 text_xalign .5 text_size 60 text_color "#295272" text_hover_color "#256799" style "menu_choice_button"
        if (len(CurrentActions) > 0):
            textbutton " Back " action Return(value='back') text_font "fonts/pkmndp.ttf" xmaximum 270 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button"

screen choosetarget(move, attacker):
    if (not renpy.get_screen("battleui")):
        use battleui()

    if (move != Range.Any):
        if (isinstance(move, int)):
            $ range = move
        else:
            $ range = GetMoveRange(move)


        $ groupselection = False
        if (range == Range.AllAdjacentFoes
            or range == Range.AllAdjacent
            or range == Range.AllAllies 
            or range == Range.AllFoes
            or range == Range.All
            or range == Range.AllAlliesAndSelf):
            $ groupselection = True
    else:
        $ groupselection = False
        $ range = Range.Any

    if (groupselection):
        vbox:
            align (0.5, 0.5)
            xanchor 1.0
            for trainer in FriendlyTrainers():
                for mon in trainer.GetLead():
                    if (mon != None):
                        textbutton "" xminimum 350 yminimum 90 background Color("#d200ab" if mon in GetTargets(attacker, range) else "#d200ac00")
        vbox:
            align (0.5, 0.5)
            xanchor 0.0
            for trainer in EnemyTrainers():
                for mon in trainer.GetLead():
                    if (mon != None):
                        textbutton "" xminimum 350 yminimum 90 background Color("#d200ab" if mon in GetTargets(attacker, range) else "#d200ac00")
    vbox:
        align (0.5, 0.5)
        xanchor 1.0
        for trainer in FriendlyTrainers():
            for mon in trainer.GetLead():
                $ istarget = mon in GetTargets(attacker, range)
                $ returnable = GetTargets(attacker, range) if groupselection else [mon]
                if (mon != None):
                    textbutton mon.GetNickname() action (Return(returnable) if istarget else NullAction()) text_font "fonts/pkmndp.ttf" xmaximum 340 text_xalign .5 text_size (60 if count_non_brace_chars(mon.GetNickname()) < 11 else 50 - (2 * (count_non_brace_chars(mon.GetNickname()) - 10))) text_color ("#000" if istarget else "#616161") style "menu_choice_button"

    vbox:
        align (0.5, 0.5)
        xanchor 0.0
        for trainer in EnemyTrainers():
            for mon in trainer.GetLead():
                $ istarget = mon in GetTargets(attacker, range)
                $ returnable = GetTargets(attacker, range) if groupselection else [mon] 
                if (mon != None):
                    textbutton mon.GetNickname() action (Return(returnable) if istarget else NullAction()) text_font "fonts/pkmndp.ttf" xmaximum 340 text_xalign .5 text_size (60 if count_non_brace_chars(mon.GetNickname()) < 11 else 50 - (2 * (count_non_brace_chars(mon.GetNickname()) - 10))) text_color ("#000" if istarget else "#616161") style "menu_choice_button"
    grid 1 1:
        xalign .5
        ypos .658
        textbutton "Back" action Return(value='back') xminimum 400 text_xalign .5 xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"


screen moves(mon):
    if (not renpy.get_screen("battleui")):
        use battleui()
    $ Moves = mon.GetMoves()
    $ NumMoves = len(Moves)

    if (HasValidMoves(mon)):
        grid 2 2:
            xalign .5
            ypos .5

            for i, move in enumerate(Moves):
                $ hovercolor = "#f0f"
                $ bodycolor = "#000"
                $ name = move.Name
                if (not MoveValid(mon, move)):
                    $ hovercolor = "#000"
                    $ bodycolor = "#616161"
                    $ name = "{s} " + name + " {/s}"
                textbutton name action [Hide("movedata", Dissolve(0.5)), Return(value=i)] xminimum 400 text_xalign .5 text_size 60 - max(len(name) - 12, 0) text_color bodycolor text_hover_color hovercolor style "menu_choice_button" text_font "fonts/pkmndp.ttf" hovered Show("movedata", Dissolve(0.5), move) unhovered Hide("movedata", Dissolve(0.5))
                
            for i in range(4 - NumMoves):
                null
    else:
        grid 1 1:
            xalign .5
            ypos .5
            textbutton "Struggle" action [Hide("movedata", Dissolve(0.5)), Return(value='Struggle')] xminimum 400 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" hovered Show("movedata", Dissolve(0.5), struggle) unhovered Hide("movedata", Dissolve(0.5))  

    grid 1 1:
        xalign .5
        ypos .658
        textbutton "Back" action Return(value='back') xminimum 400 text_xalign .5 xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"

screen movedata(move):
    add Frame("GUI/character_frame.webp", 10, 10, xmaximum=1150, ymaximum=350, xalign=.5, ypos=.07)
    if (uifuckery < 1):
        text move.Name xminimum 550 xalign .5 yalign .1 size 100
        grid 3 2:
            xalign .5
            ypos .2
            text "Category: " + move.Category xminimum 300 xalign .5 size 40
            text "Type: " + "{color=" + GetTypeColor(move.Type) + "}" + move.Type xminimum 300 xalign .5 size 40
            text "PP: " + str(move.PP) + "/" + str(move.MaxPP) xminimum 300 xalign .5 size 40
            if (move.Power in [0, "-", "", "—"]):
                text "Power: ---" xminimum 300 xalign .5 size 40
            else:
                text "Power: " + str(move.Power) xminimum 300 xalign .5 size 40
            if (usingliberationlimit):
                text "Limit: " + str(GetCalculatedMovePower(move.Name)) xminimum 300 xalign .5 size 40
            else:
                null
            if (str(move.Accuracy) in ["-", "", "—"]):
                text "Accuracy: Can't miss" xminimum 300 xalign .5 size 40
            elif (move.Accuracy in ["?", "~"]):
                text "Accuracy: Variable" xminimum 300 xalign .5 size 40
            else:
                text "Accuracy: " + str(math.floor(move.Accuracy * 100)) + "%" xminimum 300 xalign .5 size 40
        
    frame:
        background "red_eyeshine_blank"
        yalign .31
        xminimum 300 
        xalign .5
        has hbox:
            xmaximum 1100
            spacing 5
            box_wrap True
            text move.Description size 40

screen stats(pkmn):
    if (not renpy.get_screen("battleui")):
        use battleui()
    
    if (uifuckery < 3): 
        add "gui/button/choice_idle_background.webp" xalign .5 xzoom 1.5 yzoom 15
        $ gendersymbol = ""
        if (pkmn.GetGender() == Genders.Male):
            $ gendersymbol = "{font=fonts/pkmndp.ttf}{color=#2b00ff}♂{/font}"
        elif (pkmn.GetGender() == Genders.Female):
            $ gendersymbol = "{font=fonts/pkmndp.ttf}{color=#ff00b7}♀{/font}"
        add pkmn.GetImage() yalign 0.25 xalign 0.5 alpha 0.2
        $ nick = pkmn.GetNickname()
        text nick + " " + gendersymbol + ("" if nick == pokedexlookup(pkmn.GetId(), DexMacros.Name) else "\n{size=30}{color=#000}(" + pokedexlookup(pkmn.GetId(), DexMacros.Name) + "){/size}") xminimum 550 xpos .1 yalign .05 size (70 if len(nick) < 10 else 50)
        text "Lv. " + str(pkmn.GetLevel()) xminimum 550 xalign .5 ypos .03 size 50
        if (pkmn in playerparty + box):
            text "(Level Cap: " + str(math.floor(pkmn.GetLevelCap())) + ", Exp for Lv: " + str(pkmn.GetMaxLevel()) + ")" xalign .5 ypos .09 size 40
        
        $ typestring = ""
        for element in pkmn.GetTypes():
            if (typestring != ""):
                $ typestring += "{color=#fff}/{/color}"
            $ typestring += "{color=" + GetTypeColor(element) + "}" + element + "{/color}"

        text typestring yalign .07 size 70 xanchor 1.0 xpos 0.85 outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]
        
        grid 4 7:
            xalign .5
            ypos .15
            text "{b}Stat" xminimum 300 size 40
            text "{b}Value" xminimum 300 xalign .5 size 40
            text "{b}EVs" xminimum 300 xalign .5 size 40
            text "{b}IVs" xminimum 300 xalign .5 size 40
            text "HP" xminimum 300 size 40
            text str(max(pkmn.GetHealth(), pkmn.GetCaught())) + "/" + str(pkmn.GetStat(Stats.Health)) xminimum 300 xalign .5 size 40
            text str(pkmn.GetEV(Stats.Health)) + "/255" xminimum 300 xalign .5 size 40
            text str(pkmn.GetIV(Stats.Health)) + "/31" xminimum 300 xalign .5 size 40
            $ attackbonus = NatureToBonus(pkmn.GetNature(), Stats.Attack)
            text "Attack" xminimum 300 size 40 color ("#000" if attackbonus == 1 else ("#ff0000" if attackbonus == 1.1 else "#0000ff"))
            text str(pkmn.GetStat(Stats.Attack, triggerAbilities=False, absolute=True)) xminimum 300 xalign .5 size 40
            text str(pkmn.GetEV(Stats.Attack)) + "/255" xminimum 300 xalign .5 size 40
            text str(pkmn.GetIV(Stats.Attack)) + "/31" xminimum 300 xalign .5 size 40
            $ defensebonus = NatureToBonus(pkmn.GetNature(), Stats.Defense)
            text "Defense" xminimum 300 size 40 color ("#000" if defensebonus == 1 else ("#ff0000" if defensebonus == 1.1 else "#0000ff"))
            text str(pkmn.GetStat(Stats.Defense, triggerAbilities=False, absolute=True)) xminimum 300 xalign .5 size 40
            text str(pkmn.GetEV(Stats.Defense)) + "/255" xminimum 300 xalign .5 size 40
            text str(pkmn.GetIV(Stats.Defense)) + "/31" xminimum 300 xalign .5 size 40
            $ specialattackbonus = NatureToBonus(pkmn.GetNature(), Stats.SpecialAttack)
            text "Special Attack" xminimum 300 size 40 color ("#000" if specialattackbonus == 1 else ("#ff0000" if specialattackbonus == 1.1 else "#0000ff"))
            text str(pkmn.GetStat(Stats.SpecialAttack, triggerAbilities=False, absolute=True)) xminimum 300 xalign .5 size 40
            text str(pkmn.GetEV(Stats.SpecialAttack)) + "/255" xminimum 300 xalign .5 size 40
            text str(pkmn.GetIV(Stats.SpecialAttack)) + "/31" xminimum 300 xalign .5 size 40
            $ specialdefensebonus = NatureToBonus(pkmn.GetNature(), Stats.SpecialDefense)
            text "Special Defense" xminimum 300 size 40 color ("#000" if specialdefensebonus == 1 else ("#ff0000" if specialdefensebonus == 1.1 else "#0000ff"))
            text str(pkmn.GetStat(Stats.SpecialDefense, triggerAbilities=False, absolute=True)) xminimum 300 xalign .5 size 40
            text str(pkmn.GetEV(Stats.SpecialDefense)) + "/255" xminimum 300 xalign .5 size 40
            text str(pkmn.GetIV(Stats.SpecialDefense)) + "/31" xminimum 300 xalign .5 size 40
            $ speedbonus = NatureToBonus(pkmn.GetNature(), Stats.Speed)
            text "Speed" xminimum 300 size 40 color ("#000" if speedbonus == 1 else ("#ff0000" if speedbonus == 1.1 else "#0000ff"))
            text str(pkmn.GetStat(Stats.Speed, triggerAbilities=False, absolute=True)) xminimum 300 xalign .5 size 40
            text str(pkmn.GetEV(Stats.Speed)) + "/255" xminimum 300 xalign .5 size 40
            text str(pkmn.GetIV(Stats.Speed)) + "/31" xminimum 300 xalign .5 size 40

        if (pkmn in playerparty + box):
            text "EXP: " + str(math.floor(pkmn.GetExperience())) + ", To Next Level: " + str(math.floor(pkmn.CalculateAllExperienceNeededForLevel(pkmn.GetMaxLevel() + 1) - pkmn.GetExperience()) + 1) size 40 yalign .43 xalign 0.5

        $ status = "None"
        if (pkmn.GetHealthPercentage() <= 0.0 and pkmn.GetCaught() <= 0):
            $ status = "Fainted"
        else:
            for statustype in nonvolatiles:
                if (pkmn.HasStatus(statustype)):
                    $ status = statustype
        
        hbox:
            yalign .48
            xalign .5
            spacing 30
            text "Status: " + status.title() xminimum 300 size 40 yalign .5
            if (pkmn.GetItem() == None):
                text "Item: None" xminimum 300 size 40 yalign .5
            else:
                text "Item: " + pkmn.GetItem() xminimum 300 size 40 yalign .5

            text "Nature: " + NatureToString(pkmn.GetNature()) xminimum 300 size 40 yalign .5
            $ fvlability = False
            for fvl in pkmn.GetForeverals():
                if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.AddAbility):
                    $ fvlability = True
            if (not fvlability):
                text "Ability: " + pkmn.GetAbility() xminimum 300 size 40 yalign .5
            else:
                hbox:
                    text "Ability: " xminimum 300 size 40 yalign .5
                    vbox:
                        text pkmn.GetAbility() xminimum 300 size 40 yalign .5
                        for fvl in pkmn.GetForeverals():
                            if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.AddAbility):
                                for ability in lookupforeveraldata(fvl, FVLMacros.FVLTypeData):
                                    text "(" + ability + ")" xminimum 300 size 40 yalign .5
            if (usingforeverals):
                if (pkmn.GetForeverals() == []):
                    text "Foreveral: None" xminimum 300 size 40 yalign .5
                else:
                    text "Foreveral: " + pkmn.GetForeverals()[0] xminimum 300 size 40 yalign .5
        
        use battlemoves(pkmn)

    textbutton "Select" action [Hide("stats", Dissolve(0.5)), Return(value=(pkmn.GetTrainer().GetTeam().index(pkmn)))] xminimum 300 yalign .7 xalign .4 text_xalign .5 text_size 40 text_color "#228B22" text_hover_color "#00FF00" background Frame("gui/button/choice_idle_background.webp")
    textbutton "Back" action [Hide("stats", Dissolve(0.5)), Show("switch", Dissolve(0.5), pkmn.GetTrainer())] xminimum 300 yalign .7 xalign .6 text_xalign .5 text_size 40 text_color "#800000" text_hover_color "#FF0000" background Frame("gui/button/choice_idle_background.webp")

screen battlemoves(pkmn):
    grid len(pkmn.GetMoves()) 1:
        xalign .5
        yalign .57
        for move in pkmn.GetMoves():
            textbutton move.Name action NullAction() xminimum 350 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" hovered Show("movedata", Dissolve(0.5), move) unhovered Hide("movedata", Dissolve(0.5)), Show("stats", Dissolve(0.5), pkmn)

screen rememberablemoves(pkmn):
    $ rememberablemoves = GetRememberableMoves(pkmn)

    grid 5 6:
        align (0.5, 0.75)
        for move in rememberablemoves:
            textbutton move:
                xmaximum 280 text_size 40 text_xalign 0.5 text_color "#000" ymaximum 70
                text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" 
                action [Hide("rememberablemoves", Dissolve(0.5)), Hide("movedata", Dissolve(0.5)), Return(move)] 
                hovered Show("movedata", Dissolve(0.5), GetMove(move)) 
                unhovered Hide("movedata", Dissolve(0.5))

        for i in range(30 - len(rememberablemoves)):
            null

    textbutton "Back" action [Hide("movedata", Dissolve(0.5)), Hide("rememberablemoves", Dissolve(0.5)), Return("Back")] xminimum 300 yalign .4 xalign .5 text_xalign .5 text_size 40 text_color "#800000" text_hover_color "#FF0000" background Frame("gui/button/choice_idle_background.webp")

screen SelectMon():
    if (not renpy.get_screen("partyviewer")):
        use partyviewer()
        
    $ team = playerparty
    $ numMons = len(team)

    grid 3 2:
        xalign .5
        ypos .2

        for i, mon in enumerate(team):
            textbutton mon.GetNickname() + " {size=30}Lv." + str(mon.GetLevel()) action [Hide("SelectMon", Dissolve(0.5)), Return(mon)] xminimum 400 text_xmaximum 400 yminimum 140 ymaximum 140 text_xalign .5 text_yalign 0.3 text_size (60 if count_non_brace_chars(mon.GetNickname()) <= 10 else 40)  style "menu_choice_button" text_font "fonts/pkmndp.ttf" text_color "#000" text_hover_color "#f0f"
        for i in range(6 - numMons):
            null 

    grid 3 2:
        xalign .5
        ypos .29
        yspacing 100
        xspacing 12

        for i, mon in enumerate(team):
            $ maxhealth = mon.GetStat(Stats.Health, triggerAbilities=False)
            $ health = max(mon.GetHealth(), mon.WasCaught)
            $ barcolor = "#00b612"
            if (health / maxhealth <= 0.25):
                $ barcolor = "#ff0000"
            elif (health / maxhealth <= 0.5):
                $ barcolor = "#fff700"
            bar range maxhealth value health xmaximum 388 right_bar "#fff" left_bar barcolor
        for i in range(6 - numMons):
            null 

    textbutton "Back" action Return(value='back') xminimum 400 text_xalign .5 xalign .5 yalign .75 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"    

screen SendToPC():
    if (not renpy.get_screen("partyviewer")):
        use partyviewer()
        
    $ team = playerparty
    $ numMons = 7

    grid 3 3:
        xalign .5
        ypos .2

        for i in range(numMons):
            if (team[i] in Battlers() and len(EnemyBattlers()) > 0 and team[i] != EnemyBattlers()[0]):
                textbutton team[i].GetNickname() + " {size=30}(In Battle)" xminimum 400 text_xmaximum 400 yminimum 140 ymaximum 140 text_xalign .5 text_yalign 0.3 text_size (60 if len(team[i].GetNickname()) <= 10 else 40)  style "menu_choice_button" text_font "fonts/pkmndp.ttf" text_color "#000" text_hover_color "#f0f"
            else:
                textbutton team[i].GetNickname() + " {size=30}Lv." + str(team[i].GetLevel()) action ([Hide("SendToPC", Dissolve(0.5)), Return(team[i])] if team[i] != pikachuobj else NullAction()) xminimum 400 text_xmaximum 400 yminimum 140 ymaximum 140 text_xalign .5 text_yalign 0.3 text_size (60 if len(team[i].GetNickname()) <= 10 else 40)  style "menu_choice_button" text_font "fonts/pkmndp.ttf" text_color "#000" text_hover_color "#f0f"
            if (i == 5 or i == 6):
                null

    grid 3 3:
        xalign .5
        ypos .29
        yspacing 100
        xspacing 12

        for i in range(numMons):
            $ maxhealth = team[i].GetStat(Stats.Health, triggerAbilities=False)
            $ health = max(team[i].GetHealth(), team[i].WasCaught)
            $ barcolor = "#00b612"
            if (health / maxhealth <= 0.25):
                $ barcolor = "#ff0000"
            elif (health / maxhealth <= 0.5):
                $ barcolor = "#fff700"
            bar range maxhealth value health xmaximum 388 right_bar "#fff" left_bar barcolor
            if (i == 5 or i == 6):
                null      

screen switch(trainer, hideback = False):
    if (not renpy.get_screen("battleui")):
        use battleui()
    
    python:
        team = trainer.GetTeam()
        numMons = len(team)
    
    grid 3 2:
        xalign .5
        ypos .2

        for i in range(numMons):
            textbutton team[i].GetNickname() + " {size=30}Lv." + str(team[i].GetLevel()) action [Hide("switch", Dissolve(0.5)), Show("stats", Dissolve(0.5), team[i])] xminimum 400 text_xmaximum 400 yminimum 140 ymaximum 140 text_xalign .5 text_yalign 0.3 text_size (60 if len(team[i].GetNickname()) <= 10 else 40) style "menu_choice_button" text_font "fonts/pkmndp.ttf" text_color "#000" text_hover_color "#f0f"
                
        for i in range(6 - numMons):
            null

    grid 3 2:
        xalign .5
        ypos .29
        yspacing 100
        xspacing 12
        
        python:
            team = trainer.GetTeam()
            numMons = len(team)

        for i in range(numMons):
            if (taughtmove == None):
                $ maxhealth = team[i].GetStat(Stats.Health, triggerAbilities=False)
                $ health = team[i].GetHealth()
                $ barcolor = "#00b612"
                if (health / maxhealth <= 0.25):
                    $ barcolor = "#ff0000"
                elif (health / maxhealth <= 0.5):
                    $ barcolor = "#fff700"
                bar range maxhealth value health xmaximum 388 right_bar "#fff" left_bar barcolor
            else:
                hbox:
                    null width 110
                    text (("{color=#00b612}Can Learn{/color}" if MonCanLearn(team[i], taughtmove) else "{color=#ff0000}Can't Learn{/color}") if taughtmove not in team[i].GetMoveNames() else "{color=#ff0000}Learned{/color}") xalign 0.5
                    null width 110
            
        for i in range(6 - numMons):
            null

    if (not hideback and not mustswitch):
        grid 1 1:
            xalign .5
            ypos .658
            textbutton "Back" action Return(value='back') xminimum 400 text_xalign .5 xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"

##############################################################################
# Calendar
#
label blankitall:
    scene blank2
    $ renpy.call(random.choice(list(classstats.keys())).lower() + "_class_" + str(random.randint(1, 20)).zfill(2))
    scene blank2
    return

screen currentdate():
    use partyviewer()
    use wallet()

    #textbutton "Scene Tester" text_xalign 0.5 align (0, 1.0) action Call("blankitall") text_font "fonts/pkmndp.ttf" style "menu_choice_button" xmaximum 300

    if (not isgame):
        if (usinginventory):
            use inventorywidget()
        if (usingforeverals and playercharacter == None):
            use foreveralwidget()
        vbox:
            ypos 55
            if (activerepel != None):
                frame:
                    ypadding 10
                    xpadding 15
                    background Frame("GFX/DateTimeBanner.webp") at Transform(xzoom=-1)
                    text " " + activerepel + " active. Encounters left: " + str(repelstepsleft) size 28 color "#1c1c1c" at Transform(xzoom=-1) alt ""

            if (activetreat != None):
                frame:
                    ypadding 10
                    xpadding 15
                    background Frame("GFX/DateTimeBanner.webp") at Transform(xzoom=-1)
                    text " " + activetreat + " active. Bonus: " + str(wildcount + 1) + "x" size 28 color "#1c1c1c" at Transform(xzoom=-1) alt ""
                    
    frame:
        left_padding 10
        right_padding 25
        xpadding 15
        background Frame("GFX/DateTimeBanner.webp",0,0)
        xalign 1.0
        vbox:
            if (isinstance(config.version, str) and "BETA" in config.version):
                text config.version + ": " + str(renpy.call_stack_depth()) alt ""
            text "{size=28}{font=fonts/Microgramma-D-OT-Bold-Extended.ttf}[timeOfDay] -{/font}{/size} {size=28}"+getRWDay(0)+", "+str(calendar.month_name[calDate.month])+" "+getRDay(0)+"{/size}" color "#1c1c1c" alt ""

##############################################################################
# Class Electives Selection
#
# Types screens.

screen electives():
    use currentdate()

    python:
        maxlength = 3
        zoomsize = 1
        for keyname in altclassdex.keys():
            if (len(GetStudents(keyname)) == 4):
                maxlength = max(maxlength, 4)
                zoomsize = min(zoomsize, 7.0/8.0)
            elif (len(GetStudents(keyname)) == 5):
                zoomsize = min(zoomsize, 2.0/3.0)
                maxlength = max(maxlength, 5)

    grid 3 6:
        xanchor 1.0
        xpos 0.9
        yalign 0.5
        spacing 20
        for keyname in altclassdex.keys():
            if (lastclass != keyname):
                $ lowerkey = keyname.lower()
                if (keyname == "Psychic" and (IsAfter(9, 5, 2004) and IsBefore(15, 5, 2004) and not rescuedwill)):
                    null
                else:
                    imagebutton:
                        idle Transform("imagemaps/{}_still.webp".format(lowerkey), zoom=zoomsize)
                        hover Transform("imagemaps/{}_hover.webp".format(lowerkey), zoom=zoomsize)
                        action Return(keyname) 
                        hovered Show("classmates", Dissolve(0.5), keyname, maxlength)
                        unhovered Hide("classmates", Dissolve(0.5))                    
            else:
                null

screen studyfocus():
    use currentdate()

    grid 3 6:
        xalign 0.5
        yalign 0.5
        spacing 20
        for keyname in altclassdex.keys():
            $ lowerkey = keyname.lower()
            imagebutton: 
                idle "imagemaps/{}_still.webp".format(lowerkey)
                hover "imagemaps/{}_hover.webp".format(lowerkey)
                action Return(keyname)
    
    textbutton "Back" action Return("Back") xminimum 200 text_xalign .5 xalign .5 yalign .9 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"

screen picktype:
    grid 3 6:
        xalign 0.5
        yalign 0.5
        spacing 20
        for keyname in altclassdex.keys():
            $ lowerkey = keyname.lower()
            imagebutton: 
                idle "imagemaps/{}_still.webp".format(lowerkey)
                hover "imagemaps/{}_hover.webp".format(lowerkey)
                action Return(keyname)

screen inventory():
    if (not renpy.get_screen("battleui")):
        use battleui()
    frame:
        xpos 0.209
        yanchor 0.0
        ypos 0.124
        background "images/GUI/readback.webp"
        $ itemcount = 0
        grid 4 10:
            transpose True
            for item in inventory.keys():
                if (InventoryCategory(item) in ["Healing", "Poké Balls"] or item == "Poké Doll"):
                    $ itemcount += 1
                    textbutton ("" if inventory[item] == 1 else str(inventory[item]) + "x ") + item text_color "#2b2b2b" action Return(item) text_hover_color "#fff"
            for x in range(40 - itemcount):
                null

    textbutton "Back" action Return("Back") xminimum 200 text_xalign .5 xalign .5 yalign .75 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"

screen classmates(type, maxlength):
    zorder -1
    $ studentslist = SortBySize(GetStudents(type))
    for i, character in enumerate(studentslist):
        $ charcolor = GetCharColor(character)
        $ iteration = (1.25 if len(GetStudents(type)) == 3 else 1.0)
        $ length = 0.4 + (0.1 if maxlength == 5 else (0.05 if maxlength == 4 else 0))
        $ numstudents = len(GetStudents(type))
        if (character in persondex.keys() and "Named" in persondex[character].keys() and persondex[character]["Named"]):
            $ value = persondex[character]["Value"]
            $ valueceil = GetCharacterLevel(character)
            add GetCharacterSprite(character, uniform=True) xpos length / (numstudents + 1) * (i + 1)
            $ specialnature = GetNature(character) == TrainerNature.Special
            $ mood = GetMood(character)
            text "{size=50}{color=" + charcolor + "}" + character + "\n{/color}{size=30}Lv." + str(valueceil) + ", EXP: " + str(value) + ("\n{/color}{size=30}" + moodtoword(mood) + " (" + str(mood) + ")" if usingmoods and not specialnature else ("\n{/color}{size=30}Stable" if usingmoods and specialnature else "")) color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] at Transform(rotate=-15) ypos 0.03 xpos length / (numstudents + 1) * (i * 1.1 + 1) - 0.07
        else:
            $ finalmatrix = TintMatrix(charcolor) * BrightnessMatrix(1.0) * ContrastMatrix(0.0)
            add GetCharacterSprite(character, uniform=True) xpos length / (numstudents + 1) * (i + 1) matrixcolor finalmatrix

    text type + "{size=80} - Lv. " + FormatNum(classstats[type]) color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] size 120 xcenter 0.25 ypos 0.85

screen pickpokemon(choices):
    python:
        lesschosen = (chosenindex - 1) % len(choices)
        morechosen = (chosenindex + 1) % len(choices)
        modchosen = chosenindex % len(choices)
        totalstats = pokedexlookup(choices[modchosen], DexMacros.Total)
        potential = pokedexlookup(GetFinalForm(choices[modchosen]), DexMacros.Total)

    text "(Click or use keyboard to change selection.)" size 40 align (0.5, 0.1) color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]
    
    add "GUI/double-arrow.webp" align (0.5, 0.5) at Transform() 

    imagebutton idle "Pokemon/" + str(choices[lesschosen]) + ".webp" yalign 0.5 xanchor 0.5 xpos 0.15 action SetVariable("chosenindex", lesschosen)
    key "K_LEFT" action SetVariable("chosenindex", lesschosen)
    add "Pokemon/" + str(choices[lesschosen]) + ".webp" yalign 0.5 xanchor 0.5 xpos 0.15 at Transform(alpha=0.6, matrixcolor=BrightnessMatrix(-1))
    
    imagebutton idle "Pokemon/" + str(choices[modchosen]) + ".webp" align(0.5, 0.4) at Transform(zoom=1.5) action Return(choices[modchosen])
    key "K_RETURN" action Return(choices[modchosen])
    text pokedexlookup(choices[modchosen], DexMacros.Name) size 80 align (0.5, 0.75) color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]
    
    $ secondcolorstring = pokedexlookup(choices[modchosen], DexMacros.Type2)
    if (secondcolorstring == None):
        $ secondcolorstring = ""
    else:
        $ secondcolorstring = "{color=#fff}/{/color}{color=" + GetTypeColor(secondcolorstring) + "}" + secondcolorstring
    text pokedexlookup(choices[modchosen], DexMacros.Type1) + secondcolorstring size 40 align (0.5, 0.8) color GetTypeColor(pokedexlookup(choices[modchosen], DexMacros.Type1)) outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]

    grid 4 2:
        align (0.5, 0.91)
        xspacing 15
        yspacing 25
        bar value pokedexlookup(choices[modchosen], DexMacros.Health) range 120 xmaximum 300 top_bar "#FF0000" bottom_bar "#A60000"
        bar value pokedexlookup(choices[modchosen], DexMacros.Attack) range 120 xmaximum 300 top_bar "#F08030" bottom_bar "#9C531F"
        bar value pokedexlookup(choices[modchosen], DexMacros.Defense) range 120 xmaximum 300 top_bar "#F8D030" bottom_bar "#A1871F"
        bar value pokedexlookup(choices[modchosen], DexMacros.SpecialAttack) range 120 xmaximum 300 top_bar "#6890F0" bottom_bar "#445E9C"
        bar value pokedexlookup(choices[modchosen], DexMacros.SpecialDefense) range 120 xmaximum 300 top_bar "#78C850" bottom_bar "#4E8234"
        bar value pokedexlookup(choices[modchosen], DexMacros.Speed) range 120 xmaximum 300 top_bar "#F85888" bottom_bar "#A13959"
        bar value potential range 700 xmaximum 300 top_bar "#FF00E4" bottom_bar "#710066"
        bar value potential / totalstats range 2.5 xmaximum 300 top_bar "#00FFF8" bottom_bar "#00827e"

    grid 4 2:
        align (0.5, 0.9)
        text "Health: " + str(pokedexlookup(choices[modchosen], DexMacros.Health)) size 40 color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]
        text "Attack: " + str(pokedexlookup(choices[modchosen], DexMacros.Attack)) size 40 color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]
        text "Defense: " + str(pokedexlookup(choices[modchosen], DexMacros.Defense)) size 40 color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]
        text "Special Attack: " + str(pokedexlookup(choices[modchosen], DexMacros.SpecialAttack)) size 40 color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]
        text "Special Defense: " + str(pokedexlookup(choices[modchosen], DexMacros.SpecialDefense)) size 40 color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]
        text "Speed: " + str(pokedexlookup(choices[modchosen], DexMacros.Speed)) size 40 color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]
        text "Final BST: " + str(potential) size 40 color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]
        text "Potential: " + str(math.floor(potential / totalstats * 100)) + "%" size 40 color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]

    imagebutton idle "Pokemon/" + str(choices[morechosen]) + ".webp" yalign 0.5 xanchor 0.5 xpos 0.85 action SetVariable("chosenindex", morechosen)
    key "K_RIGHT" action SetVariable("chosenindex", morechosen)
    add "Pokemon/" + str(choices[morechosen]) + ".webp" yalign 0.5 xanchor 0.5 xpos 0.85 at Transform(alpha=0.6, matrixcolor=BrightnessMatrix(-1))

screen abilitysplashleft(ability):
    zorder 100
    $ username = ability[0]
    $ ability = ability[1] + "\n{size=60}activated!"
    add "GUI/double-arrow.webp" yalign 0.5 at swipeinleft, Transform(yzoom = 0.3, xzoom=-0.3)
    text "{size=60}" + username + "'s{/size}\n" + ability color "#fff" yalign 0.5 size 80 outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] at swipeinleft
    timer 2.0 action Hide("abilitysplashleft")

screen abilitysplashright(ability):
    zorder 100
    $ username = ability[0]
    $ ability = ability[1] + "\n{size=60}activated!"
    add "GUI/double-arrow.webp" yalign 0.5 xalign 1.0 at swipeinright, Transform(zoom = 0.3)
    text "{size=60}" + username + "'s{/size}\n" + ability color "#fff" yalign 0.5 size 80 xalign 1.0 outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] at swipeinright
    timer 2.0 action Hide("abilitysplashright")

screen itemsplashleft(itemname):
    zorder 100
    $ username = itemname[0]
    $ item = itemname[1] + "\n{size=60}was used!"
    add "GUI/itemarrow.webp" yalign 0.5 at swipeinleft, Transform(yzoom = 0.3, xzoom=-0.3)
    text "{size=60}" + username + "'s{/size}\n" + item color "#fff" yalign 0.5 size 80 outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] at swipeinleft
    timer 2.0 action Hide("itemsplashleft")

screen itemsplashright(itemname):
    zorder 100
    $ username = itemname[0]
    $ item = itemname[1] + "\n{size=60}was used!"
    add "GUI/itemarrow.webp" yalign 0.5 xalign 1.0 at swipeinright, Transform(zoom = 0.3)
    text "{size=60}" + username + "'s{/size}\n" + item color "#fff" yalign 0.5 size 80 xalign 1.0 outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] at swipeinright
    timer 2.0 action Hide("itemsplashright")

screen songsplash(song, artist):
    zorder 100
    text "{size=60}♪ " + song + "{/size}\nby " + artist color "#fff" yalign 0.5 size 80 outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] at swipeinleftslow
    timer 10.0 action Hide("songsplash")

screen generalsplashleft(what):
    zorder 100
    # add "GUI/itemarrow.webp" yalign 0.5 at swipeinleft, Transform(yzoom = 0.3, xzoom=-0.3)
    text what color "#fff" yalign 0.5 size 60 outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] at swipeinleftslow
    timer 5.0 action Hide("generalsplashleft")

screen newtables():
    zorder 5
    $ validtables = []
    grid 4 2:
        yalign .95
        xalign .5
        spacing 20
        $ tables = GetTables()
        for table in tables.keys():
            if ((table == None or len(set(GetTables()[table]).intersection(GetStudents())) == 0) and (table != "Melody's Table" or IsDate(28, 5, 2004))):
                null
            else:
                $ npcs = tables[table]
                $ description = ""
                if (table == "Disciplinary Table"):
                    $ description = "The Disciplinary Committee has taken over this table. Students are pointing at a map and seriously planning some future event."
                elif (table == "Home Table"):
                    $ description = "This table is filled with the residents of Dorm 25. They argue, chat, and laugh fluidly, waving you over to join them."
                    $ socialtype = RandomChoice(GetYellowStudents(), True)
                    $ description += "\n{b}Yellow can tell you about " + socialtype + ".{/b}"  
                elif (table == "Famous Table"):
                    $ description = "This table is filled with the most eye-catching students in the school. As they discuss their lives, everyone around them hangs on every word they say, trying to hear the latest celeb news."
                elif (table == "Scheming Table"):
                    $ description = "This table is filled with students, grim-faced and determined. They're huddled around some object you cannot see, and whisper to each other with clandestine purpose."
                elif (table == "Romantic Table"):
                    $ description = "This table is filled with students unabashedly flirting. Cloth doilies cover the table, and there are rose petals scattered about. Someone's lit a candle-- No, wait. That's a Litwick."
                elif (table == "Independent Table"):
                    $ description = "This table is filled with students refusing to make eye contact with each other, and a Professor trying desperately to get them to. It's peaceful, though."
                    $ classtype = RandomChoice(list(altclassdex.keys()), True)
                    $ description += "\n{b}Professor Cherry can tutor you on the " + classtype + " type.{/b}"  
                elif (table == "Medical Table"):
                    $ description = "This table is filled with students you often see by the infirmary. There's a palpable weariness in the air, but the mood is nevertheless light."
                elif (table == "Remedial Table"):
                    $ description = "This table is filled with students studying Psychic-Types frantically. It's clear they're not quite certain what they're doing, but they're trying their best without instruction."
                elif (table == "Melody's Table"):
                    $ description = "Melody sits alone at this table. Everyone, sensibly, gives her a wide berth. There's no reason to approach."

                textbutton table action Hide("newtabledescriptions", Dissolve(0.5)), Return(table) xminimum 300 text_xalign .5 text_size 40 style "menu_choice_button" text_font "fonts/pkmndp.ttf" text_color "#000" text_hover_color "#f0f" hovered Show("newtabledescriptions", Dissolve(0.5), description, npcs) unhovered Hide("newtabledescriptions", Dissolve(0.5))

screen newtabledescriptions(description, npcs):
    layer "master"
    $ newnpcs = []
    for character in npcs:
        if (character in GetStudents("All") or character == "Melody"):
            $ newnpcs.append(character)
    $ npcs = newnpcs
    for i, character in enumerate(npcs):
        $ charcolor = GetCharColor(character)
        $ value = (persondex[character]["Value"] if character in persondex.keys() and "Value" in persondex[character].keys() else 0)
        $ valueceil = GetCharacterLevel(character)
        $ xposition = 1.0 / (len(npcs) + 1) * (i + 1) - 0.05
        $ mood = GetMood(character)
        $ nature = GetNature(character)
        add GetCharacterSprite(character, uniform=True) xpos xposition + 0.05 

        if (character != "Melody"):
            text "{size=80}{color=" + charcolor + "}" + (character if character in persondex.keys() and persondex[character]["Named"] else "???").replace(" ", "\n") + "\n{/color}{size=40}Lv." + str(valueceil) + ", EXP: " + ('{color=#ff0000}' if value < 1 else "") + str(value) + ("\n{/color}{size=30}" + moodtoword(mood) + " (" + str(mood) + ")" if nature != TrainerNature.Special else "\n{/color}{size=30}Stable") xpos xposition color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] at Transform(rotate=-15)
        else:
            text "{size=80}{color=" + charcolor + "}" + (character if character in persondex.keys() and persondex[character]["Named"] else "???").replace(" ", "\n") + "\n{/color}{size=40}Just don't." xpos xposition color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] at Transform(rotate=-15)

    textbutton description xalign 0.5 ypos 0.65 xmaximum 1500 text_color "#000" background Frame("gui/button/choice_idle_background.webp") xpadding 80

screen tables():
    zorder 5
    $ validtables = []
    grid 3 2:
        yalign .95
        xalign .5
        spacing 20
        $ tables = ["Angry Table", "Cheerful Table", "Busy Table", "Romantic Table", "Calm Table", "Quiet Table"]
        if (IsDate(20, 4, 2004) and GetRelationship("Nessa") == "Date"):
            $ tables = ["Angry Table", "Cheerful Table", None, "Romantic Table", "Calm Table", "Quiet Table"]
        for table in tables:
            if (table == None):
                null
            else:
                $ description = ""
                $ npcs = GetCharsInTable(table)
                if (table == "Angry Table"):
                    $ description = "This table is filled with students loudly arguing with each other. Despite the hostile atmosphere, they seem to be enjoying their anger."
                elif (table == "Cheerful Table"):
                    $ description = "This table is filled with students chatting and gossiping. Rumors are born and killed at this table."
                elif (table == "Busy Table"):
                    $ description = "This table is filled with students multi-tasking. They're all carrying on two conversations at once, phones to their ears. They frequently mention how they \"need to take this for their job.\""
                elif (table == "Romantic Table"):
                    $ description = "This table is filled with students unabashedly flirting. Cloth doilies cover the table, and there are rose petals scattered about. Someone's lit a candle-- No, wait. That's a Litwick."
                elif (table == "Calm Table"):
                    $ description = "This table is filled with students talking seriously. They discuss their school schedules, grades, extracurriculars, and plans for the future. You note they aren't discussing their social lives."
                elif (table == "Quiet Table"):
                    $ description = "This table is filled with students refusing to make eye contact with each other, and a Professor trying desperately to get them to. It's peaceful, though."
                    if (not IsBefore(11, 4, 2004)):
                        $ classtype = RandomChoice(list(altclassdex.keys()), True)
                        $ description += "\n{b}Professor Cherry can tutor you on the " + classtype + " type.{/b}"

                $ tablevalid = True
                for i, character in enumerate(npcs):
                    $ value = (persondex[character]["Value"] if character in persondex.keys() and "Value" in persondex[character].keys() else 0)
                    if (value < 1):
                        $ tablevalid = False
                if (tablevalid):
                    $ validtables.append(table)
                textbutton table action ([Hide("tabledescriptions", Dissolve(0.5)), Return(table)] if tablevalid else NullAction()) xminimum 400 text_xalign .5 text_size 60 style "menu_choice_button" text_font "fonts/pkmndp.ttf" text_color ("#000" if tablevalid else "#616161") text_hover_color ("#f0f" if tablevalid else "#616161") hovered Show("tabledescriptions", Dissolve(0.5), description, npcs) unhovered Hide("tabledescriptions", Dissolve(0.5))
    
    if (len(validtables) == 0):
        textbutton "Sleeping Table" action [Hide("tabledescriptions", Dissolve(0.5)), Return("Sleeping Table")] xminimum 400 text_xalign .5 align (0.0, 0.0) text_size 60 style "menu_choice_button" text_font "fonts/pkmndp.ttf" text_color "#000" text_hover_color "#f0f" hovered Show("tabledescriptions", Dissolve(0.5), "Ethan is sleeping here, by himself...", ["Ethan"]) unhovered Hide("tabledescriptions", Dissolve(0.5))

screen tabledescriptions(description, npcs):
    layer "master"
    $ newnpcs = []
    for character in npcs:
        if (character in GetStudents("All")):
            $ newnpcs.append(character)
    $ npcs = newnpcs
    for i, character in enumerate(npcs):
        $ charcolor = GetCharColor(character)
        $ value = (persondex[character]["Value"] if character in persondex.keys() and "Value" in persondex[character].keys() else 0)
        $ valueceil = GetCharacterLevel(character)
        $ xposition = 1.0 / (len(npcs) + 1) * (i + 1) - 0.05
        if (len(npcs) == 1):
            $ xposition = 0.5
        if (character in persondex.keys() and "Value" in persondex[character].keys() and persondex[character]["Value"] > 0):
            if (character == "Tia" and not IsBefore(17, 4, 2004)):
                add "tia uniform hat" xpos xposition + 0.05
            elif (character == "Professor Cherry"):
                add "kris" xpos xposition + 0.05
            else:
                add character.lower() + " uniform" xpos xposition + 0.05
                
        else:
            $ finalmatrix = TintMatrix(charcolor) * BrightnessMatrix(1.0) * ContrastMatrix(0.0)
            if (character == "Tia" and not IsBefore(17, 4, 2004)):
                add "tia uniform hat" xpos xposition + 0.05
            elif (character == "Professor Cherry"):
                add "kris" xpos xposition + 0.05 matrixcolor finalmatrix
            else:
                add character.lower() + " uniform" xpos xposition + 0.05 matrixcolor finalmatrix

        text "{size=80}{color=" + charcolor + "}" + (character if character in persondex.keys() and persondex[character]["Named"] else "???").replace(" ", "\n") + "\n{/color}{size=40}Lv." + str(valueceil) + ", EXP: " + ('{color=#ff0000}' if value < 1 else "") + str(value) xpos xposition color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] at Transform(rotate=-15)

    textbutton description xalign 0.5 ypos 0.65 xmaximum 1500 text_color "#000" background Frame("gui/button/choice_idle_background.webp") xpadding 80

init python:
    def liberize(element):
        renpy.hide_screen("liberizemessage")
        global libtypes
        if (element in libtypes):
            libtypes.remove(element)
        else:
            libtypes.append(element)
            if (len(libtypes) > (2 if dawnbattle else libtypesnum)):#libtypesnum set to 2 if dawnbattle
                libtypes = libtypes[:len(libtypes) - 1]
                renpy.show_screen("liberizemessage", "You do not have the freedom to\nliberize into another type{w=0.5}\nyet.")
            else:
                libtype1 = libtypes[0]
                libtype2 = libtypes[0]
                if (len(libtypes) > 1):
                    libtype2 = libtypes[1]
                renpy.show_screen("liberizemessage", liberizefirstsentence[libtype1] + "\n" + liberizesecondsentence[libtype2])

transform liberize_scroll:
    ypos 1.0 yanchor 0.0
    ease 0.25 yalign 0.7
    ease 2.0 yalign 0.6
    ease 0.25 ypos 0.0 yanchor 1.0

screen liberizemessage(msg):
    vbox at liberize_scroll:
        xpos 0.65
        yalign 1.0
        text msg

    timer 2.5 action Hide()

screen liberize:
    add "imagemaps/libera_tail.webp" at liberizemovein
    imagemap at liberizefadein:
        idle "imagemaps/libera_idle.webp"
        hover "imagemaps/libera_hover.webp"
        alpha False 

        hotspot (278, 155, 127, 109) action Function(liberize, "Grass")#grass 
        hotspot (452, 192, 103, 129) action Function(liberize, "Fire")#fire
        hotspot (625, 249, 85, 123) action Function(liberize, "Water")#water
        hotspot (798, 308, 79, 123) action Function(liberize, "Electric")#electric
        hotspot (939, 367, 130, 109) action Function(liberize, "Fighting")#fighting
        hotspot (1114, 420, 111, 110) action Function(liberize, "Psychic")#psychic
        hotspot (206, 399, 117, 116) action Function(liberize, "Dark")#dark
        hotspot (373, 442, 123, 119) action Function(liberize, "Steel")#steel
        hotspot (547, 479, 112, 128) action Function(liberize, "Dragon")#dragon
        hotspot (710, 525, 122, 126) action Function(liberize, "Fairy")#fairy
        hotspot (880, 570, 120, 118) action Function(liberize, "Normal")#normal
        hotspot (1053, 615, 110, 122) action Function(liberize, "Ghost")#ghost
        hotspot (116, 673, 129, 97) action Function(liberize, "Flying")#flying
        hotspot (295, 685, 117, 114) action Function(liberize, "Poison")#poison
        hotspot (452, 722, 133, 91) action Function(liberize, "Ground")#ground
        hotspot (636, 748, 121, 107) action Function(liberize, "Rock")#rock
        hotspot (814, 755, 106, 124) action Function(liberize, "Bug")#bug
        hotspot (975, 785, 127, 124) action Function(liberize, "Ice")#ice

    for element in libtypes:
        add "imagemaps/libera{}.webp".format(element.lower()) at liberizeactivefadein

    textbutton "Finish" xminimum 300 text_xalign 0.5 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" xalign 1.0 yalign 1.0 action [Hide("liberize", Dissolve(0.5)), Return("liberaconfirm")]

screen map_UI():
    if (not renpy.get_screen("currentdate")):
        use currentdate()

    zorder -5
    imagemap:
        ground "BG/Map.webp"
        idle "BG/Map.webp"
        hover "imagemaps/Map_Hover.webp"
        
        hotspot (161, 121, 429, 230) action Show("map_confirm", Dissolve(0.5), "Battle Hall") hovered Show("map_people", Dissolve(0.5), GetCharsInPlace("Battle Hall"), (161, 121, 429, 230)) unhovered Hide("map_people", Dissolve(0.5))
        hotspot (658, 107, 609, 214) action Show("map_confirm", Dissolve(0.5), "Academy") hovered Show("map_people", Dissolve(0.5), GetCharsInPlace("Academy"), (658, 107, 609, 214)) unhovered Hide("map_people", Dissolve(0.5))
        hotspot (88, 343, 331, 275) action Show("map_confirm", Dissolve(0.5), "Recreation Center") hovered Show("map_people", Dissolve(0.5), GetCharsInPlace("Recreation Center"), (88, 343, 331, 275)) unhovered Hide("map_people", Dissolve(0.5))
        hotspot (88, 621, 464, 384) action Show("map_confirm", Dissolve(0.5), "Aura Hall") hovered Show("map_people", Dissolve(0.5), GetCharsInPlace("Aura Hall"), (88, 621, 464, 384)) unhovered Hide("map_people", Dissolve(0.5))
        hotspot (1451, 347, 376, 250) action Show("map_confirm", Dissolve(0.5), "Research Center") hovered Show("map_people", Dissolve(0.5), GetCharsInPlace("Research Center"), (1451, 347, 376, 250)) unhovered Hide("map_people", Dissolve(0.5))
        hotspot (733, 566, 475, 220) action Show("map_confirm", Dissolve(0.5), "Garden") hovered Show("map_people", Dissolve(0.5), GetCharsInPlace("Garden"), (733, 566, 475, 220)) unhovered Hide("map_people", Dissolve(0.5))
        hotspot (581, 780, 757, 258) action Show("map_confirm", Dissolve(0.5), "Relic Hall") hovered Show("map_people", Dissolve(0.5), GetCharsInPlace("Relic Hall"), (581, 780, 757, 258)) unhovered Hide("map_people", Dissolve(0.5))
        hotspot (734, 312, 500, 249) action Show("map_confirm", Dissolve(0.5), "Student Center") hovered Show("map_people", Dissolve(0.5), GetCharsInPlace("Student Center"), (734, 312, 500, 249)) unhovered Hide("map_people", Dissolve(0.5))
        hotspot (1456, 140, 419, 200) action Show("map_confirm", Dissolve(0.5), "Baseball Field") hovered Show("map_people", Dissolve(0.5), GetCharsInPlace("Baseball Field"), (1456, 140, 419, 200)) unhovered Hide("map_people", Dissolve(0.5))
        hotspot (232,0, 1594, 111) action [Hide("map_people", Dissolve(0.5)), Return("Town")]
        hotspot (1367, 618, 473, 385) action Show("map_confirm", Dissolve(0.5), "Pledge Hall") hovered Show("map_people", Dissolve(0.5), GetCharsInPlace("Pledge Hall"), (1367, 618, 473, 385)) unhovered Hide("map_people", Dissolve(0.5))
        hotspot (0, 964, 362, 116) action [Hide("map_people", Dissolve(0.5)), Return("Fields")]

screen egghunt():
    if (not renpy.get_screen("currentdate")):
        use currentdate()

    zorder -5
    imagemap:
        ground "BG/Map.webp"
        idle "BG/Map.webp"
        hover "imagemaps/Map_Hover.webp"
        
        hotspot (161, 121, 429, 230) action Return("Battle Hall") #Tyrogue
        hotspot (658, 107, 609, 214) action Return("Academy") #Smoochum
        hotspot (88, 343, 331, 275) action Return("Recreation Center") #Mantyke
        hotspot (88, 621, 464, 384) action Return("Aura Hall") #Togepi
        hotspot (1451, 347, 376, 250) action Return("Research Center") #Toxel
        hotspot (733, 566, 475, 220) action Return("Garden") #Happiny
        hotspot (581, 780, 757, 258) action Return("Relic Hall") #Magby
        hotspot (734, 312, 500, 249) action Return("Student Center") #Wynaut
        hotspot (1456, 140, 419, 200) action Return("Baseball Field") #Larvesta
        hotspot (1367, 618, 473, 385) action Return("Pledge Hall") #Bonsly
        hotspot (0, 964, 362, 116) action Return("Outside")

screen makeup():
    if (not renpy.get_screen("currentdate")):
        use currentdate()

    zorder -5
    imagemap:
        ground "BG/Map.webp"
        idle "BG/Map.webp"
        hover "imagemaps/Map_Hover.webp"
        
        hotspot (161, 121, 429, 230) action [Hide("map_people", Dissolve(0.5)), Return("Battle Hall")] #Returns a failure message
        hotspot (1451, 347, 376, 250) action [Hide("map_people", Dissolve(0.5)), Return("Research Center")] hovered Show("map_people", Dissolve(0.5), ["Bea", "Nate"], (1451, 347, 376, 250)) unhovered Hide("map_people", Dissolve(0.5))#Bea & Nate talking about violence
        hotspot (88, 343, 331, 275) action [Hide("map_people", Dissolve(0.5)), Return("Recreation Center")] hovered Show("map_people", Dissolve(0.5), ["Rosa", "Nessa"], (88, 343, 331, 275)) unhovered Hide("map_people", Dissolve(0.5))#Rosa & Nessa #talking about fame, and how it's ruined them
        hotspot (88, 621, 464, 384) action [Hide("map_people", Dissolve(0.5)), Return("Aura Hall")] hovered Show("map_people", Dissolve(0.5), ["Bianca", "Hilda", "May", "Serena"], (88, 621, 464, 384)) unhovered Hide("map_people", Dissolve(0.5))#Leaf's Roommates
        hotspot (581, 780, 757, 258) action [Hide("map_people", Dissolve(0.5)), Return("Relic Hall")] hovered Show("map_people", Dissolve(0.5), ["Brendan", "Calem", "Hilbert"], (581, 780, 757, 258)) unhovered Hide("map_people", Dissolve(0.5))#Roommates
        hotspot (1367, 618, 473, 385) action [Hide("map_people", Dissolve(0.5)), Return("Pledge Hall")] hovered Show("map_people", Dissolve(0.5), ["Cheren", "Silver", "Skyla"], (1367, 618, 473, 385)) unhovered Hide("map_people", Dissolve(0.5))#Disciplinary Committee
        hotspot (1456, 140, 419, 200) action [Hide("map_people", Dissolve(0.5)), Return("Baseball Field")] hovered Show("map_people", Dissolve(0.5), ["Flannery", "Whitney"], (1456, 140, 419, 200)) unhovered Hide("map_people", Dissolve(0.5))#Flannery & Whitney's Dorm
        hotspot (232,0, 1594, 111) action [Hide("map_people", Dissolve(0.5)), Return("Inspira")] hovered Show("map_people", Dissolve(0.5), ["Jasmine", "Grusha"], (232,50, 1594, 161)) unhovered Hide("map_people", Dissolve(0.5)) #The First Aid Squad (Grusha, Jasmine, Wally(?))
        hotspot (0, 964, 362, 116) action [Hide("map_people", Dissolve(0.5)), Return("Outside")]

screen map_people(people, location):
    $ numpeople = len(people)
    $ totaldist = (numpeople - 1) * 100
    $ midpoint = totaldist / 2.0
    for i, person in enumerate(people):
        $ yincrease = 0
        if (location in [(1367, 618, 473, 385), (88, 621, 464, 384)]):#pledge and aura halls
            $ yincrease = 100 
        $ centerpos = (location[0] + location[2] / 2.0 + i * 100 - midpoint, location[1] + 100 + yincrease)
        $ charcolor = GetCharColor(person)
        $ finalmatrix = TintMatrix(charcolor) * BrightnessMatrix(1.0) * ContrastMatrix(0.0)
        $ personsprite = Transform(GetChibi(person), zoom=0.2, xalign=0.5)
        if (persondex[person]["Named"]):
            add personsprite at (hovering if GetScenes([person])[0][1] else None) xpos math.floor(centerpos[0]) ypos math.floor(centerpos[1])
        else:
            add personsprite at (hovering if GetScenes([person])[0][1] else None) xpos math.floor(centerpos[0]) ypos math.floor(centerpos[1]) matrixcolor finalmatrix

screen map_confirm(location):
    modal True
    vbox:
        align (0.5, 0.5)
        if (location == "Academy" and IsAfter(11, 4, 2004)):
            textbutton "{b}Study{/b}" xminimum 800 text_xalign 0.5 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action [Hide("map_confirm", Dissolve(0.5)), Return("Study")]
            if (IsAfter(16, 5, 2004)):
                textbutton "{b}Access PC{/b}" xminimum 800 text_xalign 0.5 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action [Hide("map_confirm", Dissolve(0.5)), Return("AccessPC")]
                if (IsAfter(19, 5, 2004)):
                    textbutton "{b}Go to Cooking Club{/b}" xminimum 800 text_xalign 0.5 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action [Hide("map_confirm", Dissolve(0.5)), Return("CookingClub")]
        if (location == "Student Center"):
            textbutton "{b}Heal Party{/b}" xminimum 800 text_xalign 0.5 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action [Hide("map_confirm", Dissolve(0.5)), Function(HealParty)]
        if (location == "Baseball Field" and "Gardenia" in GetCharsInPlace("Baseball Field") and not IsBefore(25, 4, 2004) and (getRWDay(0) == "Sunday" or getRWDay(0) == "Saturday" or timeOfDay == "Evening")):
            textbutton "{b}Talk Business{/b}" xminimum 800 text_xalign 0.5 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action [Hide("map_confirm", Dissolve(0.5)), Return("Business")]
        if (location == "Battle Hall" and "Janine" in GetCharsInPlace("Battle Hall") and not IsBefore(26, 4, 2004) and (getRWDay(0) == "Sunday" or getRWDay(0) == "Saturday" or timeOfDay == "Evening")):
            textbutton "{b}Check Levels{/b}" xminimum 800 text_xalign 0.5 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action [Hide("map_confirm", Dissolve(0.5)), Return("LevelCheck")]
        if (location == "Garden" and "Professor Cherry" in GetCharsInPlace("Garden") and GetRelationshipRank("Professor Cherry") != 0):
            textbutton "{b}Check Critical Capture Rate{/b}" xminimum 800 text_xalign 0.5 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action [Hide("map_confirm", Dissolve(0.5)), Return("CriticalCheck")]
        for chartuple in GetScenes(GetCharsInPlace(location)):
            $ charname = chartuple[0]
            if (persondex[charname]["Named"]):
                $ hasscene = chartuple[1]
                $ nextscene = GetNextScene(charname)
                $ posttext = ""
                if (nextscene != None and not hasscene):
                    $ posttext = " - Next Scene: " + PrintSceneConditions(nextscene)
                textbutton ("{b}[[RANK UP!]{/b} " if hasscene else "") + ">Find " + charname + posttext xminimum 800 text_xalign 0.5 text_color "#000" text_hover_color GetCharColor(chartuple[0]) style "menu_choice_button" text_font "fonts/pkmndp.ttf" action [Hide("map_confirm", Dissolve(0.5)), Return(chartuple[0])]
        textbutton "Back" xminimum 800 text_xalign 0.5 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action [Hide("map_confirm", Dissolve(0.5)), Return ("Back")]

screen evolution(oldid, newid, liberize=False):
    modal True
    $ oldimage = "images/Pokemon/" + str(oldid) + ".webp"
    $ newimage = "images/Pokemon/" + str(newid) + ".webp"
    add "BG/Blank2.webp" at dissolvein
    add "GFX/speedlines.webp" at speedlines
    add newimage xzoom (-1 if liberize else 1) at evolvein
    if (liberize):
        add "images/Pokemon/25.2-1.webp" xzoom -1 at evolvein
        add "images/Pokemon/25.2-2.webp" xzoom -1 at evolvein
    add oldimage xzoom (-1 if liberize else 1) at evolveaway

    if (not liberize):
        hbox:
            yalign .95
            xalign .5
            spacing 300
            textbutton "Skip!" text_xalign 0.5 xmaximum 300 text_color "#000" text_hover_color "#0f0" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action [Hide("evolution"), Return(True)]    
            textbutton "Abort!" text_xalign 0.5 xmaximum 300 text_color "#000" text_hover_color "#f00" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action [Hide("evolution"), Return(False)]

    timer 25 action [Hide("evolution", Dissolve(2.0)), Return(True)]

screen shopkeep(items):
    vbox:
        xalign .5
        yalign .85
        for i in range(math.ceil(len(items) / 5)):
            hbox:
                for item in items[i * 5: i * 5 + 5]: #item is (name, cost, description)
                    $ buttontext = item[0] + " - $" + str(item[1])
                    textbutton buttontext text_size 40 - max(0, (len(buttontext) - 10)) text_xalign 0.5 xmaximum 300 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action [Show("itemdetails", Dissolve(0.5), item)]
        textbutton "Back" xalign .5 xminimum 300 text_xalign 0.5 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action [Hide("itemdetails", Dissolve(0.5)), Return("Back")]

screen itemdetails(item):
    $ itemname = item[0]
    $ itemcost = item[1]
    $ itemdescription = item[2]

    add "gui/button/choice_idle_background.webp" xalign .5 xzoom 1.5 yzoom 15 ypos -.05

    text "{b}" + itemname + "{/b}" xcenter 0.5 yalign .1 size 120
    text itemdescription xcenter 0.5 yalign .2 xmaximum 1400
    text "$" + str(itemcost) + " x" + str(boughtitems) + " = $" + str(itemcost * boughtitems) xcenter 0.5 yalign 0.3
    text "Inventory: " + str(GetNumItems(itemname)) xcenter 0.5 yalign 0.4

    hbox:
        xalign .25
        yalign .5
        textbutton "-10" xmaximum 100 text_xalign 0.5 text_color "#700" text_hover_color "#f00" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action SetVariable("boughtitems", max(1, boughtitems - 10))
        textbutton "-1" xmaximum 100 text_xalign 0.5 text_color "#700" text_hover_color "#f00" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action SetVariable("boughtitems", max(1, boughtitems - 1))
    
    vbox:
        align (0.5, 0.5)
        textbutton "Buy!" xmaximum 300 text_xalign 0.5 text_color "#000" text_hover_color "#f0f"  style "menu_choice_button" text_font "fonts/pkmndp.ttf" action [Hide("itemdetails", Dissolve(0.5)), Return(item)]
        textbutton "Back" xmaximum 250 text_xalign 0.5 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action [Hide("itemdetails", Dissolve(0.5))]
    
    hbox:
        xalign .75
        yalign .5
        textbutton "+1" xmaximum 100 text_xalign 0.5 text_color "#070" text_hover_color "#0f0" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action SetVariable("boughtitems", min(99, boughtitems + 1))
        textbutton "+10" xmaximum 100 text_xalign 0.5 text_color "#070" text_hover_color "#0f0" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action SetVariable("boughtitems", min(99, boughtitems + 10))

init python:
    def swapPokemonLocation(pkmn):
        global box
        global playerparty
        global currentbox
        pkmn.Heal()
        if (pkmn in playerparty):
            if (len(playerparty) == 2):
                renpy.invoke_in_new_context(renpy.say, None, "You need to keep at least two Pokémon in your party!")
            elif (pkmn != pikachuobj):
                playerparty.remove(pkmn)
                box.append(pkmn)
            else:
                if (not IsDate(5, 5, 2004)):
                    renpy.hide_screen("partymons")
                    renpy.jump("nopikachu")
        elif (pkmn in box and len(playerparty) < 6):
            box.remove(pkmn)
            playerparty.append(pkmn)
        else:
            renpy.invoke_in_new_context(renpy.say, None, "Your party is full!")

        if (currentbox > math.floor((len(box) - 1) / 30)):
            currentbox -= 1

screen partymons:
    zorder 0
    grid 3 2:
        xalign 0.5
        yalign 0.1
        for mon in playerparty:
            textbutton mon.GetNickname() + " {size=20}Lv." + str(mon.GetLevel()) xmaximum 310 text_size 40 text_xalign 0.5 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action Function(swapPokemonLocation, mon)
        for i in range(6 - len(playerparty)):
            null
    textbutton "Back" align (0.5, 0.4) xmaximum 300 text_xalign 0.5 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action Return()
    
    add "gui/button/choice_idle_background.webp" xalign .5 xzoom 0.35 yalign 0.56 yzoom 2.5
    text "Box #" + str(currentbox + 1) align (0.5, 0.57) color "#fff" size 120 outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]

    hbox:
        spacing 20
        align (0.5, 0.57)
        textbutton ("{b}" if currentsort == "level" else "") + "Lv. Sort" + ("" if currentsort != "level" else " " + ("↓" if reversesort else "↑")) xmaximum 300 text_xalign 0.5 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action (SetVariable("currentsort", "level") if currentsort != "level" else ToggleVariable("reversesort"))
        textbutton ("{b}" if currentsort == "abc" else "") + "ABC Sort" + ("" if currentsort != "abc" else " " + ("↓" if reversesort else "↑")) xmaximum 300 text_xalign 0.5 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action (SetVariable("currentsort", "abc") if currentsort != "abc" else ToggleVariable("reversesort"))
        null width 350
        textbutton ("{b}" if currentsort == "dex" else "") + "Dex Sort" + ("" if currentsort != "dex" else " " + ("↓" if reversesort else "↑")) xmaximum 300 text_xalign 0.5 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action (SetVariable("currentsort", "dex") if currentsort != "dex" else ToggleVariable("reversesort"))
        textbutton "Stop Sorting" xmaximum 300 text_xalign 0.5 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action SetVariable("currentsort", None)

init python:
    def SortedBox():
        global box
        if (currentsort == "level"):
            box.sort(reverse = reversesort, key=(lambda entry : entry.GetLevel()))
        elif (currentsort == "abc"):
            box.sort(reverse = reversesort, key=(lambda entry : entry.GetNickname()))
        elif (currentsort == "dex"):
            box.sort(reverse = reversesort, key=(lambda entry : entry.GetId()))
        return box[currentbox * 30:currentbox * 30 + 30]

label pokemonextraoptions(pkmn):
    $ nick = pkmn.GetNickname()
    "What would you like to do with [nick]?"

    menu:
        "Rename it.":
            $ newnick = renpy.input("What would you like to nickname it?", default=nick, exclude="{}[[]%<>", length=12)
            if (newnick == ""):
                $ newnick = pokedexlookup(pkmn.GetId(), DexMacros.Name)
            $ pkmn.Nickname = newnick
            "The Pokémon has been renamed to [newnick]."

        "Relieve it. (Of its item.)" if (pkmn.GetItem() != None):
            $ RemoveItem(pkmn)

            "You do so."

        "Relieve it. (Of its Foreveral(s).)" if (pkmn.GetForeverals() != []):
            python:
                for fvl in pkmn.GetForeverals():
                    foreveralinv.append(fvl)
                pkmn.Foreverals = []
        
            "You do so."

        "{color=#FF0000}Release it.{/color}" if (pkmn != starterobj):
            "Are you absolutely certain? There is no getting it back without reloading a save. (Or using rollback.)"

            menu:
                "Do it.":
                    python:
                        box.remove(pkmn)
                        if (pkmn.GetItem() != None):
                            GetItem(pkmn.GetItem())
                        for fvl in pkmn.GetForeverals():
                            foreveralinv.append(fvl)
                    if (currentbox > math.floor((len(box) - 1) / 30)):
                        $ currentbox -= 1
                    "The Pokémon runs away sadly..."

                "No.":
                    pass

        "Nevermind.":
            pass
return

screen boxmons:
    zorder 11
    grid 6 5:
        xalign 0.5
        yalign 0.9
        for mon in SortedBox():
            $ buttontext = mon.GetNickname() + " {size=20}Lv." + str(mon.GetLevel())
            textbutton buttontext:
                xmaximum 280 text_size 50 - max(0, (len(buttontext) - 10)) text_xalign 0.5 text_color "#000" ymaximum 70
                text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" 
                action [Hide("nonbattlemoves"), Hide("mondata"), Function(swapPokemonLocation, mon)] 
                hovered [Show("mondata", None, mon, False), Show("nonbattlemoves", None, mon, tooltips=False)] 
                unhovered [Hide("mondata"), Hide("nonbattlemoves")]
                alternate [Hide("partymons"), Hide("nonbattlemoves"), Hide("mondata"), Call("pokemonextraoptions", mon)]
        for i in range(30 - len(SortedBox())):
            null

screen pokemonswap:
    zorder -1
    if (len(box) > 30):
        textbutton "<-": 
            xmaximum 100 yminimum 200 align (0.01, 0.83) text_xalign 0.5 
            text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" 
            action SetVariable("currentbox", (currentbox - 1 if currentbox != 0 else math.ceil(len(box) / 30) - 1))
    if (len(box) > 30):
        textbutton "->": 
            align (.99, 0.83) xmaximum 100 yminimum 200 text_xalign 0.5 
            text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" 
            action SetVariable("currentbox", (currentbox + 1 if currentbox != math.ceil(len(box) / 30) - 1 else 0))

transform credits_scroll():
    yalign 0.0
    linear 50 yalign 1.0

label credits:
    $ renpy.movie_cutscene('images/videos/Credits.webm')

    show screen credits

    pause 60

    hide screen credits

    call screen main_menu()

screen credits:
    add "BG/Blank2.webp"
    vbox at credits_scroll:
        xalign 0.5
        yalign 0.1
        spacing 50
        null height 1080

        vbox:
            text "Project Recreator" size 80 color "#fff"
            text "Freudian Creations" size 40 color "#fff"

        vbox:
            text "CG Artists" size 80 color "#fff"
            text "Dahlia Wilder" size 40 color "#fff"
            text "Wolff Steel" size 40 color "#fff"
            text "Iustinus Tempus" size 40 color "#fff"
            text "Dreamcloud1283" size 40 color "#fff"

        $ spriteartists = ["Iustinus Tempus", "Chayma", "KBunink", "Dantalion", "Anthos", "Wolff Steel", "SquishyBird22", "jadespring", "Ken Sugimori", "Brumirage", "Ga Be", "codygon z", "Dreamcloud1283"]
        vbox:
            text "Sprite Artists" size 80 color "#fff"
            for name in spriteartists:
                text name size 40 color "#fff"

        $ coders = ["Flintlock", "Hewdraw", "Adingo"]
        vbox:
            text "Programming Assistance" size 80 color "#fff"
            for name in coders:
                text name size 40 color "#fff"

        $ writers = ["MMCC"]
        vbox:
            text "Writing Assistance" size 80 color "#fff"
            for name in writers:
                text name size 40 color "#fff"

        $ specialthanks = ["Drunk Old Man", "imainmeleekirby", "JumboXtraLarge", "Bartre God Dio", "Novemball", "Lexel"]
        vbox:
            text "Special Thanks" size 80 color "#fff"
            for name in specialthanks:
                text name size 40 color "#fff"
        
        $ teachingassistants = ['hope_devourer', 'Leirbag15 (Pikmin Trainer)', 'nmorrow', 'Eyen [[Capo Eternal]', 'farzalou', 'cinnaburh', 'seanmac317', 'caerulight', 'Lexel', 'Exalt', 'variaqlty', 'Adamthenoob1 (#1 simp for Hilda)', 'Monarchist MISSINGNO.', 'naototogo', 'propoke24']
        vbox:
            text "Teaching Assistants" size 80 color "#fff"
            for name in teachingassistants:
                text name size 40 color "#fff"

        $ topstudents = ['kingsting', 'pabloxdreams', 'Scotch the Bro Route Advocate', 'lordmichaeltm', 'hope_devourer', 'shinzeka', 'krok', 'soluxisofficial', 'Drunk Old Man[[Juan\'s n°1 Friend]', 'kingslayer3765', 'primename', 'Leirbag15 (Pikmin Trainer)', 'velmidos9021', 'nmorrow', 'the_pickle_man.', 'mrrjc', 'prettymiggy', 'Based King 🤴🏾 (Christian)', 'iustinustempus', 'nicksaulnier', 'MysticHobo', 'kogasaka', 'denial___', 'weez1ng', 'Bill4123', 'Raion [[Lyra and Serena Simp]', 'Adingo [[I AM PUN]', 'signofnature_eevee', 'tiggyxtaggy', 'Eyen [[Capo Eternal]', 'farzalou', 'The Hilbert Gremlin', 'carpechaz', 'review10', 'Ken', 'nathanrose115', 'myname_jonas', 'mmcc_94868', 'FlanneryHildaAreMY#1\'s', 'tgasf', 'microe', 'Guest the Rat', 'chyson', 'pesto0903', 'Orion', 'inferno6703', 'Horny [[Champion Enjoyer]', 'cinnaburh', 'zajinho2b', '#1 Leaf simp~', 'seanmac317', 'carpe_0', 'bigfan0510', 'rhaykou', 'FAKE', 'crowy13', 'JumboEggstraLarge', 'ikai210', 'Enigmatic Passerby (Yellow Fan)', 'Cobra - #1 Leaf Fan', '.jacattac', 'caerulight', 'Lexel', 'Bartre God Dio', 'Exalt', 'Egg-ural', 'himdave', 'Silver Phoenix', 'variaqlty', 'Q1justin [[Blue Deserves Love]', 'Adamthenoob1 (#1 simp for Hilda)', 'buggybluejay', 'alurayune', 'Monarchist MISSINGNO.', 'vander86', 'redrevan.', 'lastskylord', 'propoke24', 'msrco']
        vbox:
            text "Top Students" size 80 color "#fff"
            for name in topstudents:
                text name size 40 color "#fff"

        $ commissioners = ['Drunk Old Man[[Juan\'s n°1 Friend]', 'Leirbag15 (Pikmin Trainer)', 'denial___', 'JWill', 'Eyen [[Capo Eternal]', 'Night Fury (PALF YouTuber)', 'Banned for level up', '#1 Dino', 'nathanrose115', 'astaroth45', 'moka6803', 'EmpressDuplica [[Based Genwunner]', 'Horny [[Champion Enjoyer]', 'The Aura Ranger', 'JumboEggstraLarge', 'Lexel', 'Bartre God Dio', 'crippledjoe', 'Adamthenoob1 (#1 simp for Hilda)', 'Flintlock', 'vander86', 'Dolphin - Cheren Apologist']
        vbox:
            text "Commissioners" size 80 color "#fff"
            for name in commissioners:
                text name size 40 color "#fff"

        vbox:
            text "Fashion Design" size 80 color "#fff"

            text "ポケ垢" size 40 color "#fff"
            text "VIK_Works" size 40 color "#fff"
            text 'Crys (u/Epee_Prisme)' size 40 color "#fff"
        
            null height 80

            text "Backgrounds" size 80 color "#fff"

            text "Your Diary by CUBE" size 40 color "#fff"
            text "Backgrounds by Sai Gakai/Kimagure After (きまぐれアフター)" size 40 color "#fff"
            text "Background Material Shop" size 40 color "#fff"
            text "QUUN PLANT Co., Ltd." size 40 color "#fff"
            text "KNT Graphics:Yagaminiso" size 40 color "#fff"
            text "Shounensha" size 40 color "#fff"
            text "BG Spot"size 40 color "#fff"
            text "Backgrounds by Min-Chi (みんちり)" size 40 color "#fff"
            text "Taken from みんちりえ (https://min-chi.material.jp/) and みんちりのfanbox (https://min-chi.fanbox.cc/)" size 25 color "#fff"

        null height 1080