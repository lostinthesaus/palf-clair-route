init:
    layeredimage red:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body:
            attribute neutral "red_body_neutral" default
            attribute uniform "red_body_uniform" 

        group eyes auto if_not ["angrybrow", "angry"]:
            attribute neutraleyes default
            attribute noeyes "red_eyeshine_blank"
            attribute sad "red_eyes_sadeyes"
            attribute happy "red_eyes_happyeyes"
            attribute surprised "red_eyes_surprisedeyes"
            attribute closedbrow "red_eyes_closedeyes"
            attribute sadbrow "red_eyes_sadeyes"
            attribute thinking "red_eyes_closedeyes"

        group eyebrows auto if_not ["angrybrow", "angry"]:
            attribute neutraleyebrows default
            attribute sad "red_eyebrows_sadeyebrows"
            attribute happy "red_eyebrows_happyeyebrows"
            attribute surprised "red_eyebrows_surprisedeyebrows"
            attribute thinking "red_eyebrows_neutraleyebrows"
            attribute closedbrow "red_eyebrows_neutraleyebrows"
            attribute sadbrow "red_eyebrows_sadeyebrows"
            attribute confused "red_eyebrows_confusedeyebrows"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "red_mouth_sadmouth"
            attribute happy "red_mouth_happymouth"
            attribute angry "red_mouth_angrymouth"
            attribute surprised "red_mouth_surprisedmouth"
            attribute thinking "red_mouth_frownmouth"
            attribute confused "red_mouth_talking2mouth"
            
        group brow:
            attribute angrybrow "red_brow_angrybrow"
            attribute angry "red_brow_angrybrow"

        group glasses auto

        group tears auto

        group sweat auto

        group shadow auto

        group tired auto

        group anger auto

        group blush auto

        group hat auto

        group cry auto

        group eyeshine auto:
            attribute noshine "red_eyeshine_blank"

        always "red_eyesparkles" if_not ["noeyes", "noshine", "angryeyes", "angrybrow", "happybrow", "closedbrow", "closedeyes", "deadeyes", "happyeyes", "thinking", "happy", "angry", "sad2eyes"] 
        always "red_eyesparkles_sad2eyes" if_any ["sad2eyes"]
    image side red = LayeredImageProxy("red", Transform(xpos=0.08, yanchor=0.35))
    image side red night = LayeredImageProxy("red", Transform(xpos=0.08, yanchor=0.35, matrixcolor=BrightnessMatrix(-0.2) * ContrastMatrix(1.3)))
    image side red morning = LayeredImageProxy("red", Transform(xpos=0.08, yanchor=0.35, matrixcolor=TintMatrix(Color(rgb=(.95,.80,.75))) * BrightnessMatrix(-0.10) * ContrastMatrix(1.2)))

    layeredimage tia:
        zoom 0.5
        xalign 0.5
        yanchor 0.63
        ypos 1.0

        group power auto

        group poweredhat auto

        group body auto:
            attribute neutral "tia_body_neutral" default
            attribute uniform "tia_body_uniform"

        group eyes auto:
            attribute neutraleyes default
            attribute sad "tia_eyes_sadeyes"
            attribute happy "tia_eyes_happyeyes"
            attribute surprised "tia_eyes_surprisedeyes"
            attribute thinking "tia_eyes_closedeyes"
            attribute angrybrow "tia_eyes_angryeyes"
            attribute sadbrow "tia_eyes_sadeyes"
            attribute sad2brow "tia_eyes_sad2eyes"
            attribute angry "tia_eyes_angryeyes"
            attribute closedbrow "tia_eyes_closedeyes"
            attribute happybrow "tia_eyes_happyeyes"

        group eyebrows auto:
            attribute neutraleyebrows default
            attribute sad "tia_eyebrows_sadeyebrows"
            attribute happy "tia_eyebrows_happyeyebrows"
            attribute surprised "tia_eyebrows_surprisedeyebrows"
            attribute thinking "tia_eyebrows_neutraleyebrows"
            attribute angrybrow "tia_eyebrows_angryeyebrows"
            attribute sadbrow "tia_eyebrows_sadeyebrows"
            attribute sad2brow "tia_eyebrows_sadeyebrows"
            attribute angry "tia_eyebrows_angryeyebrows"
            attribute closedbrow "tia_eyebrows_neutraleyebrows"
            attribute happybrow "tia_eyebrows_happyeyebrows"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "tia_mouth_sadmouth"
            attribute happy "tia_mouth_happymouth"
            attribute angry "tia_mouth_angrymouth"
            attribute surprised "tia_mouth_surprisedmouth"
            attribute thinking "tia_mouth_frownmouth"

        group tears auto

        group sweat auto

        group shadow auto

        group tired auto

        group anger auto:
            attribute angry "tia_anger_anger"

        group blush auto

        group hat auto

        group cry auto

        always "tia_eyesparkles" if_not ["sad2brow", "happybrow", "closedbrow", "closedeyes", "deadeyes", "happyeyes", "thinking", "happy", "sad2eyes", "powered", "poweredeyes"] 
        always "tia_eyesparkles_sad2eyes" if_any ["sad2eyes", "sad2brow"]

    image side tia = LayeredImageProxy("tia", Transform(xpos=0.08, yanchor=0.45))

    layeredimage jasmine:
        zoom 0.5
        xalign 0.5
        yanchor 0.63
        ypos 1.0
        group body:
            attribute neutral "jasmine_body_neutral" default
            attribute uniform "jasmine_body_uniform"

        group eyes auto:
            attribute neutraleyes default
            attribute sad "jasmine_eyes_sadeyes"
            attribute happy "jasmine_eyes_happyeyes"
            attribute surprised "jasmine_eyes_surprisedeyes"
            attribute thinking "jasmine_eyes_closedeyes"
            attribute angrybrow "jasmine_eyes_angryeyes"
            attribute sadbrow "jasmine_eyes_sadeyes"
            attribute sad2brow "jasmine_eyes_sad2eyes"
            attribute angry "jasmine_eyes_angryeyes"
            attribute closedbrow "jasmine_eyes_closedeyes"
            attribute happybrow "jasmine_eyes_happyeyes"

        group eyebrows auto:
            attribute neutraleyebrows default
            attribute sad "jasmine_eyebrows_sadeyebrows"
            attribute happy "jasmine_eyebrows_happyeyebrows"
            attribute surprised "jasmine_eyebrows_surprisedeyebrows"
            attribute thinking "jasmine_eyebrows_neutraleyebrows"
            attribute angrybrow "jasmine_eyebrows_angryeyebrows"
            attribute sadbrow "jasmine_eyebrows_sadeyebrows"
            attribute sad2brow "jasmine_eyebrows_sadeyebrows"
            attribute angry "jasmine_eyebrows_angryeyebrows"
            attribute closedbrow "jasmine_eyebrows_neutraleyebrows"
            attribute happybrow "jasmine_eyebrows_happyeyebrows"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "jasmine_mouth_sadmouth"
            attribute happy "jasmine_mouth_happymouth"
            attribute angry "jasmine_mouth_angrymouth"
            attribute surprised "jasmine_mouth_surprisedmouth"
            attribute thinking "jasmine_mouth_frownmouth"

        group tears auto

        group sweat auto

        group shadow auto

        group tired auto

        group anger auto:
            attribute angry "jasmine_anger_anger"

        group blush auto

        group hat auto

        group cry auto

        always "jasmine_eyesparkles" if_not ["sad2brow", "happybrow", "closedbrow", "closedeyes", "deadeyes", "happyeyes", "thinking", "happy", "sad2eyes"] 
        always "jasmine_eyesparkles_sad2eyes" if_any ["sad2eyes", "sad2brow"]

    image side jasmine = LayeredImageProxy("jasmine", Transform(xpos=0.08, yanchor=0.45))

    layeredimage grusha:
        zoom 0.5
        xalign 0.5
        yanchor 0.63
        ypos 1.0
        group body:
            attribute neutral "grusha_body_neutral" default
            attribute uniform "grusha_body_uniform"

        group eyes auto:
            attribute neutraleyes default
            attribute sad "grusha_eyes_sadeyes"
            attribute happy "grusha_eyes_happyeyes"
            attribute surprised "grusha_eyes_surprisedeyes"
            attribute thinking "grusha_eyes_closedeyes"
            attribute angrybrow "grusha_eyes_angryeyes"
            attribute sadbrow "grusha_eyes_sadeyes"
            attribute sad2brow "grusha_eyes_sad2eyes"
            attribute angry "grusha_eyes_angryeyes"
            attribute closedbrow "grusha_eyes_closedeyes"
            attribute happybrow "grusha_eyes_happyeyes"

        group eyebrows auto:
            attribute neutraleyebrows default
            attribute sad "grusha_eyebrows_sadeyebrows"
            attribute happy "grusha_eyebrows_happyeyebrows"
            attribute surprised "grusha_eyebrows_surprisedeyebrows"
            attribute thinking "grusha_eyebrows_neutraleyebrows"
            attribute angrybrow "grusha_eyebrows_angryeyebrows"
            attribute sadbrow "grusha_eyebrows_sadeyebrows"
            attribute sad2brow "grusha_eyebrows_sadeyebrows"
            attribute angry "grusha_eyebrows_angryeyebrows"
            attribute closedbrow "grusha_eyebrows_neutraleyebrows"
            attribute happybrow "grusha_eyebrows_happyeyebrows"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "grusha_mouth_sadmouth"
            attribute happy "grusha_mouth_happymouth"
            attribute angry "grusha_mouth_angrymouth"
            attribute surprised "grusha_mouth_surprisedmouth"
            attribute thinking "grusha_mouth_frownmouth"

        group tears auto

        group sweat auto

        group shadow auto

        group tired auto

        group anger auto:
            attribute angry "grusha_anger_anger"

        group blush auto

        group hat auto

        group cry auto

        group scarf auto:
            attribute scarf default
            attribute noscarf "red_eyeshine_blank"

        always "grusha_scarf_scarf" if_not ["noscarf"]

        always "grusha_eyesparkles" if_not ["sad2brow", "happybrow", "closedbrow", "closedeyes", "deadeyes", "happyeyes", "thinking", "happy", "sad2eyes"] 
        always "grusha_eyesparkles_sad2eyes" if_any ["sad2eyes", "sad2brow"]

    image side grusha = LayeredImageProxy("grusha", Transform(xpos=0.08, yanchor=0.45))

    layeredimage iris:
        zoom 0.5
        xalign 0.5
        yanchor 0.63
        ypos 1.0
        group body:
            attribute neutral "iris_body_neutral" default
            attribute uniform "iris_body_uniform" 
            attribute champion "iris_body_champion"

        group eyes auto:
            attribute neutraleyes default
            attribute sad "iris_eyes_sadeyes"
            attribute happy "iris_eyes_happyeyes"
            attribute surprised "iris_eyes_surprisedeyes"
            attribute thinking "iris_eyes_closedeyes"
            attribute angrybrow "iris_eyes_angryeyes"
            attribute sadbrow "iris_eyes_sadeyes"
            attribute angry "iris_eyes_angryeyes"
            attribute closedbrow "iris_eyes_closedeyes"
            attribute happybrow "iris_eyes_happyeyes"
            attribute surprisedbrow "iris_eyes_surprisedeyes"

        group eyebrows auto:
            attribute neutraleyebrows default
            attribute sad "iris_eyebrows_sadeyebrows"
            attribute happy "iris_eyebrows_happyeyebrows"
            attribute surprised "iris_eyebrows_surprisedeyebrows"
            attribute thinking "iris_eyebrows_neutraleyebrows"
            attribute angrybrow "iris_eyebrows_angryeyebrows"
            attribute sadbrow "iris_eyebrows_sadeyebrows"
            attribute angry "iris_eyebrows_angryeyebrows"
            attribute closedbrow "iris_eyebrows_neutraleyebrows"
            attribute happybrow "iris_eyebrows_happyeyebrows"
            attribute surprisedbrow "iris_eyebrows_surprisedeyebrows"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "iris_mouth_sadmouth"
            attribute happy "iris_mouth_happymouth"
            attribute angry "iris_mouth_angrymouth"
            attribute surprised "iris_mouth_surprisedmouth"
            attribute thinking "iris_mouth_frownmouth"

        group tears auto

        group sweat auto

        group shadow auto

        group tired auto

        group anger auto:
            attribute angry "iris_anger_anger"

        group blush auto

        group cry auto

        always "iris_eyesparkles" if_not ["happybrow", "closedbrow", "closedeyes", "deadeyes", "happyeyes", "poweredeyes", "thinking", "happy"] 

    image side iris = LayeredImageProxy("iris", Transform(xpos=0.08, yanchor=0.45))

    layeredimage mom:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        always "mom_body"

        group eyes auto:
            attribute neutraleyes default
            attribute sad "mom_eyes_sadeyes"
            attribute angry "mom_eyes_angryeyes"
            attribute happy "mom_eyes_happyeyes"
            attribute surprised "mom_eyes_surprisedeyes"

        group eyebrows auto:
            attribute neutraleyebrows default
            attribute sad "mom_eyebrows_sadeyebrows"
            attribute angry "mom_eyebrows_angryeyebrows"
            attribute happy "mom_eyebrows_happyeyebrows"
            attribute surprised "mom_eyebrows_surprisedeyebrows"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "mom_mouth_sadmouth"
            attribute angry "mom_mouth_angrymouth"
            attribute happy "mom_mouth_happymouth"
            attribute surprised "mom_mouth_surprisedmouth"

        group blush auto:
            attribute blush "mom_blush_blush"

    layeredimage oak:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        always "oak_body"

        group eyes auto if_not ["angrybrow", "angry"]:
            attribute neutraleyes default
            attribute sad "oak_eyes_sadeyes"
            attribute angry "oak_eyes_angryeyes"
            attribute happy "oak_eyes_happyeyes"
            attribute surprised "oak_eyes_surprisedeyes"
            attribute surprisedbrow "oak_eyes_surprisedeyes"
            attribute closedbrow "oak_eyes_closedeyes"
            attribute thinking "oak_eyes_closedeyes"
            attribute sadbrow "oak_eyes_sadeyes"

        group eyebrows auto if_not ["angrybrow", "angry"]:
            attribute neutraleyebrows default
            attribute sad "oak_eyebrows_sadeyebrows"
            attribute angry "oak_eyebrows_angryeyebrows"
            attribute happy "oak_eyebrows_happyeyebrows"
            attribute surprised "oak_eyebrows_surprisedeyebrows"
            attribute surprisedbrow "oak_eyebrows_surprisedeyebrows"
            attribute thinking "oak_eyebrows_neutraleyebrows"
            attribute closedbrow "oak_eyebrows_neutraleyebrows"
            attribute sadbrow "oak_eyebrows_sadeyebrows"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "oak_mouth_sadmouth"
            attribute angry "oak_mouth_angrymouth"
            attribute happy "oak_mouth_happymouth"
            attribute surprised "oak_mouth_surprisedmouth"
            attribute thinking "oak_mouth_neutralmouth"

        group brow:
            attribute angrybrow "oak_brow_angrybrow"
            attribute angry "oak_brow_angrybrow"

    image oakbg = Crop((0, 0, 1000, 800), "oak", yalign=0.422, zoom=0.1)

    layeredimage blue:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body:
            attribute neutral "blue_body_neutral" default
            attribute uniform "blue_body_uniform" 

        group brow auto:
            attribute neutralbrow default
            attribute sad "blue_brow_sadbrow"
            attribute angry "blue_brow_angrybrow"
            attribute happy "blue_brow_happybrow"
            attribute surprised "blue_brow_surprisedbrow"
            attribute cocky "blue_brow_angrybrow"
            attribute thinking "blue_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "blue_mouth_sadmouth"
            attribute angry "blue_mouth_angrymouth"
            attribute happy "blue_mouth_happymouth"
            attribute surprised "blue_mouth_surprisedmouth"
            attribute cocky "blue_mouth_neutralmouth"
            attribute thinking "blue_mouth_frownmouth"

        group sweat auto:
            attribute sweat "blue_sweat"

    image side blue = LayeredImageProxy("blue", Transform(xpos=0.05, yanchor=0.35))

    layeredimage sonia:
        zoom 0.46
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body:
            attribute neutral "sonia_body_neutral" default
            attribute uniform "sonia_body_uniform" 

        group brow auto:
            attribute neutralbrow default
            attribute sad "sonia_brow_sadbrow"
            attribute angry "sonia_brow_angrybrow"
            attribute happy "sonia_brow_happybrow"
            attribute surprised "sonia_brow_surprisedbrow"
            attribute thinking "sonia_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "sonia_mouth_sadmouth"
            attribute angry "sonia_mouth_angrymouth"
            attribute happy "sonia_mouth_happymouth"
            attribute surprised "sonia_mouth_surprisedmouth"
            attribute thinking "sonia_mouth_frownmouth"

        group blush auto

    image side sonia = LayeredImageProxy("sonia", Transform(xpos=0.05, yanchor=0.35, xzoom=-1))

    layeredimage silver:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body:
            attribute neutral "silver_body_neutral" default
            attribute uniform "silver_body_uniform" 

        group brow auto:
            attribute neutralbrow default
            attribute sad "silver_brow_sadbrow"
            attribute angry "silver_brow_angrybrow"
            attribute happy "silver_brow_happybrow"
            attribute surprised "silver_brow_surprisedbrow"
            attribute thinking "silver_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "silver_mouth_sadmouth"
            attribute angry "silver_mouth_angrymouth"
            attribute happy "silver_mouth_happymouth"
            attribute surprised "silver_mouth_surprisedmouth"
            attribute thinking "silver_mouth_neutralmouth"

    image side silver = LayeredImageProxy("silver", Transform(xpos=0.05, yanchor=0.35))

    layeredimage brawly:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body:
            attribute neutral "brawly_body_neutral" default
            attribute uniform "brawly_body_uniform" 

        group brow auto:
            attribute neutralbrow default
            attribute sad "brawly_brow_sadbrow"
            attribute angry "brawly_brow_angrybrow"
            attribute happy "brawly_brow_happybrow"
            attribute surprised "brawly_brow_surprisedbrow"
            attribute thinking "brawly_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "brawly_mouth_sadmouth"
            attribute angry "brawly_mouth_angrymouth"
            attribute happy "brawly_mouth_happymouth"
            attribute surprised "brawly_mouth_surprisedmouth"
            attribute thinking "brawly_mouth_frownmouth"

    image side brawly = LayeredImageProxy("brawly", Transform(xpos=0.08, yanchor=0.35, xzoom=-1))

    layeredimage roxanne:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body:
            attribute neutral "roxanne_body_neutral" default
            attribute uniform "roxanne_body_uniform" 

        group brow auto:
            attribute neutralbrow default
            attribute sad "roxanne_brow_sadbrow"
            attribute angry "roxanne_brow_angrybrow"
            attribute happy "roxanne_brow_happybrow"
            attribute surprised "roxanne_brow_surprisedbrow"
            attribute thinking "roxanne_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "roxanne_mouth_sadmouth"
            attribute angry "roxanne_mouth_angrymouth"
            attribute happy "roxanne_mouth_happymouth"
            attribute surprised "roxanne_mouth_surprisedmouth"
            attribute thinking "roxanne_mouth_frownmouth"

    image side roxanne = LayeredImageProxy("roxanne", Transform(xpos=0.08, yanchor=0.35, xzoom=-1))

    layeredimage face:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body:
            attribute neutral "face_body_neutral" default
            attribute uniform "face_body_uniform" 

        group brow auto:
            attribute neutralbrow default
            attribute sad "face_brow_sadbrow"
            attribute angry "face_brow_angrybrow"
            attribute happy "face_brow_happybrow"
            attribute surprised "face_brow_surprisedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "face_mouth_sadmouth"
            attribute angry "face_mouth_angrymouth"
            attribute happy "face_mouth_happymouth"
            attribute surprised "face_mouth_surprisedmouth"
    
        group blush:
            attribute blush "face_blush"

    image side face = LayeredImageProxy("face", Transform(xpos=0.08, yanchor=0.35))

    layeredimage mace:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        always "mace_body"

        group brow auto:
            attribute neutralbrow default
            attribute sad "mace_brow_sadbrow"
            attribute angry "mace_brow_angrybrow"
            attribute happy "mace_brow_happybrow"
            attribute surprised "mace_brow_surprisedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "mace_mouth_sadmouth"
            attribute angry "mace_mouth_angrymouth"
            attribute happy "mace_mouth_happymouth"
            attribute surprised "mace_mouth_surprisedmouth"

        group sweat auto:
            attribute sweat "mace_sweat"

    image side mace = LayeredImageProxy("mace", Transform(xpos=0.08, yanchor=0.35))

    layeredimage falkner:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body:
            attribute neutral "falkner_body_neutral" default
            attribute uniform "falkner_body_uniform" 

        group brow auto:
            attribute neutralbrow default
            attribute sad "falkner_brow_sadbrow"
            attribute angry "falkner_brow_angrybrow"
            attribute happy "falkner_brow_happybrow"
            attribute surprised "falkner_brow_surprisedbrow"
            attribute thinking "falkner_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "falkner_mouth_sadmouth"
            attribute angry "falkner_mouth_angrymouth"
            attribute happy "falkner_mouth_happymouth"
            attribute surprised "falkner_mouth_surprisedmouth"
            attribute thinking "falkner_mouth_frownmouth"

    image side falkner = LayeredImageProxy("falkner", Transform(xpos=0.05, yanchor=0.35, xzoom=-1))

    layeredimage leaf:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body:
            attribute neutral "leaf_body_neutral" default
            attribute uniform "leaf_body_uniform" 

        group brow auto:
            attribute neutralbrow default
            attribute sad "leaf_brow_sadbrow"
            attribute angry "leaf_brow_angrybrow"
            attribute happy "leaf_brow_happybrow"
            attribute surprised "leaf_brow_surprisedbrow"
            attribute flirt "leaf_brow_flirtbrow"
            attribute embarrassed "leaf_brow_embarrassedbrow"
            attribute thinking "leaf_brow_closedbrow"
            attribute sarcastic "leaf_brow_flirtbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "leaf_mouth_sadmouth"
            attribute angry "leaf_mouth_angrymouth"
            attribute happy "leaf_mouth_happymouth"
            attribute surprised "leaf_mouth_surprisedmouth"
            attribute flirt "leaf_mouth_flirtmouth"
            attribute embarrassed "leaf_mouth_embarrassedmouth"
            attribute thinking "leaf_mouth_frownmouth"
            attribute sarcastic "leaf_mouth_talkingmouth"

        group blush auto

    image side leaf = LayeredImageProxy("leaf", Transform(xpos=0.08, yanchor=0.35, xzoom=-1))

    layeredimage ethan:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body:
            attribute neutral "ethan_body_neutral" default
            attribute uniform "ethan_body_uniform"

        group eyes auto:
            attribute neutraleyes default
            attribute noeyes "red_eyeshine_blank"
            attribute disappointed "ethan_eyes_closedeyes"
            attribute disappointedbrow "ethan_eyes_closedeyes"
            attribute closedbrow "ethan_eyes_closedeyes"
            attribute sad "ethan_eyes_sadeyes"
            attribute happy "ethan_eyes_happyeyes"
            attribute surprised "ethan_eyes_surprisedeyes"
            attribute surprisedbrow "ethan_eyes_surprisedeyes"
            attribute thinking "ethan_eyes_closedeyes"
            attribute angrybrow "ethan_eyes_angryeyes"
            attribute sadbrow "ethan_eyes_sadeyes"
            attribute sad2brow "ethan_eyes_sad2eyes"
            attribute angry "ethan_eyes_angryeyes"
            attribute angry2brow "ethan_eyes_angry2eyes"
            attribute closedbrow "ethan_eyes_closedeyes"
            attribute happybrow "ethan_eyes_happyeyes"

        group eyebrows auto:
            attribute neutraleyebrows default
            attribute closedbrow "ethan_eyebrows_neutraleyebrows"
            attribute disappointed "ethan_eyebrows_neutraleyebrows"
            attribute disappointedbrow "ethan_eyebrows_neutraleyebrows"
            attribute sad "ethan_eyebrows_sadeyebrows"
            attribute happy "ethan_eyebrows_happyeyebrows"
            attribute surprised "ethan_eyebrows_surprisedeyebrows"
            attribute surprisedbrow "ethan_eyebrows_surprisedeyebrows"
            attribute thinking "ethan_eyebrows_neutraleyebrows"
            attribute angrybrow "ethan_eyebrows_angryeyebrows"
            attribute sadbrow "ethan_eyebrows_sadeyebrows"
            attribute sad2brow "ethan_eyebrows_sadeyebrows"
            attribute angry2brow "ethan_eyebrows_angryeyebrows"
            attribute angry "ethan_eyebrows_angryeyebrows"
            attribute closedbrow "ethan_eyebrows_neutraleyebrows"
            attribute happybrow "ethan_eyebrows_happyeyebrows"
            attribute confused "ethan_eyebrows_confusedeyebrows"

        group mouth auto:
            attribute neutralmouth default
            attribute disappointed "ethan_mouth_talkingmouth"
            attribute sad "ethan_mouth_sadmouth"
            attribute happy "ethan_mouth_happymouth"
            attribute angry "ethan_mouth_angrymouth"
            attribute surprised "ethan_mouth_surprisedmouth"
            attribute thinking "ethan_mouth_frownmouth"
            attribute confused "ethan_mouth_talking2mouth"

        group tears auto

        group sweat auto

        group tired auto

        group anger auto:
            attribute angry "ethan_anger_anger"

        group blush auto

        group hat auto

        group cry auto

        group shadow auto

        group eyeshine auto:
            attribute noshine "red_eyeshine_blank"

        always "ethan_eyesparkles" if_not ["noshine", "sad2brow", "happybrow", "closedbrow", "closedeyes", "deadeyes", "happyeyes", "thinking", "happy", "sad2eyes", "angry2eyes", "angry2brow"] 
        always "ethan_eyesparkles_sad2eyes" if_any ["sad2eyes", "sad2brow"]

    image side ethan = LayeredImageProxy("ethan", Transform(xpos=0.09, yanchor=0.35))
    image side ethan night = LayeredImageProxy("ethan", Transform(xpos=0.09, yanchor=0.35, matrixcolor=BrightnessMatrix(-0.2) * ContrastMatrix(1.3)))
    
    layeredimage calem:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body:
            attribute neutral "calem_body_neutral" default
            attribute uniform "calem_body_uniform" 

        group brow auto:
            attribute neutralbrow default
            attribute sad "calem_brow_sadbrow"
            attribute angry "calem_brow_angrybrow"
            attribute happy "calem_brow_happybrow"
            attribute surprised "calem_brow_surprisedbrow"
            attribute thinking "calem_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "calem_mouth_sadmouth"
            attribute angry "calem_mouth_angrymouth"
            attribute happy "calem_mouth_happymouth"
            attribute surprised "calem_mouth_surprisedmouth"
            attribute thinking "calem_mouth_neutralmouth"

    image side calem = LayeredImageProxy("calem", Transform(xpos=0.08, yanchor=0.35))

    layeredimage hilbert:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body:
            attribute neutral "hilbert_body_neutral" default
            attribute uniform "hilbert_body_uniform" 

        group brow auto:
            attribute neutralbrow default
            attribute sad "hilbert_brow_sadbrow"
            attribute angry "hilbert_brow_angrybrow"
            attribute happy "hilbert_brow_happybrow"
            attribute surprised "hilbert_brow_surprisedbrow"
            attribute thinking "hilbert_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "hilbert_mouth_sadmouth"
            attribute angry "hilbert_mouth_angrymouth"
            attribute happy "hilbert_mouth_happymouth"
            attribute surprised "hilbert_mouth_surprisedmouth"
            attribute thinking "hilbert_mouth_neutralmouth"

    image side hilbert = LayeredImageProxy("hilbert", Transform(xpos=0.07, yanchor=0.35))

    layeredimage brendan:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body:
            attribute neutral "brendan_body_neutral" default
            attribute uniform "brendan_body_uniform" 

        group brow auto:
            attribute neutralbrow default
            attribute sad "brendan_brow_sadbrow"
            attribute angry "brendan_brow_angrybrow"
            attribute happy "brendan_brow_happybrow"
            attribute surprised "brendan_brow_surprisedbrow"
            attribute thinking "brendan_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "brendan_mouth_sadmouth"
            attribute angry "brendan_mouth_angrymouth"
            attribute happy "brendan_mouth_happymouth"
            attribute surprised "brendan_mouth_surprisedmouth"
            attribute thinking "brendan_mouth_frownmouth"

        group sweat auto

    image side brendan = LayeredImageProxy("brendan", Transform(xpos=0.08, yanchor=0.35, xzoom=-1))

    layeredimage may:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body:
            attribute neutral "may_body_neutral" default
            attribute uniform "may_body_uniform" 

        group brow auto:
            attribute neutralbrow default
            attribute sad "may_brow_sadbrow"
            attribute angry "may_brow_angrybrow"
            attribute happy "may_brow_happybrow"
            attribute surprised "may_brow_surprisedbrow"
            attribute thinking "may_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "may_mouth_sadmouth"
            attribute angry "may_mouth_angrymouth"
            attribute happy "may_mouth_happymouth"
            attribute surprised "may_mouth_surprisedmouth"
            attribute thinking "may_mouth_frownmouth"

    image side may = LayeredImageProxy("may", Transform(xpos=0.08, yanchor=0.35))

    layeredimage flannery:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body:
            attribute neutral "flannery_body_neutral" default
            attribute uniform "flannery_body_uniform" 

        group brow auto:
            attribute neutralbrow default
            attribute sad "flannery_brow_sadbrow"
            attribute angry "flannery_brow_angrybrow"
            attribute happy "flannery_brow_happybrow"
            attribute surprised "flannery_brow_surprisedbrow"
            attribute thinking "flannery_brow_closedbrow"
            attribute tired "flannery_brow_tiredbrow"
            attribute furious "flannery_brow_furiousbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "flannery_mouth_sadmouth"
            attribute angry "flannery_mouth_angrymouth"
            attribute happy "flannery_mouth_happymouth"
            attribute surprised "flannery_mouth_surprisedmouth"
            attribute thinking "flannery_mouth_tiredmouth"
            attribute tired "flannery_mouth_tiredmouth"
            attribute furious "flannery_mouth_furiousmouth"

        group sweat auto
        group veins auto

    image side flannery = LayeredImageProxy("flannery", Transform(xpos=0.08, yanchor=0.35))

    layeredimage whitney:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body:
            attribute neutral "whitney_body_neutral" default
            attribute uniform "whitney_body_uniform" 

        group brow auto:
            attribute neutralbrow default
            attribute sad "whitney_brow_sadbrow"
            attribute angry "whitney_brow_angrybrow"
            attribute happy "whitney_brow_happybrow"
            attribute surprised "whitney_brow_surprisedbrow"
            attribute thinking "whitney_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "whitney_mouth_sadmouth"
            attribute angry "whitney_mouth_angrymouth"
            attribute happy "whitney_mouth_happymouth"
            attribute surprised "whitney_mouth_surprisedmouth"
            attribute thinking "whitney_mouth_frownmouth"

    image side whitney = LayeredImageProxy("whitney", Transform(xpos=0.08, yanchor=0.35))

    layeredimage sabrina:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body:
            attribute neutral "sabrina_body_neutral" default
            attribute uniform "sabrina_body_uniform"
            attribute neutralpowered "sabrina_body_neutralpowered"
            attribute uniformpowered "sabrina_body_uniformpowered" 

        group brow auto:
            attribute neutralbrow default
            attribute happy "sabrina_brow_happybrow"
            attribute angrybrow "sabrina_brow_poweredbrow"
            attribute sad "sabrina_brow_sadbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute happy "sabrina_mouth_happymouth"
            attribute sad "sabrina_mouth_sadmouth"

        group blush auto

    layeredimage serena:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body:
            attribute neutral "serena_body_neutral" default
            attribute uniform "serena_body_uniform" 

        group brow auto:
            attribute neutralbrow default
            attribute sad "serena_brow_sadbrow"
            attribute angry "serena_brow_angrybrow"
            attribute happy "serena_brow_happybrow"
            attribute surprised "serena_brow_surprisedbrow"
            attribute thinking "serena_brow_closedbrow"
            attribute pout "serena_brow_poutbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "serena_mouth_sadmouth"
            attribute angry "serena_mouth_angrymouth"
            attribute happy "serena_mouth_happymouth"
            attribute surprised "serena_mouth_surprisedmouth"
            attribute thinking "serena_mouth_frownmouth"
            attribute pout "serena_mouth_poutmouth"

        group blush auto
    
    image side serena = LayeredImageProxy("serena", Transform(xpos=0.08, yanchor=0.35))

    layeredimage cheren:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body:
            attribute neutral "cheren_body_neutral" default
            attribute uniform "cheren_body_uniform"

        group eyes auto:
            attribute neutraleyes default
            attribute noeyes "red_eyeshine_blank"
            attribute disappointed "cheren_eyes_disappointedeyes"
            attribute disappointedbrow "cheren_eyes_disappointedeyes"
            attribute closedbrow "cheren_eyes_disappointedeyes"
            attribute sad "cheren_eyes_sadeyes"
            attribute happy "cheren_eyes_happyeyes"
            attribute surprised "cheren_eyes_surprisedeyes"
            attribute surprisedbrow "cheren_eyes_surprisedeyes"
            attribute thinking "cheren_eyes_disappointedeyes"
            attribute angrybrow "cheren_eyes_angryeyes"
            attribute sadbrow "cheren_eyes_sadeyes"
            attribute sad2brow "cheren_eyes_sad2eyes"
            attribute angry "cheren_eyes_angryeyes"
            attribute angry2brow "cheren_eyes_angry2eyes"
            attribute closedbrow "cheren_eyes_disappointedeyes"
            attribute happybrow "cheren_eyes_happyeyes"

        group eyebrows auto:
            attribute neutraleyebrows default
            attribute closedbrow "cheren_eyebrows_neutraleyebrows"
            attribute disappointed "cheren_eyebrows_neutraleyebrows"
            attribute disappointedbrow "cheren_eyebrows_neutraleyebrows"
            attribute sad "cheren_eyebrows_sadeyebrows"
            attribute happy "cheren_eyebrows_happyeyebrows"
            attribute surprised "cheren_eyebrows_surprisedeyebrows"
            attribute surprisedbrow "cheren_eyebrows_surprisedeyebrows"
            attribute thinking "cheren_eyebrows_neutraleyebrows"
            attribute angrybrow "cheren_eyebrows_angryeyebrows"
            attribute sadbrow "cheren_eyebrows_sadeyebrows"
            attribute sad2brow "cheren_eyebrows_sadeyebrows"
            attribute angry2brow "cheren_eyebrows_angryeyebrows"
            attribute angry "cheren_eyebrows_angryeyebrows"
            attribute closedbrow "cheren_eyebrows_neutraleyebrows"
            attribute happybrow "cheren_eyebrows_happyeyebrows"

        group mouth auto:
            attribute neutralmouth default
            attribute disappointed "cheren_mouth_disappointedmouth"
            attribute sad "cheren_mouth_sadmouth"
            attribute happy "cheren_mouth_happymouth"
            attribute angry "cheren_mouth_angrymouth"
            attribute surprised "cheren_mouth_surprisedmouth"
            attribute thinking "cheren_mouth_neutralmouth"

        group tears auto

        group sweat auto

        group tired auto

        group anger auto:
            attribute angry "cheren_anger_anger"

        group blush auto

        group hat auto

        group cry auto

        group shadow auto

        group eyeshine auto:
            attribute noshine "red_eyeshine_blank"

        always "cheren_eyesparkles" if_not ["noshine", "sad2brow", "happybrow", "closedbrow", "closedeyes", "deadeyes", "happyeyes", "thinking", "happy", "sad2eyes", "angry2eyes", "angry2brow", "sadeyes", "sadbrow", "sad"] 
        always "cheren_eyesparkles_sad2eyes" if_any ["sad2eyes", "sad2brow"]
        always "cheren_eyesparkles_sadeyes" if_any ["sadeyes", "sadbrow", "sad"]

    image side cheren = LayeredImageProxy("cheren", Transform(xpos=0.08, yanchor=0.35))
    image side cheren night = LayeredImageProxy("cheren", Transform(xpos=0.08, yanchor=0.35, matrixcolor=BrightnessMatrix(-0.2) * ContrastMatrix(1.3)))

    layeredimage misty:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body:
            attribute neutral "misty_body_neutral" default
            attribute uniform "misty_body_uniform" 

        group brow auto:
            attribute neutralbrow default
            attribute sad "misty_brow_sadbrow"
            attribute angry "misty_brow_angrybrow"
            attribute happy "misty_brow_happybrow"
            attribute surprised "misty_brow_surprisedbrow"
            attribute thinking "misty_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "misty_mouth_sadmouth"
            attribute angry "misty_mouth_angrymouth"
            attribute happy "misty_mouth_happymouth"
            attribute surprised "misty_mouth_surprisedmouth"
            attribute thinking "misty_mouth_neutralmouth"

        group sweat auto
    
    image side misty = LayeredImageProxy("misty", Transform(xpos=0.08, yanchor=0.35))

    layeredimage bianca:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body:
            attribute neutral "bianca_body_neutral" default
            attribute uniform "bianca_body_uniform" 

        group brow auto:
            attribute neutralbrow default
            attribute happy "bianca_brow_happybrow"
            attribute surprised "bianca_brow_surprisedbrow"
            attribute angrybrow "bianca_brow_surprisedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute happy "bianca_mouth_happymouth"
            attribute surprised "bianca_mouth_surprisedmouth"

        always "bianca_glasses_glasses"

    image side bianca = LayeredImageProxy("bianca", Transform(xpos=0.08, yanchor=0.35))

    layeredimage dawn:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body:
            attribute neutral "dawn_body_neutral" default
            attribute uniform "dawn_body_uniform" 

        group brow auto:
            attribute neutralbrow default
            attribute sad "dawn_brow_sadbrow"
            attribute angry "dawn_brow_angrybrow"
            attribute happy "dawn_brow_happybrow"
            attribute surprised "dawn_brow_surprisedbrow"
            attribute thinking "dawn_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "dawn_mouth_sadmouth"
            attribute angry "dawn_mouth_angrymouth"
            attribute happy "dawn_mouth_happymouth"
            attribute surprised "dawn_mouth_surprisedmouth"
            attribute thinking "dawn_mouth_frownmouth"

    image side dawn = LayeredImageProxy("dawn", Transform(xpos=0.08, yanchor=0.35))

    layeredimage nate:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body:
            attribute neutral "nate_body_neutral" default
            attribute uniform "nate_body_uniform" 

        group brow auto:
            attribute neutralbrow default
            attribute sad "nate_brow_sadbrow"
            attribute angry "nate_brow_angrybrow"
            attribute happy "nate_brow_happybrow"
            attribute surprised "nate_brow_surprisedbrow"
            attribute thinking "nate_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "nate_mouth_sadmouth"
            attribute angry "nate_mouth_angrymouth"
            attribute happy "nate_mouth_happymouth"
            attribute surprised "nate_mouth_surprisedmouth"
            attribute thinking "nate_mouth_frownmouth"

        group sweat auto

    image side nate = LayeredImageProxy("nate", Transform(xpos=0.08, yanchor=0.35))

    layeredimage rosa:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body:
            attribute neutral "rosa_body_neutral" default
            attribute uniform "rosa_body_uniform" 

        group brow auto:
            attribute neutralbrow default
            attribute sad "rosa_brow_sadbrow"
            attribute angry "rosa_brow_angrybrow"
            attribute happy "rosa_brow_happybrow"
            attribute surprised "rosa_brow_surprisedbrow"
            attribute thinking "rosa_brow_happybrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "rosa_mouth_sadmouth"
            attribute angry "rosa_mouth_angrymouth"
            attribute happy "rosa_mouth_happymouth"
            attribute surprised "rosa_mouth_surprisedmouth"
            attribute thinking "rosa_mouth_frownmouth"

        group sweat auto

    image side rosa = LayeredImageProxy("rosa", Transform(xpos=0.08, yanchor=0.35))

    layeredimage bea:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body:
            attribute neutral "bea_body_neutral" default
            attribute uniform "bea_body_uniform" 

        group brow auto:
            attribute neutralbrow default
            attribute sad "bea_brow_sadbrow"
            attribute angry "bea_brow_angrybrow"
            attribute happy "bea_brow_happybrow"
            attribute surprised "bea_brow_surprisedbrow"
            attribute thinking "bea_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "bea_mouth_sadmouth"
            attribute angry "bea_mouth_angrymouth"
            attribute happy "bea_mouth_happymouth"
            attribute surprised "bea_mouth_surprisedmouth"
            attribute thinking "bea_mouth_neutralmouth"

        group sweat auto
    
    image side bea = LayeredImageProxy("bea", Transform(xpos=0.08, yanchor=0.35))

    layeredimage nessa:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body:
            attribute neutral "nessa_body_neutral" default
            attribute uniform "nessa_body_uniform" 

        group brow auto:
            attribute neutralbrow default
            attribute sad "nessa_brow_sadbrow"
            attribute angry "nessa_brow_angrybrow"
            attribute happy "nessa_brow_happybrow"
            attribute surprised "nessa_brow_surprisedbrow"
            attribute thinking "nessa_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "nessa_mouth_sadmouth"
            attribute angry "nessa_mouth_angrymouth"
            attribute happy "nessa_mouth_happymouth"
            attribute surprised "nessa_mouth_surprisedmouth"
            attribute thinking "nessa_mouth_frownmouth"

    image side nessa = LayeredImageProxy("nessa", Transform(xpos=0.08, yanchor=0.35))

    layeredimage hilda:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body:
            attribute neutral "hilda_body_neutral" default
            attribute uniform "hilda_body_uniform" 

        group brow auto:
            attribute neutralbrow default
            attribute sad "hilda_brow_sadbrow"
            attribute angry "hilda_brow_angrybrow"
            attribute happy "hilda_brow_happybrow"
            attribute surprised "hilda_brow_surprisedbrow"
            attribute thinking "hilda_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "hilda_mouth_sadmouth"
            attribute angry "hilda_mouth_angrymouth"
            attribute happy "hilda_mouth_happymouth"
            attribute surprised "hilda_mouth_surprisedmouth"
            attribute thinking "hilda_mouth_frownmouth"

        group sweat auto

        group veins auto

    image side hilda = LayeredImageProxy("hilda", Transform(xpos=0.08, yanchor=0.35))

    layeredimage gardenia:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body:
            attribute neutral "gardenia_body_neutral" default
            attribute uniform "gardenia_body_uniform" 

        group brow auto:
            attribute neutralbrow default
            attribute sad "gardenia_brow_sadbrow"
            attribute angry "gardenia_brow_angrybrow"
            attribute happy "gardenia_brow_happybrow"
            attribute surprised "gardenia_brow_surprisedbrow"
            attribute cocky "gardenia_brow_angrybrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "gardenia_mouth_sadmouth"
            attribute angry "gardenia_mouth_angrymouth"
            attribute happy "gardenia_mouth_happymouth"
            attribute surprised "gardenia_mouth_surprisedmouth"
            attribute cocky "gardenia_mouth_happymouth"

    layeredimage skyla:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body:
            attribute neutral "skyla_body_neutral" default
            attribute uniform "skyla_body_uniform" 

        group brow auto:
            attribute neutralbrow default
            attribute sad "skyla_brow_sadbrow"
            attribute angry "skyla_brow_angrybrow"
            attribute happy "skyla_brow_happybrow"
            attribute surprised "skyla_brow_surprisedbrow"
            attribute thinking "skyla_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "skyla_mouth_sadmouth"
            attribute angry "skyla_mouth_angrymouth"
            attribute happy "skyla_mouth_happymouth"
            attribute surprised "skyla_mouth_surprisedmouth"
            attribute thinking "skyla_mouth_frownmouth"

        group sweat auto

    image side skyla = LayeredImageProxy("skyla", Transform(xpos=0.08, yanchor=0.35))

    layeredimage brock:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body:
            attribute neutral "brock_body_neutral" default

    image tinybrock = Crop((0, 0, 1000, 800), "brock", yalign=1.0, zoom=0.1)

    layeredimage erika:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body:
            attribute neutral "erika_body_neutral" default
            attribute uniform "erika_body_uniform" 

        group brow auto:
            attribute neutralbrow default
            attribute sad "erika_brow_sadbrow"
            attribute angry "erika_brow_angrybrow"
            attribute happy "erika_brow_happybrow"
            attribute surprised "erika_brow_surprisedbrow"
            attribute thinking "erika_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "erika_mouth_sadmouth"
            attribute angry "erika_mouth_angrymouth"
            attribute happy "erika_mouth_happymouth"
            attribute surprised "erika_mouth_surprisedmouth"
            attribute thinking "erika_mouth_frownmouth"
    
    image side erika = LayeredImageProxy("erika", Transform(xpos=0.08, yanchor=0.35))

    layeredimage janine:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body:
            attribute neutral "janine_body_neutral" default
            attribute uniform "janine_body_uniform" 

        group brow auto if_not ["koga"]:
            attribute neutralbrow default
            attribute sad "janine_brow_sadbrow"
            attribute angry "janine_brow_angrybrow"
            attribute happy "janine_brow_happybrow"
            attribute surprised "janine_brow_surprisedbrow"
            attribute thinking "janine_brow_closedbrow"

        group mouth auto if_not ["koga"]:
            attribute neutralmouth default
            attribute sad "janine_mouth_sadmouth"
            attribute angry "janine_mouth_angrymouth"
            attribute happy "janine_mouth_happymouth"
            attribute surprised "janine_mouth_surprisedmouth"
            attribute thinking "janine_mouth_neutralmouth"

        group blush auto

        group face auto
    
    image side janine = LayeredImageProxy("janine", Transform(xpos=0.08, yanchor=0.35))

    layeredimage roughneck:
        zoom 0.3
        xalign 0.5
        yanchor 1.0
        ypos 1.0

        group body:
            attribute neutral "roughneck_body_neutral" default
            attribute angry "roughneck_body_angry"
            attribute surprised "roughneck_body_surprised"
            attribute happy "roughneck_body_happy"

    image roughneck2 = LayeredImageProxy("roughneck")
    image roughneck3 = LayeredImageProxy("roughneck")

    #STAFF AFTER THIS POINT

    layeredimage kris:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body:
            attribute neutral "kris_body_neutral" default

        group brow auto:
            attribute neutralbrow default
            attribute sad "kris_brow_sadbrow"
            attribute angry "kris_brow_angrybrow"
            attribute happy "kris_brow_happybrow"
            attribute surprised "kris_brow_surprisedbrow"
            attribute thinking "kris_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "kris_mouth_sadmouth"
            attribute angry "kris_mouth_angrymouth"
            attribute happy "kris_mouth_happymouth"
            attribute surprised "kris_mouth_surprisedmouth"
            attribute thinking "kris_mouth_angrymouth"

        always "kris_glasses_glasses"

    layeredimage lenora:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body:
            attribute neutral "lenora_body_neutral" default

    image lenorabg = Crop((0, 0, 1000, 800), "lenora", yalign=0.422, zoom=0.1)

    layeredimage blaine:
        zoom 0.3
        xalign 0.5
        yanchor 1.0
        ypos 1.0

        group face auto:
            attribute neutral "blaine_face_neutral" default

    image blainebg = Crop((0, 0, 1000, 800), "blaine", ypos = 0.464, zoom=0.1)

    layeredimage wallace:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body:
            attribute neutral "wallace_body_neutral" default

    image wallacebg = Crop((0, 0, 1000, 800), "wallace", yalign=0.422, zoom=0.1)

    layeredimage ramos:
        zoom 0.3
        xalign 0.5
        yanchor 1.0
        ypos 1.0

        group face auto:
            attribute neutral "ramos_face_neutral" default

    image ramosbg = Crop((0, 0, 1000, 800), "ramos", ypos = 0.464, zoom=0.1)

    layeredimage surge:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body:
            attribute neutral "surge_body_neutral" default

        group brow auto:
            attribute neutralbrow default
            attribute sad "surge_brow_sadbrow"
            attribute angry "surge_brow_angrybrow"
            attribute happy "surge_brow_happybrow"
            attribute surprised "surge_brow_surprisedbrow"
            attribute thinking "surge_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "surge_mouth_sadmouth"
            attribute angry "surge_mouth_angrymouth"
            attribute happy "surge_mouth_happymouth"
            attribute surprised "surge_mouth_surprisedmouth"
            attribute thinking "surge_mouth_frownmouth"

        group anger auto

    image surgebg = Crop((0, 0, 1000, 800), "surge", yalign=0.422, zoom=0.1)

    layeredimage melony:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body:
            attribute neutral "melony_body_neutral" default

        group eyes auto:
            attribute neutraleyes default
            attribute sad "melony_eyes_sadeyes"
            attribute happy "melony_eyes_happyeyes"
            attribute surprised "melony_eyes_surprisedeyes"
            attribute thinking "melony_eyes_closedeyes"
            attribute angrybrow "melony_eyes_angryeyes"
            attribute sadbrow "melony_eyes_sadeyes"
            attribute angry "melony_eyes_angryeyes"
            attribute closedbrow "melony_eyes_closedeyes"
            attribute happybrow "melony_eyes_happyeyes"
            attribute surprisedbrow "melony_eyes_surprisedeyes"

        group eyebrows auto:
            attribute neutraleyebrows default
            attribute sad "melony_eyebrows_sadeyebrows"
            attribute happy "melony_eyebrows_happyeyebrows"
            attribute surprised "melony_eyebrows_surprisedeyebrows"
            attribute thinking "melony_eyebrows_neutraleyebrows"
            attribute angrybrow "melony_eyebrows_angryeyebrows"
            attribute sadbrow "melony_eyebrows_sadeyebrows"
            attribute angry "melony_eyebrows_angryeyebrows"
            attribute closedbrow "melony_eyebrows_neutraleyebrows"
            attribute happybrow "melony_eyebrows_happyeyebrows"
            attribute surprisedbrow "melony_eyebrows_surprisedeyebrows"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "melony_mouth_surprisedmouth"
            attribute happy "melony_mouth_happymouth"
            attribute angry "melony_mouth_angrymouth"
            attribute surprised "melony_mouth_surprisedmouth"
            attribute thinking "melony_mouth_frownmouth"

        group tears auto

        group sweat auto

        group shadow auto

        group tired auto

        group anger auto:
            attribute angry "melony_anger_anger"

        group blush auto

        group cry auto

        always "melony_eyesparkles" if_not ["happybrow", "closedbrow", "closedeyes", "deadeyes", "happyeyes", "poweredeyes", "thinking", "happy", "powered"] 

    image melonybg = Crop((0, 0, 1000, 800), "melony", yalign=0.422, zoom=0.1)

    layeredimage marshal:
        yanchor 1.0
        ypos 1.0

        always "marshal_body_neutral"

        group face auto:
            attribute neutral "marshal_face_neutral" default

    image marshalbg = "marshalbackground"

    layeredimage koga:
        yanchor 1.0
        ypos 1.0

        always "koga_body_neutral"

        group face auto:
            attribute neutral "koga_face_neutral" default

    image kogabg = "kogabackground"

    layeredimage bertha:
        yanchor 1.0
        ypos 1.0

        always "bertha_body_neutral"

        group face auto:
            attribute neutral "bertha_face_norm" default

    image berthabg = "berthabackground"

    layeredimage winona:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body:
            attribute neutral "winona_body_neutral" default

        group brow auto:
            attribute neutralbrow default
            attribute sad "winona_brow_sadbrow"
            attribute angry "winona_brow_angrybrow"
            attribute happy "winona_brow_happybrow"
            attribute surprised "winona_brow_surprisedbrow"
            attribute thinking "winona_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "winona_mouth_sadmouth"
            attribute angry "winona_mouth_angrymouth"
            attribute happy "winona_mouth_happymouth"
            attribute surprised "winona_mouth_surprisedmouth"
            attribute thinking "winona_mouth_frownmouth"

    image winonabg = Crop((0, 0, 1000, 800), "winona", yalign=0.422, zoom=0.1)

    layeredimage will:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body:
            attribute neutral "will_body_neutral" default
            attribute uniform "will_body_powered" 

        group brow auto:
            attribute neutralbrow default
            attribute sad "will_brow_sadbrow"
            attribute happy "will_brow_happybrow"
            attribute surprised "will_brow_surprisedbrow"
            attribute thinking "will_brow_closedbrow"
            attribute angrybrow "will_brow_angrybrow"
            attribute sadbrow "will_brow_sadbrow"
            attribute angry "will_brow_angrybrow"
            attribute closedbrow "will_brow_closedbrow"
            attribute happybrow "will_brow_happybrow"
            attribute surprisedbrow "will_brow_surprisedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "will_mouth_surprisedmouth"
            attribute happy "will_mouth_happymouth"
            attribute angry "will_mouth_angrymouth"
            attribute surprised "will_mouth_surprisedmouth"
            attribute thinking "will_mouth_frownmouth"

        group tears auto

        group sweat auto

        group shadow auto

        group tired auto

        group anger auto:
            attribute angry "will_anger_anger"

        group blush auto

        group cry auto

    image willbg = Crop((0, 0, 1000, 800), "will", yalign=0.422, zoom=0.1)

    layeredimage burgh:
        yanchor 1.0
        ypos 1.0

        always "burgh_body_neutral"

        group face auto:
            attribute neutral "burgh_face_norm" default

    image burghbg = "burghbackground"

    layeredimage olivia:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body:
            attribute neutral "olivia_body_neutral" default

    image oliviabg = Crop((0, 0, 1000, 800), "olivia", yalign=0.422, zoom=0.1)

    layeredimage fantina:
        yanchor 1.0
        ypos 1.0

        always "fantina_body_neutral"

        group face auto:
            attribute neutral "fantina_face_norm" default

    image fantinabg = "fantinabackground"

    layeredimage karen:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body:
            attribute neutral "karen_body_neutral" default

        group brow auto:
            attribute neutralbrow default
            attribute sad "karen_brow_sadbrow"
            attribute angry "karen_brow_angrybrow"
            attribute happy "karen_brow_happybrow"
            attribute surprised "karen_brow_surprisedbrow"
            attribute thinking "karen_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "karen_mouth_sadmouth"
            attribute angry "karen_mouth_angrymouth"
            attribute happy "karen_mouth_happymouth"
            attribute surprised "karen_mouth_surprisedmouth"
            attribute thinking "karen_mouth_frownmouth"

    image karenbg = Crop((0, 0, 1000, 800), "karen", yalign=0.422, zoom=0.1)

    layeredimage clair:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body:
            attribute neutral "clair_body_neutral" default

        group brow auto:
            attribute neutralbrow default
            attribute sad "clair_brow_sadbrow"
            attribute angry "clair_brow_angrybrow"
            attribute happy "clair_brow_happybrow"
            attribute surprised "clair_brow_surprisedbrow"
            attribute thinking "clair_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "clair_mouth_sadmouth"
            attribute angry "clair_mouth_angrymouth"
            attribute happy "clair_mouth_happymouth"
            attribute surprised "clair_mouth_surprisedmouth"
            attribute thinking "clair_mouth_frownmouth"
            attribute talkingmouth "clair_mouth_talkingmouth"
            attribute talking2mouth "clair_mouth_talking2mouth"
        
        group blush auto:
            attribute blush "clair_blush_blush"

    image clairbg = Crop((0, 0, 1000, 800), "clair", yalign=0.422, zoom=0.1)

    layeredimage byron:
        yanchor 1.0
        ypos 1.0

        always "byron_body_neutral"

        group face auto:
            attribute neutral "byron_face_norm" default

    image byronbg = "byronbackground"

    layeredimage valerie:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body:
            attribute neutral "valerie_body_neutral" default

        group eyes auto:
            attribute neutraleyes default
            attribute sad "valerie_eyes_sadeyes"
            attribute happy "valerie_eyes_happyeyes"
            attribute surprised "valerie_eyes_surprisedeyes"
            attribute thinking "valerie_eyes_closedeyes"
            attribute angrybrow "valerie_eyes_angryeyes"
            attribute sadbrow "valerie_eyes_sadeyes"
            attribute angry "valerie_eyes_angryeyes"
            attribute closedbrow "valerie_eyes_closedeyes"
            attribute happybrow "valerie_eyes_happyeyes"
            attribute surprisedbrow "valerie_eyes_surprisedeyes"

        group eyebrows auto:
            attribute neutraleyebrows default
            attribute sad "valerie_eyebrows_sadeyebrows"
            attribute happy "valerie_eyebrows_happyeyebrows"
            attribute surprised "valerie_eyebrows_surprisedeyebrows"
            attribute thinking "valerie_eyebrows_neutraleyebrows"
            attribute angrybrow "valerie_eyebrows_angryeyebrows"
            attribute sadbrow "valerie_eyebrows_sadeyebrows"
            attribute angry "valerie_eyebrows_angryeyebrows"
            attribute closedbrow "valerie_eyebrows_neutraleyebrows"
            attribute happybrow "valerie_eyebrows_happyeyebrows"
            attribute surprisedbrow "valerie_eyebrows_surprisedeyebrows"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "valerie_mouth_surprisedmouth"
            attribute happy "valerie_mouth_happymouth"
            attribute angry "valerie_mouth_angrymouth"
            attribute surprised "valerie_mouth_surprisedmouth"
            attribute thinking "valerie_mouth_frownmouth"

        group tears auto

        group sweat auto

        group shadow auto

        group tired auto

        group anger auto:
            attribute angry "valerie_anger_anger"

        group blush auto

        group cry auto

        always "valerie_eyesparkles" if_not ["happybrow", "closedbrow", "closedeyes", "deadeyes", "happyeyes", "poweredeyes", "thinking", "happy", "powered"] 

    image valeriebg = Crop((0, 0, 1000, 800), "valerie", yalign=0.422, zoom=0.1)

    layeredimage bruno:
        yanchor 1.0
        ypos 1.0

        always "bruno_body_neutral"

        group face auto:
            attribute neutral "bruno_face_norm" default

    layeredimage alder:
        yanchor 1.0
        ypos 1.0

        always "alder_body_neutral"

        group face auto:
            attribute neutral "alder_face_norm" default

    layeredimage lance:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body:
            attribute neutral "lance_body_neutral" default

        group brow auto:
            attribute neutralbrow default
            attribute sad "lance_brow_sadbrow"
            attribute angry "lance_brow_angrybrow"
            attribute happy "lance_brow_sadbrow"
            attribute thinking "lance_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "lance_mouth_neutralmouth"
            attribute angry "lance_mouth_neutralmouth"
            attribute happy "lance_mouth_happymouth"
            attribute thinking "lance_mouth_neutralmouth"

    layeredimage drayden:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body:
            attribute neutral "drayden_body_neutral" default

        group eyebrows auto:
            attribute neutraleyebrows default
            attribute sadbrow "drayden_eyebrows_sadeyebrows"
            attribute sad "drayden_eyebrows_sadeyebrows"
            attribute angrybrow "drayden_eyebrows_angryeyebrows"
            attribute angry "drayden_eyebrows_angryeyebrows"
            attribute happybrow "drayden_eyebrows_happyeyebrows"
            attribute happy "drayden_eyebrows_happyeyebrows"
            attribute surprisedbrow "drayden_eyebrows_surprisedeyebrows"
            attribute surprised "drayden_eyebrows_surprisedeyebrows"

        group eyes auto:
            attribute neutraleyes default
            attribute sadbrow "drayden_eyes_sadeyes"
            attribute sad "drayden_eyes_sadeyes"
            attribute angrybrow "drayden_eyes_angryeyes"
            attribute angry "drayden_eyes_angryeyes"
            attribute happybrow "drayden_eyes_happyeyes"
            attribute happy "drayden_eyes_happyeyes"
            attribute surprisedbrow "drayden_eyes_surprisedeyes"
            attribute surprised "drayden_eyes_surprisedeyes"

        group wrinkles auto:
            attribute neutralwrinkles default
            attribute sad "drayden_wrinkles_sadwrinkles"
            attribute angry "drayden_wrinkles_angrywrinkles"
            attribute happy "drayden_wrinkles_happywrinkles"
            attribute surprised "drayden_wrinkles_surprisedwrinkles"

        group shadow auto

    #pokemon after this point

    layeredimage pikachu:
        group face auto
        
    image side pikachu = LayeredImageProxy("pikachu", Transform(yanchor=0.85, ypos=1.0, xpos=-0.03))
    image side pikachu morning = LayeredImageProxy("pikachu", Transform(yanchor=0.85, ypos=1.0, xpos=-0.03, matrixcolor=TintMatrix(Color(rgb=(.95,.80,.75))) * BrightnessMatrix(-0.10) * ContrastMatrix(1.2)))

    layeredimage starterportraitfull:
        always "[starter_id]"

    image side starterportrait = LayeredImageProxy("starterportraitfull", Transform(xanchor=1.0, yanchor=0.95, ypos=1.0, xpos=1.0))

    layeredimage sideportraitfull:
        always "Pokemon/[sidemonnum].webp"

    image side sidemonportrait = LayeredImageProxy("sideportraitfull", Transform(xanchor=1.0, yanchor=0.95, ypos=1.0, xpos=1.0))

    image balloonbot = "Pokemon/0.webp"
    image shroomish = "Pokemon/285.webp"
    image pichu = "Pokemon/172.webp"
    image flabebe = "Pokemon/669.webp"
    image venomoth = "Pokemon/49.webp"
    image claydol = "Pokemon/344.webp"
    image floatzel = "Pokemon/419.webp"
    image victreebel = "Pokemon/71.webp"
    image houndour = "Pokemon/228.webp"
    image sandshrew = "Pokemon/27.webp"
    image absol = "Pokemon/359.webp"
    image megalop = "Pokemon/428.1.webp"
    image lopunny = "Pokemon/428.webp"
    image buneary = "Pokemon/427.webp"
    image cramorantthroatgoat = "Pokemon/845.2.webp"