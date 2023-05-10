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
    "gray" : [0.77, 0.77, 0.77, 0.]
}

def draw_ceil():
    glPushMatrix()
    glColor4fv(colors["white"])
    glTranslatef(0.0, 5.0, 0.0)
    glScalef(120, 1, 70)
    glutSolidCube(UNIT_PIXEL * 1)
    glPopMatrix()

def draw_floor_and_walls():
    glPushMatrix()
    glColor4fv(colors["white"])
    glTranslatef(0, -5.0, 0)
    glScalef(120, 3, 70)
    glutSolidCube(UNIT_PIXEL * 1)
    glPopMatrix()

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

    # Criação do plano na face esquerda
    #parte de baixo na face esquerda
    glPushMatrix()
    glColor4fv(colors["gray"])
    glTranslatef(12.0, -3.2, 0)
    glScalef(1, 15, 70)
    glutSolidCube(UNIT_PIXEL * 1)
    glPopMatrix()

    #parte de cima na face esquerda
    glPushMatrix()
    glColor4fv(colors["gray"])
    glTranslatef(12.0, 3.9, 0)
    glScalef(1, 10, 70)
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
    glPushMatrix()
    glColor4fv(colors["gray"])
    glTranslatef(-12.0, 0, -1.5)
    glScalef(1, 50, 52)
    glutSolidCube(UNIT_PIXEL * 1)
    glPopMatrix()

window_direction = 1
window_angle = 0.0

def update_window_angle(value):
    global window_angle, window_direction, window_animation
    if window_animation:
        window_angle += window_direction * 3 # Incrementa o ângulo da janela
        if window_angle > 90 or window_angle < 0: # Se a porta chegou no ângulo máximo ou mínimo
            window_angle = max(0, min(window_angle, 90)) # Trava o ângulo da janela dentro dos limites permitidos
            window_animation = False # Finaliza a animação
        glutPostRedisplay() # Redesenha a cena
        glutTimerFunc(50, update_window_angle, 0) # Chama a função novamente após um intervalo de tempo

def toggle_window():
    global door_angle, window_direction, window_animation
    window_animation = True # Começa a animação
    window_direction *= -1 # Inverte a direção da janela (abrir <-> fechar)
    glutTimerFunc(50, update_window_angle, 0) # Inicia a animação da janela
    glutPostRedisplay()

def windows():
    global window_angle
    glPushMatrix()
    glColor4fv(colors["white"])
    glTranslatef(12.0, 0.6, -3.4)
    glRotatef(window_angle, 0, 1, 0)
    glScalef(1, 22, 31.8)
    glutSolidCube(UNIT_PIXEL * 1)
    glPopMatrix()

    glPushMatrix()
    glColor4fv(colors["white"])
    glTranslatef(12.0, 0.6, 3.35)
    glRotatef(window_angle, 0, 1, 0)
    glScalef(1, 22, 31.0)
    glutSolidCube(UNIT_PIXEL * 1)
    glPopMatrix()

door_direction = 1
door_angle = 0.0

def update_door_angle(value):
    global door_angle, door_direction, door_animation
    if door_animation:
        door_angle += door_direction * 5 # Incrementa o ângulo da porta
        if door_angle > 90 or door_angle < 0: # Se a porta chegou no ângulo máximo ou mínimo
            door_angle = max(0, min(door_angle, 90)) # Trava o ângulo da porta dentro dos limites permitidos
            door_animation = False # Finaliza a animação
        glutPostRedisplay() # Redesenha a cena
        glutTimerFunc(50, update_door_angle, 0) # Chama a função novamente após um intervalo de tempo

def toggle_door():
    global door_angle, door_direction, door_animation
    door_animation = True # Começa a animação
    door_direction *= -1 # Inverte a direção da porta (abrir <-> fechar)
    glutTimerFunc(50, update_door_angle, 0) # Inicia a animação da porta
    glutPostRedisplay() # Redesenha a cena

def draw_door():
    global door_angle
    glPushMatrix()
    glTranslatef(-10.6, -1.2, 5.2)
    glRotatef(door_angle, 0.0, 1.0, 0.0) # adiciona a rotação em torno do eixo Y
    glTranslatef(-1.4, 0.0, 0.0) # move a porta para que ela gire em torno do canto esquerdo
    glScalef(0.2, 7.25, 3.0)
    glColor3f(0.6, 0.6, 0.6)
    glutSolidCube(1.0)
    glPopMatrix() 

def draw_viga():
    glPushMatrix()
    glTranslatef(-12.0, 3.7, 4.2)
    glScalef(0.2, 2.5, 5)
    glColor4fv(colors["gray"])
    glutSolidCube(1.0)
    glPopMatrix()

def draw_table1():
    glPushMatrix()
    glTranslatef(3.0, -1.8, 5.2)
    glScalef(15.0,0.5, 3.0)
    glColor3f(0.4, 0.4, 0.4)
    glutSolidCube(1.0)
    glPopMatrix()
    #desenha o pé esquerdo da mesa
    glPushMatrix()
    glTranslatef(9, -3.0, 4.0)
    glScalef(0.5, 3.0, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()

    #desenha o pé direito da mesa
    glPushMatrix()
    glTranslatef(-4, -3.0, 4.0)
    glScalef(0.5, 3.0, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()


def draw_cabinet():
    glPushMatrix()
    glTranslatef(2, 2.8, -5.3)
    glScalef(13,1.5, 3.0)
    glColor3f(0.5, 0.5, 0.5)
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
    glTranslatef(-11.8, 1.0, -2.0)
    glScalef(0.5,8.0, 16.0)
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

#    angle = 0.0
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

def draws():
    draw_floor_and_walls() #chamada da função floor
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
    global camera_x, camera_y, camera_z, window_angle
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


def resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, float(width)/float(height), 0.1, 100.0)

def reshape(width, height):
    pass

def special_callback(key, x, y):
    if key == GLUT_KEY_F1:
        toggle_door()

    if key == GLUT_KEY_F2:
        toggle_window()

        
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowPosition(0,0)
glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)  
glutCreateWindow("Laboratory Simulator")

#init() 

glutDisplayFunc(display)
glutReshapeFunc(reshape)

glutTimerFunc(20, update_fan_blades, 0)

glutReshapeFunc(resize)
glutSpecialFunc(special_callback)
glutKeyboardFunc(keyboard)

glutMainLoop()
