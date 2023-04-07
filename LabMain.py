from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
#import ventilador

WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720

eye = [0, 0, 0]
center = [0, 0, 0]
up = [0, 1, 0] 

UNIT_DIST = 1
UNIT_PIXEL = 0.2
unit_vel = 5

colors = {
    "white": [0.9, 0.9, 0.9, 0.],
    "red": [1.0, 0.0, 0.0, 0.],
    "green": [0.0, 1.0, 0.0, 0.],
    "blue": [0.0, 0.0, 1.0, 0.],
    "yellow": [1.0, 1.0, 0.0, 0.]
}

def init():
    global eye
    eye = [0, 20, 40]

    glClearColor(0.0, 0.1, 0.0, 1.0) 
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(eye[0]   , eye[1]   , eye[2],
              center[0], center[1], center[2],
              up[0]    , up[1]    , up[2])

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, WINDOW_WIDTH/WINDOW_HEIGHT, 0.1, 100)

def move_camera():
    global eye
    global center
    global up

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(eye[0]   , eye[1]   , eye[2],
              center[0], center[1], center[2],
              up[0]    , up[1]    , up[2])

def draw_ceil():
    glPushMatrix()
    glColor4fv(colors["white"])
    glTranslatef(0.0, 5.5, 0.0)
    glScalef(153, 5, 70)
    glutWireCube(UNIT_PIXEL * 1)
    glPopMatrix()

def draw_floor():
    glPushMatrix()
    glColor4fv(colors["white"])
    glTranslatef(0, -5.0, 0)
    glScalef(153, 3, 70)
    glutSolidCube(UNIT_PIXEL * 1)
    glPopMatrix()

    # Criação do plano na face frontal
    glPushMatrix()
    glColor4fv(colors["red"])
    glTranslatef(0, 0, 7)
    glScalef(153, 50, 3)
    glutSolidCube(UNIT_PIXEL * 1)
    glPopMatrix()

    # Criação do plano na face traseira
    glPushMatrix()
    glColor4fv(colors["green"])
    glTranslatef(0, 0, -7)
    glScalef(153, 50, 3)
    glutSolidCube(UNIT_PIXEL * 1)
    glPopMatrix()

    # Criação do plano na face esquerda
    glPushMatrix()
    glColor4fv(colors["blue"])
    glTranslatef(14.8, 0, 0)
    glScalef(5, 50, 70)
    glutSolidCube(UNIT_PIXEL * 1)
    glPopMatrix()

    # Criação do plano na face direita
    glPushMatrix()
    glColor4fv(colors["yellow"])
    glTranslatef(-14.8, 0, -2)
    glScalef(5, 50, 54)
    glutSolidCube(UNIT_PIXEL * 1)
    glPopMatrix()

def draw_door():
    glPushMatrix()
    glTranslatef(-14.8, 0.0, 5.0)
    glScalef(0.6,10.0, 3)
    glColor3f(0.3, 0.3, 0.3)
    glutSolidCube(1.0)
    glPopMatrix()   

def draw_viga():
    glPushMatrix()
    glTranslatef(-14.8, 5.0, 0.0)
    glScalef(1, 0.3, 15)
    glColor3f(0.1, 0.1, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()

def draw_table1():
    glPushMatrix()
    glTranslatef(3.0, 0.0, 5.0)
    glScalef(20.0,0.0, 3.0)
    glColor3f(0.3, 0.3, 0.3)
    glutSolidCube(1.0)
    glPopMatrix()

def draw_cabinet():
    glPushMatrix()
    glTranslatef(4, 3.5, -5.7)
    glScalef(20.0,2.0, 3.0)
    glColor3f(0.3, 0.3, 0.3)
    glutSolidCube(1.0)
    glPopMatrix()

    #desenha o pé esquerdo da mesa
    glPushMatrix()
    glTranslatef(12, -2.0, 4.0)
    glScalef(0.5, 4.0, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()

    #desenha o pé direito da mesa
    glPushMatrix()
    glTranslatef(-6, -2.0, 4.0)
    glScalef(0.5, 4.0, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()

def draw_notebook():
    glPushMatrix()
    glTranslatef(0.0, 0.3, 5)
    glScale(2.0,0.0,1.0)
    glColor3f(0.0, 0.0, 0.0)
    glutSolidCube(1.0)
    glPopMatrix()

def draw_board():
    glPushMatrix()
    glTranslatef(-14.3, 2.0, -2.0)
    glScalef(1,5.0, 16.0)
    glColor3f(1.0, 1.0, 1.0)
    glutSolidCube(0.5)
    glPopMatrix()

def draw_chair():
    glPushMatrix()

    # mover a cadeira para a posição desejada
    glTranslatef(0.0, 0.0, 3.0)

    # definir a escala da cadeira
    glScalef(3.0, 2.0, 2.0)

    # definir a cor da cadeira
    glColor3f(0.5, 0.5, 0.5)

    # desenhar o assento da cadeira
    glPushMatrix()
    glTranslatef(0.0, -0.5, 0.0)
    glScalef(0.8, 0.1, 0.8)
    glutSolidCube(1.0)
    glPopMatrix()

    #desenha a junção esquerda entre o assento o encosto
    glPushMatrix()
    glTranslatef(-0.3, 0.0, -0.4)
    glScalef(0.1, 3.0, 0.1)
    glutSolidCube(0.3)
    glPopMatrix()

    #desenha a junção direita entre o assento o encosto
    glPushMatrix()
    glTranslatef(0.3, 0.0, -0.3)
    glScalef(0.1, 3.0, 0.1)
    glutSolidCube(0.3)
    glPopMatrix()

    # desenhar os pés da cadeira
    glPushMatrix()
    glTranslatef(-0.3, -1.0, 0.3)
    glScalef(0.1, 1.0, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.3, -1.0, -0.3)
    glScalef(0.1, 1.0, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.3, -1.0, 0.3)
    glScalef(0.1, 1.0, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.3, -1.0, -0.3)
    glScalef(0.1, 1.0, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()

    # desenhar o encosto da cadeira
    glPushMatrix()
    glTranslatef(0.0, 0.5, -0.4)
    glScalef(0.8, 1.0, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()

    glPopMatrix()

def draw_fan_blades1():
    angle = 0.0
    glColor3f(1.0, 1.0, 1.0)
    glPushMatrix()
    glTranslate(-10.0, 5.3, 0.0)
    glScale(0.2, 2, 0.5)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslate(-10.0, 4.5, 0.0)
    glRotatef(angle+120.0, 0.0, 1.0, 0.0)
    glScale(5.0, 0, 0.5)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslate(-10.0, 4.5, 0.0)
    glRotatef(angle + 240, 0.0, 1.0, 0.0)
    glScale(5.0, 0, 0.5)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslate(-10.0, 4.5, 0.0)
    glRotatef(angle + 180, 0.0, 1.0, 0.0)
    glScale(4.0, 0, 0.5)
    glutSolidCube(1.0)
    glPopMatrix()

def draw_fan_blades2():
    angle = 0.0
    glColor3f(1.0, 1.0, 1.0)
    glPushMatrix()
    glTranslate(10.0, 5.3, 0.0)
    glScale(0.2, 2, 0.5)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslate(10.0, 4.5, 0.0)
    glRotatef(angle+120.0, 0.0, 1.0, 0.0)
    glScale(5.0, 0, 0.5)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslate(10.0, 4.5, 0.0)
    glRotatef(angle + 240, 0.0, 1.0, 0.0)
    glScale(5.0, 0, 0.5)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslate(10.0, 4.5, 0.0)
    glRotatef(angle + 180, 0.0, 1.0, 0.0)
    glScale(4.0, 0, 0.5)
    glutSolidCube(1.0)
    glPopMatrix()

def draws():
    draw_floor() #chamada da função floor
    draw_table1()
    draw_board()
    draw_chair()
    draw_cabinet()
    draw_notebook()
    draw_door()
    draw_viga()
    draw_ceil()
    draw_fan_blades1()
    draw_fan_blades2()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Clear color and depth buffers
    glEnable(GL_DEPTH_TEST)
    
    glMatrixMode(GL_MODELVIEW)
    draws()

    #draw_table_with_legs()
    #draw_front_face()
    #draw_wall() # chamada da função wall1
    glutSwapBuffers()

def reshape(width, height):
    pass

def keyboard_handler(key, x, y):
    global eye
    global center
    global up

    # move the camera
    if key == b"w":
        eye[2] += UNIT_DIST * UNIT_PIXEL * unit_vel
        center[2] += UNIT_DIST * UNIT_PIXEL * unit_vel

        # print(eye, center, up)
    elif key == b"s":
        eye[2] -= UNIT_DIST * UNIT_PIXEL * unit_vel
        center[2] -= UNIT_DIST * UNIT_PIXEL * unit_vel

    # elif key == b"u":
    #     up[0] = 1   
    elif key == b"z":
        eye[2] -= UNIT_DIST * UNIT_PIXEL * unit_vel

    elif key == b"x":
        eye[2] += UNIT_DIST * UNIT_PIXEL * unit_vel
        
    elif key == b"d":
        eye[0] += UNIT_DIST * UNIT_PIXEL * unit_vel
        center[0] += UNIT_DIST * UNIT_PIXEL * unit_vel
            
    elif key == b"a":
        eye[0] -= UNIT_DIST * UNIT_PIXEL * unit_vel
        center[0] -= UNIT_DIST * UNIT_PIXEL * unit_vel

    move_camera()

    glutPostRedisplay()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowPosition(0,0)
glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)  
glutCreateWindow("Laboratory Simulator")

init() 

glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard_handler)

glutMainLoop()