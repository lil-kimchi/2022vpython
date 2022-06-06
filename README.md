# 2022vpython

220607 - [프로그램 개요 일지] 포격 게임 및 vpython 3D 그림판을 만들었다.
포격 게임은 x좌표, y좌표를 입력하면 십자(+) 모양으로 ^ 모양(산 모양) 으로 가득찬 bombingfield 가 포격받게 된다.
bombingfield.py 참고해주세요!!

vpython 3D 그림판 또는 3D펜은 말 그대로 3D로 그림을 그릴 수 있는 코드이다.

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

220531 - 깃허브 가입
