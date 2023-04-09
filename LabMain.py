from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import sin, cos, radians
#import ventilador

WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720

camera_x, camera_y, camera_z = 0, 1, 0
camera_yaw, camera_pitch = 0, 0

camera_speed = 1
camera_yaw_speed = 1
camera_pitch_speed = 1

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

def move_camera(key, x, y):
    global camera_x, camera_y, camera_z
    if key == b'w':
        camera_x -= 0.1 * sin(radians(camera_y))
        camera_z -= 0.1 * cos(radians(camera_y))
    elif key == b's':
        camera_x += 0.1 * sin(radians(camera_y))
        camera_z += 0.1 * cos(radians(camera_y))
    elif key == b'a':
        camera_x -= 0.1 * cos(radians(camera_y))
        camera_z += 0.1 * sin(radians(camera_y))
    elif key == b'd':
        camera_x += 0.1 * cos(radians(camera_y))
        camera_z -= 0.1 * sin(radians(camera_y))
    glutPostRedisplay()

def draw_ceil():
    glPushMatrix()
    glColor4fv(colors["white"])
    glTranslatef(0.0, 5.0, 0.0)
    glScalef(153, 1, 70)
    glutSolidCube(UNIT_PIXEL * 1)
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
    glTranslatef(0, 0, 6.8)
    glScalef(153, 50, 1)
    glutSolidCube(UNIT_PIXEL * 1)
    glPopMatrix()

    # Criação do plano na face traseira
    glPushMatrix()
    glColor4fv(colors["green"])
    glTranslatef(0, 0, -7.2)
    glScalef(153, 50, 1)
    glutSolidCube(UNIT_PIXEL * 1)
    glPopMatrix()

    # Criação do plano na face esquerda
    #parte de baixo na face esquerda
    glPushMatrix()
    glColor4fv(colors["blue"])
    glTranslatef(15.2, -3.2, 0)
    glScalef(1, 15, 70)
    glutSolidCube(UNIT_PIXEL * 1)
    glPopMatrix()

    #parte de cima na face esquerda
    glPushMatrix()
    glColor4fv(colors["blue"])
    glTranslatef(15.2, 3.9, 0)
    glScalef(1, 10, 70)
    glutSolidCube(UNIT_PIXEL * 1)
    glPopMatrix()

    #estrutura que divide as janelas
    glPushMatrix()
    glColor4fv(colors["blue"])
    glTranslatef(15.2, 0.0, 0)
    glScalef(1, 35, 2)
    glutSolidCube(UNIT_PIXEL * 1)
    glPopMatrix()

    #estrutura lateral direita da janela
    glPushMatrix()
    glColor4fv(colors["blue"])
    glTranslatef(15.2, 0.0, 6.5)
    glScalef(1, 35, 2)
    glutSolidCube(UNIT_PIXEL * 1)
    glPopMatrix()

    #estrutura lateral esquerda da janela
    glPushMatrix()
    glColor4fv(colors["blue"])
    glTranslatef(15.2, 0.0, -6.8)
    glScalef(1, 35, 2)
    glutSolidCube(UNIT_PIXEL * 1)
    glPopMatrix()

    # Criação do plano na face direita
    glPushMatrix()
    glColor4fv(colors["yellow"])
    glTranslatef(-15.2, 0, -2)
    glScalef(1, 50, 54)
    glutSolidCube(UNIT_PIXEL * 1)
    glPopMatrix()

def window1():
    glPushMatrix()
    glColor4fv(colors["white"])
    glTranslatef(15.2, 0.6, -3.4)
    glScalef(1, 21.8, 31.8)
    glutSolidCube(UNIT_PIXEL * 1)
    glPopMatrix()

def window2():
    glPushMatrix()
    glColor4fv(colors["white"])
    glTranslatef(15.2, 0.6, 3.2)
    glScalef(1, 21.8, 30)
    glutSolidCube(UNIT_PIXEL * 1)
    glPopMatrix()

def draw_door():
    glPushMatrix()
    glTranslatef(-15.1, -1.0, 5.0)
    glScalef(0.2,7.0, 3.2)
    glColor3f(0.3, 0.3, 0.3)
    glutSolidCube(1.0)
    glPopMatrix()   

def draw_viga():
    glPushMatrix()
    glTranslatef(-15.1, 3.7, 4.2)
    glScalef(0.2, 2.5, 5)
    glColor4fv(colors["yellow"])
    glutSolidCube(1.0)
    glPopMatrix()

def draw_table1():
    glPushMatrix()
    glTranslatef(3.0, -1.8, 5.2)
    glScalef(20.0,0.5, 3.0)
    glColor3f(0.3, 0.3, 0.3)
    glutSolidCube(1.0)
    glPopMatrix()
    #desenha o pé esquerdo da mesa
    glPushMatrix()
    glTranslatef(12, -3.0, 4.0)
    glScalef(0.5, 3.0, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()

    #desenha o pé direito da mesa
    glPushMatrix()
    glTranslatef(-6, -3.0, 4.0)
    glScalef(0.5, 3.0, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()


def draw_cabinet():
    glPushMatrix()
    glTranslatef(4, 3.5, -5.7)
    glScalef(20.0,2.0, 3.0)
    glColor3f(0.3, 0.3, 0.3)
    glutSolidCube(1.0)
    glPopMatrix()



def draw_notebook():
    glPushMatrix()
    glTranslatef(0.0, -1.3, 5)
    glScale(2.0,0.0,1.0)
    glColor3f(0.0, 0.0, 0.0)
    glutSolidCube(1.0)
    glPopMatrix()

def draw_board():
    glPushMatrix()
    glTranslatef(-14.3, 1.0, -2.0)
    glScalef(1,5.0, 16.0)
    glColor3f(1.0, 1.0, 1.0)
    glutSolidCube(0.5)
    glPopMatrix()

def draw_chair():
    glPushMatrix()

    # mover a cadeira para a posição desejada
    glTranslatef(0.0, -1.0, 3.0)

    # definir a escala da cadeira
    glScalef(3.0, 2.0, 2.0)

    # definir a cor da cadeira
    glColor3f(0.5, 0.5, 0.5)

    # desenhar o assento da cadeira
    glPushMatrix()
    glTranslatef(0.0, -0.68, 0.0)
    glScalef(0.8, 0.1, 0.8)
    glutSolidCube(1.0)
    glPopMatrix()

    #desenha a junção esquerda entre o assento o encosto
    glPushMatrix()
    glTranslatef(-0.3, -0.2, -0.3)
    glScalef(0.1, 3.0, 0.1)
    glColor3f(0.7, 0.7, 0.7)
    glutSolidCube(0.3)
    glPopMatrix()

    #desenha a junção direita entre o assento o encosto
    glPushMatrix()
    glTranslatef(0.3, -0.2, -0.3)
    glScalef(0.1, 3.0, 0.1)
    glColor3f(0.7, 0.7, 0.7)
    glutSolidCube(0.3)
    glPopMatrix()

    # desenhar os pés da cadeira
    glPushMatrix()
    glTranslatef(-0.3, -1.0, 0.3)
    glScalef(0.1, 0.7, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.3, -1.0, -0.3)
    glScalef(0.1, 0.7, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.3, -1.0, 0.3)
    glScalef(0.1, 0.7, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.3, -1.0, -0.3)
    glScalef(0.1, 0.7, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()

    # desenhar o encosto da cadeira
    glPushMatrix()
    glTranslatef(0.0, 0.2, -0.3)
    glScalef(0.8, 0.5, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()

    glPopMatrix()

angle = 0.0
fan_speed = 1.0

def draw_fan_blades1():
    global angle
    
    # Desenha a base do ventilador
    glColor3f(1.0, 1.0, 1.0)
    glPushMatrix()
    glTranslate(-10.0, 3.5, 0.0)
    glScale(0.2, 2, 0.5)
    glutSolidCube(1.0)
    glPopMatrix()

    # Desenha as lâminas do ventilador
    glPushMatrix()
    glTranslate(-10.0, 2.5, 0.0)
    glRotatef(angle+120.0, 0.0, 1.0, 0.0)
    glScale(5.0, 0, 0.5)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslate(-10.0, 2.5, 0.0)
    glRotatef(angle + 240, 0.0, 1.0, 0.0)
    glScale(5.0, 0, 0.5)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslate(-10.0, 2.5, 0.0)
    glRotatef(angle + 180, 0.0, 1.0, 0.0)
    glScale(4.0, 0, 0.5)
    glutSolidCube(1.0)
    glPopMatrix()

def draw_fan_blades2():
    global angle

#    angle = 0.0
    glColor3f(1.0, 1.0, 1.0)
    glPushMatrix()
    glTranslate(10.0, 3.5, 0.0)
    glScale(0.2, 2, 0.5)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslate(10.0, 2.5, 0.0)
    glRotatef(angle+120.0, 0.0, 1.0, 0.0)
    glScale(5.0, 0, 0.5)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslate(10.0, 2.5, 0.0)
    glRotatef(angle + 240, 0.0, 1.0, 0.0)
    glScale(5.0, 0, 0.5)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslate(10.0, 2.5, 0.0)
    glRotatef(angle + 180, 0.0, 1.0, 0.0)
    glScale(4.0, 0, 0.5)
    glutSolidCube(1.0)
    glPopMatrix()

def update_fan_blades(value):
    global angle, fan_speed
    
    # Atualiza o ângulo da rotação
    angle += fan_speed
    if angle >= 360:
        angle -= 360
    
    # Solicita uma nova renderização da cena
    glutPostRedisplay()
    
    # Define o tempo para o próximo callback
    glutTimerFunc(10, update_fan_blades, 0)

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
    window1()
    window2()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Clear color and depth buffers
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_DEPTH_TEST)
    glLoadIdentity()
    gluLookAt(camera_x, camera_y, camera_z, 0, 0, 0, 0, 1, 0)
    
    draws()

    #draw_table_with_legs()
    #draw_front_face()
    #draw_wall() # chamada da função wall1
    glutSwapBuffers()

def resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, float(width)/float(height), 0.1, 100.0)

def reshape(width, height):
    pass

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowPosition(0,0)
glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)  
glutCreateWindow("Laboratory Simulator")

#init() 

glutDisplayFunc(display)
glutReshapeFunc(reshape)

glutTimerFunc(10, update_fan_blades, 0)

glutReshapeFunc(resize)
glutKeyboardFunc(move_camera)

glutMainLoop()
