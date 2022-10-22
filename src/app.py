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
    gluOrtho2D(0.0, 700.0, 0.0, 700.0)


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


def render():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor(1.0, 1.0, 0.0, 0.0)

    # translatation one
    display()
    glPushMatrix()
    glTranslate(410, 210, 0)
    glRotatef(45.0, 0.0, 0.0, 1.0)
    glScalef(0.5, 0.5, 0.5)
    display()
    glPopMatrix()

    # translatation two
    display()
    glPushMatrix()
    glTranslate(560, 540, 0)
    glRotatef(190.0, 0.0, 0.0, 1.0)
    glScalef(0.25, 0.25, 0.25)
    display()
    glPopMatrix()

    # translatation three
    display()
    glPushMatrix()
    glTranslate(530, 575, 0)
    glRotatef(260.0, 0.0, 0.0, 1.0)
    glScalef(0.15, 0.15, 0.15)
    display()
    glPopMatrix()

    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 600)
    glutInitWindowPosition(1020, 5)
    glutCreateWindow("OPENGL BRO")
    glutDisplayFunc(render)
    init()
    glutMainLoop()


main()
