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

image room:
    "bg room"
    resize(1.44)
  
image alley:
    "bg alley"
    resize(3.4)   

image nena:
    "nena_en_cuarto" 
    resize(0.4)
         
