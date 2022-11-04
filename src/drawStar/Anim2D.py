""" 
Nama    : Muhammad Farid Wijayanto
Npm     : 2013020107
"""

import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import sys
import math


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
    # glFlush()


# ! Rotated
initRootAngle = 0.0


def animRotate():
    global initRootAngle
    glPushMatrix()
    glRotate(initRootAngle, 0, 0, 1)
    display()
    initRootAngle += 1
    glPopMatrix()
    glFlush()


# ! Translasi
initTrans = 0.0


def animTrans():
    global initTrans
    glPushMatrix()
    glTranslatef(initTrans, initTrans, 0)
    display()
    initTrans += 1
    glPopMatrix()
    glFlush()


# ! Skala
initSkala = 0.0


def animSkala():
    global initSkala
    glPushMatrix()
    glScalef(initSkala, initSkala, 0)
    display()
    initSkala += 1
    glPopMatrix()
    glFlush()


def timer():
    glutPostRedisplay()
    glutTimerFunc(10, timer, 5)
    glFlush()


def render():
    glClear(GL_COLOR_BUFFER_BIT)
    # animRotate() # for Rotated
    animSkala()  # for Skalation
    # animTrans() # for Translation
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 600)
    glutInitWindowPosition(1020, 5)
    glutCreateWindow("OPENGL BRO")
    glutDisplayFunc(render)
    glutTimerFunc(10, timer, 5)
    init()
    glutMainLoop()


main()
