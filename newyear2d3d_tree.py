from OpenGL.GL import *
from OpenGL.GLUT import *
#from OpenGL.GLU import *


def square():
    glBegin(GL_QUADS)
    glVertex2f(30, 140)
    glVertex2f(470, 140)
    glVertex2f(470, 250)
    glVertex2f(30, 250)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(30, 450)
    glVertex2f(470, 450)
    glVertex2f(470, 350)
    glVertex2f(30, 350)
    glEnd()


def tree():

#central
    glRotatef(10, 0, 0, 0)

    glBegin(GL_TRIANGLES)
    glVertex2f(230, 453)
    glVertex2f(159, 307)
    glVertex2f(301, 307)
    glEnd()


    glBegin(GL_TRIANGLES)
    glVertex2f(230, 389)
    glVertex2f(320, 240)
    glVertex2f(140, 240)
    glEnd()


    glBegin(GL_TRIANGLES)
    glVertex2f(230, 333)
    glVertex2f(333, 169)
    glVertex2f(127, 169)
    glEnd()


def wood():
    glBegin(GL_QUADS)
    glVertex3f(202, 174, 0)
    glVertex3f(202, 115, 0)
    glVertex3f(250, 115, 0)
    glVertex3f(250, 174, 0)

    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(202, 174, 90)
    glVertex3f(202, 115, 90)
    glVertex3f(250, 115, 90)
    glVertex3f(250, 174, 90)

    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    glColor3f(1.0, 0.6, 0.4)
    wood()
    glColor3f(0.0, 1.0, 0.0) #rgb blue
    tree()

    glRectf(-0.5, -0.5, 0.5, 0.5)


    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("OpenGL Flag 11")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()