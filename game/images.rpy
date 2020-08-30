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


layeredimage finalBoss:

    group option:

        attribute regular default:
            "fb_final"
            zoom 0.5

        attribute mean:
            "fb_inicial"
            zoom 0.5

image fb_regular:
    "fb_final" 
    xoffset 100
    yoffset 50
    resize(0.5)

image fb_mean:
    "fb_inicial" 
    xoffset 100
    yoffset 50
    resize(0.5)  


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

layeredimage lujuria:

    group option:

        attribute regular default:
            "lujuria_happy"
            zoom 0.45

        attribute mean:
            "lujuria_mad"
            zoom 0.45

    yoffset -30

layeredimage lujuria_happy:
    always:
        "glowing_smoke_purple"
    always:
        "lujuria_feliz"


layeredimage lujuria_mad:
    always:
        "glowing_smoke_pink"
    always:
        "lujuria_enojada"
    

layeredimage soberbia:

    group option:

        attribute regular default:
            "soberbia_uno"
            zoom 0.9

        attribute mean:
            "soberbia_dos"
            zoom 0.9
    xoffset 200


layeredimage ira:
    group option:

        attribute regular default:
            "ira_uno"
            zoom 0.5

        attribute mean:
            "ira_dos"
            zoom 0.5
    yoffset 100

# ITEMS

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

image glowing_smoke_pink:
    "lujuria_enojada_humo"
    glowfloat()

image glowing_smoke_purple:
    "lujuria_feliz_humo"
    glowfloat()

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

image hell:
    "bg finalboss"
    resize(1.60)

image tunel:
    "bg tunel"
    resize(1.40)

image callejon:
    "bg callejon"
    yalign 0.5
    zoom 2.7

image ciudad:
    "bg ciudad"
    resize(1.9)

