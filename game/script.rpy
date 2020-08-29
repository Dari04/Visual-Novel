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

    "Pero entre todos los que he visto, solo hay alguien que me importa: mi dueña."

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

# Conectar nuevamente cuando Iteración 2 se realice
#    jump perrito
    jump avaricia


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

    stop music fadeout 1

    hide perrito
    with dissolve

    jump avaricia

label avaricia:

# Escena 5 - Todo el contenido

    play music "audio/acastromusic2.ogg" fadein 0.3 fadeout 0.15

    scene bank 
    with dissolve

    show avaricia 
    with dissolve

    pause(2)

    "¡Hola!, ¿puedo saber cómo consiguió ese collar?"
    
    av "¿Y tú quién eres? ¿Te refieres a ésto? Acabo de comprarlo, ¿no crees que es bellísimo? JAJAJA-"

    "Sí que es bonito, pero no era lo que buscaba, se parece al collar que usa alguien que aprecio mucho."

    av "JAJAJA, el dinero lo es todo sin él no eres nada, solo mírate, si tuvieras dinero ella no te habría abandonado JAJAJAJA."

    "¡¡¡NO ES CIERTO, ella no me abandonaría jamás porque me ama!!!"

    av "Ríndete y disfrutemos de mis riquezas juntos. es una oferta que hago a menudo ¿sabes? Decídelo mientras aún puedas JAJAJAJA, conmigo a tu lado lo tendrás todo."

    menu:

        "Tal vez tengas razón, ME IRÉ CONTIGO.":

            show avaricia mean
            
            $ ending_message = "Soy la raíz de todos los problemas, jamás serás feliz."
            jump finalabierto


        "¡¡NO ME RENDIRÉ!!":

            show avaricia mean

            av "HAZ LO QUE QUIERAS NO ME IMPORTA, ¡¡¡NO HAY NADA MEJOR QUE LAS RIQUEZAS!! LAMENTARÁS NO HABER VENIDO CONMIGO."

            "Perdone por las molestias, solo espero que algún día comprenda que las riquezas son pasajeras…"

# Conectar nuevamente cuando Iteración 2 se realice
             #jump ratita
            jump envidia

label ratita:

# Escena 6 - Todo el contenido - No hay decisión
    
    ra "Soy una ratita"

    "le hablo un poquito"

    ra "Te cuento algunas cosas"

    jump envidia


label envidia:

# Escena 7 - Todo el contenido   

    scene bg antiques 
    with dissolve 

    show envidia at right
    with dissolve
    
    "¡Hola!, ¿podrías ayudarme? Estoy buscando a alguien sumamente importante para mí."

    en "¿QUIÉN ERES TÚ? ¿Acaso sabes dónde te has metido?..."

    "Realmente no sé qué lugar sea este, pero por ella puedo llegar a cualquier lugar… Haría lo que fuera por estar con ella otra vez."

    en "¿Por qué preocuparse por alguien más? ¡Ella no te ama!  Si tanto lo hiciera nunca se hubiera ido."

    "Tienes razón, ella me adora, y eso para mí es ir más allá del amor."

    en "No lo entiendes, nunca nadie ha amado tanto a otro. Lo sé, yo esperé por un amor eterno, observando a la distancia a los enamorados,  a la gente que fingía sentir…"

    en "Nadie puede amar tanto a nadie, entiéndelo de una vez… Pero yo te ofrezco mi compañía,  unidos hasta el fin de los tiempos, burlándonos de aquellos que  pretenden amar… DE CUALQUIER FORMA YA NO PUEDES REGRESAR…"

    menu:

        "¡NO! ¡SUENA HORRIBLE!":

            en "Como tú lo prefieras,  solo espero que nunca llegues a conseguir aquello que tanto deseas. Espero que desvíes tu camino y que te pierdas en él."

            show envidia mean
            with dissolve

            "Yo espero que puedas preocuparte por tí y no por los demás. Busca la paz en tí mismo y no odies a  aquellos con los que te encuentras." 

            jump pereza

        "¿SI ME QUEDO CONTIGO PODRÍA SER FELIZ?":

            show envidia mean
            with dissolve
        
            $ ending_message = "Alguien como yo, nunca permitiría que pudieras ser feliz."
            jump finalabierto

label pereza:

# Escena 8 - Todo el contenido    

    scene tracks 
    with dissolve

    show pereza at right
    with dissolve
    
    "D-Disculpe."

    pz "Hmmm... ¿qué quieres?"

    "Busco a alguien muy importante para mí, y… no se duerma por favor…"

    pz "Aaah, te abandonó, ¿verdad? Jajajaja."

    "¡Eso no es cierto! Me desperté dentro de este extraño mundo y no sé dónde podría estar ella, nos queremos mucho y sé que ella no me abandonaría así como  así."

    show pereza yawn at right
    with dissolve
  
    pz "No te canses buscándola, quédate conmigo y descansa… puedes verla en sueños si gustas... Zzzzz..."

    show pereza at right
    with dissolve

    menu:

        "Gracias, pero la seguiré buscando.":

            show pereza tired at right
            with dissolve
           
            "Si descanso ahora, tal vez no me despierte más y me encierre en un mundo de sueños…"

            jump gula

        "Solo dormiré un poco, no será malo.":
        
            show pereza tired at right
            with dissolve
       
            $ ending_message = "“Tus metas pueden esperar, dormir no hace daño a nadie”\nAtte: Pereza"
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

 # Conectar nuevamente cuando Iteración 2 se realice
            #jump gatita
            jump lujuria

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

    stop music fadeout 2.5

    pause(1.5)
 
    scene black
    with dissolve

    show text "FIN"
    with dissolve
    with Pause(1.5)

    scene black
    with dissolve

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



