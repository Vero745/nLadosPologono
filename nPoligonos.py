from turtle import Turtle
import subprocess
print("DIBUJANDO POLIGONOS")
#Primero, se ejecuta la cláusula try las palabras reservadas try y la except 
#Si no ocurre ninguna excepción, la cláusula except se omite y la ejecución de la cláusula try finaliza.
def OKI(n): # crear objeto de tipos de datos que pueden acceder
    try:
        n=int(n)
    except:
        n=OKI(input("Caracter no valido: "))
    return n

def OK(n):
    try:
        n=float(n)
    except:
        n=OK(input("Caracter no valido: "))
    return n

def ns(c):# crear objeto de respuesta si o no 
    while c!=("s") and c!=("n"):
        print(chr(7));c=input("Escribe solo \'n\' o \'s\' según su opción: ")
    return(c)
#se evalua lo que el usuario va aingresar si es s o n, si o no
#Se eleigen los colores que se deasean
def set_color(cf):
    try:
        t.screen.bgcolor(cf)# si no se escribe en inglés
    except:
        cf=set_color(input("Color no valido: "))
    return cf
        
def set_color2(ct):
    try:
        t.color(ct)
    except:
        ct=set_color2(input("Color no valido: "))
    return ct
#se muestran las preguntas si se decea activar para dibujar 
preg=ns(input("¿Activar Turtle?: "))
if preg==("s"):
    
    t=Turtle()
    t.hideturtle() #ocultar tortuga
    while True:
        print("DIBUJAR POLIGONO")

        cf=set_color(input("Indica el color del fondo: "))
        ct=set_color2(input("Indica el color del contorno: "))
        while ct==cf:
            ct=set_color2(input("Especifica un color diferente para el contorno: "))
        qc=ns(input("¿Especificar coordenadas?: "))
        if qc==("s"):
            coordenada_x=OKI(input("Introduce coordenada\'x\': "))
            coordenada_y=OKI(input("Introduce coordenada\'y\': "))
            #HACEMOS EL COLOR DE LA LINEA IGUAL AL COLOR DEL FONDO
            t.color(cf)
            t.setx(coordenada_x)
            t.sety(coordenada_y)
            #RESTABLECEMOS EL COLOR PARA LA LINEA
            t.color(ct)
        gt=OK(input("Indica el grosor de la línea: "))
        t.pensize(gt) #Tamaño de la punta del lápiz.
        n=OKI(input("Indica el número de lados del polígono: "))
        ln=OK(input("Indica la longitud del lado: "))
        #CALCULAMOS EL ANGULO DE GIRO DEL PUNTERO
        ang=180-(((n-2)/n)*180) 
        for i in range(n):
            t.left(ang)
            t.fd(ln)
        conti=ns(input("¿Dibujar nuevo poligono?: "))
        if conti==("s"):
            t.clear()
            subprocess.call(["cmd.exe","/C","cls"])
        else:
            break
        #t.screen.mainloop()
        
