""" 
Nama    : Muhammad Farid Wijayanto
Npm     : 2013020107
"""

import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import sys

translateA = 0
translateB = 0
skala = 1
rotate = 0


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-700.0, 700.0, -700.0, 700.0)


def display():
    glColor(1.0, 1.0, 0.0, 0.0)
    glBegin(GL_POLYGON)

    # (X , Y)
    # left
    glVertex2f(220, 300)
    glVertex2f(120, 300)
    glVertex2f(120, 300)
    glVertex2f(205, 255)

    # bottom-left
    glVertex2f(205, 255)
    glVertex2f(170, 170)
    glVertex2f(170, 170)
    glVertex2f(250, 225)

    # top
    glVertex2f(220, 300)
    glVertex2f(250, 380)
    glVertex2f(250, 380)
    glVertex2f(280, 300)

    # # right
    glVertex2f(280, 300)
    glVertex2f(380, 300)
    glVertex2f(380, 300)
    glVertex2f(295, 255)

    # # bottom-right
    glVertex2f(295, 255)
    glVertex2f(330, 170)
    glVertex2f(330, 170)
    glVertex2f(250, 225)

    glEnd()


def render():
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    glTranslatef(translateA, translateB, 0)
    glScalef(skala, skala, 0)
    glRotate(rotate, 0, 0, 1)
    display()
    glPopMatrix()
    glFlush()


def myKeyboard(key, x, y):
    global rotate
    if (key == b'a'):
        rotate += 2
    elif (key == b'd'):
        rotate -= 2


def mySpecialKeyboard(key, x, y):
    global translateA, translateB, skala
    if (key == GLUT_KEY_RIGHT):
        translateA += 5
        translateB += 0
    elif (key == GLUT_KEY_LEFT):
        translateA -= 5
        translateB += 0
    elif (key == GLUT_KEY_DOWN):
        translateA += 0
        translateB -= 5
    elif (key == GLUT_KEY_UP):
        translateA += 0
        translateB += 5


def mouse(button, state, x, y):
    global skala
    if (button == GLUT_LEFT_BUTTON and state == GLUT_DOWN):
        skala += 0.05
    elif (button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN):
        skala -= 0.05


def timer(value):
    glutPostRedisplay()
    glutTimerFunc(50, timer, 0)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 600)
    glutInitWindowPosition(1020, 5)
    glutCreateWindow("OPENGL BRO")
    init()
    glutDisplayFunc(render)
    glutSpecialFunc(mySpecialKeyboard)
    glutKeyboardFunc(myKeyboard)
    glutMouseFunc(mouse)
    glutTimerFunc(10, timer, 5)
    glutMainLoop()


main()
