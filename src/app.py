import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import sys
import math


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(0.0, 500.0, 0.0, 500.0)


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor(0.0, 0.0, 0.0, 0.0)
    glBegin(GL_LINES)
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

    # right
    glVertex2f(280, 300)
    glVertex2f(380, 300)
    glVertex2f(380, 300)
    glVertex2f(295, 255)

    # bottom-right
    glVertex2f(295, 255)
    glVertex2f(330, 170)
    glVertex2f(330, 170)
    glVertex2f(250, 225)

    glEnd()
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 600)
    glutInitWindowPosition(1020, 5)
    glutCreateWindow("OPENGL BRO")
    glutDisplayFunc(display)
    init()
    glutMainLoop()


main()
