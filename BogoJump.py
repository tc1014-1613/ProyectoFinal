#encoding:UTF-8
#Autor: José Javier Rodríguez Mota
#Descripción:

#Importamos Graphics para la animación del juego
from Graphics import *

#Importamos random
from random import randint 

#Importamos myro para el sonido
from Myro import play



        
#Esto es lo que marca el puntaje
contador=0
puntosMax=0

#Ventana del juego
v=Window("Jumping Bogo",300,500)
#No utilizamos physics porque no nos gustó la simulación
#v.mode ="physics"    


#Personaje de 37x46
bogo= makePicture("res/img/bogo.png")
bogo.x=150
bogo.y=300
bogo.border=0


#Contador
txtContador = Text((90,20),"0 Rayos emprendedores")
txtContador.fontSize = 15
txtContador.color=Color("white")
txtMax=Text((90,38),"Lo más emprendedor:"+str(puntosMax))
txtMax.color=Color("white")
txtMax.fontSize=15
emprendedor=makePicture("res/img/pocoemprendedor.png")

#Lista de Plataformas
listaPlataformas=[]
#Movimiento
inc=3

#Iniciamos nuestros botones
btn_start=Button((175,200),"Jugar")
btn_salir=Button((100,200),"Salir")
btn_instrucciones=Button((120,170),"Instrucciones")
btn_start.draw(v)
btn_salir.draw(v)
btn_instrucciones.draw(v)
btn_regresar=Button((180,400),"Regresar")
btn_regresar.draw(v)
btn_regresar.Visible=False

#Texto Instrucciones
txtInstrucciones=Text((150,250),"")
txtInstrucciones.color=Color("white")

#Atendemos el teclado
def leerTecla(ventana,evento):
    tecla=evento.key
    
    #Para mover a la derecha    
    if tecla=="d":
        if bogo.x<300-10:
            bogo.x+=inc
        else:
            bogo.x=0    
    #Izquierda
    elif tecla=="a":
        if bogo.x>10:
            bogo.x-=inc
        else:
            bogo.x=300-10    

#Abrimos/creamos un archivo con los puntajes más altos
def obtenerPuntoM():
    global puntosMax
    if contador>puntosMax:
        puntosMax=contador
       
#Atendemos los botones
def atenderBoton(boton, e):
    if boton==btn_start:
        iniciarJuego()
    if boton==btn_salir:
        v.close()
    if boton==btn_instrucciones:
        mostrarInstrucciones(True)    
    if boton==btn_regresar:
        mostrarInstrucciones(False)
#Conectamos los botones a la función
btn_start.connect("click",atenderBoton)
btn_salir.connect("click",atenderBoton)  
btn_instrucciones.connect("click",atenderBoton)
btn_regresar.connect("click",atenderBoton)
#Mostramos las instrucciones
def mostrarInstrucciones(estado):
    if estado:
        btn_start.Visible=False
        btn_salir.Visible=False
        btn_instrucciones.Visible=False
        txtInstrucciones.text="Obtén la mayor cantidad de\nRayos Emprendedores posible\nBotones: izquierda (a) derecha (s)\nUn juego de Javier Rodríguez"
        txtInstrucciones.draw(v)
        btn_regresar.Visible=True
        emprendedor.undraw()
        txtContador.x=90
        txtContador.y=20
    else:
        mostrarMenu()
        txtInstrucciones.undraw()
        btn_regresar.Visible=False

#Sabemos si perdió
def pierde():
    global bogo
    if bogo.y >= 500:
        play("res/audio/pierde.wav")
        obtenerPuntoM()
        txtMax.text="Lo más emprendedor:"+str(puntosMax)
        return True 
    else:
        if bogo.y<=0:
            bogo.y=30
        return False
      
#Mostramos puntaje
def mostrarPuntaje():
    global emprendedor
    txtContador.y=250
    txtContador.x=150
    if contador>50 and contador <100:
        emprendedor=makePicture("res/img/medioemprendedor.png")
    elif contador>=100:
        emprendedor=makePicture("res/img/muyemprendedor.png")
    else:
        emprendedor=makePicture("res/img/pocoemprendedor.png")
    emprendedor.x=150
    emprendedor.y=320
    emprendedor.draw(v)     
       
#Hacemos nuestro Menú inicial
def mostrarMenu():
    bogo.x=150
    bogo.y=120
    #play("res/audio/menu.wav")
    btn_start.Visible=True
    btn_salir.Visible=True
    btn_instrucciones.Visible=True
    btn_regresar.Visible=False

#Atendemos botón start
def iniciarJuego():
    global contador
    txtContador.x=90
    txtContador.y=20
    emprendedor.undraw()
    #Ponemos a Bogo en una posición inicial
    bogo.x=150
    bogo.y=150
    btn_start.Visible=False
    btn_salir.Visible=False
    btn_instrucciones.Visible=False
    
    #Hacemos el único bloque que no es al azar
    bloque=makePicture("res/img/bloque.png")
    bloque.x=150
    bloque.y=490
    bloque.border=0
    bloque.draw(v)
    
    
    listaPlataformas.append(bloque)
    
    #Reiniciamos nuestro puntaje
    contador=0
    cambiarPuntaje()
    
   

#Aquí revisaremos si hay un salto o caída
def revisarPlataforma():
    
    #Requeriremos cambiar nuestro contador
    global contador
    #Esta variable sólo definirá si saltó o no
    pega=0
    
    #Revisamos cada una de las plataformas
    for plataforma in listaPlataformas:
        
        #Establecemos el rango de golpe
        if ((bogo.x >= plataforma.x+25 or bogo.x >= plataforma.x-25) and (bogo.y>=plataforma.y-30 and bogo.y<=plataforma.y)):
            
            #Si encontramos que agarró un rayo
            contador+=1
            
            #Salta bogo
            bogo.y-=50
            
            #Cambiamos el marcador
            cambiarPuntaje()
            play("res/audio/punto.wav")
            #Eliminamos la plataforma en la que cae
            plataforma.undraw()
            listaPlataformas.remove(plataforma)
        
        #En caso de no brincar establecemos que cae
        else:
            pega=1
            
    #Aquí establecemos que cae
    if pega==1:
        bogo.y+=10

#Animar Plataformas
def animarPlataforma():
    
    #Revisamos que no haya más de 30 rayos emprendedores
    if len(listaPlataformas)<=30:
        
        #Hacemos un rayo emprendedor nuevo
        plataforma=makePicture("res/img/bloque.png")
        plataforma.x=randint(-4,4)*30+150
        plataforma.y=randint(1,5)*randint(50,100)
        plataforma.border=0
        listaPlataformas.append(plataforma)
        plataforma.draw(v)
        
        
#Hacemos nuestra función para establecer un puntaje    
def cambiarPuntaje():
    txtContador.text=str(contador)+" Rayos emprendedores."

#Eliminar todas las plataformas
def borrarPlataformas():
    #Eliminamos cada una de las plataformas en la lista
    for plataforma in listaPlataformas:
        plataforma.undraw()
        listaPlataformas.remove(plataforma)

#Definimos Main
def main():
    global bogo
    
    #Fondo
    fondo=makePicture("res/img/background.png")
    fondo.draw(v)

    #Dibujamos a nuestro personaje
    bogo.draw(v)
    
    #Dibujamos el marcador
    txtContador.draw(v)
    txtMax.draw(v)    
    
    #Eventos del teclado
    onKeyPress(leerTecla)

    #Empezamos el loop infinito
    while True:
        #Teclas oprimidas en el ciclo
        if getKeyPressed():
            key=getLastKey()
            #Para salir del programa
            if key=="Escape":
                mostrarMenu()  
        
        #Revisamos si perdió
        if pierde():
            borrarPlataformas()
            mostrarMenu()
            mostrarPuntaje()
        else:
            #Revisamos que el juego esté corriendo y no en el menú
            if not (btn_start.Visible or btn_regresar.Visible):
                revisarPlataforma()    
                animarPlataforma()    
        
        v.step(0.025) #Retardo (sleep) NO MOVER
        
v.run(main)