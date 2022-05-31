scene.range = 5
box(size = vec(0.000001, 0.000001, 0.000001))

drag = False
s = None

def down():
    global drag, s
    s = sphere(pos=scene.mouse.pos,
        color=color.white,
        size=0.2*vec(0.1,0.1,0.1), make_trail = True)
    drag = True

def move():
    global drag, s
    if drag:
        s.pos = scene.mouse.pos

def up():
    global drag, s
    s.color = color.white
    drag = False

scene.bind("mousedown", down)

scene.bind("mousemove", move)

scene.bind("mouseup", up)
