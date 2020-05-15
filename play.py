# Game Kapal Selam
# Nama : Reno Agil Saputra
# NIM : 17102090
# Kelas : MM 4

from OpenGLContext import testingcontext
from random import randrange
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Variable Kooridinat Posisi Kapal Selam
pos_x = 0
pos_y = 0

# Variable Koordinat Posisi Kotak
koor_x = 0
koor_y = 0

# Warna Kotak
kt_red = 24
kt_green = 101
kt_blue = 164

# Warna Background
bg_red = 24
bg_green = 101
bg_blue = 164

# Warna Teks
teks_merah = 1
teks_hijau = 1
teks_biru = 1

# Teks Warna Objek
teks_lampu = "OFF"

# Rotation
rotation = 1.0

# Zoom
zoom_x = 1.0
zoom_y = 1.0

# Cahaya Lampu
light_red = 24
light_green = 101
light_blue = 164

# Poin
point = 0


def init():
    glClearColor(convert_rgb(bg_red), convert_rgb(bg_green), convert_rgb(bg_blue), 1.0)
    gluOrtho2D(-500.0, 500.0, -500.0, 500.0)

def convert_rgb(c):
    return c / 255.0

def drawBitmapText(string,x,y,z) :
    glRasterPos3f(x,y,z)
    for c in string :
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18,ord(c))

def reshape(w, h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0,w,h,0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# Fungsi untuk menampilkan Teks Pada Window
def drawText():
    glColor3f(teks_merah,teks_hijau,teks_biru)
    # Petunjuk
    drawBitmapText("Direction : ",-460,440,0)
    drawBitmapText("Find The Box!. Turn On The Lights to see The Box. And Place The X Sign In The Box So You Can Get Points.",-460,400,0)
    # Informasi dan Kontrol
    drawBitmapText("Controls :",-460,-200,0)
    drawBitmapText("Scalling Zoom In / Out => i / o ",-460,-240,0)
    drawBitmapText("Rotation Right / Left => r / l ",-460,-280,0)
    drawBitmapText("Turn On / Off Light => Left Click Mouse / Right Click Mouse ",-460,-320,0)
    drawBitmapText("Direction UP / DOWN / RIGHT / LEFT => KEY UP / KEY DOWN / KEY RIGHT / KEY LEFT ",-460,-360,0)
    drawBitmapText("Information : " ,-460,-430,0)
    drawBitmapText("Poin => " + str(point),-460,-460,0)
    drawBitmapText("Lamp => " + teks_lampu,-460,-480,0)
   
    
# Fungsi Untuk Membuat Kotak
def kotak():
    glBegin(GL_POLYGON)
    glColor3f(convert_rgb(kt_red),convert_rgb(kt_green),convert_rgb(kt_blue))
    glVertex2f(-50 + koor_x,-50 + koor_y)
    glVertex2f(50 + koor_x,-50 + koor_y)
    glVertex2f(50 + koor_x,50 + koor_y)
    glVertex2f(-50 + koor_x, 50 + koor_y)
    glEnd()

# Fungsi Untuk Membuat Kapal Selam
def shape():
    # Untuk Mengatur Scalling / Zooming Kapal Selam
    glScalef(zoom_x,zoom_y, 0.0)
    # Untuk Mengatur Translasi / Pergerakan Kapal Selam
    glTranslatef(pos_x,pos_y,0)
    # Untuk Mengatur Rotation Kapal Selam
    glRotatef(rotation, 0.0, 0.0,1.0)
    
    # Badan
    glBegin(GL_POLYGON)
    glColor3f(convert_rgb(246),convert_rgb(185),convert_rgb(59))
    # Atas
    glVertex2f(-200  ,100  )
    glVertex2f(200  ,100  )
    # Kanan
    glVertex2f(300  ,0  )
    glVertex2f(200  ,-100  )
    # Bawah
    glVertex2f(-200  ,-100  )
    # Kiri
    glVertex2f(-300  ,0  )
    glVertex2f(-200  ,100  )
    glEnd()

    # Ekor
    glBegin(GL_POLYGON)
    glColor3f(convert_rgb(250),convert_rgb(152),convert_rgb(58))
    glVertex2f(250, 50)
    glVertex2f(350, 50)
    glVertex2f(350, -50)
    glVertex2f(250, -50)
    glVertex2f(250, 50)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(convert_rgb(229),convert_rgb(142),convert_rgb(38))
    glVertex2f(350, 60)
    glVertex2f(380, 60)
    glVertex2f(380, -60)
    glVertex2f(350, -60)
    glVertex2f(350, 60)
    glEnd()

    # Kaca Depan
    glBegin(GL_POLYGON)
    glColor3f(convert_rgb(130),convert_rgb(204),convert_rgb(221))
    glVertex2f(-300  , 0  )
    glVertex2f(-150  , 0  )
    glVertex2f(-150  , 100  )
    glVertex2f(-200  , 100  )
    glVertex2f(-300  , 0  )
    glEnd()


    # X SIGN
    glBegin(GL_POLYGON)
    glColor3f(convert_rgb(255),convert_rgb(255),convert_rgb(255))
    glVertex2f(-30  ,70)
    glVertex2f(-60  ,10)
    glVertex2f(-50  ,0)
    glVertex2f(-20  ,60)
    glVertex2f(-30  ,70)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(convert_rgb(52),convert_rgb(58),convert_rgb(64))
    glVertex2f(-30  ,0)
    glVertex2f(-60  ,60)
    glVertex2f(-50  ,70)
    glVertex2f(-20  ,10)
    glVertex2f(-30  ,0)
    glEnd()

    # Jendela 1
    glBegin(GL_POLYGON)
    glColor3f(convert_rgb(130),convert_rgb(204),convert_rgb(221))
    glVertex2f(30  ,10  )
    glVertex2f(90  ,10  )
    glVertex2f(90  ,60  )
    glVertex2f(30  ,60  )
    glVertex2f(30  ,10  )
    glEnd()
    

    # Jendela 2
    glBegin(GL_POLYGON)
    glColor3f(convert_rgb(130),convert_rgb(204),convert_rgb(221))
    glVertex2f(100  ,60  )
    glVertex2f(160  ,60  )
    glVertex2f(160  ,10  )
    glVertex2f(100  ,10  )
    glVertex2f(100  ,60  )
    glEnd()


    # Teropong
    glBegin(GL_POLYGON)
    glColor3f(convert_rgb(250),convert_rgb(152),convert_rgb(58))
    glVertex2f(-20  , 100  )
    glVertex2f(20  , 100  )
    glVertex2f(20  ,250  )
    glVertex2f(-20  ,250  )
    glVertex2f(-20  ,100  )
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(convert_rgb(250),convert_rgb(152),convert_rgb(58))
    glVertex2f(-20  , 250  )
    glVertex2f(-40  , 250  )
    glVertex2f(-40  , 210  )
    glVertex2f(-20  , 210  )
    glVertex2f(-20  , 250  )
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(convert_rgb(229),convert_rgb(142),convert_rgb(38))
    glVertex2f(-40  , 260  )
    glVertex2f(-60  , 260  )
    glVertex2f(-60  , 200  )
    glVertex2f(-40  , 200  )
    glVertex2f(-40  , 260  )
    glEnd()


    glBegin(GL_POLYGON)
    glColor3f(convert_rgb(229),convert_rgb(142),convert_rgb(38))
    glVertex2f(-100  , 100  )
    glVertex2f(100  , 100  )
    glVertex2f(80  , 150  )
    glVertex2f(-80  , 150  )
    glVertex2f(-100  , 100  )
    glEnd()

    # Lampu
    glBegin(GL_POLYGON)
    glColor3f(convert_rgb(229),convert_rgb(142),convert_rgb(38))
    glVertex2f(-220  ,-50  )
    glVertex2f(-300  ,-50  )
    glVertex2f(-300  ,-80  )
    glVertex2f(-220  ,-80  )
    glVertex2f(-220  ,-50  )
    glEnd()

    # Cahaya Lampu
    glBegin(GL_POLYGON)
    glColor3f(convert_rgb(light_red),convert_rgb(light_green), convert_rgb(light_blue))
    glVertex2f(-300  ,-62  )
    glVertex2f(-450  ,-20)
    glVertex2f(-450  ,-100)
    glVertex2f(-300  ,-62)
    
    glEnd()
    

# Fungsi untuk menampilkan semua bentuk pada Window
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    # Deklarasi Bentuk Kapal Selam
    glPushMatrix()
    shape()
    glPopMatrix()
    # Deklarasi Bentuk Kotak
    kotak()
    # Deklarasi Teks
    drawText()

    glFlush()

# Fungsi untuk mendapatkan callback event handling
# Pada Mouse
def input_mouse(button, state, x, y):
    global merah, hijau, biru
    global teks_lampu
    global bg_red, bg_green, bg_blue
    global light_red, light_green, light_blue
    global kt_red, kt_green, kt_blue

    # Jika Klik Kanan ditekan maka lampu akan dimatikan
    # dan warna background dan kotak akan berubah
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        light_red = 24
        light_green = 101
        light_blue = 164
        # Warna Background
        bg_red = 24
        bg_green = 101
        bg_blue = 164
        # Warna Kotak
        kt_red = 24
        kt_green = 101
        kt_blue = 164    

        glClearColor(convert_rgb(bg_red), convert_rgb(bg_green), convert_rgb(bg_blue), 1.0)

        teks_lampu = "OFF"
        print("Klik Kanan ditekan ", "(", x, ",", y, ")")
    
    # Jika Klik Kiri ditekan maka lampu akan menyala
    # dan warna background dan kotak akan berubah
    elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        light_red = 255.0
        light_green = 255.0
        light_blue = 0.0
        # Warna Background
        bg_red = 66
        bg_green = 155
        bg_blue = 227
        # Warna Kotak
        kt_red = 255
        kt_green = 255
        kt_blue = 255

        glClearColor(convert_rgb(bg_red), convert_rgb(bg_green), convert_rgb(bg_blue), 1.0)
        teks_lampu = "ON"
        print("Klik Kiri ditekan ", "(", x, ",", y, ")")
    
    
# Fungsi untuk mendapatkan callback event handling
# Pada Keyboard Tombol khusus
def input_keyboard_special_func(key,x,y):
    global pos_x, pos_y
    global warna_background
    global teks_merah, teks_hijau, teks_biru
 
    # Untuk mengubah posisi Kapal Selam dengan menekan
    # Tombol Key UP, Key DOWN, Key RIGHT, Key LEFT
    # saat ditekan nilai pada variable pos_x dan pos_y
    # akan berubah secara increment dan decremant dengan pertambahan 20
    if key == GLUT_KEY_UP:
        pos_y += 20
        print("Tombol Atas ditekan ", "x : ", pos_x, " y : ", pos_y)
        print("Koor ", "x : ", koor_x, " y : ", koor_y)
    elif key == GLUT_KEY_DOWN:
        pos_y -= 20
        print("Tombol Bawah ditekan ", "x : ", pos_x, " y : ", pos_y)
        print("Koor ", "x : ", koor_x, " y : ", koor_y)
    elif key == GLUT_KEY_RIGHT:
        pos_x += 20
        print("Tombol Kanan ditekan ", "x : ", pos_x, " y : ", pos_y)
        print("Koor ", "x : ", koor_x, " y : ", koor_y)
    elif key == GLUT_KEY_LEFT:
        pos_x -= 20
        print("Tombol Kiri ditekan ", "x : ", pos_x, " y : ", pos_y)
        print("Koor ", "x : ", koor_x, " y : ", koor_y)

# Fungsi untuk mendapatkan callback event handling
# Pada Keyboard Tombol yang akan mengembalikan nilai ascii
def input_keyboard_func(key, x, y):

    global zoom_x, zoom_y
    global rotation

    dk = key.decode("utf-8")

    # Untuk mengatur Zoom In & Out
    # Tekan tombol i / o
    # Maka variable zoom_x dan zoom_y
    # akan berubah secara increment dan decrement
    # dengan pertamban 0.1
    if dk == 'i' or dk == 'I':
        zoom_x += 0.1
        zoom_y += 0.1
    elif dk == 'o' or dk == 'O':
        zoom_x -= 0.1
        zoom_y -= 0.1

    # Untuk mengatur Rotasi ke kanan / kiri
    # Tekan tombol r / l
    # Maka variable rotation
    # akan berubah secara increment dan decrement
    # dengan pertamban 10
    elif dk == 'r' or dk == 'R':
        rotation -= 10
        print(rotation)
    elif dk == 'l' or dk == 'L':
        rotation += 10
        print(rotation)
    

def update(value):
    global koor_x, koor_y, pos_x, pos_y
    global point
    global kt
    global kt_red, kt_green, kt_blue
    
    # Untuk mengatur posisi kotak
    # Secara Randaom
    koor_x = randrange(-800,100)
    koor_y = randrange(-100,800)

    # Untuk mendapatkan Poin
    # Ketika teks_lampu = ON
    # atau nilai koor_x, koor_y sama dengan pos_x, pos_y
    if  teks_lampu == "ON":
        if koor_x == pos_x or koor_y == pos_x:
            point += 1
           
    
    
    glutPostRedisplay()
    glutTimerFunc(10,update,0)
  
    

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(1000,800)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Game Kapal Selam")

    glutDisplayFunc(display)


    glutSpecialFunc(input_keyboard_special_func)
    glutKeyboardFunc(input_keyboard_func)
    glutMouseFunc(input_mouse)

    glutTimerFunc(50, update, 0)

    

    init()
    glutMainLoop()
    
main()