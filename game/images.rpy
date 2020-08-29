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
  

# ESCENARIOS

image room:
    "bg room"
    resize(1.43)
  
image alley:
    "bg alley"
    resize(3.4)   

image bank:
    "bg bank"
    resize(1.40)   
         
