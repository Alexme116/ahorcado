import pandas as pd
import random
import turtle
import time

def main():
    sc=turtle.Screen()
    sc.title("Ahorcado")
    sc.setup(width=1.0, height=1.0, startx=None, starty=None)
    sc.tracer(0)
    read()

    while True:
        sc.update()

def error1(palabra, mat_pal):
    turtle.penup()
    turtle.goto(-95, 120)
    turtle.pendown()
    turtle.pensize(5)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(240)
    turtle.penup()
    entry(palabra, mat_pal)

def error2(palabra, mat_pal):
    turtle.penup()
    turtle.goto(-95, 120)
    turtle.pendown()
    turtle.pensize(5)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(240)
    turtle.left(90)
    turtle.forward(160)
    turtle.left(90)
    turtle.forward(60)
    turtle.penup()
    entry(palabra, mat_pal)

def error3(palabra, mat_pal):
    turtle.penup()
    turtle.goto(-95, 120)
    turtle.pendown()
    turtle.pensize(5)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(240)
    turtle.left(90)
    turtle.forward(160)
    turtle.left(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.circle(20)
    turtle.penup()
    entry(palabra, mat_pal)

def error4(palabra, mat_pal):
    turtle.penup()
    turtle.goto(-95, 120)
    turtle.pendown()
    turtle.pensize(5)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(240)
    turtle.left(90)
    turtle.forward(160)
    turtle.left(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.circle(20)
    turtle.penup()
    turtle.left(90)
    turtle.forward(40)
    turtle.pendown()
    turtle.forward(60)
    turtle.penup()
    entry(palabra, mat_pal)

def error5(palabra, mat_pal):
    turtle.penup()
    turtle.goto(-95, 120)
    turtle.pendown()
    turtle.pensize(5)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(240)
    turtle.left(90)
    turtle.forward(160)
    turtle.left(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.circle(20)
    turtle.penup()
    turtle.left(90)
    turtle.forward(40)
    turtle.pendown()
    turtle.forward(60)
    turtle.penup()
    turtle.left(180)
    turtle.forward(60)
    turtle.right(135)
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()
    entry(palabra, mat_pal)

def error6(palabra, mat_pal):
    turtle.penup()
    turtle.goto(-95, 120)
    turtle.pendown()
    turtle.pensize(5)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(240)
    turtle.left(90)
    turtle.forward(160)
    turtle.left(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.circle(20)
    turtle.penup()
    turtle.left(90)
    turtle.forward(40)
    turtle.pendown()
    turtle.forward(60)
    turtle.penup()
    turtle.left(180)
    turtle.forward(60)
    turtle.right(135)
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()
    turtle.left(180)
    turtle.forward(20)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(20)
    turtle.right(180)
    turtle.penup()
    entry(palabra, mat_pal)

def error7(palabra, mat_pal):
    turtle.penup()
    turtle.goto(-95, 120)
    turtle.pendown()
    turtle.pensize(5)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(240)
    turtle.left(90)
    turtle.forward(160)
    turtle.left(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.circle(20)
    turtle.penup()
    turtle.left(90)
    turtle.forward(40)
    turtle.pendown()
    turtle.forward(60)
    turtle.penup()
    turtle.left(180)
    turtle.forward(60)
    turtle.right(135)
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()
    turtle.left(180)
    turtle.forward(20)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(20)
    turtle.right(180)
    turtle.penup()
    turtle.forward(20)
    turtle.right(135)
    turtle.forward(60)
    turtle.pendown()
    turtle.left(45)
    turtle.forward(20)
    turtle.left(180)
    turtle.penup()
    entry(palabra, mat_pal)

def errorfinal(palabra, mat_pal):
    turtle.penup()
    turtle.goto(-95, 120)
    turtle.pendown()
    turtle.pensize(5)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(240)
    turtle.left(90)
    turtle.forward(160)
    turtle.left(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.circle(20)
    turtle.penup()
    turtle.left(90)
    turtle.forward(40)
    turtle.pendown()
    turtle.forward(60)
    turtle.penup()
    turtle.left(180)
    turtle.forward(60)
    turtle.right(135)
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()
    turtle.left(180)
    turtle.forward(20)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(20)
    turtle.right(180)
    turtle.penup()
    turtle.forward(20)
    turtle.right(135)
    turtle.forward(60)
    turtle.pendown()
    turtle.left(45)
    turtle.forward(20)
    turtle.left(180)
    turtle.penup()
    turtle.forward(20)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()
    entry(palabra, mat_pal)

def gameover(palabra):
    turtle.clearscreen()
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(240, 100)
    turtle.write("PERDISTE", True, "right", ("arial", 80, "bold"))
    turtle.goto(150, -120)
    turtle.write(f"La palabra era: {palabra}", True, "right", ("arial", 20, "bold"))
    time.sleep(5)
    exit()

def read():
    datos = pd.read_table("https://raw.githubusercontent.com/Alexme116/ahorcado/main/palabras.txt")
    palabra=str((datos.palabras[random.randint(0,len(datos.palabras))]))
    mat_pal=[]
    pal=""
    letras=len(palabra)

    for i in range(letras):
        mat_pal.append("_")
    
    turtle.clearscreen()
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-150, -300)
    turtle.write(f"La palabra contiene: {letras} letras ", True, "right", ("arial", 20, "bold"))
    for i in mat_pal:
        pal += i + " "
    turtle.goto(75, -300)
    turtle.write(" " + pal, True, "right", ("arial", 20, "bold italic"))

    entry(palabra, mat_pal)

def entry(palabra, mat_pal):
    s=0
    while s !=1:
        letra=turtle.textinput("Letra", "\n¿Cuál es la letra oculta? ")
        if len(letra) == 1:
            s=1
        else:
            print("Solo puedes ingresar una letra")
            continue

    checker(palabra, mat_pal, letra)

def checker(palabra, mat_pal, letra):
    comp=0
    c=0
    for i in palabra:
        if i == letra:
            mat_pal[c]=i
            comp+=1
        c+=1
    if comp != 0:
        word_print(palabra, mat_pal)
    else:
        global errores
        errores+=1
        word_print(palabra, mat_pal)

def word_print(palabra, mat_pal):
    global errores
    palabra_final=list(palabra)
    s=0
    pal=""
    for i in mat_pal:
        pal += i + " "
    turtle.clearscreen()
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-150, -300)
    turtle.write(f"La palabra contiene: {len(palabra)} letras ", True, "right", ("arial", 20, "bold"))
    turtle.goto(75, -300)
    turtle.write(" " + pal, True, "right", ("arial", 20, "bold italic"))
    #Agregar los 8 errores permitidos - el 9 es el ultimo intento (si falla pierde)
    if mat_pal == palabra_final:
        turtle.penup()
        turtle.goto(225, 200)
        turtle.pendown()
        turtle.write("GANASTE!", True, "right", ("arial", 80, "bold"))
        while s != 1:
            res=turtle.textinput("Opciones", "\n(r) para repetir / (enter) para cerrar")
            if res == "r":
                global errores
                errores=0
                main()
            elif res == "":
                exit()
            else:
                print("Opcion no valida, intente de nuevo")
                continue
    elif errores == 0:
        entry(palabra, mat_pal)
    elif errores == 1:
        error1(palabra, mat_pal)
    elif errores == 2:
        error2(palabra, mat_pal)
    elif errores == 3:
        error3(palabra, mat_pal)
    elif errores == 4:
        error4(palabra, mat_pal)
    elif errores == 5:
        error5(palabra, mat_pal)
    elif errores == 6:
        error6(palabra, mat_pal)
    elif errores == 7:
        error7(palabra, mat_pal)
    elif errores == 8:
        errorfinal(palabra, mat_pal)
    elif errores > 8:
        gameover(palabra)

errores=0
main()
