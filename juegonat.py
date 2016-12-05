#Maria Fernanda Rodriguez A01371649
#videojuego

from Graphics import *
from Myro import * 

v = Window("Los patos asesinos del espacio exterior", 1000, 750)
v.mode = "physics"
v.gravity = Vector (0,0)

def musica():
    
    def reproducir_compas_uno(tiempo):
        beep(tiempo, 880)
        beep(tiempo, 659.255)
        beep(tiempo, 698.456)
        beep(tiempo, 783.991)
        
        
    def reproducir_compas_dos(tiempo):  
        beep(tiempo, 698.456)
        beep(tiempo, 659.255)
        beep(tiempo, 587.33)
        beep(tiempo, 587.33)
        beep(tiempo, 698.456)
        beep(tiempo, 880)
        beep(tiempo, 783.991)

    def reproducir_compas_tres(tiempo): 
        beep(tiempo, 698.456)
        beep(tiempo, 659.255)   
        beep(tiempo, 698.456)
        beep(tiempo, 783.991)

    def reproducir_compas_cuatro(tiempo):    
        beep(tiempo, 880)
        beep(tiempo, 698.456)
        beep(tiempo, 587.33)
        beep(tiempo, 587.33)
    base= 0.4
    reproducir_compas_uno(base)
    reproducir_compas_dos(base)
    reproducir_compas_tres(base)
    reproducir_compas_dos(base)
    reproducir_compas_cuatro(base) 

def main():
    
    fondo = makePicture("fondo.png")
    fondo.bodyType= "static"
    fondo.draw(v)
    nave = makePicture("nave.png")
    nave.x = 685
    nave.y = 670
    nave.border = 0
    nave.bodyType ="static"
    nave.draw(v)

    cord1=698
    cord2=666
    secureNum=0

    enemigo1= makePicture("enemigo1.png")
    enemigo1.x = 100
    enemigo1.y = 100
    enemigo1.border = 0
    enemigo1.draw(v)

    enemigo2= makePicture("enemigo2.png")
    enemigo2.x = 250
    enemigo2.y = 100
    enemigo2.border = 0
    enemigo2.draw(v)

    enemigo3= makePicture("enemigo3.png")
    enemigo3.x = 400
    enemigo3.y = 100
    enemigo3.border = 0
    enemigo3.draw(v)

    enemigo4= makePicture("enemigo4.png")
    enemigo4.x = 550
    enemigo4.y = 100
    enemigo4.border = 0
    enemigo4.draw(v)

    enemigo5= makePicture("enemigo5.png")
    enemigo5.x = 700
    enemigo5.y = 100
    enemigo5.border = 0
    enemigo5.draw(v)
     
    enemigo6= makePicture("enemigo6.png")
    enemigo6.x = 150
    enemigo6.y = 250
    enemigo6.border = 0
    enemigo6.draw(v)

    enemigo7= makePicture("enemigo7.png")
    enemigo7.x = 300
    enemigo7.y = 250
    enemigo7.border = 0
    enemigo7.draw(v)

    enemigo8= makePicture("enemigo8.png")
    enemigo8.x = 450
    enemigo8.y = 250
    enemigo8.border = 0
    enemigo8.draw(v)

    enemigo9= makePicture("enemigo9.png")
    enemigo9.x = 600
    enemigo9.y = 250
    enemigo9.border = 0
    enemigo9.draw(v)

    enemigo10= makePicture("enemigo10.png")
    enemigo10.x = 750
    enemigo10.y = 250
    enemigo10.border = 0
    enemigo10.draw(v)

    enemigo11= makePicture("enemigo11.png")
    enemigo11.x = 100
    enemigo11.y = 400
    enemigo11.border = 0
    enemigo11.draw(v)
     
    enemigo12= makePicture("enemigo12.png")
    enemigo12.x = 250
    enemigo12.y = 400
    enemigo12.border = 0
    enemigo12.draw(v)

    enemigo13= makePicture("enemigo13.png")
    enemigo13.x = 400
    enemigo13.y = 400
    enemigo13.border = 0
    enemigo13.draw(v)

    enemigo14= makePicture("enemigo14.png")
    enemigo14.x = 550
    enemigo14.y = 400
    enemigo14.border = 0
    enemigo14.draw(v)

    enemigo15= makePicture("enemigo15.png")
    enemigo15.x = 700
    enemigo15.y = 400
    enemigo15.border = 0
    enemigo15.draw(v)

    seconds=0
    cicloNave=0
    movim=4
    numOfBalas=1
    flag2=0
    enemDest=0
    puntos=0

    texto=Text((45,720),"Score: ")
    texto.fill=Color("white")
    texto.bodyType="static"
    texto.bounce=0.0
    texto.draw(v)

    tscore=Text((95,720),str(puntos))
    tscore.fill=Color("white")
    tscore.bodyType="static"
    tscore.bounce=0.0
    tscore.draw(v)

    enemies=Text((100,740),"Enemigos eliminados: ")
    enemies.fill=Color("white")
    enemies.bodyType="static"
    enemies.bounce=0.0
    enemies.draw(v)

    tnaves=Text((200,740),str(enemDest))
    tnaves.fill=Color("white")
    tnaves.bodyType="static"
    tnaves.bounce=0.0
    tnaves.draw(v)

    hit = None  # variable global para colision 
    hit2 = None
    
    def collide(myfixture, otherfixture, contact): 
        # funcion para colision 
        global hit
        global hit2 
        # definir colision 
        hit = myfixture.Body.UserData 
        hit2 = otherfixture.Body.UserData

    enemigo1.body.OnCollision += collide  
    enemigo2.body.OnCollision += collide 
    enemigo3.body.OnCollision += collide 
    enemigo4.body.OnCollision += collide 
    enemigo5.body.OnCollision += collide 
    enemigo6.body.OnCollision += collide  
    enemigo7.body.OnCollision += collide 
    enemigo8.body.OnCollision += collide 
    enemigo9.body.OnCollision += collide 
    enemigo10.body.OnCollision += collide
    enemigo11.body.OnCollision += collide  
    enemigo12.body.OnCollision += collide 
    enemigo13.body.OnCollision += collide 
    enemigo14.body.OnCollision += collide 
    enemigo15.body.OnCollision += collide

    time=1000

    ttiempo=Text((420,740),"Tiempo restante: ")
    ttiempo.fill=Color("white")
    ttiempo.bodyType="static"
    ttiempo.fontSize=24
    ttiempo.draw(v)

    tiempo=Text((530,738),str(time))
    tiempo.fill=Color("white")
    tiempo.bodyType="static"
    tiempo.fontSize=24
    tiempo.draw(v)
    musica()
    while True:
       
        hit=None
        hit2=None
        time=time-1
        print (time)
        if secureNum!=cord1 or seconds==10:
                flag=0
                seconds=0
        if cicloNave==40:
            movim=movim*-1
            cicloNave=0
        if numOfBalas%15==0 and flag2==0:
            movim*=1.1
            flag2=1
        if getKeyPressed():
            key = getLastKey()
            if key == "Left":
                nave.move(-5, 0)
                cord1-=5
            key = getLastKey()
            if key == "Right":
                nave.move(5, 0)
                cord1+=5
            key = getLastKey()
            if key == "space":
                coord1=cord1
                coord2=cord2
                if flag==0:
                    bala= Rectangle((cord1-1,cord2),(coord1,coord2))
                    bala.bodyType="dynamic"
                    bala.fill=makeColor(256,256,256)
                    bala.draw(v)  
                    bala.body.ApplyForce( Vector(-100, 0))
                    secureNum=cord1
                    flag=1
                    numOfBalas+=1
                    flag2=0
                
        enemigo1.move(movim,0)  
        enemigo2.move(movim,0)  
        enemigo3.move(movim,0) 
        enemigo4.move(movim,0)
        enemigo5.move(movim,0)
        enemigo6.move(movim,0)  
        enemigo7.move(movim,0)  
        enemigo8.move(movim,0) 
        enemigo9.move(movim,0)
        enemigo10.move(movim,0)
        enemigo11.move(movim,0)  
        enemigo12.move(movim,0)  
        enemigo13.move(movim,0) 
        enemigo14.move(movim,0)
        enemigo15.move(movim,0)
        
        seconds+=1 
        cicloNave+=1
        v.step(.01)
        tiempo.undraw()
        tiempo=Text((530,738),str(time))
        tiempo.fill=Color("white")
        tiempo.bodyType="static"
        tiempo.fontSize=24
        tiempo.draw(v)
        
        if hit!=None:
        
            hit.undraw()
            hit2.undraw()
            
            puntos+=130
            enemDest+=1
            
            tscore.undraw()
            
            tscore=Text((95,720),str(puntos))
            tscore.fill=Color("white")
            tscore.bodyType="static"
            tscore.draw(v)
            
            tnaves.undraw()
            
            tnaves=Text((200,740),str(enemDest))
            tnaves.fill=Color("white")
            tnaves.bodyType="static"
            tnaves.draw(v)
            
        if enemDest==15:
            time=0
            over=Rectangle((0,0),(1000,750))
            over.bodyType="static"
            over.fill=Color("green")
            over.draw(v)
            nave.undraw()
            gameOver=Text((500,350),"Juego Terminado, ganaste.")
            gameOver.fill=Color("black")
            gameOver.bodyType="static"
            gameOver.fontSize=50
            gameOver.draw(v)
            thighScore=Text((500,420),"High Score:  "+str(puntos))
            thighScore.fill=Color("black")
            thighScore.bodyType="static"
            thighScore.fontSize=35
            thighScore.draw(v)
            break   
            
        if time==0:
            over=Rectangle((0,0),(1000,750))
            over.bodyType="static"
            over.fill=Color("blue")
            over.draw(v)
            gameOver=Text((500,350),"Juego Terminado, perdiste.")
            gameOver.fill=Color("white")
            gameOver.bodyType="static"
            gameOver.fontSize=50
            gameOver.draw(v)
            thighScore=Text((500,420),"High Score:  "+str(puntos))
            thighScore.fill=Color("white")
            thighScore.bodyType="static"
            thighScore.fontSize=35
            thighScore.draw(v)  
            break

main()