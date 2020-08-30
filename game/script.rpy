# Characters

define pe = Character("Un Perrito", image="perrito")
define av = Character("Avaricia")
define ra = Character("Una Ratita")
define en = Character("Envidia")
define pz = Character("Pereza", image="pereza")
define gu = Character("Gula", image="gula")
define ir = Character("Ira", image="ira")
define ga = Character("Una Gatita")
define lu = Character("Lujuria")
define so = Character("Soberbia")
define fb = Character("????")
define ni = Character("La Niña")
define na = Character("Narrador")


init:
    python:

        ending_message = "FIN"

        happy_music = "audio/acastromusic1.ogg"

        dangerous_music = "audio/acastromusic2.ogg"

        def play_music(song, fadein_value=0.3, fadeout_value=0.15):
            if renpy.music.get_playing() is not None:
                track = renpy.music.get_playing()
                if track is not song:
                    renpy.music.play(song, "music", fadein=fadein_value, fadeout=fadeout_value)

        def play_eating_sounds():
            renpy.music.set_volume(0.3, 0.5, channel='music')
            renpy.music.play("audio/ariel_chewing.mp3", channel='sound')
            renpy.music.queue("<from 17>audio/bbrocer_wet-sloppy-eating-2.mp3", channel='sound')
            renpy.music.queue("<silence .3>", channel='sound')
            renpy.music.queue("audio/ariel_chewing.mp3", channel='sound')
            renpy.music.queue("audio/bbrocer_wet-sloppy-eating-2.mp3", channel='sound')

        def stop_eating_sounds():
            renpy.music.stop(channel='sound')
            renpy.music.set_volume(1, 0.5, channel='music')

# Game start

label start:

# Las Escenas de 1 a 3 van acá
# Todas transcurren en el cuarto de la niña y no hay toma de decisiones

    play music happy_music fadein 1 fadeout 2

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

    $ play_music(happy_music, 1, 2)

    scene alley
    with dissolve

    show perrito at adjustedleft
    with dissolve

    pe "Hola soy el perrito, qué hacés"


    menu:

        "Sí, quiero seguir camino":

            call sadperrito from _call_sadperrito
            return

        "mmmm no, mejor no":

            call sadperrito from _call_sadperrito_1
            return


label sadperrito:

# Escena 4 B - Diálogo final

    $ play_music(happy_music, 1, 2)

    pe sad "Buuuuuu"
    with dissolve

    stop music fadeout 1

    hide perrito
    with dissolve

    jump avaricia

label avaricia:

# Escena 5 - Todo el contenido

    $ play_music(dangerous_music)

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

    $ play_music(dangerous_music)

    ra "Soy una ratita"

    "le hablo un poquito"

    ra "Te cuento algunas cosas"

    jump envidia


label envidia:

# Escena 7 - Todo el contenido

    $ play_music(dangerous_music)

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

    $ play_music(dangerous_music)

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

    pz "No te canses buscándola, quédate conmigo y descansa… puedes verla en sueños si gustas… Zzzzz…"

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

    $ play_music(dangerous_music)

    scene garbage
    with dissolve

    show gula
    with dissolve

    $ play_eating_sounds()

    gu "Chomp, chomp {b}{i}*sonido grotesco al masticar*{/i}{/b} Hola pequeñín, ¿gustas un trozo de pollo? Es una delicia, jeejejeje."

    "N-No gracias ugh…"

    gu "Bueno, te lo pierdes, chomp, chomp, ¿y qué haces en un lugar como éste?… Chomp, chomp."

    "Mmm, he estado buscando a mi dueña y no la encuentro por ningún lado…"

    gu "¿¿Una amiga, eh??, Jejejeje, ¿al menos sabes que sitio es éste? Chomp, chomp… Qué bueno está ésto {b}{i}*tragar*{/i}{/b}."

    "No, solo desperté aquí… he pasado por muchos sitios…"

    gu "Eso explica mucho, chomp, chomp, de todas formas no la encontrarás jamás, te lo aseguro. Además estas tan flaco como un costal de huesos que das pena, chomp, chomp… "

    "¿P-Por qué dice eso?… Yo sé que puedo encontrarla."

    gu "Jajaja, tú no sabes nada, por eso lo dices, la falta de comida dañó tu pequeño cerebro, chomp, chomp… deja ya ese juego del pilla pilla y gocemos una vida con muchas golosinas jejeje. "

    $ stop_eating_sounds()

    show gula mean
    with dissolve

    menu:

        "Mmm…"

        "Está bien, a lo mejor ella está allí…":

            $ ending_message = "Una vida sencilla es mejor a una con excesos…"
            jump finalabierto

        "Lo siento pero debo encontrarla.":
            jump ira


label ira:

# Escena 10 - Todo el contenido

    $ play_music(dangerous_music)

    scene tunel
    with dissolve

    show ira
    with dissolve

    ir "¡Largo de aquí, estúpida criatura!"

    " Tranquilízate, no vengo a molestarte, sólo estoy buscando a mi dueña. Ella desapareció y no tengo idea de dónde está. ¿La has visto? Ella usa un collar muy hermoso."

    ir " ¡Ja! Vaya que eres tonto, ¿no te das cuenta? ¡Tu dueña te dejo! Todos lo hacen, te usan y te desechan. No pierdas el tiempo buscándola, ¡ella te hizo daño!"

    "Ella no me hizo daño, pero, he enfrentado muchas cosas por buscarla, estoy tan cansado…"

    ir "¿Vale la pena buscar a esa malagradecida? ¡Que se pudra esa maldita! ¡Olvídala!"

    show ira mean
    with dissolve

    ir "Ven conmigo, te prometo que ella pagará por todo el daño que te hizo."

    menu:

        "No voy a abandonarla, aunque ella lo haya hecho.":

           # Conectar nuevamente cuando Iteración 2 se realice
           #jump gatita
           jump lujuria

        "¡SÍ! ¡Quiero vengarme!":

           ir "¡Idiota! ¡Te arrepentirás de tu decisión!"

           show ira
           with dissolve

           $ ending_message = "La ira te confiere un gran poder."
           jump finalabierto


label gatita:

# Escena 11 - Todo el contenido

    $ play_music(dangerous_music)

    show gatita at adjustedleft(0.25)

    ga "Hola, yo soy una gatita"

    "ok, me pareció"

    ga "hablo un poco más"

    jump lujuria


label lujuria:

# Escena 12 - Todo el contenido

    $ play_music(dangerous_music)

    scene callejon
    with dissolve

    show lujuria
    with dissolve

    lu "¡HOLA CHIKIS!  ¿TE QUIERES DIVERTIR?  AQUÍ HAY ESPACIO PARA TI."

    "...Qué desagradable… ¿Eres lo que creo que eres?"

    lu "YO SOY UNO, AQUÍ NO HAY DISCRIMINACIÓN, SÓLO LA DIVERSIÓN QUE TODOS DESEAN."

    "Eso es repulsivo en muchos aspectos. Realmente este lugar es aterrador y tu presencia me desagrada muchísimo."

    lu "¿QUÉ TE DESAGRADA? ¿ACASO NO SABES DE AMOR? DAR Y RECIBIR AMOR ES LO MÁXIMO."

    " ¡Claro que sé de amor! Precisamente estoy buscando a alguien que me ama muchísimo y es alguien a quien yo amo en demasía. "

    show lujuria mean
    with dissolve

    lu "Es probable que se haya unido a mí, yo tengo la capacidad de absorber todas las muestras de amor, y convertirlas en algo mejor… ¿te unirías a mí?  Te aseguro que te sentirás mejor."

    menu:

        "NO, ES REPULSIVO.":

            lu "¡TÚ TE LO PIERDES! NO ENCONTRARÁS UN MEJOR LUGAR QUE CONMIGO, TE LO ASEGURO. SOY MUCHO MEJOR QUE EL AMOR QUE TODOS PROFESAN, ¡YO SOY EL PLACER!"

            lu " ADEMÁS, AQUELLA  NIÑA  QUE BUSCAS YA NO TIENE CAPACIDAD DE SENTIR,  RECUERDA ESTO: NUNCA MÁS PODRÁ SENTIR UNA CARICIA, NI SIQUIERA TUYA."

            jump soberbia

        "Sólo iré si ella está ahí…":

            $ ending_message = "A los sentimientos del alma, el  cuerpo escucha, y se olvida..."
            jump finalabierto

label soberbia:

# Escena 13 - Todo el contenido


    $ play_music(dangerous_music)

    scene ciudad
    with dissolve

    show soberbia at right
    with dissolve

    so "¿Quién osa entrar a mis aposentos? ¿Tú? Una criatura tan inferior a mí…"

    "Soy de la creencia de que todos somos iguales. Estoy buscando a mi dueña, ha desaparecido y no sé donde está. Pero me han dicho que tal vez cruzó por aquí."

    so " ¿Iguales? Qué tontería… y nadie importante ha pasado por aquí, bueno, claro, sólo yo."

    "Que arrogante eres."

    so "Eso dicen los mediocres, como tú, tontos que buscan a sus dueños. ¿Y qué van a hacer al encontrarlos? ¿Llevarse los huesos? ¡Jajaja! Los muertos nunca regresan."

    "Mi dueña no está muerta."

    show soberbia mean
    with dissolve

    so "Si te crees esa mentira, no es mi problema, yo tengo la verdad. Me da igual, ya perdí mi valioso tiempo contigo. Te advierto, si continúas, jamás verás a tu dueña…"

    menu:

       "Si es verdad lo que dices, entonces, me quedaré contigo.":

            show soberbia 
            with dissolve

            $ ending_message = "La soberbia somete a la naturaleza a su voluntad"
            jump finalabierto

       "Buscaré mi propia verdad.":

            so "Sólo los seres inferiores se atreven a ignorar mis consejos, retírate. "

            jump maloso


label maloso:

# Escena 14 - Todo el contenido


    $ play_music(dangerous_music)


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


    $ play_music(happy_music)

    ni "hola, llegaste"

    "parece"

    menu:

        "Quereme":

            jump finalvida

        "Te querré":

            jump finalmuerte


label finalabierto:

    $ play_music(happy_music)

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

    $ play_music(happy_music)

    ni "charlamos un poco, pero te digo chau"

    "Vuelvo a la vida"

    na "esto es lo que aprendiste - FIN"

    return

label finalmuerte:

    ni "charlamos un poco, y venís conmigo"

    "Nos unimos en la muerte"

    return
