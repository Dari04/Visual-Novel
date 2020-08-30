# PERSONAJES

layeredimage gatita:

    group background:

        attribute glow default:
            "glowing"

        attribute light:
            "gatita_fondo"

    always:
        "gatita_base"

    group orb:

        attribute moving default:
            "lantern"


        attribute stopped:
            "gatita_brillo"

image nena:
    "nena_en_cuarto" 
    resize(0.4)


layeredimage avaricia:

    group option:

        attribute regular default:
            "avaricia_regular"

        attribute mean:
            "avaricia_mean"


image avaricia_regular:
    "avaricia_base" 
    xoffset 100
    yoffset 50
    resize(0.5)
    hovering()

image avaricia_mean:
    "avaricia_con_brillo" 
    resize(0.5)

layeredimage envidia:

    group option:

        attribute regular default:
            "envidia_normal"
            zoom 0.5

        attribute mean:
            "envidia_enojado"
            zoom 0.5

layeredimage pereza:

    group body:

        attribute regular default:
            "pereza_normal"

        attribute tired:
            "pereza_cansado"

        attribute yawn:
            "pereza_bostezo"

    xoffset 350
    yoffset -75 

layeredimage gula:

    group option:

        attribute regular default:
            "gula_normal"
            zoom 0.5

        attribute mean:
            "gula_enojado"
            zoom 0.5
    yoffset -100


layeredimage humana_espiritu:

    always:         
        "glowing_background"

    always:
        "glowing_orbs"

    group base:

        attribute alone default:
            "humana_espiritu_normal"
            zoom 0.5

        attribute necklace:
            "humana_espiritu_collar"
            zoom 0.5
    group pendant:

        attribute none default:
            "transparent"

        attribute on_hand:
            "floating_necklace"
            yoffset 560
            xoffset 220


    yoffset -100

#items

image floating_necklace:
    "collar_item"
    zoom 0.05 
    soft_floating()

layeredimage glowing_necklace:

    always:         
        "glowing_backlight"

    always:
        "collar_dije"

    always:
        "glowing_shimmer"

    yoffset -150

image glowing_shimmer:
    "collar_luz_delante"
    glow()

image glowing_backlight:
    "collar_luz_atras"
    glowfloat()

image glowing_background:
    "humana_espiritu_fondo" 
    zoom 0.5
    glow()

image glowing_orbs:
    "humana_espiritu_brillo"
    zoom 0.5
    glowfloat()

image lantern:
    "gatita_brillo" 
    glowfloat()

image glowing:
    "gatita_fondo"
    glow()



# ESCENARIOS

layeredimage room:
    group option:

        attribute regular default:
            "bg room"
            zoom 1.46

        attribute gloom:
            "bg room gloom"
            zoom 1.46
    xalign 0.5
    yalign 1
  
image alley:
    "bg alley"
    resize(3.4)   

image garbage:
    "bg garbage"
    zoom 1.35

image bank:
    "bg bank"
    resize(1.40)   

image tracks:
    "bg tracks"
    resize(0.55)    
         
