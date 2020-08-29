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

image lantern:
    "gatita_brillo" 
    glowfloat()

image glowing:
    "gatita_fondo"
    glow()

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

# ESCENARIOS

image room:
    "bg room"
    resize(1.46)
  
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
         
