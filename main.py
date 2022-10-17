#
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h= 500,500
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

def white_square():
    glBegin(GL_QUADS)
    glVertex2f(30, 350)
    glVertex2f(470, 350)
    glVertex2f(470, 240)
    glVertex2f(30, 240)
    glEnd()

def stars():

#central
    glBegin(GL_TRIANGLES)
    glVertex3f(251, 325, 0)
    glVertex3f(240, 297, 0)
    glVertex3f(261, 297, 0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex3f(221, 302, 0)
    glVertex3f(254, 302, 0)
    glVertex3f(251.62, 288, 0)
    glEnd()


    glBegin(GL_TRIANGLES)
    glVertex3f(231, 272, 0)
    glVertex3f(256, 291, 0)
    glVertex3f(241, 301, 0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex3f(283, 302, 0)
    glVertex3f(249, 302, 0)
    glVertex3f(253, 288, 0)
    glEnd()


    glBegin(GL_TRIANGLES)
    glVertex3f(260, 301, 0)
    glVertex3f(246, 292, 0)
    glVertex3f(269, 272, 0)
    glEnd()

### right down
    glBegin(GL_TRIANGLES)
    glVertex3f(338, 289, 0)
    glVertex3f(332, 269, 0)
    glVertex3f(345, 269, 0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex3f(338, 263, 0)
    glVertex3f(341, 273, 0)
    glVertex3f(320, 273, 0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex3f(340, 263, 0)
    glVertex3f(337, 273, 0)
    glVertex3f(360, 273, 0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex3f(326, 253, 0)
    glVertex3f(332, 271, 0)
    glVertex3f(341, 265, 0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex3f(350, 253, 0)
    glVertex3f(335, 266, 0)
    glVertex3f(344, 272, 0)
    glEnd()

## right up
    glBegin(GL_TRIANGLES)
    glVertex3f(338, 345, 0)
    glVertex3f(332, 325, 0)
    glVertex3f(345, 325, 0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex3f(338, 319, 0)
    glVertex3f(341, 328, 0)
    glVertex3f(320, 328, 0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex3f(340, 319, 0)
    glVertex3f(337, 328, 0)
    glVertex3f(360, 328, 0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex3f(326, 309, 0)
    glVertex3f(332, 327, 0)
    glVertex3f(341, 321, 0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex3f(350, 309, 0)
    glVertex3f(335, 322, 0)
    glVertex3f(344, 327, 0)
    glEnd()

### left down
    glBegin(GL_TRIANGLES)
    glVertex3f(172, 289, 0)
    glVertex3f(166, 269, 0)
    glVertex3f(179, 269, 0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex3f(174, 263, 0)
    glVertex3f(171, 273, 0)
    glVertex3f(194, 273, 0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex3f(172, 263, 0)
    glVertex3f(175, 273, 0)
    glVertex3f(154, 273, 0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex3f(184, 253, 0)
    glVertex3f(178, 271, 0)
    glVertex3f(169, 265, 0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex3f(160, 253, 0)
    glVertex3f(175, 266, 0)
    glVertex3f(166, 272, 0)
    glEnd()

## right up
    glBegin(GL_TRIANGLES)
    glVertex3f(172, 345, 0)
    glVertex3f(166, 325, 0)
    glVertex3f(179, 325, 0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex3f(174, 319, 0)
    glVertex3f(171, 328, 0)
    glVertex3f(194, 328, 0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex3f(172, 319, 0)
    glVertex3f(175, 328, 0)
    glVertex3f(154, 328, 0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex3f(184, 309, 0)
    glVertex3f(178, 327, 0)
    glVertex3f(169, 321, 0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex3f(160, 309, 0)
    glVertex3f(175, 322, 0)
    glVertex3f(166, 327, 0)
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(0.037, 0.70, 1.0) #rgb blue
    square()
    glColor3f(1.0,1.0,1.0)
    white_square()
    glColor3f(0.037, 0.70, 1.0) #rgb blue
    stars()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("OpenGL Flag 11")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()