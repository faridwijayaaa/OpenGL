import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(0.0, 500.0, 0.0, 500.0)


def drawDiamond():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2i(80, 280)
    glVertex2i(80, 160)
    glVertex2i(150, 160)
    glEnd()

    glColor3f(0.37, 0.62, 0.7)
    glBegin(GL_TRIANGLES)
    glVertex2i(80, 280)
    glVertex2i(80, 160)
    glVertex2i(10, 160)
    glEnd()

    glColor3f(0.37, 0.62, 0.7)
    glBegin(GL_TRIANGLES)
    glVertex2i(150, 160)
    glVertex2i(80, 160)
    glVertex2i(80, 20)
    glEnd()

    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2i(80, 160)
    glVertex2i(10, 160)
    glVertex2i(80, 20)
    glEnd()
    glFlush()


initTrans = 0.0


def animTrans():
    global initTrans
    glPushMatrix()
    glTranslatef(initTrans, initTrans, 0)
    drawDiamond()
    initTrans = initTrans + 1
    glPopMatrix()
    glFlush()


def Timer():
    glutPostRedisplay()
    glutTimerFunc(10, Timer, 5)
    glFlush()


def render():
    glClear(GL_COLOR_BUFFER_BIT)
    animTrans()
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(10, 10)
    glutCreateWindow("OpenGL Iqbal")
    glutDisplayFunc(render)
    init()
    glutMainLoop()


main()
