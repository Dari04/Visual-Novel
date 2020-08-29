# Transformations 
transform glowfloat:
    parallel:
        glow(0.5)
    parallel:
        xalign 0.0
        easein 1.3 xalign 0.03
        easeout 1.2 xalign 0.0
        repeat
    parallel:
        yalign 0.0
        easeout 1.6 yalign 0.02
        easein 1.5 yalign 0.0
        repeat

transform glow(offset=0):
    pause(offset)
    alpha 1.0
    easein 1.3 alpha 0.8
    easeout 1.2 alpha  0.5
    easein 1.3 alpha  0.7
    easeout 1.2 alpha  1.0
    repeat
        
transform adjustedleft(zoomindex=0.5):
    zoom zoomindex
    xalign 0.25
    yalign 0.80

transform resize(zoomindex=4):
    zoom zoomindex
    xalign 0.5
    yalign 1

transform hovering:
    alignaround (0.5, 0.5)
    block:
        linear 30 yalign 0.1 clockwise circles 3
        repeat


