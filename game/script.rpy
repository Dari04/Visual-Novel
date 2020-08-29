# Characters 

define pe = Character("Un Perrito", image="perrito")
define av = Character("Avaricia")
define ra = Character("Una Ratita")
define en = Character("Envidia")
define pz = Character("Pereza")
define gu = Character("Gula")
define ir = Character("Ira")
define ga = Character("Una Gatita")
define lu = Character("Lujuria")
define so = Character("Soberbia")
define fb = Character("????")
define ni = Character("La Niña")
define na = Character("Narrador")



# Game start

label start:

# Las Escenas de 1 a 3 van acá
# Todas transcurren en el cuarto de la niña y no hay toma de decisiones

    $ ending_message = "FIN"

    play music "audio/acastromusic1.ogg" fadein 1 fadeout 2

    scene room 
    with dissolve

    "Los humanos son criaturas extrañas, las veo caminar velozmente en la calle, con una prisa que desconozco.  Como si no tuvieran tiempo para disfrutar."

    "Sin embargo, los he visto sonreír, llorar, dudar, amar y odiar… ¡Qué criaturas tan peculiares!"

    "Pero entre todos los que he visto, sólo hay alguien que me importa: mi dueña."

    show nena at center
    with dissolve

    "He estado con ella toda mi vida. Feliz de verme, feliz de verla."

    "No me interesa descubrir qué hay más allá de las paredes de esta habitación, mientras ella permanezca aquí."

    hide nena
    with dissolve

    pause(1)

    "¿Cuánto tiempo dormí?... ¿Dónde está?"

    "No está en su cama, ni en su escritorio haciendo tarea. Tampoco la encuentro buscando un lindo vestido que ponerse."

    "¿A dónde has ido?"

    pause(3)

    "Debe estar con los otros humanos en el piso de abajo, iré a buscarla…"

    scene black
    with dissolve

    pause(2)

    jump perrito


label perrito:

# Escena 4 A - Diálogo inicial y toma de decisiones

    scene alley
    with dissolve

    show perrito at adjustedleft
    with dissolve

    pe "Hola soy el perrito, qué hacés"


    menu:
    
        "Sí, quiero seguir camino":

            call sadperrito
            return 

        "mmmm no, mejor no":

            call sadperrito
            return 


label sadperrito:

# Escena 4 B - Diálogo final

    pe sad "Buuuuuu"
    with dissolve

    hide perrito
    with dissolve

    jump avaricia

label avaricia:

# Escena 5 - Todo el contenido
    
    av "Acá me habla con Avaricia"

    "charlamos un rato"

    av "Qué opinás"

    menu:

        "Sí, quiero seguir camino":

             "Le digo algo más antes de irme"

             jump ratita

        "mmmm no, mejor no":

            $ ending_message = "Mensaje del personaje"
            jump finalabierto

label ratita:

# Escena 6 - Todo el contenido - No hay decisión
    
    ra "Soy una ratita"

    "le hablo un poquito"

    ra "Te cuento algunas cosas"

    jump envidia


label envidia:

# Escena 7 - Todo el contenido    
    
    "Acá hablo con Envidia"

    en "Sí, charlamos un poco"

    menu:

        "Pienso un rato y le respondo"

        "Sí, quiero seguir camino":

            "Le digo algo más antes de irme"

            jump pereza

        "mmmm no, mejor no":
        
            $ ending_message = "Mensaje del personaje"
            jump finalabierto

label pereza:

# Escena 8 - Todo el contenido    

    
    "Acá hablo con Pereza"

    pz "tenemos una charla interesante, no?"

    menu:

        "Sí, quiero seguir camino":
           
            "Le digo algo más antes de irme"

            jump gula

        "mmmm no, mejor no":
        
        
            $ ending_message = "Mensaje del personaje"
            jump finalabierto

label gula:

# Escena 9 - Todo el contenido    
    
    gu "Acá hablás conmigo"

    "Pienso un rato y le respondo"

    menu:

        "Sí, quiero seguir camino":

            gu "Me dice algo más"

            jump ira

        "mmmm no, mejor no":
        
        
            $ ending_message = "Mensaje del personaje"
            jump finalabierto

label ira:

# Escena 10 - Todo el contenido    
    
    ir "yo soy mala onda"

    menu:

        "Pienso un rato y le respondo"

        "Sí, quiero seguir camino":

            ir "Te digo un par de cosas más"

            jump gatita

        "mmmm no, mejor no":
        
        
            $ ending_message = "Mensaje del personaje"
            jump finalabierto

label gatita:

# Escena 11 - Todo el contenido    

    show gatita at adjustedleft(0.25)
    
    ga "Hola, yo soy una gatita"

    "ok, me pareció"

    ga "hablo un poco más"

    jump lujuria

label lujuria:

# Escena 12 - Todo el contenido    

    
    lu "Hola soy Lujuria"

    "ok, como anda todo che"

    menu:

        "Pienso un rato y le respondo"

        "Sí, quiero seguir camino":

            lu "Me dice más cosas"

            jump soberbia

        "mmmm no, mejor no":
        
            $ ending_message = "Mensaje del personaje"
            jump finalabierto

label soberbia:

# Escena 13 - Todo el contenido   
    
    so "Soy Soberbia"

    "Ajá"

    so "Soy la mejor, te quedás"

    menu:


        "No, quiero seguir camino":

            so "siempre tengo razón"

            jump maloso

        "mmmm no, mejor no":
        
            $ ending_message = "Mensaje del personaje"
            jump finalabierto

label maloso:

# Escena 14 - Todo el contenido  

    fb "Soy el maloso final, tengamos una linda charla"

    menu:

        "No, quiero ver a la niña":

            fb "ok ok prosiga"

            jump encuentro

        "Ma sí matame":
        
            $ ending_message = "Mensaje del personaje"
            jump finalabierto

label encuentro:

 # Escena 15 - Todo el contenido   
 
    ni "hola, llegaste"

    "parece" 

    menu:

        "Quereme":

            jump finalvida

        "Te querré":
          
            jump finalmuerte


label finalabierto:

    "[ending_message]"

    return

label finalvida:

    ni "charlamos un poco, pero te digo chau"

    "Vuelvo a la vida"

    na "esto es lo que aprendiste - FIN"

    return

label finalmuerte:

    ni "charlamos un poco, y venís conmigo"

    "Nos unimos en la muerte"

    return



