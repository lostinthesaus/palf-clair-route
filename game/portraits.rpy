define config.gl2 = True

init python:
    libtypes = []#needs to be declared here for the libpikachu later on

init:
    layeredimage red:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body auto:
            attribute neutralbody "red_body_neutralbody" default
            attribute neutralhatless "red_body_hatless"
            attribute swimsuithatless "red_body_hatless"
            attribute battleteam "red_eyeshine_blank"

        group costume auto:
            attribute neutralcostume "red_costume_neutralcostume" default
            attribute uniform "red_costume_uniform"
            attribute neutralhatless "red_costume_neutralcostume"
            attribute swimsuithatless "red_costume_swimsuit"

        group fullblush auto

        group tired auto

        group shadow auto

        group eyes auto if_not ["angrybrow", "angry"]:
            attribute neutraleyes default
            attribute noeyes "red_eyeshine_blank"
            attribute sad "red_eyes_sadeyes"
            attribute happy "red_eyes_happyeyes"
            attribute happybrow "red_eyes_happyeyes"
            attribute surprised "red_eyes_surprisedeyes"
            attribute surprisedbrow "red_eyes_surprisedeyes"
            attribute closedbrow "red_eyes_closedeyes"
            attribute confusedbrow "red_eyes_neutraleyes"
            attribute sadbrow "red_eyes_sadeyes"
            attribute playfulbrow "red_eyes_playfuleyes"
            attribute thinking "red_eyes_closedeyes"
            attribute unamusedbrow "red_eyes_playfuleyes"
            attribute winkbrow "red_eyes_winkeyes"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "red_mouth_sadmouth"
            attribute happy "red_mouth_happymouth"
            attribute angry "red_mouth_angrymouth"
            attribute surprised "red_mouth_surprisedmouth"
            attribute thinking "red_mouth_frownmouth"
            attribute confused "red_mouth_talking2mouth"

        group eyebrows auto if_not ["angrybrow", "angry"]:
            attribute neutraleyebrows default
            attribute sad "red_eyebrows_sadeyebrows"
            attribute thinking "red_eyebrows_neutraleyebrows"
            attribute closedbrow "red_eyebrows_neutraleyebrows"
            attribute sadbrow "red_eyebrows_sadeyebrows"
            attribute playfulbrow "red_eyebrows_playfuleyebrows"
            attribute unamusedbrow "red_eyebrows_unamusedeyebrows"
            attribute happy "red_eyebrows_happyeyebrows"
            attribute happybrow "red_eyebrows_happyeyebrows"
            attribute surprised "red_eyebrows_surprisedeyebrows"
            attribute surprisedbrow "red_eyebrows_surprisedeyebrows"
            attribute confused "red_eyebrows_confusedeyebrows"
            attribute confusedeyebrows "red_eyebrows_confusedeyebrows"
            attribute confusedbrow "red_eyebrows_confusedeyebrows"
            attribute winkbrow "red_eyebrows_neutraleyebrows"
            
        group brow:
            attribute angrybrow "red_brow_angrybrow"
            attribute angry "red_brow_angrybrow"
        
        group hat auto:
            attribute hat "red_hat_hat" default
            attribute neutralhatless "red_eyeshine_blank"
            attribute swimsuithatless "red_eyeshine_blank"

        group tears auto

        group sweat auto

        group anger auto

        group blush auto

        group cry auto

        group eyeshine auto:
            attribute noshine "red_eyeshine_blank"

        group glasses auto

        always "red_eyesparkles" if_not ["noeyes", "noshine", "happybrow", "closedbrow", "closedeyes", "deadeyes", "happyeyes", "thinking", "happy", "sad2eyes", "sad2brow", "winkeyes", "winkbrow", "upeyes", "upbrow", "downeyes", "downbrow", "angry2eyes", "angryeyes"] 
        always "red_eyesparkles_sad2eyes" if_any ["sad2eyes", "sad2brow"]
        always "red_eyesparkles_winkeyes" if_any ["winkeyes", "winkbrow"]
        always "red_eyesparkles_upeyes" if_any ["upeyes", "upbrow"]
        always "red_eyesparkles_downeyes" if_any ["downeyes", "downbrow"]
    
    image side red = LayeredImageProxy("red", Transform(xpos=0.08, yanchor=0.35))
    image side red night = LayeredImageProxy("red", Transform(xpos=0.08, yanchor=0.35, matrixcolor=nightmatrix))
    image side red sepia = LayeredImageProxy("red", Transform(xpos=0.08, yanchor=0.35, matrixcolor=SepiaMatrix()))
    image side red morning = LayeredImageProxy("red", Transform(xpos=0.08, yanchor=0.35, matrixcolor=TintMatrix(Color(rgb=(.95,.80,.75))) * BrightnessMatrix(-0.10) * ContrastMatrix(1.2)))

    layeredimage tia:
        zoom 0.5
        xalign 0.5
        yanchor 0.63
        ypos 1.0

        group power auto

        group poweredhat auto

        always "tia_body_neutral"

        group clothes auto:
            attribute neutralclothes "tia_clothes_neutral" default
            attribute uniform "tia_clothes_uniform"

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
            attribute surprisedbrow "tia_eyes_surprisedeyes"

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
            attribute surprisedbrow "tia_eyebrows_surprisedeyebrows"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "tia_mouth_sadmouth"
            attribute happy "tia_mouth_happymouth"
            attribute angry "tia_mouth_angrymouth"
            attribute surprised "tia_mouth_surprisedmouth"
            attribute thinking "tia_mouth_frownmouth"

        group sweat auto

        group tired auto

        group anger auto:
            attribute angry "tia_anger_anger"

        group blush auto

        group hat auto

        group tears auto

        group cry auto

        always "tia_eyesparkles" if_not ["sad2brow", "happybrow", "closedbrow", "closedeyes", "deadeyes", "happyeyes", "thinking", "happy", "sad2eyes", "powered", "poweredeyes", "downeyes", "downbrow"] 
        always "tia_eyesparkles_sad2eyes" if_any ["sad2eyes", "sad2brow"]
        always "tia_eyesparkles_downeyes" if_any ["downeyes", "downbrow"]

        group shadow auto

    image side tia = LayeredImageProxy("tia", Transform(xpos=0.08, yanchor=0.45))

    layeredimage latias:
        zoom 0.5
        xalign 0.25
        yanchor 0.8
        ypos 1.0

        group power auto

        group poweredruffle auto

        group poweredhat auto

        group body auto:
            attribute neutral "latias_body_neutral" default

        group eyes auto:
            attribute neutraleyes default
            attribute sad "latias_eyes_sadeyes"
            attribute happy "latias_eyes_happyeyes"
            attribute surprised "latias_eyes_surprisedeyes"
            attribute thinking "latias_eyes_closedeyes"
            attribute angrybrow "latias_eyes_angryeyes"
            attribute sadbrow "latias_eyes_sadeyes"
            attribute sad2brow "latias_eyes_sad2eyes"
            attribute angry "latias_eyes_angryeyes"
            attribute closedbrow "latias_eyes_closedeyes"
            attribute happybrow "latias_eyes_happyeyes"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "latias_mouth_sadmouth"
            attribute happy "latias_mouth_happymouth"
            attribute angry "latias_mouth_angrymouth"
            attribute surprised "latias_mouth_surprisedmouth"
            attribute thinking "latias_mouth_frownmouth"

        group tears auto

        group sweat auto

        group tired auto

        group anger auto:
            attribute angry "latias_anger_anger"

        group blush auto

        group ruffle auto

        group hat auto:
            attribute nohat "red_eyeshine_blank"

        group cry auto

        always "latias_eyesparkles" if_not ["sad2brow", "happybrow", "closedbrow", "closedeyes", "deadeyes", "happyeyes", "thinking", "happy", "sad2eyes", "powered", "poweredeyes", "playfuleyes", "playfulbrow", "soullesseyes", "downeyes", "downbrow"] 
        always "latias_eyesparkles_sad2eyes" if_any ["sad2eyes", "sad2brow"]
        always "latias_eyesparkles_downeyes" if_any ["downeyes", "downbrow"]
        always "latias_eyesparkles_playfuleyes" if_any ["playfuleyes", "playfulbrow"]

        group shadow auto

    image side latias = LayeredImageProxy("latias", Transform(xpos=0.08, yanchor=0.45))
    image side latias night = LayeredImageProxy("latias", Transform(xpos=0.08, yanchor=0.45, matrixcolor=nightmatrix))
    image latias flip = LayeredImageProxy("latias", Transform(xzoom=-1, xanchor=0.75))

    layeredimage jasmine:
        zoom 0.5
        xalign 0.5
        yanchor 0.63
        ypos 1.0

        group body auto:
            attribute neutralbody "jasmine_body_neutral" default

        group hair auto:
            attribute long "jasmine_hair_long" default

        group eyes auto:
            attribute neutraleyes default
            attribute sad "jasmine_eyes_sadeyes"
            attribute happy "jasmine_eyes_happyeyes"
            attribute surprised "jasmine_eyes_surprisedeyes"
            attribute surprisedbrow "jasmine_eyes_surprisedeyes"
            attribute thinking "jasmine_eyes_closedeyes"
            attribute angrybrow "jasmine_eyes_angryeyes"
            attribute sadbrow "jasmine_eyes_sadeyes"
            attribute sad2brow "jasmine_eyes_sad2eyes"
            attribute angry "jasmine_eyes_angryeyes"
            attribute closedbrow "jasmine_eyes_closedeyes"
            attribute happybrow "jasmine_eyes_happyeyes"
            attribute embarrassed "jasmine_eyes_embarrassedeyes"
            attribute embarrassedbrow "jasmine_eyes_embarrassedeyes"

        group eyebrows auto:
            attribute neutraleyebrows default
            attribute sad "jasmine_eyebrows_sadeyebrows"
            attribute happy "jasmine_eyebrows_happyeyebrows"
            attribute surprised "jasmine_eyebrows_surprisedeyebrows"
            attribute surprisedbrow "jasmine_eyebrows_surprisedeyebrows"
            attribute thinking "jasmine_eyebrows_neutraleyebrows"
            attribute angrybrow "jasmine_eyebrows_angryeyebrows"
            attribute sadbrow "jasmine_eyebrows_sadeyebrows"
            attribute sad2brow "jasmine_eyebrows_sadeyebrows"
            attribute angry "jasmine_eyebrows_angryeyebrows"
            attribute closedbrow "jasmine_eyebrows_neutraleyebrows"
            attribute happybrow "jasmine_eyebrows_happyeyebrows"
            attribute embarrassed "jasmine_eyebrows_embarrassedeyebrows"
            attribute embarrassedbrow "jasmine_eyebrows_embarrassedeyebrows"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "jasmine_mouth_sadmouth"
            attribute happy "jasmine_mouth_happymouth"
            attribute angry "jasmine_mouth_angrymouth"
            attribute surprised "jasmine_mouth_surprisedmouth"
            attribute thinking "jasmine_mouth_frownmouth"
            attribute embarrassed "jasmine_mouth_embarrassedmouth"

        group tears auto

        group sweat auto

        group tired auto

        group anger auto:
            attribute angry "jasmine_anger_anger"

        group blush auto

        group cry auto

        group hairshadow auto:
            attribute wethair "jasmine_hairshadow_wethairshadow"
            attribute wetterhair "jasmine_hairshadow_wethairshadow"

        group fronthair auto:
            attribute bunches "jasmine_fronthair_bunches" default

        group headwear auto:
            attribute hairties "jasmine_headwear_hairties" default
            attribute noties "red_eyeshine_blank"
            attribute wethair "red_eyeshine_blank"
            attribute wetterhair "red_eyeshine_blank"
        
        group clothes auto:
            attribute neutral "jasmine_clothes_neutral" default

        group sarong auto
        
        always "jasmine_eyesparkles" if_not ["sad2brow", "happybrow", "closedbrow", "closedeyes", "deadeyes", "happyeyes", "thinking", "happy", "sad2eyes", "playfuleyes", "playfulbrow"] 
        always "jasmine_eyesparkles_playfuleyes" if_any ["playfuleyes", "playfulbrow"]
        always "jasmine_eyesparkles_sad2eyes" if_any ["sad2eyes", "sad2brow"]

        group shadow auto

    image side jasmine = LayeredImageProxy("jasmine", Transform(xpos=0.08, yanchor=0.45))

    layeredimage grusha:
        zoom 0.5
        xalign 0.5
        yanchor 0.63
        ypos 1.0

        group body auto:
            attribute neutralbody "grusha_body_neutralbody" default

        group clothes auto:
            attribute neutral "grusha_clothes_neutral" default

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
            attribute playfulbrow "grusha_eyes_playfuleyes"

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
            attribute playfulbrow "grusha_eyebrows_playfuleyebrows"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "grusha_mouth_sadmouth"
            attribute happy "grusha_mouth_happymouth"
            attribute angry "grusha_mouth_angrymouth"
            attribute surprised "grusha_mouth_surprisedmouth"
            attribute thinking "grusha_mouth_frownmouth"

        group tears auto

        group sweat auto

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

        always "grusha_eyesparkles" if_not ["sad2brow", "happybrow", "closedbrow", "closedeyes", "deadeyes", "happyeyes", "thinking", "happy", "sad2eyes", "playfuleyes", "playfulbrow"] 
        always "grusha_eyesparkles_playfuleyes" if_any ["playfuleyes", "playfulbrow"]
        always "grusha_eyesparkles_sad2eyes" if_any ["sad2eyes", "sad2brow"]

        group shadow auto

    image side grusha = LayeredImageProxy("grusha", Transform(xpos=0.08, yanchor=0.45))

    layeredimage iris:
        zoom 0.5
        xalign 0.5
        yanchor 0.63
        ypos 1.0

        group hairunderlay auto:
            attribute defaultunderlay "iris_hairunderlay_defaultunderlay" default
            attribute champion "iris_hairunderlay_championunderlay"

        always "iris_body_neutral"

        group hairshadow auto:
            attribute hair "iris_hairshadow_defaultshadow" default
            attribute champion "iris_hairshadow_championshadow"

        group hair auto:
            attribute hair "iris_hair_default" default

        group costume auto:
            attribute neutral default

        group fullblush auto

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

        group tired auto

        group anger auto:
            attribute angry "iris_anger_anger"

        group blush auto

        group cry auto

        always "iris_eyesparkles" if_not ["happybrow", "closedbrow", "closedeyes", "deadeyes", "happyeyes", "poweredeyes", "thinking", "happy"] 

        group shadow auto

    image side iris = LayeredImageProxy("iris", Transform(xpos=0.08, yanchor=0.45))

    layeredimage mom:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body auto:
            attribute neutral "mom_body_neutral" default
            attribute uniform "mom_body_uniform"

        group tired auto

        group eyes auto:
            attribute neutraleyes default
            attribute noeyes "red_eyeshine_blank"
            attribute disappointed "mom_eyes_closedeyes"
            attribute disappointedbrow "mom_eyes_closedeyes"
            attribute closedbrow "mom_eyes_closedeyes"
            attribute sad "mom_eyes_sadeyes"
            attribute happy "mom_eyes_happyeyes"
            attribute surprised "mom_eyes_surprisedeyes"
            attribute surprisedbrow "mom_eyes_surprisedeyes"
            attribute thinking "mom_eyes_closedeyes"
            attribute angrybrow "mom_eyes_angryeyes"
            attribute sadbrow "mom_eyes_sadeyes"
            attribute sad2brow "mom_eyes_sad2eyes"
            attribute angry "mom_eyes_angryeyes"
            attribute angry2brow "mom_eyes_angry2eyes"
            attribute closedbrow "mom_eyes_closedeyes"
            attribute happybrow "mom_eyes_happyeyes"
            attribute confusedbrow "mom_eyes_neutraleyes"

        group eyebrows auto:
            attribute neutraleyebrows default
            attribute closedbrow "mom_eyebrows_neutraleyebrows"
            attribute disappointed "mom_eyebrows_neutraleyebrows"
            attribute disappointedbrow "mom_eyebrows_neutraleyebrows"
            attribute sad "mom_eyebrows_sadeyebrows"
            attribute happy "mom_eyebrows_happyeyebrows"
            attribute surprised "mom_eyebrows_surprisedeyebrows"
            attribute surprisedbrow "mom_eyebrows_surprisedeyebrows"
            attribute thinking "mom_eyebrows_neutraleyebrows"
            attribute angrybrow "mom_eyebrows_angryeyebrows"
            attribute sadbrow "mom_eyebrows_sadeyebrows"
            attribute sad2brow "mom_eyebrows_sadeyebrows"
            attribute angry2brow "mom_eyebrows_angryeyebrows"
            attribute angry "mom_eyebrows_angryeyebrows"
            attribute closedbrow "mom_eyebrows_neutraleyebrows"
            attribute happybrow "mom_eyebrows_happyeyebrows"
            attribute confused "mom_eyebrows_confusedeyebrows"
            attribute confusedbrow "mom_eyebrows_confusedeyebrows"

        group mouth auto:
            attribute neutralmouth default
            attribute disappointed "mom_mouth_talkingmouth"
            attribute sad "mom_mouth_sadmouth"
            attribute happy "mom_mouth_happymouth"
            attribute angry "mom_mouth_angrymouth"
            attribute surprised "mom_mouth_surprisedmouth"
            attribute thinking "mom_mouth_frownmouth"
            attribute confused "mom_mouth_talking2mouth"

        group tears auto

        group sweat auto

        group anger auto:
            attribute angry "mom_anger_anger"

        group blush auto

        group cry auto

        group eyeshine auto:
            attribute noshine "red_eyeshine_blank"

        always "mom_eyesparkles" if_not ["noshine", "sad2brow", "happybrow", "closedbrow", "closedeyes", "deadeyes", "happyeyes", "thinking", "happy", "sad2eyes", "angry2eyes", "angry2brow", "playfuleyes"] 
        always "mom_eyesparkles_sad2eyes" if_any ["sad2eyes", "sad2brow"]
        always "mom_eyesparkles_playfuleyes" if_any ["playfuleyes"]

        group shadow auto

    image side mom = LayeredImageProxy("mom", Transform(xpos=0.08, yanchor=0.35)) 
    image side mom night = LayeredImageProxy("mom", Transform(xpos=0.08, yanchor=0.35, matrixcolor=nightmatrix))

    layeredimage oak:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body auto:
            attribute neutral "oak_body_neutral" default
            attribute imposter "oak_body_imposter"

        group scar auto

        group tired auto

        group eyes auto:
            attribute neutraleyes default
            attribute neutralbrow "oak_eyes_neutraleyes"
            attribute noeyes "red_eyeshine_blank"
            attribute disappointed "oak_eyes_closedeyes"
            attribute disappointedbrow "oak_eyes_closedeyes"
            attribute closedbrow "oak_eyes_closedeyes"
            attribute sad "oak_eyes_sadeyes"
            attribute happy "oak_eyes_happyeyes"
            attribute surprised "oak_eyes_surprisedeyes"
            attribute surprisedbrow "oak_eyes_surprisedeyes"
            attribute thinking "oak_eyes_closedeyes"
            attribute angrybrow "oak_eyes_angryeyes"
            attribute sadbrow "oak_eyes_sadeyes"
            attribute sad2brow "oak_eyes_sad2eyes"
            attribute angry "oak_eyes_angryeyes"
            attribute angry2brow "oak_eyes_angry2eyes"
            attribute closedbrow "oak_eyes_closedeyes"
            attribute happybrow "oak_eyes_happyeyes"
            attribute confusedbrow "oak_eyes_neutraleyes"

        group eyebrows auto:
            attribute neutraleyebrows default
            attribute neutralbrow "oak_eyebrows_neutraleyebrows"
            attribute closedbrow "oak_eyebrows_neutraleyebrows"
            attribute disappointed "oak_eyebrows_neutraleyebrows"
            attribute disappointedbrow "oak_eyebrows_neutraleyebrows"
            attribute sad "oak_eyebrows_sadeyebrows"
            attribute happy "oak_eyebrows_happyeyebrows"
            attribute surprised "oak_eyebrows_surprisedeyebrows"
            attribute surprisedbrow "oak_eyebrows_surprisedeyebrows"
            attribute thinking "oak_eyebrows_neutraleyebrows"
            attribute angrybrow "oak_eyebrows_angryeyebrows"
            attribute sadbrow "oak_eyebrows_sadeyebrows"
            attribute sad2brow "oak_eyebrows_sadeyebrows"
            attribute angry2brow "oak_eyebrows_angryeyebrows"
            attribute angry "oak_eyebrows_angryeyebrows"
            attribute closedbrow "oak_eyebrows_neutraleyebrows"
            attribute happybrow "oak_eyebrows_happyeyebrows"
            attribute confused "oak_eyebrows_confusedeyebrows"
            attribute confusedbrow "oak_eyebrows_confusedeyebrows"

        group mouth auto:
            attribute neutralmouth default
            attribute disappointed "oak_mouth_talkingmouth"
            attribute sad "oak_mouth_sadmouth"
            attribute happy "oak_mouth_happymouth"
            attribute angry "oak_mouth_angrymouth"
            attribute surprised "oak_mouth_surprisedmouth"
            attribute thinking "oak_mouth_frownmouth"
            attribute confused "oak_mouth_talking2mouth"

        group tears auto

        group sweat auto

        group anger auto:
            attribute angry "oak_anger_anger"

        group blush auto

        group cry auto

        group eyeshine auto:
            attribute noshine "red_eyeshine_blank"

        always "oak_eyesparkles" if_not ["noshine", "sad2brow", "happybrow", "closedbrow", "closedeyes", "deadeyes", "happyeyes", "thinking", "happy", "sad2eyes", "angry2eyes", "angry2brow"] 
        always "oak_eyesparkles_sad2eyes" if_any ["sad2eyes", "sad2brow"]

        group shadow auto

    image oakbg = Crop((0, 0, 1000, 800), "oak", yalign=0.422, zoom=0.1)

    layeredimage yellow:
        zoom 0.46
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        
        group body auto:
            attribute neutral ConditionSwitch(
                "getRWDay(0) not in ['Saturday', 'Sunday'] and timeOfDay != 'Evening'", "yellow_body_neutralhat",
                "str(calDate.day)[-1] in [1, 2]", "yellow_body_neutral",
                "str(calDate.day)[-1] in [3, 4]", "yellow_body_neutralbraid",
                "str(calDate.day)[-1] in [5, 6]", "yellow_body_neutralbraidfront",
                "str(calDate.day)[-1] in [7, 8]", "yellow_body_neutralhairdown",
                "True", "yellow_body_neutrallowponytail") default

            attribute uniform ConditionSwitch(
                "getRWDay(0) not in ['Saturday', 'Sunday'] and timeOfDay != 'Evening'", "yellow_body_uniformhat",
                "str(calDate.day)[-1] in [1, 2]", "yellow_body_uniform",
                "str(calDate.day)[-1] in [3, 4]", "yellow_body_uniformbraid",
                "str(calDate.day)[-1] in [5, 6]", "yellow_body_uniformbraidfront",
                "str(calDate.day)[-1] in [7, 8]", "yellow_body_uniformhairdown",
                "True", "yellow_body_uniformlowponytail")

        group fullblush auto

        group blush auto

        group eyes auto:
            attribute neutraleyes default
            attribute sad "yellow_eyes_sadeyes"
            attribute angry "yellow_eyes_angryeyes"
            attribute angrybrow "yellow_eyes_angryeyes"
            attribute happy "yellow_eyes_happyeyes"
            attribute happybrow "yellow_eyes_happyeyes"
            attribute surprised "yellow_eyes_surprisedeyes"
            attribute surprisedbrow "yellow_eyes_surprisedeyes"
            attribute closedbrow "yellow_eyes_closedeyes"
            attribute thinking "yellow_eyes_closedeyes"
            attribute sadbrow "yellow_eyes_sadeyes"
            attribute unamusedbrow "yellow_eyes_unamusedeyes"

        group eyebrows auto:
            attribute neutraleyebrows default
            attribute sad "yellow_eyebrows_sadeyebrows"
            attribute angry "yellow_eyebrows_angryeyebrows"
            attribute angrybrow "yellow_eyebrows_angryeyebrows"
            attribute happy "yellow_eyebrows_happyeyebrows"
            attribute happybrow "yellow_eyebrows_happyeyebrows"
            attribute surprised "yellow_eyebrows_surprisedeyebrows"
            attribute surprisedbrow "yellow_eyebrows_surprisedeyebrows"
            attribute thinking "yellow_eyebrows_neutraleyebrows"
            attribute closedbrow "yellow_eyebrows_neutraleyebrows"
            attribute sadbrow "yellow_eyebrows_sadeyebrows"
            attribute unamusedbrow "yellow_eyebrows_unamusedeyebrows"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "yellow_mouth_sadmouth"
            attribute angry "yellow_mouth_angrymouth"
            attribute happy "yellow_mouth_happymouth"
            attribute surprised "yellow_mouth_surprisedmouth"
            attribute thinking "yellow_mouth_neutralmouth"
            attribute talking2mouth "yellow_mouth_challengingmouth"

        group tears auto

        group cry auto

        group anger auto

        group shadow auto

    image side yellow = LayeredImageProxy("yellow", Transform(xpos=0.08, yanchor=0.35))

    layeredimage blue:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        
        group body auto:
            attribute neutral "blue_body_neutral" default
            attribute uniform "blue_body_uniform"
        
        group tired auto

        group blush auto

        group eyes auto:
            attribute neutraleyes default
            attribute sad "blue_eyes_sadeyes"
            attribute angry "blue_eyes_angryeyes"
            attribute angrybrow "blue_eyes_angryeyes"
            attribute happy "blue_eyes_happyeyes"
            attribute happybrow "blue_eyes_happyeyes"
            attribute surprised "blue_eyes_surprisedeyes"
            attribute surprisedbrow "blue_eyes_surprisedeyes"
            attribute closedbrow "blue_eyes_closedeyes"
            attribute thinking "blue_eyes_closedeyes"
            attribute sadbrow "blue_eyes_sadeyes"
            attribute cocky "blue_eyes_angryeyes"
            attribute wistfulbrow "blue_eyes_sad2eyes"
            attribute wistful "blue_eyes_sad2eyes"
            attribute glancebrow "blue_eyes_glanceeyes"
            attribute scaredbrow "blue_eyes_scaredeyes"

        group eyebrows auto:
            attribute neutraleyebrows default
            attribute sad "blue_eyebrows_sadeyebrows"
            attribute angry "blue_eyebrows_angryeyebrows"
            attribute angrybrow "blue_eyebrows_angryeyebrows"
            attribute happy "blue_eyebrows_happyeyebrows"
            attribute happybrow "blue_eyebrows_happyeyebrows"
            attribute surprised "blue_eyebrows_surprisedeyebrows"
            attribute surprisedbrow "blue_eyebrows_surprisedeyebrows"
            attribute closedbrow "blue_eyebrows_closedeyebrows"
            attribute thinking "blue_eyebrows_closedeyebrows"
            attribute sadbrow "blue_eyebrows_sadeyebrows"
            attribute cocky "blue_eyebrows_happyeyebrows"
            attribute wistfulbrow "blue_eyebrows_wistfuleyebrows"
            attribute wistful "blue_eyebrows_wistfuleyebrows"
            attribute glancebrow "blue_eyebrows_glanceeyebrows"
            attribute scaredbrow "blue_eyebrows_scaredeyebrows"
            
        group mouth auto:
            attribute neutralmouth default
            attribute disappointed "blue_mouth_talkingmouth"
            attribute sad "blue_mouth_sadmouth"
            attribute happy "blue_mouth_happymouth"
            attribute angry "blue_mouth_angrymouth"
            attribute surprised "blue_mouth_surprisedmouth"
            attribute thinking "blue_mouth_frownmouth"
            attribute confused "blue_mouth_surprisedmouth"
            attribute talking2mouth "blue_mouth_talkingmouth"
            attribute wistful "blue_mouth_wistfulmouth"

        group tears auto

        group sweat auto

        group anger auto:
            attribute angry "blue_anger_anger"

        group cry auto

        group shadow auto

    image side blue = LayeredImageProxy("blue", Transform(xpos=0.05, yanchor=0.35))
    image side blue night = LayeredImageProxy("blue", Transform(xpos=0.05, yanchor=0.35, matrixcolor=nightmatrix))

    layeredimage sonia:
        zoom 0.46
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body auto:
            attribute neutral "sonia_body_neutral" default
            attribute uniform "sonia_body_uniform" 

        group brow auto:
            attribute neutralbrow default
            attribute sad "sonia_brow_sadbrow"
            attribute angry "sonia_brow_angrybrow"
            attribute happy "sonia_brow_happybrow"
            attribute surprised "sonia_brow_surprisedbrow"
            attribute confused "sonia_brow_surprisedbrow"
            attribute thinking "sonia_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "sonia_mouth_sadmouth"
            attribute angry "sonia_mouth_angrymouth"
            attribute happy "sonia_mouth_happymouth"
            attribute surprised "sonia_mouth_surprisedmouth"
            attribute confused "sonia_mouth_surprisedmouth"
            attribute thinking "sonia_mouth_frownmouth"

        group blush auto

    image side sonia = LayeredImageProxy("sonia", Transform(xpos=0.08, yanchor=0.35, xzoom=-1))
    image side sonia night = LayeredImageProxy("sonia", Transform(xpos=0.08, yanchor=0.35, xzoom=-1, matrixcolor=nightmatrix))

    layeredimage silver:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body auto if_not ["winter"]:
            attribute neutral "silver_body_neutral" default
            attribute uniform "silver_body_uniform" 

        always "silver_body_nude" if_any ["winter"]

        group outfit auto

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
            attribute talking2mouth "silver_mouth_sadmouth"

    image side silver = LayeredImageProxy("silver", Transform(xpos=0.08, yanchor=0.35))
    image side silver night = LayeredImageProxy("silver", Transform(xpos=0.08, yanchor=0.35, matrixcolor=nightmatrix))

    layeredimage brawly:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body auto:
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

        group body auto:
            attribute neutral "roxanne_body_neutral" default
            attribute uniform "roxanne_body_uniform" 

        group blush auto

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

        group sweat auto

        group shadow auto

    image side roxanne = LayeredImageProxy("roxanne", Transform(xpos=0.08, yanchor=0.35, xzoom=-1))

    layeredimage face:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body auto:
            attribute neutral "face_body_neutral" default
            attribute uniform "face_body_uniform" 

        group eyes auto:
            attribute neutraleyes default
            attribute sad "face_eyes_sadeyes"
            attribute angry "face_eyes_angryeyes"
            attribute happy "face_eyes_happyeyes"
            attribute surprised "face_eyes_surprisedeyes"

        group eyebrows auto:
            attribute neutraleyebrows default
            attribute sad "face_eyebrows_sadeyebrows"
            attribute angry "face_eyebrows_angryeyebrows"
            attribute happy "face_eyebrows_happyeyebrows"
            attribute surprised "face_eyebrows_surprisedeyebrows"

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

        group body auto:
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

        group body auto:
            attribute neutral "leaf_body_neutral" default
            attribute uniform "leaf_body_uniform" 
            attribute template "leaf_body_template"
            attribute date "leaf_body_adventure"
            attribute battleteam "leaf_body_battleteam"

        group brow auto if_not ["makeup"]:
            attribute neutralbrow default
            attribute sad "leaf_brow_sadbrow"
            attribute angry "leaf_brow_angrybrow"
            attribute happy "leaf_brow_happybrow"
            attribute surprised "leaf_brow_surprisedbrow"
            attribute flirt "leaf_brow_flirtbrow"
            attribute embarrassed "leaf_brow_embarrassedbrow"
            attribute thinking "leaf_brow_closedbrow"
            attribute sarcastic "leaf_brow_flirtbrow"

        group mouth auto if_not ["makeup"]:
            attribute neutralmouth default
            attribute sad "leaf_mouth_sadmouth"
            attribute angry "leaf_mouth_angrymouth"
            attribute happy "leaf_mouth_happymouth"
            attribute surprised "leaf_mouth_surprisedmouth"
            attribute flirt "leaf_mouth_flirtmouth"
            attribute embarrassed "leaf_mouth_embarrassedmouth"
            attribute thinking "leaf_mouth_frownmouth"
            attribute sarcastic "leaf_mouth_talkingmouth"

        group makeupbrow auto if_any ["makeup"]:
            attribute neutralbrow default
            attribute sad "leaf_makeupbrow_sadbrow"
            attribute angry "leaf_makeupbrow_angrybrow"
            attribute happy "leaf_makeupbrow_happybrow"
            attribute surprised "leaf_makeupbrow_surprisedbrow"
            attribute flirt "leaf_makeupbrow_flirtbrow"
            attribute embarrassed "leaf_makeupbrow_embarrassedbrow"
            attribute thinking "leaf_makeupbrow_closedbrow"
            attribute sarcastic "leaf_makeupbrow_flirtbrow"

        group makeupmouth auto if_any ["makeup"]:
            #attribute neutralmouth default
            attribute neutralmouth "leaf_mouth_neutralmouth" default
            attribute talking2mouth "leaf_mouth_talking2mouth"

            attribute sad "leaf_makeupmouth_sadmouth"
            attribute angry "leaf_makeupmouth_angrymouth"
            attribute happy "leaf_makeupmouth_happymouth"
            attribute surprised "leaf_makeupmouth_surprisedmouth"
            attribute flirt "leaf_makeupmouth_flirtmouth"
            attribute embarrassed "leaf_makeupmouth_embarrassedmouth"
            attribute thinking "leaf_makeupmouth_frownmouth"
            attribute sarcastic "leaf_makeupmouth_talkingmouth"

        group blush auto

        group cry auto

        group shadow auto

        group disguise auto:
            attribute nodisguise "red_eyeshine_blank"

        group makeup:
            attribute makeup "red_eyeshine_blank"
            attribute nomakeup "red_eyeshine_blank"

    image side leaf = LayeredImageProxy("leaf", Transform(xpos=0.08, yanchor=0.35, xzoom=-1))
    image side leaf night = LayeredImageProxy("leaf", Transform(xpos=0.08, yanchor=0.35, xzoom=-1, matrixcolor=nightmatrix))

    layeredimage leafdate:
        always "leafdate_base"

        group eyes auto:
            attribute neutraleyes default
            attribute happybrow "leafdate_eyes_happyeyes"
            attribute sadbrow "leafdate_eyes_sadeyes"
            attribute angrybrow "leafdate_eyes_angryeyes"
            attribute happy "leafdate_eyes_happyeyes"
            attribute sad "leafdate_eyes_sadeyes"
            attribute angry "leafdate_eyes_angryeyes"

        group eyebrows auto:
            attribute neutraleyebrows default
            attribute happybrow "leafdate_eyebrows_happyeyebrows"
            attribute sadbrow "leafdate_eyebrows_sadeyebrows"
            attribute angrybrow "leafdate_eyebrows_angryeyebrows"
            attribute happy "leafdate_eyebrows_happyeyebrows"
            attribute sad "leafdate_eyebrows_sadeyebrows"
            attribute angry "leafdate_eyebrows_angryeyebrows"

        group mouth auto:
            attribute neutralmouth default
            attribute happy "leafdate_mouth_happymouth"
            attribute sad "leafdate_mouth_sadmouth"
            attribute angry "leafdate_mouth_angrymouth"

        group sweat auto

    layeredimage ethan:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body auto:
            attribute neutral "ethan_body_neutral" default
            attribute uniform "ethan_body_uniform"
        
        group tired auto

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
            attribute confusedbrow "ethan_eyes_neutraleyes"
            attribute playfulbrow "ethan_eyes_playfuleyes"
            attribute winkbrow "ethan_eyes_winkeyes"
            attribute unamusedbrow "ethan_eyes_playfuleyes"

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
            attribute confusedbrow "ethan_eyebrows_confusedeyebrows"
            attribute playfulbrow "ethan_eyebrows_playfuleyebrows"
            attribute winkbrow "ethan_eyebrows_neutraleyebrows"
            attribute unamusedbrow "ethan_eyebrows_unamusedeyebrows"

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

        group anger auto:
            attribute angry "ethan_anger_anger"

        group blush auto

        group hat auto

        group cry auto

        group eyeshine auto:
            attribute noshine "red_eyeshine_blank"

        always "ethan_eyesparkles" if_not ["noshine", "sad2brow", "happybrow", "closedbrow", "closedeyes", "deadeyes", "happyeyes", "thinking", "happy", "sad2eyes", "angry2eyes", "angry2brow", "playfuleyes", "playfulbrow", "winkeyes", "winkbrow", "unamusedbrow", "downeyes", "downbrow", "upeyes", "upbrow"] 
        always "ethan_eyesparkles_sad2eyes" if_any ["sad2eyes", "sad2brow"] if_not ["noshine"]
        always "ethan_eyesparkles_playfuleyes" if_any ["playfuleyes", "playfulbrow", "unamusedbrow"]
        always "ethan_eyesparkles_winkeyes" if_any ["winkeyes", "winkbrow"]
        always "ethan_eyesparkles_downeyes" if_any ["downeyes", "downbrow"]
        always "ethan_eyesparkles_upeyes" if_any ["upeyes", "upbrow"]

        group shadow auto

    image side ethan = LayeredImageProxy("ethan", Transform(xpos=0.09, yanchor=0.35))
    image side ethan night = LayeredImageProxy("ethan", Transform(xpos=0.09, yanchor=0.35, matrixcolor=nightmatrix))
    
    layeredimage calem:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body auto:
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
        group body auto:
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
    image side hilbert night = LayeredImageProxy("hilbert", Transform(xpos=0.07, yanchor=0.35))

    layeredimage brendan:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body auto:
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

    layeredimage wally:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        
        group body auto:
            attribute neutral "wally_body_neutral" default
            attribute uniform "wally_body_uniform"

        group fullblush auto
        
        group tired auto

        group eyes auto:
            attribute neutraleyes default
            attribute noeyes "red_eyeshine_blank"
            attribute disappointed "wally_eyes_closedeyes"
            attribute disappointedbrow "wally_eyes_closedeyes"
            attribute closedbrow "wally_eyes_closedeyes"
            attribute sad "wally_eyes_sadeyes"
            attribute happy "wally_eyes_happyeyes"
            attribute surprised "wally_eyes_surprisedeyes"
            attribute surprisedbrow "wally_eyes_surprisedeyes"
            attribute thinking "wally_eyes_closedeyes"
            attribute angrybrow "wally_eyes_angryeyes"
            attribute sadbrow "wally_eyes_sadeyes"
            attribute sad2brow "wally_eyes_sideeyes"
            attribute sad2eyes "wally_eyes_sideeyes"
            attribute angry "wally_eyes_angryeyes"
            attribute angry2brow "wally_eyes_angry2eyes"
            attribute closedbrow "wally_eyes_closedeyes"
            attribute happybrow "wally_eyes_happyeyes"
            attribute confusedbrow "wally_eyes_neutraleyes"
            attribute playfulbrow "wally_eyes_playfuleyes"
            attribute surprisedbrow "wally_eyes_surprisedeyes"

        group eyebrows auto:
            attribute neutraleyebrows default
            attribute closedbrow "wally_eyebrows_neutraleyebrows"
            attribute disappointed "wally_eyebrows_neutraleyebrows"
            attribute disappointedbrow "wally_eyebrows_neutraleyebrows"
            attribute sad "wally_eyebrows_sadeyebrows"
            attribute happy "wally_eyebrows_happyeyebrows"
            attribute surprised "wally_eyebrows_surprisedeyebrows"
            attribute surprisedbrow "wally_eyebrows_surprisedeyebrows"
            attribute thinking "wally_eyebrows_neutraleyebrows"
            attribute angrybrow "wally_eyebrows_angryeyebrows"
            attribute sadbrow "wally_eyebrows_sadeyebrows"
            attribute sad2brow "wally_eyebrows_sadeyebrows"
            attribute angry2brow "wally_eyebrows_angryeyebrows"
            attribute angry "wally_eyebrows_angryeyebrows"
            attribute closedbrow "wally_eyebrows_neutraleyebrows"
            attribute happybrow "wally_eyebrows_happyeyebrows"
            attribute confused "wally_eyebrows_confusedeyebrows"
            attribute confusedbrow "wally_eyebrows_confusedeyebrows"
            attribute playfulbrow "wally_eyebrows_playfuleyebrows"
            attribute surprisedbrow "wally_eyebrows_surprisedeyebrows"

        group mouth auto:
            attribute neutralmouth default
            attribute disappointed "wally_mouth_talkingmouth"
            attribute sad "wally_mouth_sadmouth"
            attribute happy "wally_mouth_happymouth"
            attribute angry "wally_mouth_angrymouth"
            attribute surprised "wally_mouth_surprisedmouth"
            attribute thinking "wally_mouth_frownmouth"
            attribute confused "wally_mouth_talking2mouth"

        group tears auto

        group sweat auto

        group blush auto

        group cry auto

        group shadow auto

    image side wally = LayeredImageProxy("wally", Transform(xpos=0.08, yanchor=0.35))

    layeredimage may:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body auto:
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

        always "may_eyesparkles_neutralbrow" if_not ["noshine", "sad2brow", "happybrow", "closedbrow", "closedeyes", "deadeyes", "happyeyes", "thinking", "happy", "sad2eyes", "angry2eyes", "angry2brow", "playfuleyes", "playfulbrow", "flirtbrow", "angrybrow"] 
        always "may_eyesparkles_sadbrow" if_any ["sadbrow"] if_not ["noshine"]
        always "may_eyesparkles_flirtbrow" if_any ["flirtbrow"]
        always "may_eyesparkles_angrybrow" if_any ["angrybrow"]
        always "may_eyesparkles_surprisedbrow" if_any ["surprisedbrow"]

    image side may = LayeredImageProxy("may", Transform(xpos=0.08, yanchor=0.35))
    image side may night = LayeredImageProxy("may", Transform(xpos=0.08, yanchor=0.35, matrixcolor=nightmatrix))

    layeredimage flannery:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body auto:
            attribute neutral "flannery_body_neutral" default
            attribute uniform "flannery_body_uniform"

        group hair auto:
            attribute tired "flannery_hair_frazzled"
            attribute tiredbrow "flannery_hair_frazzled"
        
        group eyebags auto:
            attribute tired "flannery_eyebags_eyebags"
            attribute tiredbrow "flannery_eyebags_eyebags"

        group eyes auto:
            attribute neutraleyes default
            attribute noeyes "red_eyeshine_blank"
            attribute disappointed "flannery_eyes_closedeyes"
            attribute disappointedbrow "flannery_eyes_closedeyes"
            attribute closedbrow "flannery_eyes_closedeyes"
            attribute sad "flannery_eyes_sadeyes"
            attribute happy "flannery_eyes_happyeyes"
            attribute surprised "flannery_eyes_surprisedeyes"
            attribute surprisedbrow "flannery_eyes_surprisedeyes"
            attribute thinking "flannery_eyes_closedeyes"
            attribute angrybrow "flannery_eyes_angryeyes"
            attribute sadbrow "flannery_eyes_sadeyes"
            attribute sad2brow "flannery_eyes_sad2eyes"
            attribute angry "flannery_eyes_angryeyes"
            attribute angry2brow "flannery_eyes_angry2eyes"
            attribute closedbrow "flannery_eyes_closedeyes"
            attribute happybrow "flannery_eyes_happyeyes"
            attribute confusedbrow "flannery_eyes_neutraleyes"
            attribute playfulbrow "flannery_eyes_playfuleyes"
            attribute tired "flannery_eyes_tiredeyes"
            attribute tiredbrow "flannery_eyes_tiredeyes"
            attribute furious "flannery_eyes_angry2eyes"
            attribute furiousbrow "flannery_eyes_angry2eyes"
            attribute winkbrow "flannery_eyes_winkeyes"

        group eyebrows auto:
            attribute neutraleyebrows default
            attribute closedbrow "flannery_eyebrows_neutraleyebrows"
            attribute disappointed "flannery_eyebrows_neutraleyebrows"
            attribute disappointedbrow "flannery_eyebrows_neutraleyebrows"
            attribute sad "flannery_eyebrows_sadeyebrows"
            attribute happy "flannery_eyebrows_happyeyebrows"
            attribute surprised "flannery_eyebrows_surprisedeyebrows"
            attribute surprisedbrow "flannery_eyebrows_surprisedeyebrows"
            attribute thinking "flannery_eyebrows_neutraleyebrows"
            attribute angrybrow "flannery_eyebrows_angryeyebrows"
            attribute sadbrow "flannery_eyebrows_sadeyebrows"
            attribute sad2brow "flannery_eyebrows_sadeyebrows"
            attribute angry2brow "flannery_eyebrows_angryeyebrows"
            attribute angry "flannery_eyebrows_angryeyebrows"
            attribute closedbrow "flannery_eyebrows_neutraleyebrows"
            attribute happybrow "flannery_eyebrows_happyeyebrows"
            attribute confused "flannery_eyebrows_confusedeyebrows"
            attribute confusedbrow "flannery_eyebrows_confusedeyebrows"
            attribute playfulbrow "flannery_eyebrows_playfuleyebrows"
            attribute tired "flannery_eyebrows_tiredeyebrows"
            attribute tiredbrow "flannery_eyebrows_tiredeyebrows"
            attribute furious "flannery_eyebrows_angry2eyebrows"
            attribute furiousbrow "flannery_eyebrows_angry2eyebrows"
            attribute winkbrow "flannery_eyebrows_neutraleyebrows"

        group mouth auto:
            attribute neutralmouth default
            attribute disappointed "flannery_mouth_talkingmouth"
            attribute sad "flannery_mouth_sadmouth"
            attribute happy "flannery_mouth_happymouth"
            attribute angry "flannery_mouth_angrymouth"
            attribute surprised "flannery_mouth_surprisedmouth"
            attribute thinking "flannery_mouth_frownmouth"
            attribute confused "flannery_mouth_talking2mouth"
            attribute tired "flannery_mouth_tiredmouth"
            attribute furious "flannery_mouth_angrymouth"

        group tears auto

        group sweat auto

        group anger auto:
            attribute angry "flannery_anger_anger"
            attribute furious "flannery_anger_anger2"

        group blush auto

        group hat auto

        group cry auto

        group veins auto

        group eyeshine auto:
            attribute noshine "red_eyeshine_blank"

        always "flannery_eyesparkles" if_not ["noshine", "sad2brow", "happybrow", "closedbrow", "closedeyes", "deadeyes", "happyeyes", "thinking", "happy", "sad2eyes", "angry2eyes", "angry2brow", "furious", "furiouseyes", "furiousbrow", "winkeyes", "winkbrow"] 
        always "flannery_eyesparkles_sad2eyes" if_any ["sad2eyes", "sad2brow"]
        always "flannery_eyesparkles_winkeyes" if_any ["winkeyes", "winkbrow"]

        group shadow auto

    image side flannery = LayeredImageProxy("flannery", Transform(xpos=0.08, yanchor=0.35))
    image side flannery night = LayeredImageProxy("flannery", Transform(xpos=0.08, yanchor=0.35, matrixcolor=nightmatrix))

    layeredimage whitney:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body auto:
            attribute neutral "whitney_body_neutral" default
            attribute uniform "whitney_body_uniform"

        group fullblush auto
        
        group tired auto

        group cry auto

        group eyes auto:
            attribute neutraleyes default
            attribute noeyes "red_eyeshine_blank"
            attribute disappointed "whitney_eyes_closedeyes"
            attribute disappointedbrow "whitney_eyes_closedeyes"
            attribute closedbrow "whitney_eyes_closedeyes"
            attribute sad "whitney_eyes_sadeyes"
            attribute happy "whitney_eyes_happyeyes"
            attribute surprised "whitney_eyes_surprisedeyes"
            attribute surprisedbrow "whitney_eyes_surprisedeyes"
            attribute thinking "whitney_eyes_closedeyes"
            attribute angrybrow "whitney_eyes_angryeyes"
            attribute sadbrow "whitney_eyes_sadeyes"
            attribute sad2brow "whitney_eyes_sad2eyes"
            attribute angry "whitney_eyes_angryeyes"
            attribute angry2brow "whitney_eyes_angry2eyes"
            attribute closedbrow "whitney_eyes_closedeyes"
            attribute happybrow "whitney_eyes_happyeyes"
            attribute confusedbrow "whitney_eyes_neutraleyes"
            attribute playfulbrow "whitney_eyes_playfuleyes"

        group eyebrows auto:
            attribute neutraleyebrows default
            attribute closedbrow "whitney_eyebrows_neutraleyebrows"
            attribute disappointed "whitney_eyebrows_neutraleyebrows"
            attribute disappointedbrow "whitney_eyebrows_neutraleyebrows"
            attribute sad "whitney_eyebrows_sadeyebrows"
            attribute happy "whitney_eyebrows_happyeyebrows"
            attribute surprised "whitney_eyebrows_surprisedeyebrows"
            attribute surprisedbrow "whitney_eyebrows_surprisedeyebrows"
            attribute thinking "whitney_eyebrows_neutraleyebrows"
            attribute angrybrow "whitney_eyebrows_angryeyebrows"
            attribute sadbrow "whitney_eyebrows_sadeyebrows"
            attribute sad2brow "whitney_eyebrows_sadeyebrows"
            attribute angry2brow "whitney_eyebrows_angryeyebrows"
            attribute angry "whitney_eyebrows_angryeyebrows"
            attribute closedbrow "whitney_eyebrows_neutraleyebrows"
            attribute happybrow "whitney_eyebrows_happyeyebrows"
            attribute confused "whitney_eyebrows_confusedeyebrows"
            attribute confusedbrow "whitney_eyebrows_confusedeyebrows"
            attribute playfulbrow "whitney_eyebrows_playfuleyebrows"

        group mouth auto:
            attribute neutralmouth default
            attribute disappointed "whitney_mouth_talkingmouth"
            attribute sad "whitney_mouth_sadmouth"
            attribute happy "whitney_mouth_happymouth"
            attribute angry "whitney_mouth_angrymouth"
            attribute surprised "whitney_mouth_surprisedmouth"
            attribute thinking "whitney_mouth_frownmouth"
            attribute confused "whitney_mouth_talking2mouth"

        group tears auto

        group sweat auto

        group anger auto:
            attribute angry "whitney_anger_anger"

        group blush auto

        group hat auto

        group eyeshine auto:
            attribute noshine "red_eyeshine_blank"

        always "whitney_eyesparkles" if_not ["noshine", "sad2brow", "happybrow", "closedbrow", "closedeyes", "deadeyes", "happyeyes", "thinking", "happy", "sad2eyes", "angry2eyes", "angry2brow", "playfuleyes", "playfulbrow", "winkeyes", "winkbrow"] 
        always "whitney_eyesparkles_sad2eyes" if_any ["sad2eyes", "sad2brow"]
        always "whitney_eyesparkles_playfuleyes" if_any ["playfuleyes", "playfulbrow"]
        always "whitney_eyesparkles_winkeyes" if_any ["winkeyes", "winkbrow"]

    image side whitney = LayeredImageProxy("whitney", Transform(xpos=0.08, yanchor=0.35))
    image side whitney night = LayeredImageProxy("whitney", Transform(xpos=0.08, yanchor=0.35, matrixcolor=nightmatrix))

    layeredimage sabrina:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        
        group aura auto:
            attribute powered "sabrina_aura_gen1aura"
            attribute neutralpowered "sabrina_aura_gen1aura"
            attribute uniformpowered "sabrina_aura_gen1aura"

        group base auto:
            attribute gen1base default

        group face auto

        group shadow auto
        
        group tired auto

        group clothes auto:
            attribute neutral "sabrina_clothes_gen1" default
            attribute casualoldhair "sabrina_clothes_gen2"
            attribute uniformpowered "sabrina_clothes_uniform"

        group hair auto:
            attribute neutralhair "sabrina_hair_gen1hair" default
            attribute casualoldhair "sabrina_hair_gen1hair"

        group eyes auto:
            attribute neutraleyes default
            attribute noeyes "red_eyeshine_blank"
            attribute disappointed "sabrina_eyes_closedeyes"
            attribute disappointedbrow "sabrina_eyes_closedeyes"
            attribute closedbrow "sabrina_eyes_closedeyes"
            attribute sad "sabrina_eyes_sadeyes"
            attribute happy "sabrina_eyes_happyeyes"
            attribute surprised "sabrina_eyes_surprisedeyes"
            attribute surprisedbrow "sabrina_eyes_surprisedeyes"
            attribute thinking "sabrina_eyes_closedeyes"
            attribute angrybrow "sabrina_eyes_angryeyes"
            attribute sadbrow "sabrina_eyes_sadeyes"
            attribute sad2brow "sabrina_eyes_sad2eyes"
            attribute angry "sabrina_eyes_angryeyes"
            attribute angry2brow "sabrina_eyes_angry2eyes"
            attribute closedbrow "sabrina_eyes_closedeyes"
            attribute happybrow "sabrina_eyes_happyeyes"
            attribute confusedbrow "sabrina_eyes_neutraleyes"
            attribute playfulbrow "sabrina_eyes_playfuleyes"
            attribute poweredbrow "sabrina_eyes_psychicangryeyes"

        group eyebrows auto:
            attribute neutraleyebrows default
            attribute closedbrow "sabrina_eyebrows_neutraleyebrows"
            attribute disappointed "sabrina_eyebrows_neutraleyebrows"
            attribute disappointedbrow "sabrina_eyebrows_neutraleyebrows"
            attribute sad "sabrina_eyebrows_sadeyebrows"
            attribute happy "sabrina_eyebrows_happyeyebrows"
            attribute surprised "sabrina_eyebrows_surprisedeyebrows"
            attribute surprisedbrow "sabrina_eyebrows_surprisedeyebrows"
            attribute thinking "sabrina_eyebrows_neutraleyebrows"
            attribute angrybrow "sabrina_eyebrows_angryeyebrows"
            attribute sadbrow "sabrina_eyebrows_sadeyebrows"
            attribute sad2brow "sabrina_eyebrows_sadeyebrows"
            attribute angry2brow "sabrina_eyebrows_angryeyebrows"
            attribute angry "sabrina_eyebrows_angryeyebrows"
            attribute closedbrow "sabrina_eyebrows_neutraleyebrows"
            attribute happybrow "sabrina_eyebrows_happyeyebrows"
            attribute confused "sabrina_eyebrows_confusedeyebrows"
            attribute confusedbrow "sabrina_eyebrows_confusedeyebrows"
            attribute playfulbrow "sabrina_eyebrows_playfuleyebrows"
            attribute poweredbrow "sabrina_eyebrows_angryeyebrows"

        group mouth auto:
            attribute neutralmouth default
            attribute disappointed "sabrina_mouth_talkingmouth"
            attribute sad "sabrina_mouth_sadmouth"
            attribute happy "sabrina_mouth_happymouth"
            attribute angry "sabrina_mouth_angrymouth"
            attribute surprised "sabrina_mouth_surprisedmouth"
            attribute thinking "sabrina_mouth_neutralmouth"
            attribute confused "sabrina_mouth_talking2mouth"

        group blush auto

        group sweat auto

        group blush auto

        group cry auto:
            attribute tears "sabrina_cry_cry"

    image side sabrina = LayeredImageProxy("sabrina", Transform(xpos=0.08, yanchor=0.35))

    layeredimage serena:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body auto:
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

        group tail auto

        group body auto:
            attribute neutral "cheren_body_neutral" default
            attribute uniform "cheren_body_uniform"
            attribute shirtless "cheren_body_shirtless"

        group tired auto

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
            attribute closedeyes "cheren_eyes_disappointedeyes"
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
            attribute talking2mouth "cheren_mouth_sadmouth"

        group tears auto

        group sweat auto

        group anger auto:
            attribute angry "cheren_anger_anger"

        group blush auto

        group hat auto

        group cry auto

        group eyeshine auto:
            attribute noshine "red_eyeshine_blank"

        always "cheren_eyesparkles" if_not ["noshine", "sad2brow", "happybrow", "closedbrow", "disappointed", "closedeyes", "deadeyes", "happyeyes", "thinking", "happy", "sad2eyes", "angry2eyes", "angry2brow", "sadeyes", "sadbrow", "sad", "disappointedeyes", "disappointedbrow", "angryeyes", "angrybrow", "angry", "upeyes", "upbrow", "playfuleyes", "playfulbrow", "playful", "downeyes", "downbrow"] 
        always "cheren_eyesparkles_playfuleyes" if_any ["playfuleyes", "playfulbrow", "playful"]
        always "cheren_eyesparkles_angryeyes" if_any ["angryeyes", "angrybrow", "angry"]
        always "cheren_eyesparkles_sad2eyes" if_any ["sad2eyes", "sad2brow"]
        always "cheren_eyesparkles_sadeyes" if_any ["sadeyes", "sadbrow", "sad"]
        always "cheren_eyesparkles_upeyes" if_any ["upeyes", "upbrow"]
        always "cheren_eyesparkles_downeyes" if_any ["downeyes", "downbrow"]

        group shadow auto

        group ears auto

        group ribbon auto

    image side cheren = LayeredImageProxy("cheren", Transform(xpos=0.08, yanchor=0.35))
    image side cheren night = LayeredImageProxy("cheren", Transform(xpos=0.08, yanchor=0.35, matrixcolor=nightmatrix))
    image side cheren sepia = LayeredImageProxy("cheren", Transform(xpos=0.08, yanchor=0.35, matrixcolor=SepiaMatrix()))
    
    layeredimage misty:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body auto:
            attribute gen1body default

        group blush auto

        group cry auto

        group hair auto if_not ["wetbody"]:
            attribute gen1hair default

        group clothes auto:
            attribute neutral "misty_clothes_default" default

        group jacket auto

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

        group anger auto
    
    image side misty = LayeredImageProxy("misty", Transform(xpos=0.08, yanchor=0.35))

    layeredimage bianca:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        
        group body auto:
            attribute neutral "bianca_body_neutral" default
            attribute uniform "bianca_body_uniform"
        
        group tired auto

        group shadow auto

        group eyes auto:
            attribute neutraleyes default
            attribute noeyes "red_eyeshine_blank"
            attribute disappointed "bianca_eyes_closedeyes"
            attribute disappointedbrow "bianca_eyes_closedeyes"
            attribute closedbrow "bianca_eyes_closedeyes"
            attribute sad "bianca_eyes_sadeyes"
            attribute happy "bianca_eyes_happyeyes"
            attribute surprised "bianca_eyes_surprisedeyes"
            attribute surprisedbrow "bianca_eyes_surprisedeyes"
            attribute thinking "bianca_eyes_closedeyes"
            attribute angrybrow "bianca_eyes_angryeyes"
            attribute sadbrow "bianca_eyes_sadeyes"
            attribute sad2brow "bianca_eyes_sad2eyes"
            attribute angry "bianca_eyes_angryeyes"
            attribute angry2brow "bianca_eyes_angry2eyes"
            attribute closedbrow "bianca_eyes_closedeyes"
            attribute happybrow "bianca_eyes_happyeyes"
            attribute confusedbrow "bianca_eyes_neutraleyes"
            attribute playfulbrow "bianca_eyes_playfuleyes"

        group eyebrows auto:
            attribute neutraleyebrows default
            attribute closedbrow "bianca_eyebrows_neutraleyebrows"
            attribute disappointed "bianca_eyebrows_neutraleyebrows"
            attribute disappointedbrow "bianca_eyebrows_neutraleyebrows"
            attribute sad "bianca_eyebrows_sadeyebrows"
            attribute happy "bianca_eyebrows_happyeyebrows"
            attribute surprised "bianca_eyebrows_surprisedeyebrows"
            attribute surprisedbrow "bianca_eyebrows_surprisedeyebrows"
            attribute thinking "bianca_eyebrows_neutraleyebrows"
            attribute angrybrow "bianca_eyebrows_angryeyebrows"
            attribute sadbrow "bianca_eyebrows_sadeyebrows"
            attribute sad2brow "bianca_eyebrows_sadeyebrows"
            attribute angry2brow "bianca_eyebrows_angryeyebrows"
            attribute angry "bianca_eyebrows_angryeyebrows"
            attribute closedbrow "bianca_eyebrows_neutraleyebrows"
            attribute happybrow "bianca_eyebrows_happyeyebrows"
            attribute confused "bianca_eyebrows_confusedeyebrows"
            attribute confusedbrow "bianca_eyebrows_confusedeyebrows"
            attribute playfulbrow "bianca_eyebrows_playfuleyebrows"

        group mouth auto:
            attribute neutralmouth default
            attribute disappointed "bianca_mouth_talkingmouth"
            attribute sad "bianca_mouth_sadmouth"
            attribute happy "bianca_mouth_happymouth"
            attribute angry "bianca_mouth_angrymouth"
            attribute surprised "bianca_mouth_surprisedmouth"
            attribute thinking "bianca_mouth_frownmouth"
            attribute confused "bianca_mouth_talking2mouth"
            
        group sweat auto

        group blush auto

        group cry auto

        group glasses auto:
            attribute glasses default
            attribute noglasses "red_eyeshine_blank"
        
    image side bianca = LayeredImageProxy("bianca", Transform(xpos=0.08, yanchor=0.35))
    image side bianca sepia = LayeredImageProxy("red", Transform(xpos=0.08, yanchor=0.35, matrixcolor=SepiaMatrix()))

    layeredimage dawn:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body auto:
            attribute neutral "dawn_body_neutral" default
            attribute uniform "dawn_body_uniform" 

        group hatlessbrow auto if_any ["contest", "date"]:
            attribute neutralbrow "dawn_hatlessbrow_neutralbrow" default
            attribute sad "dawn_hatlessbrow_sadbrow"
            attribute angry "dawn_hatlessbrow_angrybrow"
            attribute happy "dawn_hatlessbrow_happybrow"
            attribute surprised "dawn_hatlessbrow_surprisedbrow"
            attribute thinking "dawn_hatlessbrow_closedbrow"

        group brow auto if_not ["contest", "date"]:
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
            attribute talking2mouth "dawn_mouth_sadmouth"

        group accessory:
            attribute contest "dawn_accessory_bangles"

    image side dawn = LayeredImageProxy("dawn", Transform(xpos=0.08, yanchor=0.35))
    image side dawn night = LayeredImageProxy("dawn", Transform(xpos=0.08, yanchor=0.35, matrixcolor=nightmatrix))

    layeredimage nate:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body auto:
            attribute neutral "nate_body_neutral" default
            attribute uniform "nate_body_uniform"
        
        group tired auto

        group eyes auto:
            attribute neutraleyes default
            attribute noeyes "red_eyeshine_blank"
            attribute disappointed "nate_eyes_closedeyes"
            attribute disappointedbrow "nate_eyes_closedeyes"
            attribute closedbrow "nate_eyes_closedeyes"
            attribute sad "nate_eyes_sadeyes"
            attribute happy "nate_eyes_happyeyes"
            attribute surprised "nate_eyes_surprisedeyes"
            attribute surprisedbrow "nate_eyes_surprisedeyes"
            attribute thinking "nate_eyes_closedeyes"
            attribute angrybrow "nate_eyes_angryeyes"
            attribute sadbrow "nate_eyes_sadeyes"
            attribute sad2brow "nate_eyes_sad2eyes"
            attribute angry "nate_eyes_angryeyes"
            attribute angry2brow "nate_eyes_angry2eyes"
            attribute closedbrow "nate_eyes_closedeyes"
            attribute happybrow "nate_eyes_happyeyes"
            attribute confusedbrow "nate_eyes_neutraleyes"
            attribute playfulbrow "nate_eyes_playfuleyes"
            attribute unamusedbrow "nate_eyes_playfuleyes"
            attribute winkbrow "nate_eyes_winkeyes"

        group eyebrows auto:
            attribute neutraleyebrows default
            attribute closedbrow "nate_eyebrows_neutraleyebrows"
            attribute disappointed "nate_eyebrows_neutraleyebrows"
            attribute disappointedbrow "nate_eyebrows_neutraleyebrows"
            attribute sad "nate_eyebrows_sadeyebrows"
            attribute happy "nate_eyebrows_happyeyebrows"
            attribute surprised "nate_eyebrows_surprisedeyebrows"
            attribute surprisedbrow "nate_eyebrows_surprisedeyebrows"
            attribute thinking "nate_eyebrows_neutraleyebrows"
            attribute angrybrow "nate_eyebrows_angryeyebrows"
            attribute sadbrow "nate_eyebrows_sadeyebrows"
            attribute sad2brow "nate_eyebrows_sadeyebrows"
            attribute angry2brow "nate_eyebrows_angryeyebrows"
            attribute angry "nate_eyebrows_angryeyebrows"
            attribute closedbrow "nate_eyebrows_neutraleyebrows"
            attribute happybrow "nate_eyebrows_happyeyebrows"
            attribute confused "nate_eyebrows_confusedeyebrows"
            attribute confusedbrow "nate_eyebrows_confusedeyebrows"
            attribute playfulbrow "nate_eyebrows_playfuleyebrows"
            attribute unamusedbrow "nate_eyebrows_unamusedeyebrows"
            attribute winkbrow "nate_eyebrows_neutraleyebrows"

        group mouth auto:
            attribute neutralmouth default
            attribute disappointed "nate_mouth_talkingmouth"
            attribute sad "nate_mouth_sadmouth"
            attribute happy "nate_mouth_happymouth"
            attribute angry "nate_mouth_angrymouth"
            attribute surprised "nate_mouth_surprisedmouth"
            attribute thinking "nate_mouth_frownmouth"
            attribute confused "nate_mouth_talking2mouth"

        group tears auto

        group sweat auto

        group anger auto:
            attribute angry "nate_anger_anger"

        group blush auto

        group hat auto

        group cry auto

        group eyeshine auto:
            attribute noshine "red_eyeshine_blank"

        always "nate_eyesparkles" if_not ["noshine", "sad2brow", "happybrow", "closedbrow", "closedeyes", "deadeyes", "happyeyes", "thinking", "happy", "sad2eyes", "angry2eyes", "angry2brow", "playfuleyes", "playfulbrow", "winkeyes", "winkbrow", "unamusedbrow", "unamusedeyes", "upeyes", "upbrow"] 
        #always "nate_eyesparkles_sad2eyes" if_any ["sad2eyes", "sad2brow"] if_not ["noshine"]
        always "nate_eyesparkles_playfuleyes" if_any ["playfuleyes", "playfulbrow", "unamusedbrow", "unamusedeyes"]
        always "nate_eyesparkles_winkeyes" if_any ["winkeyes", "winkbrow"]
        always "nate_eyesparkles_upeyes" if_any ["upeyes", "upbrow"]

        group shadow auto

    image side nate = LayeredImageProxy("nate", Transform(xpos=0.09, yanchor=0.35))
    image side nate night = LayeredImageProxy("nate", Transform(xpos=0.09, yanchor=0.35, matrixcolor=nightmatrix))

    layeredimage rosa:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body auto if_not ["streetwear"]:
            attribute neutral "rosa_body_neutral" default
            attribute uniform "rosa_body_uniform"

        always "rosa_body_base" if_any ["streetwear"]

        group outfit auto

        group cry auto

        group eyes auto:
            attribute neutraleyes default
            attribute sad "rosa_eyes_sadeyes"
            attribute sadbrow "rosa_eyes_sadeyes"
            attribute angry "rosa_eyes_angryeyes"
            attribute angrybrow "rosa_eyes_angryeyes"
            attribute happy "rosa_eyes_happyeyes"
            attribute happybrow "rosa_eyes_happyeyes"
            attribute surprised "rosa_eyes_surprisedeyes"
            attribute surprisedbrow "rosa_eyes_surprisedeyes"
            attribute thinking "rosa_eyes_closedeyes"
            attribute thinkingbrow "rosa_eyes_closedeyes"
            attribute closedbrow "rosa_eyes_closedeyes"

        group eyebrows auto:
            attribute neutraleyebrows default
            attribute sad "rosa_eyebrows_sadeyebrows"
            attribute sadbrow "rosa_eyebrows_sadeyebrows"
            attribute angry "rosa_eyebrows_angryeyebrows"
            attribute angrybrow "rosa_eyebrows_angryeyebrows"
            attribute happy "rosa_eyebrows_happyeyebrows"
            attribute happybrow "rosa_eyebrows_happyeyebrows"
            attribute surprised "rosa_eyebrows_surprisedeyebrows"
            attribute surprisedbrow "rosa_eyebrows_surprisedeyebrows"
            attribute thinking "rosa_eyebrows_neutraleyebrows"
            attribute thinkingbrow "rosa_eyebrows_neutraleyebrows"
            attribute closedbrow "rosa_eyebrows_neutraleyebrows"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "rosa_mouth_sadmouth"
            attribute angry "rosa_mouth_angrymouth"
            attribute happy "rosa_mouth_happymouth"
            attribute surprised "rosa_mouth_surprisedmouth"
            attribute thinking "rosa_mouth_frownmouth"
            attribute talking2mouth "rosa_mouth_sadmouth"

        group blush auto

        group sweat auto

        group animefect auto

    image side rosa = LayeredImageProxy("rosa", Transform(xpos=0.08, yanchor=0.35))
    image side rosa night = LayeredImageProxy("rosa", Transform(xpos=0.08, yanchor=0.35, matrixcolor=nightmatrix))

    layeredimage bea:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body auto:
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
    image side bea night = LayeredImageProxy("bea", Transform(xpos=0.08, yanchor=0.35, matrixcolor=nightmatrix))

    layeredimage allister:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        
        group body auto:
            attribute neutral "allister_body_neutral" default
            attribute uniform "allister_body_uniform"

        group mask:
            attribute mask "allister_mask_mask" default
            attribute nomask "red_eyeshine_blank"

        group fullblush auto
        
        group tired auto

        group eyes auto:
            attribute noeyes "red_eyeshine_blank"
            attribute disappointed "allister_eyes_closedeyes"
            attribute disappointedbrow "allister_eyes_closedeyes"
            attribute closedbrow "allister_eyes_closedeyes"
            attribute sad "allister_eyes_sadeyes"
            attribute happy "allister_eyes_happyeyes"
            attribute surprised "allister_eyes_surprisedeyes"
            attribute surprisedbrow "allister_eyes_surprisedeyes"
            attribute thinking "allister_eyes_closedeyes"
            attribute angrybrow "allister_eyes_angryeyes"
            attribute sadbrow "allister_eyes_sadeyes"
            attribute sad2brow "allister_eyes_sideeyes"
            attribute sad2eyes "allister_eyes_sideeyes"
            attribute angry "allister_eyes_angryeyes"
            attribute angry2brow "allister_eyes_angry2eyes"
            attribute closedbrow "allister_eyes_closedeyes"
            attribute happybrow "allister_eyes_happyeyes"
            attribute confusedbrow "allister_eyes_neutraleyes"
            attribute playfulbrow "allister_eyes_playfuleyes"
            attribute surprisedbrow "allister_eyes_surprisedeyes"

        group eyebrows auto:
            attribute closedbrow "allister_eyebrows_neutraleyebrows"
            attribute disappointed "allister_eyebrows_neutraleyebrows"
            attribute disappointedbrow "allister_eyebrows_neutraleyebrows"
            attribute sad "allister_eyebrows_sadeyebrows"
            attribute happy "allister_eyebrows_happyeyebrows"
            attribute surprised "allister_eyebrows_surprisedeyebrows"
            attribute surprisedbrow "allister_eyebrows_surprisedeyebrows"
            attribute thinking "allister_eyebrows_neutraleyebrows"
            attribute angrybrow "allister_eyebrows_angryeyebrows"
            attribute sadbrow "allister_eyebrows_sadeyebrows"
            attribute sad2brow "allister_eyebrows_sadeyebrows"
            attribute angry2brow "allister_eyebrows_angryeyebrows"
            attribute angry "allister_eyebrows_angryeyebrows"
            attribute closedbrow "allister_eyebrows_neutraleyebrows"
            attribute happybrow "allister_eyebrows_happyeyebrows"
            attribute confused "allister_eyebrows_confusedeyebrows"
            attribute confusedbrow "allister_eyebrows_confusedeyebrows"
            attribute playfulbrow "allister_eyebrows_playfuleyebrows"
            attribute surprisedbrow "allister_eyebrows_surprisedeyebrows"

        group mouth auto:
            attribute disappointed "allister_mouth_talkingmouth"
            attribute sad "allister_mouth_sadmouth"
            attribute happy "allister_mouth_happymouth"
            attribute angry "allister_mouth_angrymouth"
            attribute surprised "allister_mouth_surprisedmouth"
            attribute thinking "allister_mouth_frownmouth"
            attribute confused "allister_mouth_talking2mouth"

        group tears auto

        group sweat auto

        group blush auto

        group cry auto

        group shadow auto

    image side allister = LayeredImageProxy("allister", Transform(xpos=0.08, yanchor=0.35))

    layeredimage nessa:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body auto:
            attribute neutral ConditionSwitch(
                "HasEvent(\"Nessa\", \"OutfitSwap\")", "nessa_body_casual",
                "True", "nessa_body_neutral") default
            attribute swim "nessa_body_neutral"
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
    image side nessa night = LayeredImageProxy("nessa", Transform(xpos=0.08, yanchor=0.35, matrixcolor=nightmatrix))

    layeredimage hilda:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body auto:
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
            attribute talking2mouth "hilda_mouth_smirkmouth"

        group sweat auto

        group veins auto

    image side hilda = LayeredImageProxy("hilda", Transform(xpos=0.08, yanchor=0.35))
    image side hilda night = LayeredImageProxy("hilda", Transform(xpos=0.08, yanchor=0.35, matrixcolor=nightmatrix))

    layeredimage gardenia:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body auto:
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

    image side gardenia = LayeredImageProxy("gardenia", Transform(xpos=0.08, yanchor=0.35))

    layeredimage skyla:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body auto:
            attribute neutral "skyla_body_neutral" default
            attribute uniform "skyla_body_uniform"
            attribute template "skyla_body_template"

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
    image side skylatease = LayeredImageProxy("skyla", Transform(xpos=0.08, yanchor=0.33))
    image side skyla night = LayeredImageProxy("skyla", Transform(xpos=0.08, yanchor=0.35, matrixcolor=nightmatrix))

    layeredimage brock:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body auto:
            attribute neutral "brock_body_neutral" default
            attribute uniform "brock_body_uniform" 

        group blush auto

        group brow auto:
            attribute neutralbrow default
            attribute sad "brock_brow_sadbrow"
            attribute angry "brock_brow_angrybrow"
            attribute happy "brock_brow_neutralbrow"
            attribute surprised "brock_brow_surprisedbrow"
            attribute thinking "brock_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "brock_mouth_sadmouth"
            attribute angry "brock_mouth_angrymouth"
            attribute happy "brock_mouth_happymouth"
            attribute surprised "brock_mouth_surprisedmouth"
            attribute thinking "brock_mouth_frownmouth"

        group sweat auto

        group shadow auto

        group tears auto

        group gloves auto:
            attribute finger default

    image side brock = LayeredImageProxy("brock", Transform(xpos=0.08, yanchor=0.35))
    image tinybrock = Crop((0, 0, 1000, 800), "brock", yalign=1.0, zoom=0.1)

    layeredimage erika:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body auto:
            attribute neutral "erika_body_neutral" default
            attribute uniform "erika_body_uniform"
        
        group tired auto

        group eyes auto:
            attribute neutraleyes default
            attribute noeyes "red_eyeshine_blank"
            attribute disappointed "erika_eyes_closedeyes"
            attribute disappointedbrow "erika_eyes_closedeyes"
            attribute closedbrow "erika_eyes_closedeyes"
            attribute sad "erika_eyes_sadeyes"
            attribute happy "erika_eyes_happyeyes"
            attribute surprised "erika_eyes_surprisedeyes"
            attribute surprisedbrow "erika_eyes_surprisedeyes"
            attribute thinking "erika_eyes_closedeyes"
            attribute angrybrow "erika_eyes_angryeyes"
            attribute sadbrow "erika_eyes_sadeyes"
            attribute sad2brow "erika_eyes_sad2eyes"
            attribute angry "erika_eyes_angryeyes"
            attribute angry2brow "erika_eyes_angry2eyes"
            attribute closedbrow "erika_eyes_closedeyes"
            attribute happybrow "erika_eyes_happyeyes"
            attribute confusedbrow "erika_eyes_neutraleyes"
            attribute playfulbrow "erika_eyes_playfuleyes"
            attribute unamusedeyes "erika_eyes_playfuleyes"
            attribute unamusedbrow "erika_eyes_playfuleyes"

        group eyebrows auto:
            attribute neutraleyebrows default
            attribute closedbrow "erika_eyebrows_neutraleyebrows"
            attribute disappointed "erika_eyebrows_neutraleyebrows"
            attribute disappointedbrow "erika_eyebrows_neutraleyebrows"
            attribute sad "erika_eyebrows_sadeyebrows"
            attribute happy "erika_eyebrows_happyeyebrows"
            attribute surprised "erika_eyebrows_surprisedeyebrows"
            attribute surprisedbrow "erika_eyebrows_surprisedeyebrows"
            attribute thinking "erika_eyebrows_neutraleyebrows"
            attribute angrybrow "erika_eyebrows_angryeyebrows"
            attribute sadbrow "erika_eyebrows_sadeyebrows"
            attribute sad2brow "erika_eyebrows_sadeyebrows"
            attribute angry2brow "erika_eyebrows_angryeyebrows"
            attribute angry "erika_eyebrows_angryeyebrows"
            attribute closedbrow "erika_eyebrows_neutraleyebrows"
            attribute happybrow "erika_eyebrows_happyeyebrows"
            attribute confused "erika_eyebrows_confusedeyebrows"
            attribute confusedbrow "erika_eyebrows_confusedeyebrows"
            attribute playfulbrow "erika_eyebrows_playfuleyebrows"
            attribute unamusedbrow "erika_eyebrows_unamusedeyebrows"

        group mouth auto:
            attribute neutralmouth default
            attribute disappointed "erika_mouth_talkingmouth"
            attribute sad "erika_mouth_sadmouth"
            attribute happy "erika_mouth_happymouth"
            attribute angry "erika_mouth_angrymouth"
            attribute surprised "erika_mouth_surprisedmouth"
            attribute thinking "erika_mouth_frownmouth"
            attribute confused "erika_mouth_talking2mouth"

        group tears auto

        group sweat auto

        group anger auto:
            attribute angry "erika_anger_anger"

        group blush auto

        group hat auto

        group cry auto

        group eyeshine auto:
            attribute noshine "red_eyeshine_blank"

        always "erika_eyesparkles" if_not ["noshine", "sad2brow", "happybrow", "closedbrow", "closedeyes", "deadeyes", "happyeyes", "thinking", "happy", "sad2eyes", "angry2eyes", "angry2brow", "playfuleyes", "playfulbrow", "winkeyes", "unamusedeyes", "unamusedbrow", "downeyes", "downbrow"] 
        always "erika_eyesparkles_sad2eyes" if_any ["sad2eyes", "sad2brow"] if_not ["noshine"]
        always "erika_eyesparkles_playfuleyes" if_any ["playfuleyes", "playfulbrow", "unamusedeyes", "unamusedbrow"]
        always "erika_eyesparkles_downeyes" if_any ["downeyes", "downbrow"]
        always "erika_eyesparkles_winkeyes" if_any ["winkeyes"]

        group shadow auto

    image side erika = LayeredImageProxy("erika", Transform(xpos=0.09, yanchor=0.35))
    image side erika night = LayeredImageProxy("erika", Transform(xpos=0.09, yanchor=0.35, matrixcolor=nightmatrix))

    layeredimage janine:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body auto:
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
            attribute talking2mouth "janine_mouth_smirkmouth"
            attribute smilemouth "janine_mouth_happyneutralmouth"

        group blush auto

        group face auto
    
    image side janine = LayeredImageProxy("janine", Transform(xpos=0.08, yanchor=0.35))

    layeredimage raihan:
        zoom 0.5
        xalign 0.4
        yanchor 0.6
        ypos 1.0

        group blush auto

        always "raihan_body_neutral"

        group outfit auto:
            attribute neutral "raihan_outfit_neutral" default

        group brow auto:
            attribute neutralbrow default
            attribute sad "raihan_brow_sadbrow"
            attribute angry "raihan_brow_angrybrow"
            attribute happy "raihan_brow_happybrow"
            attribute surprised "raihan_brow_surprisedbrow"
            attribute thinking "raihan_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "raihan_mouth_sadmouth"
            attribute angry "raihan_mouth_angrymouth"
            attribute happy "raihan_mouth_happymouth"
            attribute surprised "raihan_mouth_surprisedmouth"
            attribute thinking "raihan_mouth_frownmouth"

        group blush auto

        group accessories auto

        group headwear auto:
            attribute headband default

    image side raihan = LayeredImageProxy("raihan", Transform(xpos=0.08, yanchor=0.35))
    image side raihan night = LayeredImageProxy("raihan", Transform(xpos=0.08, yanchor=0.35, matrixcolor=nightmatrix))

    layeredimage eri:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body auto:
            attribute neutral "eri_body_neutral" default

        group brow auto:
            attribute neutralbrow default
            attribute sad "eri_brow_sadbrow"
            attribute angry "eri_brow_angrybrow"
            attribute happy "eri_brow_happybrow"
            attribute surprised "eri_brow_surprisedbrow"
            attribute thinking "eri_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "eri_mouth_sadmouth"
            attribute angry "eri_mouth_angrymouth"
            attribute happy "eri_mouth_happymouth"
            attribute surprised "eri_mouth_surprisedmouth"
            attribute thinking "eri_mouth_frownmouth"

    image side eri = LayeredImageProxy("eri", Transform(xpos=0.08, yanchor=0.35))

    layeredimage mallow:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body auto:
            attribute neutral "mallow_body_neutral" default

        group blush auto

        group brow auto:
            attribute neutralbrow default
            attribute sad "mallow_brow_sadbrow"
            attribute angry "mallow_brow_angrybrow"
            attribute happy "mallow_brow_happybrow"
            attribute surprised "mallow_brow_surprisedbrow"
            attribute thinking "mallow_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "mallow_mouth_sadmouth"
            attribute angry "mallow_mouth_angrymouth"
            attribute happy "mallow_mouth_happymouth"
            attribute surprised "mallow_mouth_surprisedmouth"
            attribute thinking "mallow_mouth_frownmouth"
    
    image side mallow = LayeredImageProxy("mallow", Transform(xpos=0.08, yanchor=0.35))

    #KLARA NOTE: Hey, cutie! I see you're checking out my assets. Can't blame you!~ ;D
    # Think there's something special you'd really like me to wear? Well, why don't you tell Dantalion?
    # I'm sure he could be convinced if you make it worth his while!~ And I'd really appreciate it.
    # Maybe I'd even wear it for you...? ;;;;D
    layeredimage klara:
        zoom 0.49
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body auto:
            attribute neutral "klara_body_neutral" default

        group shadow auto

        group blush auto

        group brow auto if_not ["makeup"]:
            attribute neutralbrow default
            attribute sad "klara_brow_sadbrow"
            attribute angry "klara_brow_angrybrow"
            attribute happy "klara_brow_happybrow"
            attribute surprised "klara_brow_surprisedbrow"
            attribute thinking "klara_brow_closedbrow"

        group browmakeup auto if_any ["makeup"]:
            attribute neutralbrow default
            attribute sad "klara_browmakeup_sadbrow"
            attribute angry "klara_browmakeup_angrybrow"
            attribute happy "klara_browmakeup_happybrow"
            attribute surprised "klara_browmakeup_surprisedbrow"
            attribute thinking "klara_browmakeup_closedbrow" 

        always "klara_eyelight_wrathbrow" if_any ["wrathbrow", "wrathbrowmakeup"] 
        always "klara_eyelight_frightenedbrow" if_any ["frightenedbrow", "frightenedbrowmakeup"] 
        always "klara_eyelight_angrybrow" if_any ["angrybrow", "angrybrowmakeup"] 

        group lipstick auto if_any ["makeup"]:
            attribute neutralmouth default
            attribute sad "klara_lipstick_sadmouth"
            attribute angrymouth "klara_lipstick_wrathmouth"
            attribute angry "klara_lipstick_wrathmouth"
            attribute happy "klara_lipstick_happymouth"
            attribute surprised "klara_lipstick_surprisedmouth"
            attribute thinking "klara_lipstick_frownmouth"

        group makeup:
            attribute makeup "red_eyeshine_blank"
            attribute nomakeup "red_eyeshine_blank"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "klara_mouth_sadmouth"
            attribute angrymouth "klara_mouth_wrathmouth"
            attribute angry "klara_mouth_wrathmouth"
            attribute happy "klara_mouth_happymouth"
            attribute surprised "klara_mouth_surprisedmouth"
            attribute thinking "klara_mouth_frownmouth"

        group hairpin auto

        group accessory auto

        group dynamax auto

        group sweat auto

        group anger auto
    
    image side klara = LayeredImageProxy("klara", Transform(xpos=0.08, yanchor=0.35))
    image side klara night = LayeredImageProxy("klara", Transform(xpos=0.08, yanchor=0.35, matrixcolor=nightmatrix))

    layeredimage melody:
        zoom 0.52
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body auto:
            attribute neutral "melody_body_neutral" default

        group blush auto

        group brow auto:
            attribute neutralbrow default

            attribute sad "melody_brow_sadbrow"
            attribute sadeyes "melody_brow_sadbrow"
            attribute sadeyebrows "melody_brow_sadbrow"

            attribute surprised "melody_brow_surprisedbrow"
            attribute surprisedeyes "melody_brow_surprisedbrow"
            attribute surprisedeyebrows "melody_brow_surprisedbrow"
            
            attribute happy "melody_brow_happybrow"
            attribute happyeyes "melody_brow_happybrow"
            attribute happyeyebrows "melody_brow_happybrow"
            
            attribute angry "melody_brow_angrybrow"
            attribute angryeyes "melody_brow_angrybrow"
            attribute angryeyebrows "melody_brow_angrybrow"

            attribute thinking "melody_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute disappointed "melody_mouth_talkingmouth"
            attribute sad "melody_mouth_sadmouth"
            attribute happy "melody_mouth_happymouth"
            attribute angry "melody_mouth_angrymouth"
            attribute surprised "melody_mouth_surprisedmouth"
            attribute confused "melody_mouth_talking2mouth"

        group glasses auto:
            attribute up default
    
    image side melody = LayeredImageProxy("melody", Transform(xpos=0.08, yanchor=0.35))

    layeredimage roughneck:
        zoom 0.3
        xalign 0.5
        yanchor 1.0
        ypos 1.0

        group body auto:
            attribute neutral "roughneck_body_neutral" default
            attribute angry "roughneck_body_angry"
            attribute surprised "roughneck_body_surprised"
            attribute happy "roughneck_body_happy"

    image roughneck2 = LayeredImageProxy("roughneck")
    image roughneck3 = LayeredImageProxy("roughneck")

    layeredimage femthug:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        always "femthug_base"

        always "femthug_clothes_neutral"

        always "femthug_hair"

        group shadow auto

        group blush auto

        group brow auto:
            attribute neutralbrow default
            attribute sad "femthug_brow_sadbrow"
            attribute angry "femthug_brow_angrybrow"
            attribute happy "femthug_brow_happybrow"
            attribute surprised "femthug_brow_surprisedbrow"
            attribute thinking "femthug_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "femthug_mouth_sadmouth"
            attribute angry "femthug_mouth_angrymouth"
            attribute happy "femthug_mouth_happymouth"
            attribute surprised "femthug_mouth_surprisedmouth"
            attribute thinking "femthug_mouth_frownmouth"
    
    image side femthug = LayeredImageProxy("femthug", Transform(xpos=0.08, yanchor=0.35))

    #STAFF AFTER THIS POINT

    layeredimage miriam:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group blush auto

        group body auto:
            attribute neutral "miriam_body_neutral" default

        group brow auto:
            attribute neutralbrow default
            attribute sad "miriam_brow_sadbrow"
            attribute angry "miriam_brow_angrybrow"
            attribute happy "miriam_brow_happybrow"
            attribute surprised "miriam_brow_surprisedbrow"
            attribute thinking "miriam_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "miriam_mouth_sadmouth"
            attribute angry "miriam_mouth_angrymouth"
            attribute happy "miriam_mouth_happymouth"
            attribute surprised "miriam_mouth_surprisedmouth"
            attribute thinking "miriam_mouth_frownmouth"

    image side miriam = LayeredImageProxy("miriam", Transform(xpos=0.08, yanchor=0.35))

    layeredimage kris:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body auto:
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

    image side kris = LayeredImageProxy("kris", Transform(xpos=0.08, yanchor=0.35))

    layeredimage lenora:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body auto:
            attribute neutral "lenora_body_neutral" default

        group brow auto:
            attribute neutralbrow default
            attribute sad "lenora_brow_sadbrow"
            attribute angry "lenora_brow_angrybrow"
            attribute happy "lenora_brow_happybrow"
            attribute surprised "lenora_brow_surprisedbrow"
            attribute thinking "lenora_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "lenora_mouth_sadmouth"
            attribute angry "lenora_mouth_angrymouth"
            attribute happy "lenora_mouth_happymouth"
            attribute surprised "lenora_mouth_surprisedmouth"
            attribute thinking "lenora_mouth_frownmouth"

    image lenorabg = Crop((0, 0, 1000, 800), "lenora", yalign=0.422, zoom=0.1)

    layeredimage blaine:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        always "blaine_body"

        group brow auto:
            attribute neutralbrow default
            attribute neutral "blaine_brow_neutralbrow"
            attribute sad "blaine_brow_sadbrow"
            attribute angry "blaine_brow_angrybrow"
            attribute happy "blaine_brow_happybrow"
            attribute surprised "blaine_brow_surprisedbrow"
            attribute thinking "blaine_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute neutral "blaine_mouth_neutralmouth"
            attribute sad "blaine_mouth_sadmouth"
            attribute angry "blaine_mouth_angrymouth"
            attribute happy "blaine_mouth_happymouth"
            attribute surprised "blaine_mouth_surprisedmouth"
            attribute thinking "blaine_mouth_frownmouth"

        group accessory auto:
            attribute glasses default

        always "blaine_moustache"

    image blainebg = Crop((0, 0, 1000, 800), "blaine", yalign=0.422, zoom=0.1)

    layeredimage wallace:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body auto:
            attribute neutral "wallace_body_neutral" default

        group brow auto:
            attribute neutralbrow default
            attribute sad "wallace_brow_sadbrow"
            attribute angry "wallace_brow_angrybrow"
            attribute happy "wallace_brow_happybrow"
            attribute surprised "wallace_brow_surprisedbrow"
            attribute thinking "wallace_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "wallace_mouth_sadmouth"
            attribute angry "wallace_mouth_angrymouth"
            attribute happy "wallace_mouth_happymouth"
            attribute surprised "wallace_mouth_surprisedmouth"
            attribute thinking "wallace_mouth_frownmouth"

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

        group body auto:
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
        group body auto:
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

        group tired auto

        group anger auto:
            attribute angry "melony_anger_anger"

        group blush auto

        group cry auto

        always "melony_eyesparkles" if_not ["happybrow", "closedbrow", "closedeyes", "deadeyes", "happyeyes", "poweredeyes", "thinking", "happy", "powered"] 

        group shadow auto

    image melonybg = Crop((0, 0, 1000, 800), "melony", yalign=0.422, zoom=0.1)

    layeredimage marshal:
        yanchor 1.0
        ypos 1.0

        always "marshal_body_neutral"

        group face auto:
            attribute neutral "marshal_face_neutral" default

    image marshalbg = "marshalbackground"

    layeredimage koga:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        always "koga_body_neutral"

        group body auto:
            attribute neutral "koga_body_neutral" default

        group brow auto:
            attribute neutralbrow default
            attribute sad "koga_brow_sadbrow"
            attribute angry "koga_brow_angrybrow"
            attribute happy "koga_brow_happybrow"
            attribute surprised "koga_brow_surprisedbrow"
            attribute thinking "koga_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "koga_mouth_sadmouth"
            attribute angry "koga_mouth_angrymouth"
            attribute happy "koga_mouth_happymouth"
            attribute surprised "koga_mouth_surprisedmouth"
            attribute thinking "koga_mouth_neutralmouth"

        group scarf auto:
            attribute neutralscarf default

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

        group body auto:
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

        group power auto:
            attribute uniform "will_power_powered"

        group body auto:
            attribute neutral "will_body_neutral" default

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

        group tired auto

        group anger auto:
            attribute angry "will_anger_anger"

        group blush auto

        group cry auto

        group shadow auto

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

        group body auto:
            attribute neutral "olivia_body_neutral" default

        group brow auto:
            attribute neutralbrow default
            attribute sad "olivia_brow_sadbrow"
            attribute angry "olivia_brow_angrybrow"
            attribute happy "olivia_brow_happybrow"
            attribute surprised "olivia_brow_surprisedbrow"
            attribute thinking "olivia_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "olivia_mouth_sadmouth"
            attribute angry "olivia_mouth_angrymouth"
            attribute happy "olivia_mouth_happymouth"
            attribute surprised "olivia_mouth_surprisedmouth"
            attribute thinking "olivia_mouth_frownmouth"

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

        group body auto:
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

        group body auto:
            attribute neutral "clair_body_neutral" default

        group brow auto:
            attribute neutralbrow default
            attribute sad "clair_brow_sadbrow"
            attribute angry "clair_brow_angrybrow"
            attribute happy "clair_brow_happybrow"
            attribute surprised "clair_brow_surprisedbrow"
            attribute thinking "clair_brow_closedbrow"
            attribute beta "clair_brow_beta"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "clair_mouth_sadmouth"
            attribute angry "clair_mouth_angrymouth"
            attribute happy "clair_mouth_happymouth"
            attribute surprised "clair_mouth_surprisedmouth"
            attribute thinking "clair_mouth_frownmouth"
            attribute beta "clair_mouth_beta"
        
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
        
        always "valerie_body_neutral" 

        group clothes auto:
            attribute neutral "valerie_clothes_neutral" default

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

        group tired auto

        group anger auto:
            attribute angry "valerie_anger_anger"

        group blush auto

        group cry auto

        always "valerie_eyesparkles" if_not ["noshine", "sad2brow", "happybrow", "closedbrow", "closedeyes", "deadeyes", "happyeyes", "thinking", "happy", "sad2eyes", "angry2eyes", "angry2brow", "playfuleyes", "playfulbrow", "winkeyes", "winkbrow", "unamusedbrow", "downeyes", "downbrow", "upeyes", "upbrow"] 
        always "valerie_eyesparkles_sad2eyes" if_any ["sad2eyes", "sad2brow"] if_not ["noshine"]
        always "valerie_eyesparkles_playfuleyes" if_any ["playfuleyes", "playfulbrow", "unamusedbrow"]
        always "valerie_eyesparkles_winkeyes" if_any ["winkeyes", "winkbrow"]
        always "valerie_eyesparkles_downeyes" if_any ["downeyes", "downbrow"]
        always "valerie_eyesparkles_upeyes" if_any ["upeyes", "upbrow"]

        group shadow auto

        group hat auto

        group hatshadow auto

    image valeriebg = Crop((0, 0, 1000, 800), "valerie", yalign=0.422, zoom=0.1)

    layeredimage bruno:
        yanchor 1.0
        ypos 1.0

        always "bruno_body_neutral"

        group face auto:
            attribute neutral "bruno_face_norm" default

    layeredimage alder:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body auto:
            attribute neutral "alder_body_neutral" default

        group brow auto:
            attribute neutralbrow default
            attribute sad "alder_brow_sadbrow"
            attribute sad2 "alder_brow_sadbrow"
            attribute angry "alder_brow_angrybrow"
            attribute angry2 "alder_brow_angrybrow"
            attribute angry3 "alder_brow_angrybrow"
            attribute angry4 "alder_brow_angrybrow"
            attribute happy "alder_brow_happybrow"
            attribute happy2 "alder_brow_happybrow"
            attribute surprised "alder_brow_surprisedbrow"
            attribute surprised2 "alder_brow_surprisedbrow"
            attribute thinking "alder_brow_closedbrow"
            attribute thinking2 "alder_brow_closedbrow"
            attribute spunky "alder_brow_winkbrow"
            attribute spunky2 "alder_brow_winkbrow"
            attribute norm "alder_brow_neutralbrow"
            attribute norm2 "alder_brow_neutralbrow"
            attribute norm3 "alder_brow_neutralbrow"
            attribute norm4 "alder_brow_neutralbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "alder_mouth_frownmouth"
            attribute sad2 "alder_mouth_talking2mouth"
            attribute angry "alder_mouth_frownmouth"
            attribute angry2 "alder_mouth_talking2mouth"
            attribute angry3 "alder_mouth_frownmouth"
            attribute angry4 "alder_mouth_angrymouth"
            attribute happy "alder_mouth_neutralmouth"
            attribute happy2 "alder_mouth_talkingmouth"
            attribute surprised "alder_mouth_frownmouth"
            attribute surprised2 "alder_mouth_talking2mouth"
            attribute thinking "alder_mouth_frownmouth"
            attribute thinking2 "alder_mouth_talking2mouth"
            attribute spunky "alder_mouth_neutralmouth"
            attribute spunky2 "alder_mouth_talkingmouth"
            attribute norm "alder_mouth_neutralmouth"
            attribute norm2 "alder_mouth_talkingmouth"
            attribute norm3 "alder_mouth_frownmouth"
            attribute norm4 "alder_mouth_talking2mouth"

    layeredimage lance:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0
        group body auto:
            attribute neutral "lance_body_neutral" default
            attribute uniform "lance_body_uniform"
        
        group tired auto

        group eyes auto:
            attribute neutraleyes default
            attribute noeyes "red_eyeshine_blank"
            attribute disappointed "lance_eyes_closedeyes"
            attribute disappointedbrow "lance_eyes_closedeyes"
            attribute closedbrow "lance_eyes_closedeyes"
            attribute sad "lance_eyes_sadeyes"
            attribute happy "lance_eyes_happyeyes"
            attribute surprised "lance_eyes_surprisedeyes"
            attribute surprisedbrow "lance_eyes_surprisedeyes"
            attribute thinking "lance_eyes_closedeyes"
            attribute angrybrow "lance_eyes_angryeyes"
            attribute sadbrow "lance_eyes_sadeyes"
            attribute sad2brow "lance_eyes_sad2eyes"
            attribute angry "lance_eyes_angryeyes"
            attribute angry2brow "lance_eyes_angry2eyes"
            attribute closedbrow "lance_eyes_closedeyes"
            attribute happybrow "lance_eyes_happyeyes"
            attribute confusedbrow "lance_eyes_neutraleyes"

        group eyebrows auto:
            attribute neutraleyebrows default
            attribute closedbrow "lance_eyebrows_neutraleyebrows"
            attribute disappointed "lance_eyebrows_neutraleyebrows"
            attribute disappointedbrow "lance_eyebrows_neutraleyebrows"
            attribute sad "lance_eyebrows_sadeyebrows"
            attribute happy "lance_eyebrows_happyeyebrows"
            attribute surprised "lance_eyebrows_surprisedeyebrows"
            attribute surprisedbrow "lance_eyebrows_surprisedeyebrows"
            attribute thinking "lance_eyebrows_neutraleyebrows"
            attribute angrybrow "lance_eyebrows_angryeyebrows"
            attribute angry2brow "lance_eyebrows_angryeyebrows"
            attribute angry "lance_eyebrows_angryeyebrows"
            attribute closedbrow "lance_eyebrows_neutraleyebrows"
            attribute happybrow "lance_eyebrows_happyeyebrows"
            attribute confused "lance_eyebrows_confusedeyebrows"
            attribute confusedbrow "lance_eyebrows_confusedeyebrows"

        group mouth auto:
            attribute neutralmouth default
            attribute disappointed "lance_mouth_talkingmouth"
            attribute sad "lance_mouth_sadmouth"
            attribute happy "lance_mouth_happymouth"
            attribute angry "lance_mouth_angrymouth"
            attribute surprised "lance_mouth_surprisedmouth"
            attribute thinking "lance_mouth_frownmouth"
            attribute confused "lance_mouth_talking2mouth"

        group tears auto

        group sweat auto

        group anger auto

        group blush auto

        group hat auto

        group cry auto

        group eyeshine auto:
            attribute noshine "red_eyeshine_blank"

        always "lance_eyesparkles" if_not ["noshine", "sadbrow", "happybrow", "closedbrow", "closedeyes", "deadeyes", "happyeyes", "thinking", "happy", "sadeyes", "angry2eyes", "angry2brow", "upeyes"] 
        always "lance_eyesparkles_upeyes" if_any ["upeyes", "upbrow"]
        always "lance_eyesparkles_sad2eyes" if_any ["sadeyes", "sadbrow"]

        group shadow auto

    image side lance = LayeredImageProxy("lance", Transform(xpos=0.08, yanchor=0.35))

    layeredimage drayden:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body auto:
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
            attribute closedbrow "drayden_eyebrows_neutraleyebrows"

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
            attribute closedbrow "drayden_eyes_closedeyes"

        group wrinkles auto:
            attribute neutralwrinkles default
            attribute sad "drayden_wrinkles_sadwrinkles"
            attribute angry "drayden_wrinkles_angrywrinkles"
            attribute happy "drayden_wrinkles_happywrinkles"
            attribute surprised "drayden_wrinkles_surprisedwrinkles"

        group shadow auto

    layeredimage lace:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        always "lace_body_neutral"

        group face auto:
            attribute neutral default

    layeredimage oldman:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        always "oldman_body_neutral"

        group brow auto:
            attribute neutralbrow default

        group mouth auto:
            attribute neutralmouth default

        always "oldman_cane_normal"

        group alcohol auto

        group canecover auto

        group blush auto

    layeredimage lisia:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group body auto:
            attribute neutral "lisia_body_neutral" default
            attribute incognito "lisia_body_incognito"

        group brow auto:
            attribute neutralbrow default
            attribute sad "lisia_brow_sadbrow"
            attribute angry "lisia_brow_angrybrow"
            attribute happy "lisia_brow_happybrow"
            attribute surprised "lisia_brow_surprisedbrow"
            attribute thinking "lisia_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "lisia_mouth_sadmouth"
            attribute angry "lisia_mouth_angrymouth"
            attribute happy "lisia_mouth_happymouth"
            attribute surprised "lisia_mouth_surprisedmouth"
            attribute thinking "lisia_mouth_frownmouth"

        group shades auto

    image side lisia = LayeredImageProxy("lisia", Transform(xpos=0.08, yanchor=0.35))

    layeredimage anabel:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        always "anabel_base"

        always "anabel_hair"

        always "anabel_clothes_neutral"

        group brow auto:
            attribute neutralbrow default
            attribute sad "anabel_brow_sadbrow"
            attribute angry "anabel_brow_angrybrow"
            attribute happy "anabel_brow_happybrow"
            attribute surprised "anabel_brow_surprisedbrow"
            attribute thinking "anabel_brow_closedbrow"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "anabel_mouth_sadmouth"
            attribute angry "anabel_mouth_angrymouth"
            attribute happy "anabel_mouth_happymouth"
            attribute surprised "anabel_mouth_surprisedmouth"
            attribute thinking "anabel_mouth_frownmouth"

        group accessory auto

    image side anabel = LayeredImageProxy("anabel", Transform(xpos=0.08, yanchor=0.35))

    layeredimage phobosface:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        always "phobos_eyewear_goggles"
        always "phobos_mouth_talkingsharkmouth"

    layeredimage phobos:
        zoom 0.5
        xalign 0.5
        yanchor 0.6
        ypos 1.0

        group chair auto:
            attribute chair default

        group body auto:
            attribute neutral default

        always "phobos_accessories_earring"
        always "phobos_accessories_goldring"
        always "phobos_accessories_silverring"
        always "phobos_accessories_lunatonering"

        group hair auto:
            attribute hair default

        group clothes auto:
            attribute neutral default

        group tired auto

        group eyes auto:
            attribute neutraleyes default
            attribute noeyes "red_eyeshine_blank"
            attribute disappointed "phobos_eyes_closedeyes"
            attribute disappointedbrow "phobos_eyes_closedeyes"
            attribute closedbrow "phobos_eyes_closedeyes"
            attribute sad "phobos_eyes_sadeyes"
            attribute happy "phobos_eyes_happyeyes"
            attribute surprised "phobos_eyes_surprisedeyes"
            attribute surprisedbrow "phobos_eyes_surprisedeyes"
            attribute thinking "phobos_eyes_closedeyes"
            attribute angrybrow "phobos_eyes_angryeyes"
            attribute sadbrow "phobos_eyes_sadeyes"
            attribute sad2brow "phobos_eyes_sad2eyes"
            attribute angry "phobos_eyes_angryeyes"
            attribute angry2brow "phobos_eyes_angry2eyes"
            attribute closedbrow "phobos_eyes_closedeyes"
            attribute happybrow "phobos_eyes_happyeyes"
            attribute confusedbrow "phobos_eyes_neutraleyes"
            attribute playfulbrow "phobos_eyes_playfuleyes"
            attribute winkbrow "phobos_eyes_winkeyes"
            attribute unamusedbrow "phobos_eyes_playfuleyes"

        group eyebrows auto:
            attribute neutraleyebrows default
            attribute closedbrow "phobos_eyebrows_neutraleyebrows"
            attribute disappointed "phobos_eyebrows_neutraleyebrows"
            attribute disappointedbrow "phobos_eyebrows_neutraleyebrows"
            attribute sad "phobos_eyebrows_sadeyebrows"
            attribute happy "phobos_eyebrows_happyeyebrows"
            attribute surprised "phobos_eyebrows_surprisedeyebrows"
            attribute surprisedbrow "phobos_eyebrows_surprisedeyebrows"
            attribute thinking "phobos_eyebrows_neutraleyebrows"
            attribute angrybrow "phobos_eyebrows_angryeyebrows"
            attribute sadbrow "phobos_eyebrows_sadeyebrows"
            attribute sad2brow "phobos_eyebrows_sadeyebrows"
            attribute angry2brow "phobos_eyebrows_angryeyebrows"
            attribute angry "phobos_eyebrows_angryeyebrows"
            attribute closedbrow "phobos_eyebrows_neutraleyebrows"
            attribute happybrow "phobos_eyebrows_happyeyebrows"
            attribute confused "phobos_eyebrows_confusedeyebrows"
            attribute confusedbrow "phobos_eyebrows_confusedeyebrows"
            attribute playfulbrow "phobos_eyebrows_playfuleyebrows"
            attribute winkbrow "phobos_eyebrows_neutraleyebrows"
            attribute unamusedbrow "phobos_eyebrows_unamusedeyebrows"

        group mouth auto:
            attribute neutralmouth default
            attribute disappointed "phobos_mouth_talkingmouth"
            attribute sad "phobos_mouth_sadmouth"
            attribute happy "phobos_mouth_happymouth"
            attribute angry "phobos_mouth_angrymouth"
            attribute surprised "phobos_mouth_surprisedmouth"
            attribute thinking "phobos_mouth_frownmouth"
            attribute confused "phobos_mouth_talking2mouth"

        group eyewear auto

        group tears auto

        group sweat auto

        group anger auto:
            attribute angry "phobos_anger_anger"

        group blush auto

        group cry auto

        group eyeshine auto:
            attribute noshine "red_eyeshine_blank"

        always "phobos_eyesparkles" if_not ["noshine", "sad2brow", "happybrow", "closedbrow", "closedeyes", "deadeyes", "happyeyes", "thinking", "happy", "sad2eyes", "angry2eyes", "angry2brow", "playfuleyes", "playfulbrow", "winkeyes", "winkbrow", "unamusedbrow", "downeyes", "downbrow", "upeyes", "upbrow"] 
        always "phobos_eyesparkles_sad2eyes" if_any ["sad2eyes", "sad2brow"] if_not ["noshine"]
        always "phobos_eyesparkles_playfuleyes" if_any ["playfuleyes", "playfulbrow", "unamusedbrow"]
        always "phobos_eyesparkles_winkeyes" if_any ["winkeyes", "winkbrow"]
        always "phobos_eyesparkles_downeyes" if_any ["downeyes", "downbrow"]
        always "phobos_eyesparkles_upeyes" if_any ["upeyes", "upbrow"]
        
        group shadow auto

    #pokemon after this point

    layeredimage pikachu:
        group face auto
        
    image side pikachu = LayeredImageProxy("pikachu", Transform(yanchor=0.85, ypos=1.0, xpos=-0.03))
    image side pikachu night = LayeredImageProxy("pikachu", Transform(yanchor=0.85, ypos=1.0, xpos=-0.03, matrixcolor=nightmatrix))

    image libpikachuglow1: 
        "images/expressions/libpikachu/libpikachu_glow1_glow1.webp"
        matrixcolor TintMatrix(GetLiberaColor())
    image libpikachuglow2: 
        "images/expressions/libpikachu/libpikachu_glow2_glow2.webp"
        matrixcolor TintMatrix(GetLiberaColor(False))

    layeredimage libpikachu:
        zoom 0.3
        xalign 0.5
        yanchor 1.0
        ypos 1.0

        group tail auto:
            attribute neutraltail default
            attribute glowing "libpikachu_tail_neutral2tail"

        group body auto:
            attribute neutralbody default

        group glow1:
            attribute glowing "libpikachuglow1"

        group glow2:
            attribute glowing "libpikachuglow2"

        group eyes auto:
            attribute neutraleyes default
            attribute sad "libpikachu_eyes_sadeyes"
            attribute happy "libpikachu_eyes_happyeyes"
            attribute surprised "libpikachu_eyes_surprisedeyes"
            attribute thinking "libpikachu_eyes_closedeyes"
            attribute angrybrow "libpikachu_eyes_angryeyes"
            attribute sadbrow "libpikachu_eyes_sadeyes"
            attribute sad2brow "libpikachu_eyes_sad2eyes"
            attribute angry "libpikachu_eyes_angryeyes"
            attribute closedbrow "libpikachu_eyes_closedeyes"
            attribute happybrow "libpikachu_eyes_happyeyes"

        group mouth auto:
            attribute neutralmouth default
            attribute sad "libpikachu_mouth_sadmouth"
            attribute happy "libpikachu_mouth_happymouth"
            attribute angry "libpikachu_mouth_angrymouth"
            attribute surprised "libpikachu_mouth_surprisedmouth"
            attribute thinking "libpikachu_mouth_frownmouth"

        group tears auto

        group sweat auto

        group tired auto

        group anger auto:
            attribute angry "libpikachu_anger_anger"

        group blush auto

        group sparks auto

        group cry auto

        always "libpikachu_eyesparkles" if_not ["sad2brow", "happybrow", "closedbrow", "closedeyes", "deadeyes", "happyeyes", "thinking", "happy", "sad2eyes", "playfuleyes", "playfulbrow", "dizzyeyes"] 
        always "libpikachu_eyesparkles_sad2eyes" if_any ["sad2eyes", "sad2brow"]
        always "libpikachu_eyesparkles_playfuleyes" if_any ["playfuleyes", "playfulbrow"]

        group shadow auto
 
    image side libpikachu = LayeredImageProxy("libpikachu", Transform(xpos=0.05, yanchor=0.9))
    image side libpikachu night = LayeredImageProxy("libpikachu", Transform(yanchor=0.85, ypos=1.0, xpos=-0.03, matrixcolor=nightmatrix))

    layeredimage starterportraitfull:
        always "[starter_id]"

    image side starterportrait = LayeredImageProxy("starterportraitfull", Transform(xanchor=1.0, yanchor=0.95, ypos=1.0, xpos=1.0))

    layeredimage sideportraitfull:
        always "Pokemon/[sidemonnum].webp"

    layeredimage sideportraitfull2:
        always "Pokemon/[sidemonnum2].webp"

    layeredimage sideportraitfull3:
        always "Pokemon/[sidemonnum3].webp"

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
    image grimer = "Pokemon/88.1.webp"
    image aninetales = "Pokemon/fullaninetales.webp"
    image sugimoripikachu = "Pokemon/25.webp"
    image liberationpikachu = "Pokemon/25.2.webp"
    image liberationpikachutail = "Pokemon/25.2-1.webp"
    image liberationpikachucollar = "Pokemon/25.2-2.webp"
    image megaaltaria = "Pokemon/334.1.webp"
    image hypno = "Pokemon/fullhypno.webp"
    image deoxys = "Pokemon/fulldeoxys.webp"
    layeredimage deoxysblackeyes:
        always "Pokemon/fulldeoxys.webp"
        always "Pokemon/fulldeoxysblackeyes.webp"
    image supereevee:
        block:
            "Pokemon/134.webp"
            pause 0.5
            "Pokemon/135.webp"
            pause 0.5
            "Pokemon/136.webp"
            pause 0.5
            "Pokemon/196.webp"
            pause 0.5
            "Pokemon/197.webp"
            pause 0.5
            "Pokemon/470.webp"
            pause 0.5
            "Pokemon/471.webp"
            pause 0.5
            "Pokemon/700.webp"
            pause 0.5
            "Pokemon/134.webp"
            pause 0.5
            "Pokemon/135.webp"
            pause 0.5
            "Pokemon/136.webp"
            pause 0.5
            "Pokemon/196.webp"
            pause 0.5
            "Pokemon/197.webp"
            pause 0.5
            "Pokemon/470.webp"
            pause 0.5
            "Pokemon/471.webp"
            pause 0.5
            "Pokemon/700.webp"
        block:
            pause 0.5
            "Pokemon/134.webp"
            pause 0.25
            "Pokemon/135.webp"
            pause 0.25
            "Pokemon/136.webp"
            pause 0.25
            "Pokemon/196.webp"
            pause 0.25
            "Pokemon/197.webp"
            pause 0.25
            "Pokemon/470.webp"
            pause 0.25
            "Pokemon/471.webp"
            pause 0.25
            "Pokemon/700.webp"
            pause 0.25
            "Pokemon/134.webp"
            pause 0.25
            "Pokemon/135.webp"
            pause 0.25
            "Pokemon/136.webp"
            pause 0.25
            "Pokemon/196.webp"
            pause 0.25
            "Pokemon/197.webp"
            pause 0.25
            "Pokemon/470.webp"
            pause 0.25
            "Pokemon/471.webp"
            pause 0.25
            repeat 2
        block:
            "Pokemon/700.webp"
            pause 0.125
            "Pokemon/135.webp"
            pause 0.125
            "Pokemon/136.webp"
            pause 0.125
            "Pokemon/196.webp"
            pause 0.125
            "Pokemon/197.webp"
            pause 0.125
            "Pokemon/470.webp"
            pause 0.125
            "Pokemon/471.webp"
            pause 0.125
            "Pokemon/700.webp"
            pause 0.125
            "Pokemon/135.webp"
            pause 0.125
            "Pokemon/136.webp"
            pause 0.125
            "Pokemon/196.webp"
            pause 0.125
            "Pokemon/197.webp"
            pause 0.125
            "Pokemon/470.webp"
            pause 0.125
            "Pokemon/471.webp"
            pause 0.125
            "Pokemon/700.webp"
            pause 0.125
            "Pokemon/133.webp"
            repeat 3
    image flattia = Flatten("tia happy")
    image flatphobos = Flatten("phobos happy")
    image slowpoke = "Pokemon/79.webp"
    image gslowpoke = "Pokemon/79.1.webp"