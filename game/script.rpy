# Characters 

define pe = Character("Un Perrito", image="perrito")
define av = Character("Avaricia")
define rb = Character("Una Ratita")
define en = Character("Envidia")
define pz = Character("Pereza")
define gu = Character("Gula")
define ir = Character("Ira")
define ga = Character("Una Gatita")
define lu = Character("Lujuria")
define so = Character("Soberbia")
define fb = Character("Un extraño")

# Game start

label start:

    play music "audio/audioloco.mp3"

    "El juego empieza pero no sé dónde estoy"

    jump perrito


label perrito:

    scene bg alley at adjustedbg
    with dissolve

    show perrito at adjustedleft
    with dissolve

    pe "Hola soy el perrito"

    pe "Acá te voy a estar contando algo"

    "uuuu no tengo idea de qué se trata este juego" 

    pe @ sad "Buuuuuu"
    with dissolve

    pe "Bueno, a ver decime, querés seguir?"

    menu:
    
        "Sí, quiero seguir camino":

            hide perrito
            with dissolve

            jump avaricia

        "mmmm no, mejor no":

            jump finalabierto



label avaricia:
    
    "Acá hablo con Avaricia"

    menu:

        "Pienso un rato y le respondo"

        "Sí, quiero seguir camino":

            jump ratita

        "mmmm no, mejor no":

            jump finalabierto

label ratita:
    
    "Acá hablo con una ratita"

    menu:

        "Pienso un rato y le respondo"

        "Sí, quiero seguir camino":

            jump envidia

        "mmmm no, mejor no":

            jump finalabierto


label envidia:
    
    "Acá hablo con Envidia"

    menu:

        "Pienso un rato y le respondo"

        "Sí, quiero seguir camino":

            jump pereza

        "mmmm no, mejor no":
        
            jump finalabierto

label pereza:
    
    "Acá hablo con Pereza"

    menu:

        "Pienso un rato y le respondo"

        "Sí, quiero seguir camino":

            jump gula

        "mmmm no, mejor no":
        
            jump finalabierto

label gula:
    
    "Acá hablo con Gula"

    menu:

        "Pienso un rato y le respondo"

        "Sí, quiero seguir camino":

            jump ira

        "mmmm no, mejor no":
        
            jump finalabierto

label ira:
    
    "Acá hablo con Ira"

    menu:

        "Pienso un rato y le respondo"

        "Sí, quiero seguir camino":

            jump gatita

        "mmmm no, mejor no":
        
            jump finalabierto

label gatita:

    show gatita at adjustedleft(0.25)
    
    ga "Hola, yo soy una gatita"

    ga "Querés venir conmigo?"

    menu:

        "No, quiero seguir camino":

            jump lujuria

        "Bueno!":
        
            jump finalabierto

label lujuria:
    
    "Acá hablo con Lujuria"

    menu:

        "Pienso un rato y le respondo"

        "Sí, quiero seguir camino":

            jump soberbia

        "mmmm no, mejor no":
        
            jump finalabierto

label soberbia:
    
    "Acá hablo con Soberbia"

    menu:

        "Pienso un rato y le respondo"

        "Sí, quiero seguir camino":

            jump maloso

        "mmmm no, mejor no":
        
            jump finalabierto

label maloso:

    "Acá hablo con el maloso final, me pregunta si quiero vivir solito"

    menu:

        "No, quiero ver a la niña":

            jump finalmuerte

        "Sí, quiero volver a mi casita":
        
            jump finalvida

label finalabierto:

    "Me FUIIIIIII con este personaje"

    return

label finalmuerte:

    "Nos unimos en la muerte"

    return

label finalvida:

    "Vuelvo a la vida"

    return



