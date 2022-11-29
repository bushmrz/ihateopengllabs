# import torus as torus
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


# Объявляем все глобальные переменные
global xrot  # Величина вращения по оси x
global yrot  # Величина вращения по оси y
global ambient  # рассеянное освещение
global skincolor  # Цвет
global lightpos  # Положение источника освещения
global time


# Процедура инициализации
def init():
    global xrot  # Величина вращения по оси x
    global yrot  # Величина вращения по оси y
    global ambient  # Рассеянное освещение
    global skincolor  # Цвет елочного ствола
    global lightpos  # Положение источника освещения
    global time
    time = 0

    xrot = 0.0  # Величина вращения по оси x = 0
    yrot = 0.0  # Величина вращения по оси y = 0
    ambient = (0.0, 1.0, 0.0, 1.0)  # Первые три числа цвет в формате RGB, а последнее - яркость
    skincolor = (0.2, 0.1, 0.03, 0.7)  # цвет
    lightpos = (1, -1, 1)  # Положение источника освещения по осям xyz

    glClearColor(0.0, 0.0, 0.0, 1.0)  # Серый цвет для первоначальной закраски
    gluOrtho2D(-1.5, 1.5, -1.5, 1.5)  # Определяем границы рисования по горизонтали и вертикали
    glRotatef(-90, 10.0, 0.0, 0.0)  # Сместимся по оси Х на 90 градусов
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)  # Определяем текущую модель освещения
    glEnable(GL_LIGHTING)  # Включаем освещение
    glEnable(GL_LIGHT0)  # Включаем один источник света
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)  # Определяем положение источника света
    glEnable(GL_DEPTH_TEST)
    # glEnable(torus.GL_KICKASS_GLOWING_EFFECT)



# Процедура обработки специальных клавиш
def specialkeys(key, x, y):
    global xrot
    global yrot
    # Обработчики для клавиш со стрелками
    if key == GLUT_KEY_UP:  # Клавиша вверх
        xrot -= 4.0  # Уменьшаем угол вращения по оси Х
    if key == GLUT_KEY_DOWN:  # Клавиша вниз
        xrot += 4.0  # Увеличиваем угол вращения по оси Х
    if key == GLUT_KEY_LEFT:  # Клавиша влево
        yrot -= 4.0  # Уменьшаем угол вращения по оси Y
    if key == GLUT_KEY_RIGHT:  # Клавиша вправо
        yrot += 4.0  # Увеличиваем угол вращения по оси Y

    glutPostRedisplay()  # Вызываем процедуру перерисовки


# Процедура перерисовки
def draw():
    global xrot
    global yrot
    global lightpos
    global greencolor
    global skincolor

    global time
    time += 0.1
    # glClear(GL_COLOR_BUFFER_BIT)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)  # Источник света

    # glColor3d(0, 0.0, 1.0)
    # glLightModeli(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)

    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (1, 1, 1))
    # glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, (0,1,0))
    glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, (0, 0.5, 0))
    # glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, 10)
    glMaterialfv(GL_BACK, GL_SHININESS, 1)

    glRotatef(time/2, 1.0, 0.0, 0.0)
    glRotatef(time, 0.0, 1.0, 0.0)

    glutSolidTorus(0.25, 0.5, 100, 100)
    glPopMatrix()


    glutSwapBuffers()  # Выводим все нарисованное в памяти на экран


def redraw():
    glutPostRedisplay()
# Здесь начинается выполнение программы
# Использовать двойную буферизацию и цвета в формате RGB (Красный, Зеленый, Синий)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
# Указываем начальный размер окна (ширина, высота)
glutInitWindowSize(400, 400)
# Указываем начальное положение окна относительно левого верхнего угла экрана
glutInitWindowPosition(40, 30)
# Инициализация OpenGl
glutInit(sys.argv)

glutCreateWindow(b"Torus")
# Определяем процедуру, отвечающую за перерисовку
glutDisplayFunc(draw)
# Определяем процедуру, отвечающую за обработку клавиш
glutSpecialFunc(specialkeys)

glutIdleFunc(redraw)
# Вызываем нашу функцию инициализации
init()
# Запускаем основной цикл
glutMainLoop()