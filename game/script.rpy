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

    "Tranquilízate, no vengo a molestarte, solo estoy buscando a mi dueña. Ella desapareció y no tengo idea de dónde está. ¿La has visto? Ella usa un collar muy hermoso."

    ir "¡Ja! Vaya que eres tonto, ¿no te das cuenta? ¡Tu dueña te dejó! Todos lo hacen, te usan y te desechan. No pierdas el tiempo buscándola, ¡ella te hizo daño!"

    "Ella no me hizo daño, pero, he enfrentado muchas cosas por buscarla, estoy tan cansado…"

    ir "¿Vale la pena buscar a esa malagradecida? ¡Que se pudra esa maldita! ¡Olvídala!"

    show ira mean

    ir "Ven conmigo, te prometo que ella pagará por todo el daño que te hizo."

    menu:

        "No voy a abandonarla, aunque ella lo haya hecho.":

            ir "¡Idiota! ¡Te arrepentirás de tu decisión!"

            ir "Sal de mi vista…"

            # Conectar nuevamente cuando Iteración 2 se realice
            #jump gatita
            jump lujuria

        "¡SÍ! ¡Quiero vengarme!":

            show ira regular
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

    show lujuria at left
    with dissolve

    lu "¡HOLA CHIKIS!  ¿TE QUIERES DIVERTIR?  AQUÍ HAY ESPACIO PARA TI."

    "¡Hola! Ahora mismo no tengo tiempo para divertirme, estoy buscando a alguien a quien amo pero de repente desapareció"

    lu "¡¿Amor?! ¡Yo sé de eso! En mí vamos más allá del amor, todo lo que hacemos es darnos amor, amor y más amor… Tanto así que vamos al límite. ¡Hasta el placer!"

    "¿Placer? ¿Eso es como sentirte feliz? Realmente no lo entiendo muy bien."

    lu "¡DAR Y RECIBIR AMOR ES LO MEJOR! Esto va más allá de pequeños toques, esto implica fusionarse con más y más seres llenos de deseo… ¿O acaso no sabes qué es este tipo de amor?"

    "¡Claro que sé de amor! Precisamente estoy buscando a alguien que me ama muchísimo y es alguien a quien yo amo en demasía."

    lu "Entonces es probable que se haya unido a mí, yo tengo la capacidad de absorber todas las muestras de amor, y convertirlas en algo mejor… ¿te unirías a mí?  Te aseguro que te sentirás mejor."

    show lujuria mean at left
    with dissolve

    menu:

        "NO, NO CREO QUE SEA EL AMOR QUE BUSCO.":

            lu "¡TÚ TE LO PIERDES! NO ENCONTRARÁS UN MEJOR LUGAR QUE CONMIGO, TE LO ASEGURO. SOY MUCHO MEJOR QUE EL AMOR QUE TODOS PROFESAN, ¡YO SOY EL PLACER!"

            lu "ADEMÁS, AQUELLA  NIÑA  QUE BUSCAS YA NO TIENE CAPACIDAD DE SENTIR, RECUERDA ESTO: NUNCA MÁS PODRÁ SENTIR UNA CARICIA, NI SIQUIERA TUYA."

            jump soberbia

        "Solo iré si ella está ahí…":

            $ ending_message = "A los sentimientos del alma, el  cuerpo escucha, y se olvida…"
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

    so "¿Iguales? Qué tontería… y nadie importante ha pasado por aquí, bueno, claro, sólo yo."

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

            so "Solo los seres inferiores se atreven a ignorar mis consejos, retírate. "

            jump maloso


label maloso:

# Escena 14 - Todo el contenido


    $ play_music(dangerous_music)


    scene hell
    with dissolve
    
    show finalBoss mean
    with dissolve

    fb "AL FIN HAS LLEGADO, ME HE CANSADO DEMASIADO DE ESPERAR POR TI."
    
    "Después de todo lo que acabo de ver, solo quisiera descansar. Mi alma  ya no aguanta y mi corazón está roto. Ya no quiero ver a nadie más, excepto a ella."
    
    fb "ADMIRO TODO LO QUE HAS HECHO HASTA AHORA, PERO TEMO DECIRTE QUE TODOS AQUELLOS QUE APARECEN EN ESTE MUNDO ESTÁN CONDENADOS AL DOLOR Y SUFRIMIENTO ETERNO."
    
    fb "ESTÁS EN UN PUNTO DE NO RETORNO. NUNCA MÁS LA VERÁS. NUNCA MÁS VERÁS LA LUZ DEL SOL. Y SOBRE TODO, ESTÁS CONDENADO A VAGAR PARA SIEMPRE EN ESTE LUGAR."
    
    "¿Tú me dirás que es este lugar? Tengo miedo, quiero volver, pero también quiero verla, quiero verla una última vez antes de sufrir para siempre..."
    
    fb "ESTE ES UN LUGAR AL QUE TÚ NO PERTENECES. AQUÍ SOLO VIENEN AQUELLOS QUE SUFRIERON DEMASIADO ESTANDO VIVOS."
    
    fb "TODO EL DOLOR DE LA EXISTENCIA HUMANA SE MANTIENE EN ESTE LUGAR."
    
    fb "PERO YO PUEDO CALMAR TU DOLOR. PODRÍA TERMINAR CON TU VIDA EN ESTE INSTANTE Y ENVIARTE AL  UNIVERSO QUE MERECES. DE CUALQUIER  FORMA, VERLA YA NO ES UNA OPCIÓN."
    
    fb "EL DOLOR  QUE TUVO EN SUS ÚLTIMOS INSTANTES FUE SUFICIENTE PARA QUE ELLA APARECIERA AQUÍ. DE CUALQUIER MODO, ES IMPOSIBLE QUE VUELVAN A ENCONTRARSE."
    
    "Ha sido un largo viaje, sólo quisiera verla pero..."
    
    menu:

        "SI MORIR ES LA ÚNICA OPCIÓN  PARA YA NO SUFRIR, ENTONCES TERMINA CONMIGO.":

            show finalBoss regular
            with dissolve

            fb "ME AGRADA TANTO TU HONESTIDAD Y TU DOLOR,  AL FIN TE HAS RENDIDO. ASÍ QUE TE PERMITIRÉ CUMPLIR CON TU PROPÓSITO Y DE ESTA FORMA,  NO SERÉ YO QUIEN TERMINE CON TU VIDA…"

            jump encuentro

        "¿LA CONOCES? NECESITO VERLA, POR ÚLTIMA VEZ.":
        
            $ ending_message = "DEBES APRENDER A VIVIR POR TI Y NO POR ALGUIEN.  EXTRAÑAR A ALGUIEN QUE AMAS, SOLO TE ARRASTRA AL DOLOR."
            jump finalabierto

label encuentro:

 # Escena 15 - Todo el contenido

    $ play_music(happy_music)

    scene room gloom
    with dissolve

    show humana_muerta
    with dissolve

    ni "¿Mi habitación? Parece que han pasado siglos desde la última vez que estuve aquí. En aquel lugar había edificios gigantes."

    ni "Calles que resultaban interminables… Aromas nauseabundos, y justo cuando creí que estaba destinada a sufrir por la eternidad, volviste por mí."

    ni "Pero deberías entender, ya no puedo estar aquí. Y no puedo estar más tiempo contigo…"

    "¿ERES TÚ? ¿DE VERDAD ERES TÚ? {w=2} ¡No sabes cuánto te extrañé! ¿POR QUÉ ME ABANDONASTE?"

    ni "Ha pasado de todo,  incluso ahora puedo entender lo que dices… Nunca te abandoné,  me obligaron a irme. Yo jamás me iría sin ti."

    ni "Podría decir que solo tú me mantenías con vida.  Te extrañé tanto, pero no puedo estar contigo nuevamente."

    "¡NO QUIERO! ¡QUIERO ESTAR CONTIGO POR SIEMPRE!, NO ME IMPORTA LO QUE TENGA QUE HACER, A DÓNDE DEBA IR O CON CUÁNTOS MONSTRUOS DEBA LIDIAR, NO QUIERO DEJARTE."

    ni "Mírame bien, ahora no puedo pertenecer a este mundo…  Debo dejarte aquí y volver.  No queda mucho tiempo, si permanezco aquí no podré volver a verte, incluso si tú mueres, no podrías verme. Desaparecería para siempre."

    "NO QUIERO QUE DESAPAREZCAS, QUIERO ESTAR CONTIGO POR LA ETERNIDAD"

    show humana_muerta triste
    with dissolve

    pause(2)

    ni "Yo no puedo ofrecerte una hermosa eternidad, has visto ese lugar. Lo que menos deseo es compartir dolor y sufrimiento contigo. Te adoro tanto, y te adoraré para siempre.  Pero no quiero decidir por tí así que dime algo…"

    ni "¿Realmente me amas tanto?"

    menu:

        "ÁMAME PARA SIEMPRE,  JUSTO COMO YO LO HAGO":

            show humana_muerta regular
            with dissolve

            jump finalvida

        "TE AMARÉ Y TE ACOMPAÑARÉ PARA SIEMPRE":

            jump finalmuerte

label finalvida:

    $ play_music(happy_music)

    show humana_espiritu necklace
    with dissolve

    hide humana_muerta regular
    
    ni "LO HARÉ, JAMÁS DEJARÉ DE AMARTE… PROMETE QUE VIVIRÁS Y SERÁS FELIZ A PESAR DE TODO…"

    "YO… LO PROMETO,  aunque no sé si tenga las fuerzas suficientes para hacerlo…"

    ni "SE QUE PODRÁS, PORQUE SIEMPRE ESTARÉ CONTIGO…"

    show humana_espiritu alone on_hand
    with dissolve

    ni "ESTE COLLAR ES LA PRUEBA DE ELLO… mira este collar cuando te sientas solo y triste."

    ni "Recuerda que yo estaré contigo aunque no me puedas ver, juntos venceremos cada obstáculo como lo hicimos hasta ahora…"

    "¡GRACIAS! LO ATESORARÉ POR SIEMPRE… JAMÁS TE OLVIDARÉ… ¡¡¡JAMÁS!!!"

    ni "Lo sé… sé que serás feliz… debes seguir tu camino, apresúrate antes de que sea tarde."

    scene room regular
    with dissolve

    show glowing_necklace at resize(0.5) 
    with dissolve

    "Ese día aprendí que aunque no la vuelva a ver jamás... ella siempre vivirá en mi corazón y con este collar, ella estará conmigo siempre que me sienta solo…"

    "Los años pasaron y como lo había prometido continué mi vida, disfrutando cada momento, superando cada obstáculo,  sabía que ella estaría siempre ahí, para mí."

    window hide

    stop music fadeout 2.5

    pause(1.5)
 
    scene black
    with dissolve

    jump credits

label finalmuerte:

    $ play_music(happy_music)

    ni "¿Estás de acuerdo? Volveremos a aquellos lugares que cruzaste, aunque de ser posible encontraríamos algo mejor."

    "Lo único que importa es que estaremos juntos, como siempre."

    hide humana_muerta triste

    show humana_fuego
    with dissolve

    ni "Tienes razón, nuestras almas siempre estuvieron juntas, incluso en la distancia."

    ni "Una parte de mí habría querido que vivieras y disfrutaras de muchas mañanas cálidas, pero en el fondo, me alegra saber que te quedarás conmigo. Ya no tengo miedo de seguir caminando hacia la luz."

    "Te quiero mucho."

    ni "Yo también te quiero mucho, gracias por enfrentar a la oscuridad por mí."

    show humana_fuego encendido

    ni "Es momento de irnos, hay que seguir adelante."

    window hide

    stop music fadeout 2.5

    pause(3)
 
    scene black
    with dissolve

    jump credits

label credits:

    show text "Acá van los créditos"

    pause(2)

    return 


label finalabierto:

    $ play_music(dangerous_music)
    
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

