from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import sin, cos, radians
import time
import pygame

WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720

camera_x, camera_y, camera_z = 0, 1, 0
camera_yaw, camera_pitch = 0, 0

camera_speed = 5
camera_yaw_speed = 1
camera_pitch_speed = 1

UNIT_DIST = 1
UNIT_PIXEL = 0.2
unit_vel = 5

colors = {
    "white": [0.9, 0.9, 0.9, 0.0],
    "gray" : [0.77, 0.77, 0.77, 0.0]
}

#textures
textures = {
    "notebook" : None,
    "notebook2" : None,
    "notebook3" : None,
    "floor" : None,
    "ceil" : None,
    "board" : None,
    "table" : None,
    "viga" : None,
    "wall_board" : None
}

def draw_ceil(ceil):

    glEnable(GL_TEXTURE_2D)

    glBindTexture(GL_TEXTURE_2D, ceil)

    glPushMatrix()
    glTranslatef(0.0, 5.0, 0.0)
    glScalef(15.3, 3, 9)
    glColor4fv(colors["white"])

    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-0.8, 0.0, -0.8)
    glTexCoord2f(5.0, 0.0)
    glVertex3f(0.8, 0.0, -0.8)
    glTexCoord2f(5.0, 5.0)
    glVertex3f(0.8, 0.0, 0.8)
    glTexCoord2f(0.0, 5.0)
    glVertex3f(-0.8, 0.0, 0.8)

    glEnd()
    glPopMatrix()
    glDisable(GL_TEXTURE_2D)

def draw_floor(floor):

    glEnable(GL_TEXTURE_2D)

    glBindTexture(GL_TEXTURE_2D, floor)

    glPushMatrix()
    glTranslatef(0, -5.0, 0)
    glScalef(15.3, 3, 9)
    glColor4fv(colors["white"])

    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-0.8, 0.0, -0.8)
    glTexCoord2f(7.0, 0.0)
    glVertex3f(0.8, 0.0, -0.8)
    glTexCoord2f(7.0, 7.0)
    glVertex3f(0.8, 0.0, 0.8)
    glTexCoord2f(0.0, 7.0)
    glVertex3f(-0.8, 0.0, 0.8)

    glEnd()
    glPopMatrix()
    glDisable(GL_TEXTURE_2D)

def draw_walls1(wall_texture):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, wall_texture)

    # Criação do plano na face frontal
    glPushMatrix()
    glColor4fv(colors["gray"])
    glTranslatef(0, 0, 6.8)
    glScalef(120, 50, 1)
    glutSolidCube(UNIT_PIXEL * 1)
    glPopMatrix()

    # Criação do plano na face traseira
    glPushMatrix()
    glColor4fv(colors["gray"])
    glTranslatef(0, 0, -6.8)
    glScalef(120, 50, 1)
    glutSolidCube(UNIT_PIXEL * 1)
    glPopMatrix()

    glPushMatrix()
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-12, -5, 6.699)
    glTexCoord2f(5.0, 0.0)
    glVertex3f(12, -5, 6.699)
    glTexCoord2f(5.0, 5.0)
    glVertex3f(12, 5, 6.699)
    glTexCoord2f(0.0, 5.0)
    glVertex3f(-12, 5, 6.699)
    glEnd()
    glPopMatrix()
    
    glPushMatrix()
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-12, -5, -6.699)
    glTexCoord2f(5.0, 0.0)
    glVertex3f(12, -5, -6.699)
    glTexCoord2f(5.0, 5.0)
    glVertex3f(12, 5, -6.699)
    glTexCoord2f(0.0, 5.0)
    glVertex3f(-12, 5, -6.699)
    glEnd()
    glPopMatrix()

    glDisable(GL_TEXTURE_2D)

def draw_walls2(wall_board):
    # Criação do plano na face esquerda
    #parte de baixo na face esquerda
    glPushMatrix()
    glColor4fv(colors["gray"])
    glTranslatef(12.0, -3.2, 0)
    glScalef(1, 17, 70)
    glutSolidCube(UNIT_PIXEL * 1)
    glPopMatrix()

    #parte de cima na face esquerda
    glPushMatrix()
    glColor4fv(colors["gray"])
    glTranslatef(12.0, 3.9, 0)
    glScalef(1, 11, 70)
    glutSolidCube(UNIT_PIXEL * 1)
    glPopMatrix()

    #estrutura que divide as janelas
    glPushMatrix()
    glColor4fv(colors["gray"])
    glTranslatef(12.0, 0.0, 0)
    glScalef(1, 35, 2)
    glutSolidCube(UNIT_PIXEL * 1)
    glPopMatrix()

    #estrutura lateral direita da janela
    glPushMatrix()
    glColor4fv(colors["gray"])
    glTranslatef(12.0, 0.0, 6.8)
    glScalef(1, 35, 2)
    glutSolidCube(UNIT_PIXEL * 1)
    glPopMatrix()

    #estrutura lateral esquerda da janela
    glPushMatrix()
    glColor4fv(colors["gray"])
    glTranslatef(12.0, 0.0, -6.8)
    glScalef(1, 35, 2)
    glutSolidCube(UNIT_PIXEL * 1)
    glPopMatrix()

    # Criação do plano na face direita
    glEnable(GL_TEXTURE_2D)

    glBindTexture(GL_TEXTURE_2D, wall_board)
    glPushMatrix()
    glColor4fv(colors["gray"])
    glTranslatef(-12.0, 0, -1.5)
    glScalef(1, 6.3, 6.5)
    glColor4fv(colors["white"])
    glRotatef(90, 1, 0, 0)

    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(0.0, 0.8, 0.8)
    glTexCoord2f(4.0, 0.0)
    glVertex3f(0.0, -0.8, 0.8)
    glTexCoord2f(4.0, 4.0)
    glVertex3f(0.0, -0.8, -0.8)
    glTexCoord2f(0.0, 4.0)
    glVertex3f(0.0, 0.8, -0.8)

    glEnd()

    glPopMatrix()

    glDisable(GL_TEXTURE_2D)

window_direction = 1
window_angle = 0.0

angles = [0, 0, 0, 0, 0]
opening = False
animation_start = None
animation_duration = 2.0

def windows():
    global angles

    glPushMatrix()
    glColor4fv(colors["white"])
    glTranslatef(14.5, 0.65, -3.4)

    for i in range(5):
        glPushMatrix()
        glTranslatef(-2.49, 0.0, (i - 2) * 1.25)
        glRotatef(angles[i], 0, 1, 0)
        glScalef(0.5, 21.5, 7.5)
        glutSolidCube(UNIT_PIXEL * 1)
        glPopMatrix()

    glPopMatrix()

    glPushMatrix()
    glColor4fv(colors["white"])
    glTranslatef(14.5, 0.65, 3.35)

    for i in range(5):
        glPushMatrix()
        glTranslatef(-2.49, 0.0, (i - 2) * 1.25)
        glRotatef(angles[i], 0, 1, 0)
        glScalef(0.5, 21.5, 7.5)
        glutSolidCube(UNIT_PIXEL * 1)
        glPopMatrix()

    glPopMatrix()

def animate():
    global angles, opening, animation_start

    current_time = time.time()

    if opening:
        elapsed_time = current_time - animation_start
        progress = elapsed_time / animation_duration

        if progress >= 1.0:
            progress = 1.0
            opening = False
            angles = [90, 90, 90, 90, 90] 
            animation_start = None  
            glutPostRedisplay()

        angle_step = 90 * progress
        angles = [angle_step, angle_step, angle_step, angle_step, angle_step]
        glutPostRedisplay()

    elif animation_start is not None:
        elapsed_time = current_time - animation_start
        progress = elapsed_time / animation_duration

        if progress >= 1.0:
            progress = 1.0
            angles = [0, 0, 0, 0, 0]
            animation_start = None
        else:
            angle_step = 90 * (1 - progress)
            angles = [angle_step, angle_step, angle_step, angle_step, angle_step]

        glutPostRedisplay()

door_angle = 0
door_open = False
door_speed = 40
start_time = None

def draw_door():
    global door_angle
    glPushMatrix()
    glTranslatef(-10.6, -1.2, 5.2)
    glTranslatef(-1.33, 3.625, 1.5)
    glRotatef(door_angle, 0.0, 1.0, 0.0)
    glTranslatef(0.0, -3.625, -1.5)
    glScalef(0.2, 7.5, 3.0)
    glColor3f(0.6, 0.6, 0.6)
    glutSolidCube(1.0)
    glPopMatrix()

def animate_door(open):
    global door_angle, door_speed, start_time
    if open:
        if door_angle > -90:
            if start_time is None:
                start_time = time.time()
            elapsed_time = time.time() - start_time
            door_angle -= door_speed * elapsed_time
            start_time = time.time()
            glutPostRedisplay()
            glutTimerFunc(10, animate_door, 1)
        else:
            start_time = None
    else:
        if door_angle < 0:
            if start_time is None:
                start_time = time.time()
            elapsed_time = time.time() - start_time
            door_angle += door_speed * elapsed_time
            start_time = time.time()
            glutPostRedisplay()
            glutTimerFunc(10, animate_door, 0)
        else:
            start_time = None

def draw_viga(viga):
    glEnable(GL_TEXTURE_2D)

    glBindTexture(GL_TEXTURE_2D, viga)

    glPushMatrix()
    glTranslatef(-12.0, 3.7, 5.3)
    glScalef(0.2, 1.7, 2.0)
    glColor4fv(colors["white"])
    glRotatef(90, 1, 0, 0)

    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(0.0, 0.8, 0.8)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(0.0, -0.8, 0.8)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(0.0, -0.8, -0.8)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(0.0, 0.8, -0.8)

    glEnd()

    glPopMatrix()

    glDisable(GL_TEXTURE_2D)

def draw_table1(table):

    glEnable(GL_TEXTURE_2D)

    glBindTexture(GL_TEXTURE_2D, table)

    glPushMatrix()
    glTranslatef(3.0, -1.8, 5.2)
    glScalef(9.0,0.5, 2.0)
    glColor3f(0.9, 0.9, 0.9)

    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-0.8, 0.0, -0.8)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(0.8, 0.0, -0.8)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(0.8, 0.0, 0.8)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-0.8, 0.0, 0.8)

    glEnd()

    glPopMatrix()

    glDisable(GL_TEXTURE_2D)
    
    #desenha o pé esquerdo da mesa
    glPushMatrix()
    glTranslatef(9, -3.5, 4.0)
    glScalef(0.5, 3.3, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()

    #desenha o pé direito da mesa
    glPushMatrix()
    glTranslatef(-4, -3.5, 4.0)
    glScalef(0.5, 3.3, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()


def draw_cabinet():
    glPushMatrix()
    glTranslatef(2, 2.8, -5.3)
    glScalef(13,1.5, 3.0)
    glColor3f(0.5, 0.5, 0.5)
    glutSolidCube(1.0)
    glPopMatrix()

def draw_lamp():
    # base da luminária
    glPushMatrix()
    glTranslatef(2, -1.6, 5)
    glScalef(0.8, 0.2, 0.8)
    glColor3f(0.5, 0.5, 0.5)
    glutSolidCube(1.0)
    glPopMatrix()

    # haste da luminária
    glPushMatrix()
    glTranslatef(2, -1, 5)
    glScalef(0.1, 1.5, 0.1)
    glColor3f(0.5, 0.5, 0.5)
    glutSolidCube(1.0)
    glPopMatrix()

    # cabeça da luminária
    glPushMatrix()
    glTranslatef(2, 0.0, 5)
    glScalef(0.8, 0.5, 0.8)
    glColor3f(1.0, 1.0, 1.0)  # amarelo
    glutSolidCube(1.0)
    glPopMatrix()

def draw_lamp2():
    # base da luminária
    glPushMatrix()
    glTranslatef(5.5, -1.6, 5)
    glScalef(0.8, 0.2, 0.8)
    glColor3f(0.5, 0.5, 0.5)
    glutSolidCube(1.0)
    glPopMatrix()

    # haste da luminária
    glPushMatrix()
    glTranslatef(5.5, -1, 5)
    glScalef(0.1, 1.5, 0.1)
    glColor3f(0.5, 0.5, 0.5)
    glutSolidCube(1.0)
    glPopMatrix()

    # cabeça da luminária
    glPushMatrix()
    glTranslatef(5.5, 0.0, 5)
    glScalef(0.8, 0.5, 0.8)
    glColor3f(1.0, 1.0, 1.0)  # amarelo
    glutSolidCube(1.0)
    glPopMatrix()

def draw_lamp3():
    # base da luminária
    glPushMatrix()
    glTranslatef(-3, -1.6, 5)
    glScalef(0.8, 0.2, 0.8)
    glColor3f(0.5, 0.5, 0.5)
    glutSolidCube(1.0)
    glPopMatrix()

    # haste da luminária
    glPushMatrix()
    glTranslatef(-3, -1, 5)
    glScalef(0.1, 1.5, 0.1)
    glColor3f(0.5, 0.5, 0.5)
    glutSolidCube(1.0)
    glPopMatrix()

    # cabeça da luminária
    glPushMatrix()
    glTranslatef(-3, 0.0, 5)
    glScalef(0.8, 0.5, 0.8)
    glColor3f(1.0, 1.0, 1.0)  # amarelo
    glutSolidCube(1.0)
    glPopMatrix()

def draw_notebook(texture_notebook):
    glEnable(GL_TEXTURE_2D)

    glBindTexture(GL_TEXTURE_2D, texture_notebook)

    glPushMatrix()
    glTranslatef(-1.0, -1.6, 5)
    glScale(1.0,0.0,1.0)
    glColor3f(0.5, 0.5, 0.5)

    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-0.8, 0.0, -0.8)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(0.8, 0.0, -0.8)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(0.8, 0.0, 0.8)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-0.8, 0.0, 0.8)

    glEnd()

    glPopMatrix()

    glDisable(GL_TEXTURE_2D)

def draw_notebook2(texture_notebook2):

    glEnable(GL_TEXTURE_2D)

    glBindTexture(GL_TEXTURE_2D, texture_notebook2)

    glPushMatrix()
    glTranslatef(3.5, -1.6, 5)
    glScale(1.0,0.0,1.0)
    glColor3f(0.5, 0.5, 0.5)

    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-0.8, 0.0, -0.8)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(0.8, 0.0, -0.8)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(0.8, 0.0, 0.8)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-0.8, 0.0, 0.8)

    glEnd()

    glPopMatrix()

    glDisable(GL_TEXTURE_2D)

def draw_notebook3(texture_notebook3):

    glEnable(GL_TEXTURE_2D)

    glBindTexture(GL_TEXTURE_2D, texture_notebook3)

    glPushMatrix()
    glTranslatef(8, -1.6, 5)
    glScale(1.0,0.0,1.0)
    glColor3f(0.5, 0.5, 0.5)

    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-0.8, 0.0, -0.8)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(0.8, 0.0, -0.8)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(0.8, 0.0, 0.8)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-0.8, 0.0, 0.8)

    glEnd()

    glPopMatrix()

    glDisable(GL_TEXTURE_2D)

def draw_board(board):

    glEnable(GL_TEXTURE_2D)

    glBindTexture(GL_TEXTURE_2D, board)

    glPushMatrix()
    glTranslatef(-11.8, 0.4, -2.0)
    glScalef(4.0, 2.0, 5.0)
    glColor4fv(colors["white"])
    glRotatef(90, 1, 0, 0)

    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(0.0, 0.8, 0.8)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(0.0, -0.8, 0.8)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(0.0, -0.8, -0.8)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(0.0, 0.8, -0.8)

    glEnd()

    glPopMatrix()

    glDisable(GL_TEXTURE_2D)


def draw_chair():
    glPushMatrix()

    # mover a cadeira para a posição desejada
    glTranslatef(-1.0, -1.5, 3.0)

    # definir a escala da cadeira
    glScalef(3.0, 2.0, 2.0)

    # definir a cor da cadeira
    glColor3f(0.0, 0.0, 0.0)

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
    glColor3f(0.0, 0.0, 0.0)
    glutSolidCube(0.3)
    glPopMatrix()

    #desenha a junção direita entre o assento o encosto
    glPushMatrix()
    glTranslatef(0.3, -0.2, -0.3)
    glScalef(0.1, 3.0, 0.1)
    glColor3f(0.0, 0.0, 0.0)
    glutSolidCube(0.3)
    glPopMatrix()

    # desenhar os pés da cadeira
    glPushMatrix()
    glTranslatef(-0.3, -1.2, 0.3)
    glScalef(0.1,1, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.3, -1.2, -0.3)
    glScalef(0.1, 1, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.3, -1.2, 0.3)
    glScalef(0.1, 1, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.3, -1.2, -0.3)
    glScalef(0.1, 1, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()

    # desenhar o encosto da cadeira
    glPushMatrix()
    glTranslatef(0.0, 0.2, -0.3)
    glScalef(0.8, 0.5, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()

    glPopMatrix()

def draw_chair2():
    glPushMatrix()

    # mover a cadeira para a posição desejada
    glTranslatef(3.5, -1.5, 3.0)

    # definir a escala da cadeira
    glScalef(3.0, 2.0, 2.0)

    # definir a cor da cadeira
    glColor3f(0.0, 0.0, 0.0)

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
    glColor3f(0.0, 0.0, 0.0)
    glutSolidCube(0.3)
    glPopMatrix()

    #desenha a junção direita entre o assento o encosto
    glPushMatrix()
    glTranslatef(0.3, -0.2, -0.3)
    glScalef(0.1, 3.0, 0.1)
    glColor3f(0.0, 0.0, 0.0)
    glutSolidCube(0.3)
    glPopMatrix()

    # desenhar os pés da cadeira
    glPushMatrix()
    glTranslatef(-0.3, -1.2, 0.3)
    glScalef(0.1,1, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.3, -1.2, -0.3)
    glScalef(0.1, 1, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.3, -1.2, 0.3)
    glScalef(0.1, 1, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.3, -1.2, -0.3)
    glScalef(0.1, 1, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()

    # desenhar o encosto da cadeira
    glPushMatrix()
    glTranslatef(0.0, 0.2, -0.3)
    glScalef(0.8, 0.5, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()

    glPopMatrix()

def draw_chair3():
    glPushMatrix()

    # mover a cadeira para a posição desejada
    glTranslatef(7.0, -1.5, 3.0)

    # definir a escala da cadeira
    glScalef(3.0, 2.0, 2.0)

    # definir a cor da cadeira
    glColor3f(0.0, 0.0, 0.0)

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
    glColor3f(0.0, 0.0, 0.0)
    glutSolidCube(0.3)
    glPopMatrix()

    #desenha a junção direita entre o assento o encosto
    glPushMatrix()
    glTranslatef(0.3, -0.2, -0.3)
    glScalef(0.1, 3.0, 0.1)
    glColor3f(0.0, 0.0, 0.0)
    glutSolidCube(0.3)
    glPopMatrix()

    # desenhar os pés da cadeira
    glPushMatrix()
    glTranslatef(-0.3, -1.2, 0.3)
    glScalef(0.1,1, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.3, -1.2, -0.3)
    glScalef(0.1, 1, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.3, -1.2, 0.3)
    glScalef(0.1, 1, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.3, -1.2, -0.3)
    glScalef(0.1, 1, 0.1)
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
fan_speed = 1.0 # Para mudar o sentido da rotação define para -1.0

def draw_fan_blades1():
    global angle
    
    # Desenha a base do ventilador
    glColor3f(1.0, 1.0, 1.0)
    glPushMatrix()
    glTranslate(-8.0, 3.5, 0.0)
    glScale(0.2, 2, 0.5)
    glColor3f(0.5, 0.5, 0.5)
    glutSolidCube(1.0)
    glPopMatrix()

    # Desenha as lâminas do ventilador
    glPushMatrix()
    glTranslate(-8.0, 2.5, 0.0)
    glRotatef(angle+120.0, 0.0, 1.0, 0.0)
    glScale(5.0, 0, 0.5)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslate(-8.0, 2.5, 0.0)
    glRotatef(angle + 240, 0.0, 1.0, 0.0)
    glScale(5.0, 0, 0.5)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslate(-8.0, 2.5, 0.0)
    glRotatef(angle + 180, 0.0, 1.0, 0.0)
    glScale(4.0, 0, 0.5)
    glutSolidCube(1.0)
    glPopMatrix()

def draw_fan_blades2():
    global angle
    #angle = 0.0
    glColor3f(1.0, 1.0, 1.0)
    glPushMatrix()
    glTranslate(8.0, 3.5, 0.0)
    glScale(0.2, 2, 0.5)
    glColor3f(0.5, 0.5, 0.5)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslate(8.0, 2.5, 0.0)
    glRotatef(angle+120.0, 0.0, 1.0, 0.0)
    glScale(5.0, 0, 0.5)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslate(8.0, 2.5, 0.0)
    glRotatef(angle + 240, 0.0, 1.0, 0.0)
    glScale(5.0, 0, 0.5)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslate(8.0, 2.5, 0.0)
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
    glutTimerFunc(20, update_fan_blades, 0)

def draw_sphere():
    glPushMatrix()
    glColor4fv(colors["white"])
    glTranslatef(0, 15, 0)  # Coordenadas da esfera no topo do laboratório
    glutSolidSphere(3.0, 32, 32)  # Ajuste o tamanho da esfera conforme necessário
    glPopMatrix()


def draws():
    draw_walls1(textures["ceil"]) #chamada da função floor
    draw_walls2(textures["wall_board"])
    draw_floor(textures["floor"])
    draw_table1(textures["table"])
    draw_board(textures["board"])
    draw_sphere()
    draw_chair()
    draw_chair2()
    draw_chair3()
    draw_cabinet()
    draw_lamp()
    draw_lamp2()
    draw_lamp3()
    draw_notebook(textures["notebook"])
    draw_notebook2(textures["notebook2"])
    draw_notebook3(textures["notebook3"])
    draw_door()
    draw_viga(textures["viga"])
    draw_ceil(textures["ceil"])
    draw_fan_blades1()
    draw_fan_blades2()
    windows()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Clear color and depth buffers
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_DEPTH_TEST)
    glLoadIdentity()
    gluLookAt(camera_x, camera_y, camera_z, 0, 0, 0, 0, 1, 0)
    
    draws()

    glutSwapBuffers()

def keyboard(key, x, y):
    global camera_x, camera_y, camera_z, window_angle, light_ambient, light_specular, light_diffuse
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
    elif key == b'q':
        #camera_z -= 0.5 * sin(radians(camera_x))
        camera_y += -0.1 * cos(radians(camera_x))
    elif key == b'z':
        #camera_z -= 0.5 * sin(radians(camera_x))
        camera_y -= -0.1 * cos(radians(camera_x))

    #controle da iluminação
    if key == b'r':
        glEnable(GL_LIGHT0)
    elif key == b't':
        glDisable(GL_LIGHT0)
    elif key == b'f':
        glEnable(GL_LIGHT1)
    elif key == b'g':
        glDisable(GL_LIGHT1)
    
    glutPostRedisplay()

def resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, float(width)/float(height), 0.1, 100.0)

def reshape(width, height):
    pass

def special_callback(key, x, y):
    global door_open, opening, animation_start, angles
    if key == GLUT_KEY_F1:
        door_open = not door_open
        animate_door(door_open)
    if key == GLUT_KEY_F2 and all(angle == 0 for angle in angles):
        if animation_start is None:
            animation_start = time.time()
            opening = True
            glutIdleFunc(animate)
    elif key == GLUT_KEY_F3 and all(angle == 90 for angle in angles):
        if animation_start is None:
            animation_start = time.time()
            opening = False
            glutIdleFunc(animate)

def load_texture(image):
    textureSurface = pygame.image.load(image)
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    texid = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texid)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_MIRRORED_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_MIRRORED_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)

    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glGenerateMipmap(GL_TEXTURE_2D)

    return texid


def setup_lighting():
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_NORMALIZE)

    glMaterialfv(GL_FRONT, GL_SPECULAR, [0.1, 0.1, 0.1, 1])

    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.8, 0.8, 0.8, 1])
    # glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.2, 0.2, 0.2, 1])

    glLightfv(GL_LIGHT0, GL_SPECULAR, [0.7, 0.7, 0.7, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.3, 0.3, 0.3, 1])
    glLightfv(GL_LIGHT0, GL_POSITION, [0, 0, 0, 1])

    # spot light
    glLightfv(GL_LIGHT1, GL_DIFFUSE, [1, 1, 1, 1])
    glLightfv(GL_LIGHT1, GL_SPECULAR, [1, 1, 1, 1])

    glLightfv(GL_LIGHT1, GL_SPOT_DIRECTION, [0, -1, 0])
    glLightfv(GL_LIGHT1, GL_POSITION, [0, 6, -1])

    glLightf(GL_LIGHT1, GL_SPOT_CUTOFF, 20)
    glLightf(GL_LIGHT1, GL_SPOT_EXPONENT, 2.0)


def func_textures():
    #textures
    textures["notebook"] = load_texture("textures\\notebook1.png")
    textures["notebook2"] = load_texture("textures\\notebook1.png")
    textures["notebook3"] = load_texture("textures\\notebook1.png")
    textures["floor"] = load_texture("textures\\granite.webp")
    textures["ceil"] = load_texture("textures\\parede1.jpg")
    textures["board"] = load_texture("textures\\board.png")
    textures["table"] = load_texture("textures\\mesa.jpg")
    textures["viga"] = load_texture("textures\\parede1.jpg")
    textures["wall_board"] = load_texture("textures\\parede1.jpg")

def main():

    global textures

    glutInit()
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowPosition(0,0)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)  
    glutCreateWindow("Laboratory Simulator")

    #iluminação
    setup_lighting()

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    glutTimerFunc(20, update_fan_blades, 0)

    glutReshapeFunc(resize)
    glutSpecialFunc(special_callback)
    glutKeyboardFunc(keyboard)

    #textures
    func_textures()

    glutMainLoop()

main()
