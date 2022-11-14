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
    glVertex2f(251, 325)
    glVertex2f(240, 297)
    glVertex2f(261, 297)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(221, 302)
    glVertex2f(254, 302)
    glVertex2f(251.62, 288)
    glEnd()


    glBegin(GL_TRIANGLES)
    glVertex2f(231, 272)
    glVertex2f(256, 291)
    glVertex2f(241, 301)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(283, 302)
    glVertex2f(249, 302)
    glVertex2f(253, 288)
    glEnd()


    glBegin(GL_TRIANGLES)
    glVertex2f(260, 301)
    glVertex2f(246, 292)
    glVertex2f(269, 272)
    glEnd()

### right down
    glBegin(GL_TRIANGLES)
    glVertex2f(338, 289)
    glVertex2f(332, 269)
    glVertex2f(345, 269)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(338, 263)
    glVertex2f(341, 273)
    glVertex2f(320, 273)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(340, 263)
    glVertex2f(337, 273)
    glVertex2f(360, 273)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(326, 253)
    glVertex2f(332, 271)
    glVertex2f(341, 265)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(350, 253)
    glVertex2f(335, 266)
    glVertex2f(344, 272)
    glEnd()

## right up
    glBegin(GL_TRIANGLES)
    glVertex2f(338, 345)
    glVertex2f(332, 325)
    glVertex2f(345, 325)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(338, 319)
    glVertex2f(341, 328)
    glVertex2f(320, 328)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(340, 319)
    glVertex2f(337, 328)
    glVertex2f(360, 328)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(326, 309)
    glVertex2f(332, 327)
    glVertex2f(341, 321)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(350, 309)
    glVertex2f(335, 322)
    glVertex2f(344, 327)
    glEnd()

### left down
    glBegin(GL_TRIANGLES)
    glVertex2f(172, 289)
    glVertex2f(166, 269)
    glVertex2f(179, 269)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(174, 263)
    glVertex2f(171, 273)
    glVertex2f(194, 273)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(172, 263)
    glVertex2f(175, 273)
    glVertex2f(154, 273)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(184, 253)
    glVertex2f(178, 271)
    glVertex2f(169, 265)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(160, 253)
    glVertex2f(175, 266)
    glVertex2f(166, 272)
    glEnd()

## right up
    glBegin(GL_TRIANGLES)
    glVertex2f(172, 345)
    glVertex2f(166, 325)
    glVertex2f(179, 325)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(174, 319)
    glVertex2f(171, 328)
    glVertex2f(194, 328)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(172, 319)
    glVertex2f(175, 328)
    glVertex2f(154, 328)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(184, 309)
    glVertex2f(178, 327)
    glVertex2f(169, 321)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(160, 309)
    glVertex2f(175, 322)
    glVertex2f(166, 327)
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
    glColor3f(0.037, 0.70, 1.0) #rgb blue
    square()
    glColor3f(1.0, 1.0, 1.0)
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