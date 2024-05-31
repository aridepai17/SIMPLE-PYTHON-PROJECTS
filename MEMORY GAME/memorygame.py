import simpleguitk as simplegui
import random

click1 = 0
click2 = 0
label = None
deckcards = []
exposed = []
state = 0
turns = 0

def newgame():
    global deckcards, exposed, turns, state 
    state = 0
    turns = 0
    deckcards = [i % 8 for i in range(16)]
    exposed = [False for _ in range(16)]
    
    random.shuffle(deckcards)
    label.set_text("Turns = " + str(turns))

def mouseclick(pos):
    global click1, click2, turns, state, exposed, deckcards
    choice = int(pos[0] / 50)
    
    if not exposed[choice]:  
        if state == 0:
            state = 1
            click1 = choice
            exposed[click1] = True
        elif state == 1:
            state = 2
            click2 = choice
            exposed[click2] = True
            turns += 1
        elif state == 2:
            if deckcards[click1] != deckcards[click2]:
                exposed[click1] = False
                exposed[click2] = False
            click1 = choice
            exposed[click1] = True
            state = 1

        label.set_text("Turns = " + str(turns))

def draw(canvas):
    for i in range(16):
        if exposed[i]:
            canvas.draw_text(str(deckcards[i]), (i * 50 + 10, 60), 40, "Pink")
        else:
            canvas.draw_polygon([(50 * i, 0), (50 * i, 100), (50 * i + 50, 0), (50 * i + 50, 100)], 3, "White", "Grey")

frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", newgame, 150)
label = frame.add_label("Turns = 0")

frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

newgame()
frame.start()
