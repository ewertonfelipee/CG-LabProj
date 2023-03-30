from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720

eye = [0, 0, 0]
center = [0, 0, 0]
up = [0, 1, 0] 

UNIT_DIST = 1
UNIT_PIXEL = 0.2
unit_vel = 5

colors ={
    #"green": [0.1, 1., 0.1, 0.],
    "white": [0.9, 0.9, 0.9, 0.],
    "blue": [0.9, 0.9, 0.9, 0.]
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

def draw_floor():  
    glPushMatrix()
    glColor4fv(colors["white"])
    glScalef(205, 5, 100)
    glutSolidCube(UNIT_PIXEL * 1)
    glPopMatrix()

def draw_wall1():  # parede
    glPushMatrix()
    glColor4fv(colors["blue"])
    glScalef(205, 5, 100)
    glutWireCube(UNIT_PIXEL * 1)
    glPopMatrix()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Clear color and depth buffers
    glEnable(GL_DEPTH_TEST)
    
    glMatrixMode(GL_MODELVIEW)

    draw_floor() #chamada da função floor
    draw_wall1() # chamada da função wall1
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